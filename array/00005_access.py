"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the basic array operations.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
import array as arr

a = arr.array('f', [1.1, 2.33, 4.55, 6.44])

print("a    : {}".format([a[i] for i in range(len(a))]))

# we can access the element by subscript operator
print("a[0] : {:.2f}".format(a[0]))
print("a[1] : {:.2f}".format(a[1]))

