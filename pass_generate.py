import random
length = 8
passwd = list('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
random.shuffle(passwd)
passwd = ''.join([random.choice(passwd) for x in range(length)])