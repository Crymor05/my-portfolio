#Menu
def print_options ():
    print("Options")
    print(" 'p' print options")
    print(" 'c' Covert from Celsius")
    print(" 'f' Convert from Farenheit")
    print(" 'q' quit the program")
#Conversion
def Celsius_to_Farenheit(c_temp):q

    return 9.0 / 5.0 * c_temp + 32
    
def Farenheit_to_Celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0
#user input    
choice = "p"
while choice != "q":
    if choice == "c":
        c_temp = float(input("Celsius temperature: "))
        print("Farenheit:", Celsius_to_Farenheit(c_temp))
        choice = input("option: ")
    elif choice == "f":
        f_temp = float(input("Farenheit temperature: "))
        print("Celsius:", Farenheit_to_Celsius(f_temp))
        choice = input("option: ")
    elif choice == "p":
        print_options()
        choice = input("option: ")
   
            
        
    
    


