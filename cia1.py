import math
''' 
custom hash function

my hash function initializes a value as 0, takes the letters in the text and converts it into
ascii values (using ord function), it adds position based weighting (where order matters). 
then modulo by 1,00,000 is done to limit the size of the number.
then comes bit-mixing, which is left shift by 3 then xor. finally it takes only the last
32 bits of the number.
''' 
def simple_hash(text):
    hash_val = 0

    for i, ch in enumerate(text):
        hash_val = (hash_val + (ord(ch) * (i + 1))) % 100000
        hash_val = (hash_val ^ (hash_val << 3)) & 0xFFFFFFFF

    return hex(hash_val)[2:].upper()

''' 
myszkowski key is decided by the order and frequency of the letters.
if the passphrase is given as "mammal" then its first arranged in ascending order of the 
letters, which is aalmmm. then numbers are assigned like 112333. same letters have the same
number assigned to them. then the original order is preserved, so the key becomes 313312
'''
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

def clean_text(text):
    return text.replace(" ", "").upper()

def myszkowski_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    num_cols = len(key)
    num_rows = math.ceil(len(plaintext) / num_cols)

    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    idx = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if idx < len(plaintext):
                grid[r][c] = plaintext[idx]
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

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    passphrase = input("Enter passphrase: ")

    key = get_myszkowski_key(passphrase)
    print("\nKey from myszkowski cipher:", key)

    ciphertext = myszkowski_encrypt(plaintext, key)
    print("\nCipher Text:\n", ciphertext)

    hashed_cipher = simple_hash(ciphertext)
    print("\nHashed cipher text:\n", hashed_cipher)