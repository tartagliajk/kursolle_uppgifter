'''
- Beräkna årsinkomst från månadslön och skriv ut
- Om de tjänar mindre än 19 247 kr per år så beralar de ingen skatt
- Räkna ej ut skatt om de är mindre än 19 247 kr
'''

#bl=bruttolön, yl=årslön
bl=float(input("Hej, var vänligen och skriv in din bruttolön i hela kronor, dvs inga decimaler:\n"))
yl=bl * 12

#if selektioner
if yl >= 19247:
#ks=kommunalskatt, ls=landstingsskatt & es=efter skatt
    ks=bl*0.2136
    ls=bl*0.1148
    es=bl-ks-ls
#utskrift
    print("Månadslön           {:.0f}kr (Årslön:{:.0f}kr)".format(bl, yl))
    print("Kommunal skatt      {:.0f}kr".format(ks))
    print("Landstingsskatt     {:.0f}kr".format(ls))
    print("Kvar efter skatt    {:.0f}kr".format(es))

if yl < 19247:
    print("Månadslön           {:.0f}kr (Årslön:{:.0f}kr)".format(bl, yl))
    print("Kvar efter skatt    {:.0f}kr".format(bl))
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt")