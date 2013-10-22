# -*- coding: utf-8 -*-

#this file will call another file whose name is encrypt.

import encrypt
 
e = encrypt.Encrypt()

print
print(e)
s1 = "There is no spoon."
print("input: " + s1)
s2 = e.toEncode(s1)
print("encode: " + s2)
s3 = e.toDecode(s2)
print("decode: " + s3)
print
