# CIA: Cryptography Concepts - Myszkowski Transposition Cipher
**Name:** R. Ananyaa Sri  
**Reg No:** 23011102069  
**Class:** CSE IoT-B  

---

## 1. Algorithm Design

### 1. Myszkowski Key Generation
The core difference between a standard columnar cipher and the Myszkowski variant lies in how keyword repetitions are handled. 
* Identical characters in the passphrase are assigned the **same rank**.
* **Example:** In the passphrase `MAMMAL`, the letters are ranked as `3 1 3 3 1 2`. 
* Columns sharing the same rank are read row-by-row during the transposition phase, whereas unique ranks are read column-by-column.

### 2. Encryption and Padding
1. **Preprocessing:** The plaintext is sanitized by removing whitespace and converting all characters to uppercase.
2. **Matrix Mapping:** The text is mapped into a grid where the number of columns corresponds to the passphrase length. 
3. **Padding:** If the message length is not a multiple of the key length, 'X' characters are used as null-fills to complete the final row.
4. **Transposition:** The grid is read out based on the ascending order of the generated ranks.

### 3. The Hashing Function (`simple_hash`)
The hashing algorithm follows a two-stage transformation to ensure a high avalanche effect:
hash_val = (hash_val + (ord(ch) * (i + 1))) % 100000
hash_val = (hash_val ^ (hash_val << 3)) & 0xFFFFFFFF

---

## 4. LLM Prompt
> Write a Python code that implements a Myszkowski transposition cipher and a custom hash function. The cipher must assign identical ranks to duplicate letters in the passphrase. Encryption involves horizontal grid filling with 'X' padding and rank-ordered reading (shared ranks read row-by-row). The hash function must use 1-indexed positional weighting, a 100,000 modulo, and a 3-bit left-shift XOR mix, returning a 32-bit uppercase hex string.