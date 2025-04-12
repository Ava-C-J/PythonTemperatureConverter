def fahrenheit_to_celsius(fahrenheit): #Function definition to convert Fahrenheit to Celsius
    """Convert Fahrenheit to Celsius."""
    celcius = (fahrenheit - 32) * 5.0/9.0 #Conversion forumula
    return celcius 

if __name__ == "__main__": #
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: ")) #Prompt the user to input a temperature in F
        celsius = fahrenheit_to_celsius(fahrenheit) #Call the function to convert F to C
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C") #Display the result
    except ValueError: #When user inputs something else
        print("Please enter a valid number.") 
    