"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the basic array operations.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
import array as arr
from re import A

a = arr.array('i', [1, 2, 3, 4, 5])
print("Before insertion : {}".format([a[x] for x in range(len(a))]))

# now insertion 
# here we are inserting 100 at 5 index
a.insert(5, 100)
print("After insertion :  {}".format([a[x] for x in range(len(a))]))

# we can also use append method -> which append the element at the last.
a.append(10000)
print("After the append : {}".format([a[x] for x in range(len(a))]))
