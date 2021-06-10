# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:43:42 2021

@author: user
"""

def KSA(key):   #key scheduling 
    length=len(key)
    S=list(range(256))
    j=0
    for i in range (256):
        j = (j+ S[i] + key[i%length])%256
        S[i], S[j]=S[j], S[i] 
    return S


def PRGA( S, n):  #pseudo random generation algorithm
    i=0
    j=0
    key=[]
    while n>0:
        n=n-1
        i=(i+1) % 256
        j = (j+S[i]) % 256
        S[i], S[j]= S[j], S[i]
        K=  S[(S[i]+S[j])  %256]
        key.append(K)
    return key


key= 'HOUSE'
text= 'MISTAKES ARE AS SERIUS AS THE RESULTS THEY CAUSE'


def prep(s):
    return [ord(c) for c in s]

def un_prep(s):
    return [chr(c) for c in s]


key = prep(key)

import numpy as np

S=KSA(key)


keystream =np.array(PRGA(S, len(text)))
print("Keystream")
print(keystream)


#text=np.array ([ord(i) for i in text])
text=np.array(prep(text))

cipher = keystream ^ text    ### Encryption

print("Encrypted: ")
print(cipher)
#print(cipher.astype(np.uint8))

original= keystream^cipher
original=un_prep(original)
str1=''
print(str1.join(original)) 





        