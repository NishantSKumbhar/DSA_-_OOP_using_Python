"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the basic array operations.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
import array as arr

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)

print("Initially the array     : ", end=" ")
for i in range(len(a)):
    print(a[i], end=" ")
print()

slice_1 = a[:]
print("After slicing [:]       : ", end=" ")
for i in range(len(slice_1)):
    print(slice_1[i], end=" ")
print()

slice_2 = a[1:]
print("After slicing [1:]      : ", end=" ")
for i in range(len(slice_2)):
    print(slice_2[i], end=" ")
print()

slice_3 = a[3:]
print("After slicing [1:]      : ", end=" ")
for i in range(len(slice_3)):
    print(slice_3[i], end=" ")
print()

slice_4 = a[1:7]
print("After slicing [1:7]     : ", end=" ")
for i in range(len(slice_4)):
    print(slice_4[i], end=" ")
print()

# to print the array in reverse ->
slice_5 = a[::-1]
print("After slicing [::-1]    : ", end=" ")
for i in range(len(slice_5)):
    print(slice_5[i], end=" ")
print()

slice_6 = a[:-5]
print("After slicing [:-5]     : ", end=" ")
for i in range(len(slice_6)):
    print(slice_6[i], end=" ")
print()

slice_7 = a[-5:]
print("After slicing [-5:]     : ", end=" ")
for i in range(len(slice_7)):
    print(slice_7[i], end=" ")
print()
