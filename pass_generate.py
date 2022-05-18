import random

# length = 8
# passwd = list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
# random.shuffle(passwd)
# passwd = ''.join([random.choice(passwd) for x in range(length)])


chars = 'abcdefghjkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
length = 8
while True:
    passwd = ''
    for c in range(length):
        passwd += random.choice(chars)
    if (any(c.islower() for c in passwd)
            and any(c.isupper() for c in passwd)
            and sum(c.isdigit() for c in passwd) >= 1):
            # print('right passwd:', passwd)
        break
        # else:
        # print('wrong passwd:', passwd)