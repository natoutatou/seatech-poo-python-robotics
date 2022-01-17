class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """
    	
    def __init__(self, name=None):
        if name:
            self.__name = name
        global ROBOT_COUNT
        ROBOT_COUNT += 1


    def __init__(self, power=False):  
      if (power == True):
        self.__states = 'Running'
        self.__power = True
      else:
        self.__states = 'Sutdown'


def charge (self, __battery_level):
  if (__battery_level>80):
    print("Robot chargé à au moins 80%, chargez plus tard")
  else:
    charge_length = 101 - __battery_level
  for i in range(charge_length):
    print(__battery_level)
    __battery_level += 1
  print("Le Robot est chargé")

#def move (self, __current_speed):

r = Robot(power=True)
r.__name = "Roger"
print(r.__name)
charge(r, 7)



