from vpython import *
from random import *

def get_horizontal_distance(target):
    
    return sqrt(target.pos.x**2 + target.pos.z**2)

def define_max_flight_height(horizontal_distance):
    
    max_flight_height = (horizontal_distance) / 2
    return max_flight_height
    
def define_launch_angle(horizontal_distance, max_flight_height):

    print(horizontal_distance / (2*max_flight_height))
    vertical_angle = 1/2 * (asin(horizontal_distance / (2*max_flight_height)))
    return vertical_angle

def define_initial_velocity(horizontal_distance, vertical_angle):

    absolute_initial_velocity = sqrt((horizontal_distance * abs(gravity)) / (sin(2 * vertical_angle)))
    return absolute_initial_velocity

def get_horizontal_angle(target_coordinates):
    
    x, z = target_coordinates.x, target_coordinates.z
    horizontal_angle = atan2(x, z)
    return horizontal_angle
    
def define_vectorial_velocity(launch_angle, horizontal_angle, absolute_initial_velocity):
    
    initial_velocity = vector(0, 0, 0)
    initial_velocity.x = absolute_initial_velocity * cos(launch_angle) * sin(horizontal_angle)
    initial_velocity.y = absolute_initial_velocity * sin(launch_angle)
    initial_velocity.z = absolute_initial_velocity * cos(launch_angle) * cos(horizontal_angle)
    
    return initial_velocity
    
def launch_projectile(target, initial_velocity):
    
    time = 0
    delta_time = 1/60
    gravity = vector(0, -9.81, 0)
    velocity = vector(0, 0, 0)
    
    projectile = sphere(radius=0.2, color=target.color, make_trail=True)
    
    while projectile.pos.y >= 0:
    
        rate(60)
        velocity = initial_velocity + gravity * time
        projectile.pos = initial_velocity * time + gravity * pow(time, 2) / 2
        
        time = time + delta_time
        
    print("Target reached in : {} s".format(time))
        
    

#Orientation Porpouses
origin = sphere(pos=vector(0, 0, 0), radius=0.2, color=color.white)
x_axis = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.red)
y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.green)
z_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.blue)

gravity = 9.81


blocks = list()
colors = [color.blue, color.orange, color.green, color.purple, color.yellow, color.cyan, color.magenta]

for x in range(100):
    for z in range(100):
        blocks.append(box(pos=vector(x-50, 0, z-50), size=vector(0.9, 0.9, 0.9), color=color.white))



#Setting random targets
targets = []
for i in range(50):
    
    target_number = randint(0, 100*100 - 1)
    blocks[target_number].color = vector(500*round(random()), 500*round(random()), 500*round(random()))
    targets.append(blocks[target_number])
    
for target in targets:
    
    print("Target coordinates: {}".format(target.pos))
    
    horizontal_distance = get_horizontal_distance(target)
    print("Distance from center: {}".format(horizontal_distance))
    
    max_flight_height = define_max_flight_height(horizontal_distance)
    print("MAX flight height: {}".format(max_flight_height))
    
    launch_angle = define_launch_angle(horizontal_distance, max_flight_height)
    print("Launch angle: {}".format(launch_angle * 180 / pi))
    
    absolute_initial_velocity = define_initial_velocity(horizontal_distance, launch_angle)
    print("Absolute initial velocity: {}".format(absolute_initial_velocity))
    
    horizontal_angle = get_horizontal_angle(target.pos)
    print("Horizontal angle: {}".format(horizontal_angle * 180 / pi))
    
    vectorial_velocity = define_vectorial_velocity(launch_angle, horizontal_angle, absolute_initial_velocity)
    print("Vectorial initial velocity: {}".format(vectorial_velocity))
    
    
    print("ALL SET FOR LAUNCH!!!!")
    
    launch_projectile(target, vectorial_velocity)
    
    print("*#" * 25)