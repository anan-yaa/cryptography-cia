import hashlib
import math

# ✅ Classical Myszkowski key (CORRECT)
def get_myszkowski_key(passphrase):
    passphrase = passphrase.lower()

    sorted_chars = sorted(passphrase)

    rank_map = {}
    rank = 1

    for ch in sorted_chars:
        if ch not in rank_map:
            rank_map[ch] = rank
            rank += 1

    return [rank_map[ch] for ch in passphrase]


# ✅ SHA-256 on plaintext
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest().upper()


def myszkowski_encrypt(text, key):
    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)

    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    idx = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if idx < len(text):
                grid[r][c] = text[idx]
                idx += 1
            else:
                grid[r][c] = 'X'

    ciphertext = ""

    for rank in sorted(set(key)):
        cols = [i for i, k in enumerate(key) if k == rank]

        for r in range(num_rows):
            for c in cols:
                ciphertext += grid[r][c]

    return ciphertext


# 🔥 MAIN
if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    passphrase = input("Enter passphrase: ")

    # Step 1: SHA-256
    hashed_text = sha256_hash(plaintext)
    print("\nSHA-256 Hash:\n", hashed_text)

    # Step 2: Myszkowski key
    key = get_myszkowski_key(passphrase)
    print("\nGenerated Key:", key)

    # Step 3: Encrypt hash
    cipher = myszkowski_encrypt(hashed_text, key)
    print("\nFinal Cipher Text:\n", cipher)