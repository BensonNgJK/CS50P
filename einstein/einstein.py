# Define main function which convert input mass into energy using formula E = mc^2
def main():
    # Ask user to input mass in kg and convert mass to interger
    mass = int(input("Pls input mass (in kg): "))
    # Define the speed of light
    speed = 300000000
    # Define function E = mc^2
    energy = mass * speed**2
    # print result
    print(energy)

main()
