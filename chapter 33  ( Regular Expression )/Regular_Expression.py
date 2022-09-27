import re

mystr='''A Block, Shivasagar Estate,
Dr. Annie Besant Road,
Worli, Mumbai - 400018
+91(22) 67577200

Area office Commercial and Passenger Vehicles
Tata Motors Ltd
4th Floor, Live in Tower,
N.H.Bye pass,
Opp. Gold Souk, Vyttila,
Cochin - 682 019
Contact: 0484 6601400

Regional office Commercial and Passenger Vehicles
Tata Motors Ltd
2nd & 3rd floor, Rene Tower,
1842 Rajdanga Main Road,
Kasba, P.O - EKTP,
Kolkata - 700107,
West Bengal '''

# patt=re.compile(r"Tata")
# patt=re.compile(r".ors")
# patt=re.compile(r"^A")
# patt=re.compile(r"al $")
# patt=re.compile(r"of*")
patt=re.compile(r"of+")


match=patt.finditer(mystr)

for i in match :
    print(i)