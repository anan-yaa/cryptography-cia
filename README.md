
# Crptography CIA : Implementing Myszkowski Cipher
- Name: R. Ananyaa Sri 
- Class: CSE IoT-B
- Reg No. : 23011102069

## 1. Brief Theory

### History of the Cipher: Myszkowski Transposition
The **Myszkowski Cipher** is a variation of the Columnar Transposition cipher. In a standard columnar transposition, duplicate letters in a keyword are numbered sequentially. However, in Myszkowski, duplicate letters are given the same rank. 

When the algorithm encounters these duplicate ranks:
- **Standard Rule:** Read down the columns one by one.
- **Myszkowski Rule:** Read **across** the duplicate columns row-by-row.
This provides a unique scrambling method that is more complex to crack manually than standard transposition.

### The Hash: 32-bit Custom Positional Mixer
Since the project requires an implementation from scratch without external libraries, I implemented a **Custom 32-bit Mixer Hash**. 
- **Positional Weighting:** Each character is multiplied by its index to ensure that "ABC" and "CBA" produce different results.
- **Bitwise Diffusion:** It uses bit-shifting (`<<`) and XOR operations to ensure the "Avalanche Effect"—meaning a small change in input produces a large, unpredictable change in the output.
- **Collision Resistance:** A 32-bit modulo ensures over 4 billion possible hash values, making accidental collisions highly unlikely.

---

## 2. Instructions to Run the Code

### Prerequisites
- Python 3.x installed.
- No external libraries are required (standard `math` library only).

### Execution
1. Clone this repository to your local machine.
2. Navigate to the directory on your local machine.
3. Run the script using the following command:
   ```bash
   python main.py
   ```
4. Enter the plain text and the key.
---

## 3. Worked Examples

### Example 1
- **Plaintext:** `HELLO WORLD`
- **Key:** `BANANA`
- **Ciphertext:** `ELWRDXHOLOLX`
- **Hash Output:** `EBF9AFA1` 

### Example 2
- **Plaintext:** `CRYPTOGRAPHY`
- **Key:** `CONCEPTS`
- **Ciphertext:** `CPAYTXYHRPOXRXGX`
- **Hash Output:** `6706B3B9`

---

## 4. Test Script Results (Encrypt → Hash → Decrypt)

The script includes a built-in test suite that demonstrates the full round-trip. When executed, it performs the following steps:
1. **Normalization:** Removes spaces and pads the plaintext with 'X' to fit the grid.
2. **Encryption:** Transforms the plaintext into ciphertext using the Myszkowski key-ranking rule.
3. **Hashing:** Generates a unique 32-bit fingerprint of the resulting ciphertext.
4. **Decryption:** Reverses the transposition and strips the padding to recover the original message.

---

## 5. Implementation Constraints Checklist
- [x] **Language:** Python
- [x] **No Crypto Libraries:** All logic (including hashing) implemented from scratch.
- [x] **Unique Hash:** Custom implementation different from standard MD5/SHA libraries.
- [x] **GitHub Ready:** Structured for immediate push.