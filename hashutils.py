import hashlib

def make_pwd_hash(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()


def check_pwd_hash(pwd, hash):
    if make_pwd_hash(pwd) == hash:
        return True
    return False



