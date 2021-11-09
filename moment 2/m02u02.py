#1
a=9
b=2
f=4.0
namn="Nina Vazae"

#2
test=a*b
print(test)
print(type(test))

#3
test=a*f
print(test)
print(type(test))

#4, det blir en float eftersom att svaret är i decimaler och inte heltal.
test=a/b
print(test)
print(type(test))

#5
test=namn
print(test)
print(type(test))

#6, int eftersom heltal
test=a//b
print(test)
print(type(test))

#7, float eftersom decimal
test=a%b
print(test)
print(type(test))

#9, int eftersom heltal
test=a**0,5
print(test)
print(type(test))

#10, float eftersom deci
test=b**2
print(test)
print(type(test))

#11, int eftersom heltal
test=f**2
print(test)
print(type(test))

#13, funkar ej
a=+b
print(a)