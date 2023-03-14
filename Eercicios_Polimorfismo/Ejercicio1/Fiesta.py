from amigo1 import amigo_1
from amigo2 import amigo_2

class Fiesta(amigo_1,amigo_2):
    pass
    def bailar():
       
        return'En la fiesta de año nuevo , {} y {}  bailaron hasta el amanecer'.format(amigo_1.invitado1,amigo_2.invitado2)
bailan = Fiesta
print(bailan.bailar())
