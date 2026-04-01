from cipher import encrypt, decrypt
from hash import simple_hash

def main():
    plaintext = input("Enter Plain text: ")
    key = input("Enter Key: ")

    print("=== INPUT ===")
    print("Plaintext:", plaintext)
    print("Key:", key)

    # Step 1: Encrypt
    cipher = encrypt(plaintext, key)
    print("\n=== ENCRYPTION ===")
    print("Ciphertext:", cipher)

    # Step 2: Hash
    hash_val = simple_hash(cipher)
    print("\n=== HASH ===")
    print("Custom Hash value:", hash_val)

    # Step 3: Verify integrity
    print("\n=== VERIFICATION ===")
    if simple_hash(cipher) == hash_val:
        print("Integrity Verified")
    else:
        print("Data Tampered")

    # Step 4: Decrypt (round-trip)
    decrypted = decrypt(cipher, key)
    print("\n=== DECRYPTION ===")
    print("Decrypted:", decrypted)

    # Final check
    print("\n=== ROUND-TRIP CHECK ===")
    if decrypted == plaintext.replace(" ", "").upper():
        print("Round-trip Successful")
    else:
        print("Round-trip Failed.")


if __name__ == "__main__":
    main()