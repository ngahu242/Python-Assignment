def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not possible.")
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    if celsius < -273.15:
        raise ValueError("Temperature below absolute zero is not possible.")
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError("Temperature below absolute zero is not possible.")
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError("Temperature below absolute zero is not possible.")
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero is not possible.")
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero is not possible.")
    return (kelvin * 9/5) - 459.67

# Example usage:
try:
    temp_c = 25  # Celsius temperature
    print(f"{temp_c}°C to Fahrenheit: {celsius_to_fahrenheit(temp_c)}°F")
    print(f"{temp_c}°C to Kelvin: {celsius_to_kelvin(temp_c)}K")

    temp_f = 77  # Fahrenheit temperature
    print(f"{temp_f}°F to Celsius: {fahrenheit_to_celsius(temp_f)}°C")
    print(f"{temp_f}°F to Kelvin: {fahrenheit_to_kelvin(temp_f)}K")

    temp_k = 298.15  # Kelvin temperature
    print(f"{temp_k}K to Celsius: {kelvin_to_celsius(temp_k)}°C")
    print(f"{temp_k}K to Fahrenheit: {kelvin_to_fahrenheit(temp_k)}°F")
except ValueError as e:
    print(e)
