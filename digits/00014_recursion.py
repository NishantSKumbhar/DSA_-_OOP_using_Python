"""
@author  : Nishant Sanjay Kumbhar.
@goal    : Recursion. In python Max limit -> 1000 times
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""


def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

a = factorial(5)
print(a)
