def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def validate_temperature(scale, temp):
    if scale == "C" and temp < -273.15:
        raise ValueError("Temperature below absolute zero is not possible in Celsius.")
    elif scale == "F" and temp < -459.67:
        raise ValueError("Temperature below absolute zero is not possible in Fahrenheit.")
    elif scale == "K" and temp < 0:
        raise ValueError("Temperature below absolute zero is not possible in Kelvin.")
    return temp

def main():
    print("Temperature Conversion App")
    print("Choose a conversion option:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        temp = validate_temperature("C", temp)
        print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")

    elif choice == "2":
        temp = float(input("Enter temperature in Celsius: "))
        temp = validate_temperature("C", temp)
        print(f"{temp}°C is {celsius_to_kelvin(temp):.2f}K")

    elif choice == "3":
        temp = float(input("Enter temperature in Fahrenheit: "))
        temp = validate_temperature("F", temp)
        print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")

    elif choice == "4":
        temp = float(input("Enter temperature in Fahrenheit: "))
        temp = validate_temperature("F", temp)
        print(f"{temp}°F is {fahrenheit_to_kelvin(temp):.2f}K")

    elif choice == "5":
        temp = float(input("Enter temperature in Kelvin: "))
        temp = validate_temperature("K", temp)
        print(f"{temp}K is {kelvin_to_celsius(temp):.2f}°C")

    elif choice == "6":
        temp = float(input("Enter temperature in Kelvin: "))
        temp = validate_temperature("K", temp)
        print(f"{temp}K is {kelvin_to_fahrenheit(temp):.2f}°F")

    else:
        print("Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
