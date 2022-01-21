import time 

class Human():
    sexe = ['homme', 'femme', 'non-binaire', 'autres?!']
    
    

    def __init__(self, sexe='non-binaire'):
        self.sexe = sexe
        self.estomac = ['petit-dej']

    def eat(self, aliment):
        self.estomac.append(aliment)
        if (len(self.estomac) > 10):
            print('Humain a déjà bien mangé')
            
        #     percent = 0
        # for percent in range(10):
        #     time.sleep(10)
        #     self.estomac.pop(0) 
        #     percent +=1

        if (len(self.estomac) <= 3):
            print('ON A FAIM!')
