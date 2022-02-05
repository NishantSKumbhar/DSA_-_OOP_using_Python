"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the Bitwise Operator.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""

a = 10
b = 4
print("Decimal -> a : {} \nDecimal -> b : {}".format(a, b))
print("Binary ->  a : {0:b}".format(a))
print("Binary ->  b : {0:b}".format(b))

# bitwise operator :
print("a & b : ", a&b)
print("a | b : ", a|b)
print("~a    : ",~a)       # this is ones complement
print("a ^ b : ", a ^ b)