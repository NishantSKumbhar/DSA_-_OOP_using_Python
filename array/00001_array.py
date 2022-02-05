"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the basic array operations.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
"""
here , i = integer array -> maximum size bytes : 2
"""

print("Array a : {}".format(a))
for i in range(len(a)):
    print("index {} : {} and id : {} ".format(i, a[i], id(a[i])))


b = arr.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])

"""
here , f = float array -> maximum size bytes : 4
"""

print("Array b : {}".format(b))
for i in range(len(b)):
    print("index {} : {:.2f} and id : {} ".format(i, b[i], id(b[i])))


"""
d : double -> maximum size bytes : 8
"""

