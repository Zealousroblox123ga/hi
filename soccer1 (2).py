## assinng value  and printing
import random

manager=10000000
print(manager)
print("messi=10000, cristono ronoldo=10000, neymer=900, mbappe=900, halland=800, lewendoski=800, kevin de buryne=700, Virgil van Dijk=700, Luis Suarez=700, Sadio Mane=600, Harry Kane=700, Karim Benzema=600, Zlatan Ibrahimovic=1000, Antoine Griezmann=800, Sergio Ramos=600, Mohamed Salah=400, David Silva=850, Gareth Bale=550, Toni Kroos=480, Eden Hazard=150, Paulo Dybala=220, Pierre-Emerick Aubameyang=720, Thomas Muller=380, Son Heung-min=420, Marcelo=570, Jadon Sancho=660 ")
##the player dicanaroy
d={"messi":10000, 
   "cristono ronoldo":10000, 
   "neymer":900, 
   "mbappe":900, 
   "halland":800, 
   "lewendoski":800, 
   "kevin de buryne":700, 
   "Virgil van Dijk":700, 
   "Luis Suarez":700, 
   "Sadio Mane":600, 
   "Harry Kane":700, 
   "Karim Benzema":600, 
   "Zlatan Ibrahimovic":1000, 
   "Antoine Griezmann":800, 
   "Sergio Ramos":600, 
   "Mohamed Salah":400, 
   "David Silva":850, 
   "Gareth Bale":550, 
   "Toni Kroos":480, 
   "Eden Hazard":150, 
   "Paulo Dybala":220, 
   "Pierre-Emerick Aubameyang":720, 
   "Thomas Muller":380, 
   "Son Heung-min":420, 
   "Marcelo":570, 
   "Jadon Sancho":660}
##loops and inputs buying selling
i=12
players=[]
while (i!=0):
 buy=input("player want to get")
 if buy in d: 
   manager=manager-d[buy]
   print(manager)   
   players.append(buy)
   print(players)
   if (manager<d[buy]):
      print("not enough money to buy")
      sell=input(" you dont have enough whould you like to sell one or 2 players or just buy a difrient player if  you  want to sell 1 or 2 players type yes if buy difrint player type no  ")
      if sell==("yes"):
        print(players)
        sell1=input("what player do you want to sell")
        players.remove(sell1)
        print(players)
        manager=manager+d[sell1]
        print(manager)
        
   i=i-1

temp_list=["psg is the team your versusing ","bvb is the team your versusing","Barcelona is the team your versusing"]
print(random.choice(temp_list))
##make a list 
a=["messi", "cristono ronoldo", "neymer", "mbappe", "halland", "lewendoski", "kevin de buryne", "Virgil van Dijk", "Luis Suarez", "Sadio Mane", "Harry Kane", "Karim Benzema", "Zlatan Ibrahimovic", "Antoine Griezmann", "Sergio Ramos", "Mohamed Salah", "David Silva", "Gareth Bale", "Toni Kroos", "Eden Hazard", "Paulo Dybala", "Pierre-Emerick Aubameyang", "Thomas Muller", "Son Heung-min", "Marcelo", "Jadon Sancho"]
## now make it chose 12 random strings from the list
c=random.sample(a, k=12)
print(c)
## now in need to put gifs
from PIL import Image
from IPython.display import display

gif_file = "messigame.gif"
image = Image.open(gif_file)
display(image)






  
