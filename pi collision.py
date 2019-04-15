import pygame
from math import floor
import matplotlib.pyplot as plt
pygame.init()


def getFinalVelocities(masse_one, masse_two, velocity_one, velocity_two):
	final_veloity_two = (((2*masse_one*velocity_one)/(masse_one+masse_two)))-((((masse_one-masse_two)*velocity_two)/(masse_one+masse_two)))
	final_veloity_one = (((2*masse_two*velocity_two)/(masse_one+masse_two)))+((((masse_one-masse_two)*velocity_one)/(masse_one+masse_two)))
	return [final_veloity_one, final_veloity_two]

print(getFinalVelocities(10,1000,40.68, -9.3801))
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [400, 300]

#size=[size[i]*3 for i in range(len(size))]

screen = pygame.display.set_mode(size)

Big_x = size[0]/2+20
small_x = size[0]/2-100

counter = 0
 
#pygame.display.set_caption("Example code for the draw module")
 
done = False
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 20)

Big_velocity=-1
small_velocity=0
mass_one=1
mass_two=10000

velocities=[]

velocities_small=[]

estimated_times=[]


def checkCollisions(Big_x, small_x):

    if Big_x<=(small_x+50):
        return True

    elif small_x<=17:
    	return False

 
while not done:

    clock.tick(100)

    approx_time = ((small_x+50)-Big_x)/(Big_velocity-small_velocity)

    #print(Big_velocity)
    #print(pygame.time.get_ticks()/1000.0)

    #print(approx_time)

    print(abs(small_velocity))

    velocities.append(Big_velocity)
    velocities_small.append(small_velocity)
    estimated_times.append(approx_time)


    if checkCollisions(Big_x, small_x)==True: #or approx_time<1 and approx_time>0:
        newVelocities= getFinalVelocities(mass_one,mass_two,small_velocity, Big_velocity)
        Big_velocity=newVelocities[1]
        small_velocity=newVelocities[0]
        counter+=1
        #print(newVelocities)

    elif checkCollisions(Big_x, small_x)==False:
        small_velocity=-small_velocity
        counter+=1

    Big_x+=Big_velocity
    small_x+=small_velocity

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True
 
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, [0, size[1]], [size[0], size[1]], floor(size[1]-(size[1]/2.1)))
    pygame.draw.line(screen, BLACK, [0, size[1]-size[1]/4], [0,0], 30)
 

    pygame.draw.rect(screen, RED, [Big_x, size[1]-size[1]/4-50,70,50])

    pygame.draw.rect(screen, BLUE, [small_x, size[1]-size[1]/4-30,50,30])

    text = font.render(str(counter), True, (0,0,0))

    screen.blit(text,
        (size[0]/2 - text.get_width() // 2, int(size[1] - size[1]/1.5)))

    #print(counter)
 
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    if counter==3141:
    	break


pygame.quit()

plt.subplot(2, 1, 1)
plt.plot(velocities)
plt.subplot(2, 1, 2)
plt.plot(velocities_small)
plt.show()

