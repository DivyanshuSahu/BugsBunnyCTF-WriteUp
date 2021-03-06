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

n = 412460203584740978970185080155274765823237615982150661072746604041385717906706098256415230390148737678989448404730885157667896599397615737297545930957425615121654272472589331747646564634264520011009284080299605233265170506809736069720838542498970453928922703911186788239628906189362646418960560442406497717567

d = '0x3ddba53a9dcd14a91e9d668a7572b4d930b65620008e7c017b2bca2f82ea6ec7L'
d = d[2:-1]
d = int(d,16)

c = '0x217c8bf9b45601267624c3b1ba89ae93d04c8fae32dc15496262f36f48d06c0dc9e178a77b77a33708dcbe1fcd55ea9eb636fe5684c2f0f08df3389f47b36a128636671eba300491c829ed1e252b1bb4dbb3b93bc46d98a10bb5d55347752052ab45e143fd46799be1d06ac3ff7e8b1eb181dfbba8dfac3910202fd0b9a25befe'
c = c[2:]
c = int(c,16)

m = pow_mod(c,d,n)
m = hex(m)[2:-1].decode('hex')
print m

