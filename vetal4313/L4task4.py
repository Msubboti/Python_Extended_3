from random import randint

distance = [x*randint(2, 60) for x in range(16) if x > 5]

hours = [x**2 for x in range(11)if x > 0]

speed = [x / y for x in distance for y in hours if x / y > (sum(distance) / sum(hours))]

print(speed)

print(len(speed))
