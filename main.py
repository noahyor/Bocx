"""This example spawns (bouncing) balls randomly on a L-shape constructed of 
two segment shapes. Displays collsion strength and rotating balls thanks to 
friction. Not interactive.
"""

import random
import sys

import pygame

import pymunk
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = True


def draw_collision(arbiter, space, data):
    for c in arbiter.contact_point_set.points:
        r = max(3, abs(c.distance * 5))
        r = int(r)

        p = pymunk.pygame_util.to_pygame(c.point_a, data["surface"])
        pygame.draw.circle(data["surface"], pygame.Color("black"), p, r, 1)


def main():

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running = True

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    # disable the build in debug draw of collision point since we use our own code.
    draw_options.flags = (
        draw_options.flags ^ pymunk.pygame_util.DrawOptions.DRAW_COLLISION_POINTS
    )
    ## Balls
    balls = []

    ### walls
    static_lines = [
        pymunk.Segment(space.static_body, (0.0, 100.0), (600.0, 100.0), 0.0),
        pymunk.Segment(space.static_body, (0.0, 600.0), (0.0, 100.0), 0.0),
        pymunk.Segment(space.static_body, (600.0, 600.0), (600.0, 100.0), 0.0),
        pymunk.Segment(space.static_body, ())
    ]
    for l in static_lines:
        l.friction = 0.5
        l.elasticity = 0.75
    space.add(*static_lines)
            
    mass = 0.1
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = 300, 400
    ball = pymunk.Circle(body, radius, (0, 0))
    ball.friction = 0.5
    ball.elasticity = 1.0
    space.add(body, ball)
    
    ch = space.add_collision_handler(0, 0)
    ch.data["surface"] = screen
    ch.post_solve = draw_collision

    left = False
    right = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_DOWN:
                    center_world = ball.body.local_to_world((0,0))
                    ball.body.apply_impulse_at_world_point((0,-40),center_world)
                elif event.key == pygame.K_RIGHT:
                    right = True
                elif event.key == pygame.K_LEFT:
                    left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                elif event.key == pygame.K_RIGHT:
                    right = False
        if right:
            ball.body.angular_velocity -= 0.5
        elif left:
            ball.body.angular_velocity += 0.5


        ### Clear screen
        screen.fill(pygame.Color("white"))

        ### Draw stuff
        space.debug_draw(draw_options)

        framerate = 50
        
        ### Update physics
        dt = 1.0 / framerate
        for x in range(1):
            space.step(dt)

        ### Flip screen
        pygame.display.flip()
        clock.tick(framerate)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    sys.exit(main())