import math
# Credits:
# Uses assets from "Lap Rusher Assets" by Virgate Designs
#   https://opengameart.org/content/lap-rusher-assets

road = Actor("road", topleft=(0, 0))
road_upper = Actor("road", topleft=(0, road.height))
road_lower = Actor("road", topleft=(0, -road.height))
car = Actor("car_blue")
car.x = 200
car.y = 200
car.vx = 0
car.vy = 0

frame_count = 0
speed = 1
accel = 0.14
turningStep = 5
turbo_boost_amount = 6

def update_road():
    # Plan:
    #  1. First calculate the y-position of the central road piece
    #  2. Then place an upper and lower copy of the road

    # Implementation:
    # 1. Calculate central road section's y-position based on
    #   the car's supposed vertical speed
    road.y += car.vy
    if road.top > road.height:
        road.y -= road.height
    if road.top <= 0:
        road.y += road.height
    # 2. Place upper and lower road copies above and below central road section
    road_upper.y = road.y - road.height
    road_lower.y = road.y + road.height


def update():
    global speed, frame_count

    frame_count += 1

    # handle player inputs
    if keyboard.right:
        car.angle -= turningStep
        if car.angle < 0:
            car.angle += 360

    if keyboard.left:
        car.angle += turningStep
        if car.angle > 359:
            car.angle -= 360

    if keyboard.down:
        speed -= accel

    if keyboard.up:
        speed += accel

    if keyboard.space:
        speed += turbo_boost_amount

    speed = speed * 0.98
    move_actor_forward_in_fixed_y(car, speed)

    update_road()


def move_actor_forward_in_fixed_y(actor, spd):
    car.vx = spd * math.cos(math.radians(actor.angle))
    car.vy = spd * math.sin(math.radians(actor.angle))

    actor.x += car.vx


def draw():
    screen.fill((255, 0, 0))

    road.draw()
    road_upper.draw()
    road_lower.draw()

    car.draw()
    draw_hud()


def draw_hud():
    screen.draw.textbox("%.2f" % speed, (100, 100, 200, 50))
    screen.draw.textbox("%.2f" % (road.top), (100, 300, 200, 50))
