while True:
    input("Denna applikation gör ett antal beräkningar på en rektangel/rätblock.")
    sida1=int(input("Skriv in ena sidan av rektangeln. OBS det måste vara heltal.\n>"))
    sida2=int(input("SKriv in den andra sidans värde. OBS det måste vara ett heltal.\n>"))
    area=sida1*sida2
    input("Rektangeln har sidorna {} och {}, vilket gör att arean är {}.".format(sida1,sida2,area))
    if sida1 == sida2:
        input("Eftersom bägge sidorna är lika långa så är denna rektangel en kvadrat.")
    if sida1 != sida2:
        input("Eftersom att sidorna är inte lika långa så är det inte en kvadrat.")
    print("Höjden      ┃    Volymen")
    print("------------------------")
    for i in range (0,11):
        volym=area*i
        print("        {}   ┃    {}".format(i,volym))
    #cont=continue
    cont=input("Vill du göra en till beräkning? [j/n]\n>")
    cont=cont.lower()
    if cont == "j":
        print("\n")
    if cont == "n":
        #tyckte det var onödigt att ha med den senaste uträckningen som uppgiften hade
        print("Tack för att du använde pogrammet.")
        break