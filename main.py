from cube import *
from solver import *
"""
    A Rubik-kocka animációja 
"""

c = Cube() #Cube object létrehozása
c.cube_method_all_side_loader() #Cube kiszínezése
c.cube_method_mixer() #Cube bekeverése ( default 20 lépés )

print(c.historystring) # bekeverés lépései
cube_solver(c) #a kocka kirakás lépéseinek legyártása

print(c.historystring) # a kirakási lépések string-je
print(len(c.historystring)) # a kirakás lépéseinek száma

"""
    Statisztikai tesztek:
"""

d = Cube()  # Összehasonlításhoz kirakott Rubik-kocka
d.cube_method_all_side_loader()
l=[] #ide gyűjti a tesztek értékét
k=[] #kirakások hossza
for i in range(100): # kb egy perc alatt megvan 1000szer ellenőrizve
    e = Cube()
    e.cube_method_all_side_loader()
    e.cube_method_mixer(100) #100 random keverési lépés
    mixer_len = len(e.historystring)
    cube_solver(e)
    l.append(cube_check(e, d)) # leellenőrzi a két kocka közötti kis cubie-kat
    k.append(len(e.historystring)-mixer_len)
print(l)
a=0
for i in range(len(l)):
    if l[i]==False: #megnézi, hogy lett e hibás cubie
       a+=1
print(a) # hibás esetek száma

print(sum(k)/100) # az átlagos kirakási lépés hossz ( ebben benne van, hogy a visszaforgatásokat, három rendes írányú forgatásként számolja )

c.cube_method_3d_drawer(c.historystring)# a kirakás animációja


