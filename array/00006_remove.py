"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the basic array operations.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Initially the array : ", end=" ")
for i in range(len(a)):
    print(a[i], end=" ")
print()
a.pop()

print("After using pop()   : ", end=" ")
for i in range(len(a)):
    print(a[i], end=" ")
print()
a.pop(5)  # delete the 5th index element

print("After using pop(5)  : ", end=" ")
for i in range(len(a)):
    print(a[i], end=" ")
print()
# remove is used to remove the first occurence of n element
# for that purpose we add the same element in array
a.append(1)
a.append(3)

print("New the array       : ", end=" ")
for i in range(len(a)):
    print(a[i], end=" ")
print()

# so now we can use remove(1) ->
# remove the first occurence of 1
a.remove(1)
print("Removing the first occurence the array       : ", end=" ")
for i in range(len(a)):
    print(a[i], end=" ")
print()

