import breakingToolsPt
import  breakingToolsEn

def breakingTheLaw (encripeted, max_key_len, lenguage):

    if lenguage == 1:
        key_size = breakingToolsPt.key_size(encripeted, max_key_len)

        key = breakingToolsPt.key_refactor(encripeted, key_size)

    else:
        key_size = breakingToolsEn.key_size(encripeted, max_key_len)

        key = breakingToolsEn.key_refactor(encripeted, key_size)

    return key


