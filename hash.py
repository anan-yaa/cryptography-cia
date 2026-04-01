def simple_hash(text):
    # use a larger prime number for the modulo to reduce collisions
    # 2**32 - 1 is a standard size for a 32-bit hash
    modulo = 0xFFFFFFFF 
    hash_val = 5381 # a classic starting 'salt' value

    for i, ch in enumerate(text):
        # use bitwise operations to mix the data more thoroughly
        # multiplying by 33 is a standard technique (hash * 33 + char)
        hash_val = ((hash_val << 5) + hash_val) + ord(ch)
        # include the position to ensure order matters
        hash_val = (hash_val ^ (i + 1)) & modulo

    # use zfill to ensure the hash is always the same length (8 hex chars)
    return hex(hash_val)[2:].upper().zfill(8)