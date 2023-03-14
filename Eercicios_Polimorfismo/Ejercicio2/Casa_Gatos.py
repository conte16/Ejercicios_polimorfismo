from pinki import pinki
from piruleto import piruleto
from kiras import kiras

class casa_gatos(pinki,piruleto,kiras):
    pass
    def comer():
       
        return'En la casa de los gatos {} come {} , {} come {} y {} come {}.'.format(pinki.gato1,pinki.come,piruleto.gato2,piruleto.come, kiras.gato3, kiras.come)
desayuno = casa_gatos
print(desayuno.comer())
