#Pennor
pencil=4
pencil_nr=3
pencil_p=pencil*pencil_nr

#äpple
apple_nr=1
apple_w=0.2
apple_p=19*apple_w

#total summa
total=apple_p+pencil_p

print("Jag har handlat {} pennor för {}kr och {} äpple för {}kr vilket blev toalt {}.".format(pencil_nr, pencil_p,apple_nr, apple_p,total))

#lägga in värden själv
pn=int(input("Hur många pennor har du köpt?"))
apple_nr=int(input("Hur många äpple har du köpt?"))
apple_we=float(input("Hur mycket väger äpplerna, svara i kg"))
pencil_p=pn*pencil
apple_p=apple_nr*apple_we*19
total=pencil_p+apple_p
print("Jag har handlat {} pennor för {}kr och {} äpple för {}kr vilket blev toalt {}.\n".format(pn, pencil_p,apple_nr, apple_p,total))

#utskrifter
#1
print("Jag handlade", 3, "pennor för", 12,"kr och", 1," äpple för", 3.80,"kr vilket totalt blev", 15.80,"kr.")

#2
a="Jag handlade 3 pennor för 12kr"
b="och 1 äpple för 3.80kr vilket totalt blev 15.80kr."
print(a+b)

#3
c="Jag handlade 3 pennor för 12kr och 1 äpple för 3.80kr vilket totalt blev 15.80kr."
print(c)

#4
print()

#5
print("Jag har handlat {} pennor för {}kr och {} äpple för {}kr vilket blev toalt {}.".format(pn, pencil_p,apple_nr, apple_p,total))

#6
print(f"Jag handlade {pencil_nr} pennor för {pencil_p}kr och {apple_nr} äpple för {apple_nr}kr vilket totalt blev {total}kr.")  