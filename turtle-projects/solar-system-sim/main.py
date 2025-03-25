from turtle import Turtle, Screen
import math




screen = Screen()
screen.bgcolor("black")
screen.title("Solar System Simulation")
screen.screensize(400,600)


sun = Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2)
sun.penup()
sun.goto(0,0)


base_speed = 0.5
base_distance =50

planets = []

def create_planet(color, size, distance_multiplier):
    #  Using Kepler's Third Law: The farther a planet is from the sun, the slower it orbits.
    distance = base_distance * distance_multiplier
    speed = base_speed/  math.sqrt(distance_multiplier)
    planet = Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(size)
    planet.penup()
    planet.goto(0,-distance)
    planets.append([planet, distance, 0, speed])

create_planet("gray", 0.3, 1)
create_planet("orange", 0.5, 1.5)
create_planet("blue", 0.6, 2)
create_planet("red", 0.4, 2.8)

    
    

def move_planets():
    
    for p in planets:
        
        planet, radius, angle, speed = p
        planet.pendown()
        angle += speed
        x = radius * math.sin(math.radians(angle))
        y = -radius * math.cos(math.radians(angle))
        planet.goto(x, y)
        p[2] = angle  # update angle
    screen.ontimer(move_planets, 20)

move_planets()
screen.mainloop()

