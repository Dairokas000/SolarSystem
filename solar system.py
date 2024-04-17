import turtle
import math

class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0)
        self.ssscreen.tracer(50)


    def addPlanets(self, aplanet):
        self.planets.append(aplanet)


    def addSun(self, asun):
        self.thesun = asun



    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())


            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt(rx**2 + ry**2)

            gravityx = G * self.thesun.getMass()*rx/r**3
            gravityy = G * self.thesun.getMass()*ry/r**3


            p.setXVel(p.getXVel() + dt * gravityx)


            p.setYVel(p.getYVel() + dt * gravityy)








class Sun:
    def __init__(self, sname, srad, smass):
        self.name = sname
        self.radius = srad
        self.mass = smass
        self.x = 0
        self.y = 0


        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y


    









class Planet:
    def __init__(self, pname, prad, pmass, pdist, pvx, pvy, pcolor):
        self.name = pname
        self.radius = prad
        self. mass = pmass
        self.distance = pdist
        self.x = pdist
        self.y = 0
        self.velocityx = pvx
        self.velocityy = pvy
        self.color = pcolor

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x,self.y)
        self.pturtle.down()

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velocityx

    def getYVel(self):
        return self.velocityy

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)

    def setXVel(self, newvelx):
        self.velocityx = newvelx

    def setYVel(self, newvely):
        self.velocityy = newvely
























def createSSandAnimate():
    ss = SolarSystem(2,2)

    sun = Sun("SUN", 5000, 10)
    ss.addSun(sun)

    m = Planet("Earth" , 47.5, 5000, 0.3, 0, 2.0, "green")
    ss.addPlanets(m)

    numTimePeriods = 20000
    for amove in range(numTimePeriods):
        ss.movePlanets()





createSSandAnimate()
