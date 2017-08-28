import sys
sys.setrecursionlimit(1000000)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def pow_mod(x, y, z):
    #"Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

n = 20473673450356553867543177537
p = 2165121523231
q = 9456131321351327
e = 17

phi = (p-1)*(q-1)

d = mulinv(e,phi)
m = ''
message = ''

f = open('enc.txt','r')
a = f.readlines()
for c in a:
    c = int(c)
    m = pow_mod(c,d,n)
    m = hex(m)[2:-1].strip().decode('hex')
    message += m

print message