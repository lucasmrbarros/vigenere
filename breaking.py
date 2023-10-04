import breakingTools

def breakingTheLaw (encripeted, max_key_len, lenguage):

    key_size = breakingTools.key_size(encripeted, max_key_len, lenguage)

    key = breakingTools.key_refactor(encripeted, key_size, lenguage)

    return key


33