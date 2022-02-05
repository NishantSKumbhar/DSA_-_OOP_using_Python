"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the basic array operations.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])

for i in range(len(a)):  # this will print the numbers in assending order
    print(a[i])

print('*' * 20)

for i in range(len(a)-1, -1, -1):    # this will print the numbers in desending order
    print(a[i])

print('*' * 20)