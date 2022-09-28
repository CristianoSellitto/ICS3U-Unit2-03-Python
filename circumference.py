#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in September 2022
# A program that finds the circumference of a circle, using user inputted variables

import constants


def main():
    # Finds the circumference of a circle with using a radius sent by the user

    radius_of_circle = int(input("Enter the radius of the circle (cm): "))
    circumference_of_rectangle = constants.TAU * radius_of_circle
    print("\nThis circle's circumference is {}cm".format(circumference_of_rectangle))

    print("\nDone.")


if __name__ == "__main__":
    main()
