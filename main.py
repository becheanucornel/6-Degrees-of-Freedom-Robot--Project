import geometry
import animation
import trajectory
import time

def main():
    print("\nHello there!\n")
    print("This is a robotics tool dedicated to visualising how industrial robots work!\n")
    print("Please wait for the visual representations to pop up! \n")
    time.sleep(1)
    geometry.main()
    time.sleep(1)
    animation.main()
    time.sleep(1)
    trajectory.main()

if __name__ == "__main__":
    main()