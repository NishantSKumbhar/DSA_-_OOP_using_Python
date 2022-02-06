"""
@author  : Nishant Sanjay Kumbhar.
@goal    : Separate the Digits of Number.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
# type 1
num = int(input("Enter the Number : "))
"""
for i in str(num):
    print(int(i))

"""
# type 2

while(num > 0):
    digit = num % 10
    print(digit)
    num = num // 10

