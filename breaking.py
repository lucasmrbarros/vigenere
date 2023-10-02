import utilites

def breakingTheLaw (encripeted, max_key_len):

    key_size = utilites.key_size(encripeted, max_key_len)

    key = utilites.key_refactor(encripeted, key_size)

    return key


