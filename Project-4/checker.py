import hashlib, json, sys, os
from datetime import datetime

HASH_FILE = os.path.abspath("hashes.json")
LOG_FILE  = os.path.abspath("logs.txt")

def calculate_hash(file_path, method="sha256"):
    h = hashlib.new(method)
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

def log(msg):
    with open(LOG_FILE, "a") as logf:
        logf.write(f"{datetime.now().isoformat(timespec='seconds')} - {msg}\n")

def load_db():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f: return json.load(f)
    return {}

def save_db(db):
    tmp = HASH_FILE + ".tmp"
    with open(tmp, "w") as f: json.dump(db, f, indent=2)
    os.replace(tmp, HASH_FILE)

def store(file_path, method="sha256"):
    file_path = os.path.abspath(file_path)
    if not os.path.isfile(file_path):
        print(f"[ERR] File not found: {file_path}")
        sys.exit(1)
    hv = calculate_hash(file_path, method)
    db = load_db()
    db[file_path] = {"hash": hv, "algo": method}
    save_db(db)
    log(f"Stored hash ({method}) for {file_path}: {hv}")
    print(f"[STORED] {file_path}")

def check(file_path):
    file_path = os.path.abspath(file_path)
    if not os.path.isfile(file_path):
        print(f"[ERR] File not found: {file_path}")
        sys.exit(1)
    if not os.path.exists(HASH_FILE):
        print("No baseline yet. Run 'store' first.")
        sys.exit(1)
    db = load_db()
    if file_path not in db:
        print(f"No stored hash for {file_path}. Run 'store' first.")
        sys.exit(1)
    method = db[file_path]["algo"]
    expected = db[file_path]["hash"]
    current  = calculate_hash(file_path, method)
    if current == expected:
        print(f"[OK] {file_path} integrity verified.")
        log(f"Integrity verified for {file_path}")
        sys.exit(0)
    else:
        print(f"[ALERT] {file_path} tampering detected!")
        log(f"TAMPERING DETECTED in {file_path} - Expected {expected}, Found {current}")
        sys.exit(2)  # non-zero so cron/email can alert

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("store","check"):
        print("Usage: python3 checker.py [store|check] <file1> [file2 ...]")
        sys.exit(1)
    mode = sys.argv[1]
    files = sys.argv[2:]
    rc = 0
    for fp in files:
        try:
            if mode == "store": store(fp)
            else:                check(fp)
        except SystemExit as e:
            if e.code != 0 and mode == "check": rc = e.code
    sys.exit(rc)
