import turtle
import pygame
import math

# Axis 0, 1  - Left joystick
# Axis 2, 3  - Right joystick

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

xbox = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())][0]
xbox.init()

SPEED = 5
print(xbox.get_name())
while True:
    try:
        pygame.event.get()

        # Get the locations of the joystick
        ax0 = xbox.get_axis(0)
        ax1 = - xbox.get_axis(1)

        # Use these locations to power the turtle
        pos = turtle.pos()
        mov = turtle.Vec2D(ax0, ax1)

        # Combine the movement with our position
        new_pos = pos + SPEED * mov

        if ax0 != 0 and ax1 != 0:
            # print(f"Heading: {turtle.heading()}")
            # print(f"Angle Between: {angle_between}")
            angle = turtle.towards(new_pos)
            turtle.setheading(angle)

        turtle.setpos(new_pos)
        clock.tick(20)
    except KeyboardInterrupt:
        break

pygame.quit()
