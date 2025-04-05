# Temperature Converter 

temperature = float(input("Enter the current temperature: "))
current_unit = input("Enter the current unit (K, C, F): ").upper()

if current_unit == "K":
    target_unit = input("Convert to (C, F): ").upper()
    if target_unit == "C":
        converted_temp = temperature - 273.15
        print(f"Temperature in Celsius: {converted_temp:.2f}°C")
    elif target_unit == "F":
        converted_temp = ((temperature - 273.15) * 9/5) + 32
        print(f"Temperature in Fahrenheit: {converted_temp:.2f}°F")
    else:
        print("Invalid target unit.")

elif current_unit == "C":
    target_unit = input("Convert to (K, F): ").upper()
    if target_unit == "K":
        converted_temp = temperature + 273.15
        print(f"Temperature in Kelvin: {converted_temp:.2f}K")
    elif target_unit == "F":
        converted_temp = (temperature * 9/5) + 32
        print(f"Temperature in Fahrenheit: {converted_temp:.2f}°F")
    else:
        print("Invalid target unit.")

elif current_unit == "F":
    target_unit = input("Convert to (K, C): ").upper()
    if target_unit == "K":
        converted_temp = ((temperature - 32) * 5/9) + 273.15
        print(f"Temperature in Kelvin: {converted_temp:.2f}K")
    elif target_unit == "C":
        converted_temp = (temperature - 32) * 5/9
        print(f"Temperature in Celsius: {converted_temp:.2f}°C")
    else:
        print("Invalid target unit.")

else:
    print("Invalid current unit. Please enter K, C, or F.")
