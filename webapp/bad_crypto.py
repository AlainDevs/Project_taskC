import hashlib

def generate_hash(data):
    # Dummy code using md5 to test custom Semgrep rule
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()
