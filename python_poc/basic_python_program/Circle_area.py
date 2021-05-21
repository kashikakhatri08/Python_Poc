import math


def user_input():
    radius = int(input("Enter the radius: "))
    return radius


def circle_radius(radius):
    circle_radius_result = math.pi * pow(radius, 2)
    print("circle radius of radius {} is : {} ".format(radius, circle_radius_result))


def main():
    radius = user_input()
    circle_radius(radius)


main()
