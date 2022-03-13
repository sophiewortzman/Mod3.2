from qset_lib import Rover
from time import sleep

def main():
    rover = Rover()

    i = 0

    left_side_speed = 1
    right_side_speed = 1

    while i < 1000:
        print("X: " + rover.x + " Y: " + rover.y + " Heading: " + rover.heading)
        for dist in rover.laser_distances:
            if dist < 0.1:
                print("TOO CLOSE")
        rover.send_command(left_side_speed, right_side_speed)
        i = i + 1
        sleep(0.01)


if __name__ == "__main__":
    main()
