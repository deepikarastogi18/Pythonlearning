#to view all the keywords
import keyword
print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
 #'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
 #'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 #'try', 'while', 'with', 'yield']

a=45
_=10
print(_)
_=_+1
print(_)

#variable name cannot start with special characters and numbers
#below are invalid names
#123abc
#$df
#&355


#Can check type of vairable by using type
pi=3.14
name="deepika"
Isfemale=True
print(type(pi))
print(type(name))
print(type(Isfemale))

Complex_number=2+3j
print(Complex_number.real)
print(Complex_number.imag)
