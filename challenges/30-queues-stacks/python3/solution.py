#!/bin/python3

import sys



class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
        
        
    def pushCharacter(self, c):
        self.stack += c
        
    def popCharacter(self):
        c = self.stack[len(self.stack) - 1]
        self.stack = self.stack[:-1]
        return c
    
    def enqueueCharacter(self, c):
        self.queue += c
       
    def dequeueCharacter(self):
        c = self.queue[0]
        self.queue = self.queue[1:]
        return c
    
    

    
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")