from sysconfig import get_python_version
from controller import Robot, Motor, Keyboard, Camera, DistanceSensor, CameraRecognitionObject, DistanceSensor

class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)


class SeatechRobot(Robot, Camera): #, DistanceSensor):
    def __init__(self):
        super().__init__()
        self.__leftMotor = RobotMotor('left wheel motor')
        self.__rightMotor = RobotMotor('right wheel motor')
        self.cam = EpuckCamera('camera')

    def run(self):
        self.__leftMotor.setVelocity(MAX_SPEED)
        self.__rightMotor.setVelocity(MAX_SPEED)

    def backward(self):
        self.__leftMotor.setVelocity(-MAX_SPEED)
        self.__rightMotor.setVelocity(-MAX_SPEED)       

    def turn_left(self):
        self.__leftMotor.setVelocity(-MAX_SPEED)
        self.__rightMotor.setVelocity(MAX_SPEED)

    def turn_right(self):
        self.__leftMotor.setVelocity(MAX_SPEED)
        self.__rightMotor.setVelocity(-MAX_SPEED)


    #radar0 = DistanceSensor("ps0")
    #radar1 = DistanceSensor("ps1")
    #radar2 = DistanceSensor("ps2")
    #radar3 = DistanceSensor("ps3")
    #radar4 = DistanceSensor("ps4")
    #radar5 = DistanceSensor("ps5")
    #radar6 = DistanceSensor("ps6")
    #radar7 = DistanceSensor("ps7")

    #radar0.enable(samplingPeriod=50)
    #radar1.enable(samplingPeriod=50)
    #radar2.enable(samplingPeriod=50)
    #radar3.enable(samplingPeriod=50)
    #radar4.enable(samplingPeriod=50)
    #radar5.enable(samplingPeriod=50)
    #radar6.enable(samplingPeriod=50)
    #radar7.enable(samplingPeriod=50)

    
    
    #def flee_turn(self):
    #    for i in range(8):
    #        radari = self.getValue()/4096
    #    if (max(radari) == 0.02):


class EpuckCamera(Camera):
    def __init__(self, name):
        super().__init__(name)
        self.enable(samplingPeriod=50)
        self.recognitionEnable(samplingPeriod=100)


    def getRecognitionObjects(self):
        window_min = int(0.25*self.getWidth())
        window_max = int(0.75*self.getWidth())
        objets = super().getRecognitionObjects()
        for objet in objets:
            if (objet.get_colors() == [1, 0, 0]):
                if (window_min < objet.get_position_on_image()[0] < window_max): 
                    robot.backward()
            else :
                pass
                

if __name__ == '__main__':
    TIME_STEP = 64
    MAX_SPEED = 6.28

    # create the Robot instance.
    robot = SeatechRobot()
    keyboard = Keyboard()
    keyboard.enable(samplingPeriod=100)


    while robot.step(TIME_STEP) != -1:
        robot.cam.getRecognitionObjects()
        key = keyboard.getKey()
        if key == keyboard.LEFT:
            print('A GAUCHE A GAUCHE ABRUTI')
            robot.turn_left()

        elif key == keyboard.RIGHT:
            print('A DROITEUUUUH')
            robot.turn_right()

        elif key == keyboard.DOWN:
            print("OK J'arrête")
            robot.backward()
            
        elif key == keyboard.UP:
            print('hm ouais hein')
            robot.run()

