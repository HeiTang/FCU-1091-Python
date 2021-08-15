def GCD(m, n):
    return m if n == 0 else GCD(n, m % n)
def LCM(m, n):
    return m * n // GCD(m, n)

a, b = eval(input('')) # 此行勿改

gcd = GCD(a, b)
lcm = LCM(a, b)
print ('gcd = {}; lcm = {}'.format(gcd, lcm)) # 此行勿改