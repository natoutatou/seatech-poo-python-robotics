from robot import Robot 
from human import Human 

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        super().__init__(name)
        Human.__init__(self, sexe)
        super().__init__(sexe)



#cyborg = Cyborg('Deux Ex Machina', 'M')

#print(cyborg.name, 'sexe', cyborg.sexe)
#print('Charging battery...')
#cyborg.charge()
#cyborg.status()
#cyborg.eat('banana')
#cyborg.eat(['coca', 'chips'])
#cyborg.digest()