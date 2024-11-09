import geometry
import animation

def main():
    print("\nHello there!\n")
    print("This is a robotics tool dedicated to visualising how industrial robots work!\n")
    print("Please choose what type of action you would like to perform: \n")
    option = input("1 - Geometric Model | 2 - Animation :")

    if option == '1':
        geometry.main()
    elif option == '2':
        animation.main()
    else:
        print("Your choice is not listed above, bye for now! :(")

if __name__ == "__main__":
    main()