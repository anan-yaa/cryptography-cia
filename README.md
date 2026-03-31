# Cryptography Concepts CIA: Myszkowski Transposition Cipher 

Name: R. Ananyaa Sri
Reg No. 23011102069
Class : CSE IoT-B

Python implementation of the Myszkowski Transposition Cipher with a Custom 32-bit Bit-Mixed Hash Function. 
---

## Features

* **Myszkowski Cipher**: A variation of the columnar transposition cipher that handles keyword repetitions by processing columns of the same rank together.
* **Custom Hash Function**: A proprietary hashing algorithm utilizing positional weighting, modulo arithmetic, and XOR bit-mixing.
* **32-bit Simulation**: Uses bit-masking (`& 0xFFFFFFFF`) to ensure consistent 32-bit output, simulating hardware register behavior within Python's arbitrary-precision environment.



---

## Logic Overview

### 1. Key Generation (Myszkowski)
The key is derived from the alphabetical order of the passphrase. Unlike standard columnar transposition where identical letters are numbered sequentially, Myszkowski assigns the **same rank** to identical letters.
* **Example**: `MAMMAL` $\rightarrow$ `3 1 3 3 1 2`
* This ensures that columns with the same rank are read row-by-row, increasing the complexity of the resulting ciphertext.

### 2. Encryption Process
1.  **Cleaning**: Plaintext is stripped of spaces and converted to uppercase.
2.  **Grid Mapping**: Text is written horizontally across a grid dictated by the key length.
3.  **Transposition**: Columns are read based on the alphabetical rank of the key. 
    * If a rank is unique, the entire column is read. 
    * If ranks are shared (e.g., two 'A's in the key), those columns are read together, row by row.
4.  **Padding**: The character 'X' is used to fill any remaining slots in the grid.

### 3. Integrity Hashing
The `simple_hash` function provides a digital fingerprint of the ciphertext using a two-step process:
1.  **Positional Accumulation**: $Hash_{val} = ((Hash_{val} + (ASCII \times Position)) \pmod{100,000})$
2.  **Bit-Mixing**: $Hash_{val} = (Hash_{val} \oplus (Hash_{val} \ll 3)) \ \& \ 0xFFFFFFFF$

---
## Prompt used

Write a Python script that implements a Myszkowski transposition cipher and a custom hash function for a cryptography project. For the cipher, the code should take a passphrase and assign numeric ranks to each letter based on alphabetical order, ensuring that duplicate letters receive the identical rank. The encryption process must clean the input text by removing spaces and converting it to uppercase, then arrange it into a grid where the number of columns matches the passphrase length, using 'X' for any necessary padding. When reading the ciphertext, the logic should follow the numeric ranks of the key, where columns with the same rank are processed together row-by-row. Additionally, include a hash function that starts at zero and iterates through the ciphertext, adding the ASCII value of each character multiplied by its 1-indexed position. This value should be moduloed by 100,000, then mixed using a bitwise left-shift of 3 XORed with itself, finally masking the result to 32 bits and returning it as an uppercase hexadecimal string. The script should include a main block to take user input and display the resulting key, ciphertext, and hash.

## Security Analysis
* **Diffusion**: Achieved by the positional weighting in the hash and the columnar shifting in the cipher.
* **Confusion**: The Myszkowski rank system masks the relationship between the key and the ciphertext more effectively than simple columnar transposition.
* **Integrity**: The bit-mixing step ensures that even minor changes to the ciphertext result in a significantly different hash value.
