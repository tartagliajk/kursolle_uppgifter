#fick ej if satsen att fungera, vet dock ej varför
list=(1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000)
print('''Årsinkomst    / Månadsinkomst    / Total skatt        / Kommunals.    / Landstingss.     / Statlig s.     / Total skatt     /''')
for x in list:
    x *12
    if x >= 19247 and x < 468700:
        bl=x/12
        ks=bl*0.2136
        ls=bl*0.1148
        es=bl-ks-ls
        ts=ks+ls
        abs=(ts/bl)*100
    if x < 19247:
        bl=x/12
        print('''        {:.0f}kr /             {:.0f}kr /                0kr /           0kr /              0kr /            0kr /              0% /'''.format(x,bl))    
    if x>=468700 and x < 675700:
        ks=bl*0.2136
        ls=bl*0.1148
        bp=bl-ks-ls
        ss=bp*0.2
        es=bl-ks-ls-ss
        ts=ks+ls+ss
        abs=(ts/bl)*100
        print('''        {:.0f}kr /             {:.0f}kr /               {:.0f}kr /          {:.0f}kr /             {:.0f}kr /           {:.0f}kr /            {:.0f}%  /'''.format(x,bl,ts,ks,ls,ss,ts))    
    if x >=675700:
        ks=bl*0.2136
        ls=bl*0.1148
        bp=bl-ks-ls
        vs=bp*0.05
        ss=(bp*0.2)+vs
        es=bl-ks-ls-ss-vs
        ts=ks+ls+ss+vs
        abs=(ts/bl)*100
        print('''        {:.0f}kr /             {:.0f}kr /               {:.0f}kr /          {:.0f}kr /             {:.0f}kr /           {:.0f}kr /             {:.0f}% /'''.format(x,bl,ts,ks,ls,ss,ts))    