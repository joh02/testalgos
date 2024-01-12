# see https://www.pinterest.de/pin/2674081022192913/
# the decimal challange :)
#
#
#
#


def str1(n):
    '''
    :param n: 1-9
    :return: Zahlenstring z.B. n=5 --> '12345'
    '''
    s=''
    for i in range(n):
        s += str(i+1)
    return s


for i in range(1,10):
    print(int(str1(i)) * 8 + i)

print(80*'-','\n')

for i in range(1,10):
    print(int(str1(i)) * 9 + 1 + i)

print(80*'-','\n')

def str2(n):
    '''
    :param n: 1-8
    :return: str z.B. n=3 --> '987'
    '''
    s=''
    for i in range(n):
        s += str(9-i)
    return s

for n in range(1,8+1):
    print(int(str2(n))*9+8-n)

print(80*'-','\n')

def str3(n):
    '''
    :param n: int 1..9
    :return: z.B. n=3 --> '111'
    '''
    return '1'*n

for n in range(1,9+1):
    z = int(str3(n))
    print(z**2)
