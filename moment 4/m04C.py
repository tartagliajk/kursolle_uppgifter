while True:
    input("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")
    while True:
        sida1=input("Skriv in ena sidan av rektangeln. OBS det måste vara heltal.\n>")
        if sida1.isnumeric() == False:
            print("Detta är inte ett positivt heltal, försök igen.")
        if sida1.isnumeric() == True:
            intsida1=int(sida1)
            break
    while True:
        sida2=input("Skriv in den andra sidans värde. OBS det måste vara ett heltal.\n>")
        if sida2.isnumeric() == False:
            print("Detta är inte ett positivt heltal, försök igen.")
        if sida2.isnumeric() == True:
            intsida2=int(sida2)
            break
    while True:
        #valde att göra så att använderen ska skriva in ett positivt heltal och därmed kan inga negativa tal läggas in
        height=input("Skriv in höjden. OBS det måste vara ett heltal.\n>")
        if height.isnumeric() == False:
            print("Detta är inte ett positivt heltal, försök igen.")
        if height.isnumeric() == True:
            intheight=int(height)
            break
    if intheight > 10:
        intheight = 10
    area=intsida1*intsida2
    input("Rektangeln har sidorna {} och {}, vilket gör att arean är {}.".format(intsida1,intsida2,area))
    if intsida1 == intsida2:
        input("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
    if intsida1 != intsida2:
        input("Eftersom att sidorna är inte lika långa så är det inte en kvadrat.")
    print("Höjden      ┃    Volymen")
    print("------------------------")
    if intheight == 10:
        for i in range(1,11):
            volym=area*i
            print("        {}   ┃    {}".format(i,volym))
    if intheight <= 9:
        for i in range (1,intheight+1):
            volym=area*i
            print("        {}   ┃    {}".format(i,volym))
    #cont=continue
    cont=input("Vill du göra en till beräkning? [j/n]\n>")
    cont=cont.lower()
    if cont == "j":
        print("\n")
    if cont == "n":
        print("Tack för att du använde pogrammet.")
        break