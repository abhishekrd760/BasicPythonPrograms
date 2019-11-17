class Rocket():
    reach = 0
    def __init__(self):
        print("the Rocket reached stratosphere")

class Marsrover(Rocket):
    def __init__(self):
        Rocket.__init__(self)
        print("The MarsRover Reached Mars")
        print("The MarsRover is launched by ISRO")

m = Marsrover()




