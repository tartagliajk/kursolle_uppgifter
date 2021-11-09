pencil=3
pn=int(input("Hur många pennor har du köpt?"))
apple_nr=int(input("Hur många äpple har du köpt?"))
apple_we=float(input("Hur mycket väger äpplerna, svara i kg"))
pencil_p=pn*pencil
apple_ogp=22.9
apple_p=int(apple_nr*apple_we*apple_ogp)
total=pencil_p+apple_p

print('''\nPenna, {}st á {}kr                    {}kr'''.format(pn, pencil, pencil_p))
print('''Äpplen, {}kg á {}kr              {}kr'''.format(apple_we,apple_ogp, apple_p))
print('''----------------------------------------- ''')
print('''Summa                               {}kr'''.format(total))