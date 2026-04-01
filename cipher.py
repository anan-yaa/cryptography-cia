import math
''' 
myszkowski key is decided by the order and frequency of the letters.
if the passphrase is given as "mammal" then its first arranged in ascending order of the 
letters, which is aalmmm. then numbers are assigned like 112333. same letters have the same
number assigned to them. then the original order is preserved, so the key becomes 313312
'''
def get_order(key):
    key = key.upper()
    sorted_unique = sorted(list(set(key)))
    # map each unique char to its rank in the alphabet
    order_map = {ch: i for i, ch in enumerate(sorted_unique)}
    # return the rank for each character in the original key
    return [order_map[ch] for ch in key]

def encrypt(plaintext, key):
    # normalize text and calculate dimensions
    plaintext = plaintext.replace(" ", "").upper()
    cols = len(key)
    
    # add padding so the text fits the grid perfectly
    # only adding letter 'x' as padding for simplicity, until the length is a multiple of the number of columns
    while len(plaintext) % cols != 0:
        plaintext += 'X'
        
    rows = math.ceil(len(plaintext) / cols)
    
    # create the grid and fill it row by row
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    for i, char in enumerate(plaintext):
        matrix[i // cols][i % cols] = char

    order = get_order(key)
    ciphertext = ""
    
    # process columns based on alphabetical order of the key
    for num in sorted(set(order)):
        cols_same = [c for c in range(cols) if order[c] == num]
        
        if len(cols_same) == 1:
            # standard column: read the single column top to bottom
            c = cols_same[0]
            for r in range(rows):
                if matrix[r][c]:
                    ciphertext += matrix[r][c]
        else:
            # myszkowski rule: for duplicate keys, read those columns together row by row
            for r in range(rows):
                for c in cols_same:
                    if matrix[r][c]:
                        ciphertext += matrix[r][c]
    return ciphertext

def decrypt(ciphertext, key):
    cols = len(key)
    rows = math.ceil(len(ciphertext) / cols)
    order = get_order(key)
    
    # the grid is full because of the padding added during encryption
    num_chars = len(ciphertext)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    
    # fill the matrix using the same order logic as encryption
    for num in sorted(set(order)):
        cols_same = [c for c in range(cols) if order[c] == num]
        
        if len(cols_same) == 1:
            # fill single column top down
            c = cols_same[0]
            for r in range(rows):
                if idx < num_chars:
                    matrix[r][c] = ciphertext[idx]
                    idx += 1
        else:
            # fill multiple duplicate columns row by row
            for r in range(rows):
                for c in cols_same:
                    if idx < num_chars:
                        matrix[r][c] = ciphertext[idx]
                        idx += 1

    # read out the final grid row by row
    plaintext = ""
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c]:
                plaintext += matrix[r][c]
    
    # remove the 'x' padding from the end of the string
    return plaintext.rstrip('X')