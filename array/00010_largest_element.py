"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To find the Largest Element in array.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""

import array as arr


def largest( arr, n):
    max = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    
    return max

a = arr.array('i', [1, 2, 78, 45, 33, 55])

l = largest(a, len(a))
print("Largest Element : ", l)
