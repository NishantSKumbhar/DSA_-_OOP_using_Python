"""
@author  : Nishant Sanjay Kumbhar.
@goal    : To implement the basic array operations.
@github  : https://github.com/NishantSKumbhar
@spotify : https://open.spotify.com/playlist/5xxjcOn9Dt8dhTCrN6S7Wb?si=e926b46a636a4d22
"""
import array as arr
from tkinter import N
num = int(input("How many elements do you want to insert in array : "))
l=[]
print("Enter the {} numbers -> ".format(num))
for i in range(0,num):
    l_ = int(input())
    l.append(l_)

a = arr.array('i', l)

# to get the index of any element use index(element) i.e first occurence of that element.

print("Here is your array : ")
for i in range(len(a)):
    print(a[i], end = " ")
print()

n = int(input("Choose the Element to get the index : "))
if n in a:
    print(a.index(n))
else:
    print("Sorry , this element does not occour in array .")

