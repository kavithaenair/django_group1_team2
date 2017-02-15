def gcd(a,b):
    if a == 0:
      return b
    while b != 0:
      if a>b:
        a -= b
      else
        b=b-a
     return a
     
     
def test_gcd():
     assert gcd(48,64) == 16
     assert gcd(44,19) == 1
test_gcd()
