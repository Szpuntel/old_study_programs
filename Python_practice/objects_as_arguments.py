from calendar import c


class Car:

    color = None


class Motor:

    color = None

def change_color(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

motor = Motor()

change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "bleck")
change_color(motor, "grrrrreeeen")


print(car_1.color)
print(car_2.color)
print(car_3.color)

print(motor.color)