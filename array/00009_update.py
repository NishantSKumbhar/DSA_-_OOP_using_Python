"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the basic array operations.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""

import array as arr

# we can also update the array by subscript operator

l = [1, 2, 3, 4, 5, 6, 7]
a = arr.array('i', l)

print("Before Updating : {}".format([a[i] for i in range(len(a))]))

a[3] = 99
a[1] = 777

print("After Updating : {}".format([a[i] for i in range(len(a))]))
