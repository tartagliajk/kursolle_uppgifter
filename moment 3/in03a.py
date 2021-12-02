'''
- fråga användare efter bruttolön i hela kronor
- råkna ut kommunalskatt och landstingsskatt
'''

#bl=bruttolön
bl=float(input("Hej, var vänligen och skriv in din bruttolön i hela kronor, dvs inga decimaler:\n"))
#ks=kommunalskatt, ls=landstingsskatt & es=efter skatt
ks=bl*0.2136
ls=bl*0.1148
es=bl-ks-ls
#utskrift
print("Månadslön           {:.0f}kr".format(bl))
print("Kommunal skatt      {:.0f}kr".format(ks))
print("Landstingsskatt     {:.0f}kr".format(ls))
print("Kvar efter skatt    {:.0f}kr".format(es))