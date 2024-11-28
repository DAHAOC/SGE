from Cotxe import Cotxe
from Colibri import Colibri
#declaro el objecte cotxe
cotxe_1 = Cotxe("blau", 799, "100000")

#faig els gets de cotxe
print(f'El cotxe es de color: {cotxe_1.getColor()}')
print(f'El cotxe te: {cotxe_1.getCavalls()} cavalls')
print(f'El cotxe costa: {cotxe_1.getPreu()} $')

#modifico els Atributs i ho mostro  
cotxe_1.setColor("negre")
print(f'També pot ser {cotxe_1.getColor()}')

cotxe_1.setPreu(110000)
print(f'Pero costa: {cotxe_1.getPreu()} $')

#Espai per separar colibri i cotxe
print()

#Colibri 
colibri_1 = Colibri("Loero", "98km/h", 2) 
# Mostro 4 getters de colibrí
print(f'Tinc un colibri, què es diu {colibri_1.getName()}')
print(f'Els colibris volen a una velocitat de {colibri_1.getSpeed()}')
print(f'Pero com el meu colibri es ja vell perque té {colibri_1.getAge()} anys')
print(f'Vola més lent que {colibri_1.getSpeed()}')

# Modifico els getters i ho mostro 
colibri_1.setName("Peti")
print(f'El colibri del meu amic es diu: {colibri_1.getName()}')

colibri_1.setAge(1)
print(f'Es més jove que el meu colibri, i té {colibri_1.getAge()} anys')
