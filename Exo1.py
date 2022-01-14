class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """


    def __init__(self, name)


    def __init__(self, power=False):  
      if (power == True):
        self.__states = 'Running'
        self.__power = True
      else
        self.__states = 'Sutdown'

    def __init__(self, states, __battery_level, )


r = Robot(power=True)