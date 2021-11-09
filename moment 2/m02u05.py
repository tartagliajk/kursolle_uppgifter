#inget fullt varibel namn, fixas genom att ha ett nytt varibel namn, 8,82 är inte att tal utan en tuple så man måste skriva 8.82
exchange = 8.82

#inga "", så de blir ingen sträng, fixas genom att lägga ""
print("Detta är ett program där vi kan växla mellan SEK & dollar")

#man kan inte börja varibelnamn med siffror, tar bort 1. ingen " islutet av strängen, måste även diffinera att inputen är en int
sek = int(input("Hur många SEK vill du växla till dollar:"))

#ändra varibel namn till de som funkar
dollar = sek / exchange

#det ska inte vara ngr 1 & 0 i {}, plus det saknas en parantes i slutet
print("Du ville växla {} SEK vilket blir {} dollar.".format(sek, dollar))