"""
@author  : Nishant Sanjay Kumbhar.
@goal    : Convert Decimal to Binary.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
#  type 1
a = 14
print("Binary Form : {0:b}".format(a))

# type 2

def decimal_to_binary(num: int):
    if num > 1:
        decimal_to_binary(num // 2)
    
    print("Binary Formation : {}".format(num % 2))


number = int(input("Enter the Number to Convert in Binary : "))
decimal_to_binary(number)
