from random import randint
def generate_access_code():
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    code = ''
    for _ in range(30):
        code = f'{code}{chars[randint(0, len(chars)-1)]}'
    return code