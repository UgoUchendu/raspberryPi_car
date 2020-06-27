import pygame
from gpiozero import Robot

# Axis 0, 1  - Left joystick
# Axis 2, 3  - Right joystick

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

xbox = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())][0]
xbox.init()

robby = Robot(left=(7, 8), right=(10, 9))

while True:
    try:
        pygame.event.get()

        # Get the locations of the joystick
        ax1 = -xbox.get_axis(1)
        ax4 = (xbox.get_axis(4) + 1) / 2
        ax5 = (xbox.get_axis(5) + 1) / 2

        # axis originally from -1 to 1
        # we need a value from 0 to 1
        # 0 ==> 0.5
        # -1 ==> 0
        # 1 ==> 1

        # add 1 to move the range to 0 - 2
        # then divide the number by 2

        # 0: 0 + 1 = 1. 1 /2 = 0.5
        # 0.75: 0.75 + 1 = 1.75. 1.75 / 2 = 0.875
        print(ax4, ax5)
        # Left 5 right 4
        if ax1 > 0:
            if ax5 > 0:  # left trigger is down
                robby.forward(speed=abs(ax1), curve_left=ax5)
            elif ax4 > 0:  # right trigger is down
                robby.forward(speed=abs(ax1), curve_right=ax4)
            else:
                robby.forward(abs(ax1))

        else:
            if ax5 > 0:
                robby.backward(speed=abs(ax1), curve_left=ax5)
            elif ax4 > 0:
                robby.backward(speed=abs(ax1), curve_right=ax4)
            else:
                robby.backward(abs(ax1))

        clock.tick(20)
    except KeyboardInterrupt:
        break

pygame.quit()
