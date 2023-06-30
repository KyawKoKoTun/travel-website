import hashlib

def generate_sha256_hash(data):

    if isinstance(data, str):
        data = data.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data)
    hex_digest = sha256_hash.hexdigest()

    return hex_digest


if __name__ == '__main__':
    data = 'Hello, world!'
    hash_value = generate_sha256_hash(data)
    print(hash_value)
