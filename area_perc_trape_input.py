#!/usr/bin/env python3
# Created By:Adrian student
# Date: Oct 10, 2026
# This program asks the user for the top base , bottom base ,
# left leg , right leg and height of a trapezium and then
# calculates its area and perimeter


def main():
    # set the unit of measurement 
    unit = input("Enter the unit of measurement(m , mm , cm) :")

    # get the top base value from the user
    top_base = int(input(f"Enter top base value ({unit}) : " ))

    # get the bottom base value from user
    bottom_base = int(input(f"Enter bottom base value ({unit}): "))

    # get the right leg value from user
    right_leg = int(input(f"Enter the right leg value ({unit}): "))

    # get the left leg value from user
    left_leg = int(input(f"Enter the left leg value ({unit}): "))

    # get the height from user
    height = int(input(f"Enter the height ({unit}): "))

    # calculate the area of the trapezium
    area = float(0.5 * (bottom_base + top_base) * height)

    # calculate the perimeter of the trapezium
    perimeter = right_leg + left_leg + bottom_base + top_base

    # display the area of the trapezium
    print("")
    print("The area of the trapezium is :{:,.2f}{}".format(area, unit + "²"))

    # display the perimeter of the trapezium
    print("")
    print("The perimeter of the trapezium is :{}{}".format(perimeter, unit))


if __name__ == "__main__":
    main()
