'''
- om årslön är större än 468 700 kr, statlig skatt 20%
- om årslön är större än 675 700 kr, statllig skatt 20% & värnskatt 5%
'''

#bl=bruttolön, yl=årslön
bl=float(input("Hej, var vänligen och skriv in din bruttolön i hela kronor, dvs inga decimaler:\n"))
yl=bl * 12

#if selektioner
if yl >= 19247 and yl < 468700:
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

#ss=statlig skatt, bp=över från brytpunkt
if yl>=468700 and yl < 675700:
    ks=bl*0.2136
    ls=bl*0.1148
    bp=bl-ks-ls
    ss=bp*0.2
    es=bl-ks-ls-ss
    print("Månadslön           {:.0f}kr (Årslön:{:.0f}kr)".format(bl, yl))
    print("Kommunal skatt      {:.0f}kr".format(ks))
    print("Landstingsskatt     {:.0f}kr".format(ls))
    print("Statlig skatt       {:.0f}kr".format(ss))
    print("Kvar efter skatt    {:.0f}kr".format(es))

#vs=värnskatt
if yl>=675700:
    ks=bl*0.2136
    ls=bl*0.1148
    bp=bl-ks-ls
    vs=bp*0.05
    ss=(bp*0.2)+vs
    es=bl-ks-ls-ss-vs
    print("Månadslön           {:.0f}kr (Årslön:{:.0f}kr)".format(bl, yl))
    print("Kommunal skatt      {:.0f}kr".format(ks))
    print("Landstingsskatt     {:.0f}kr".format(ls))
    print("Statlig skatt       {:.0f}kr".format(ss))
    print("Kvar efter skatt    {:.0f}kr".format(es))