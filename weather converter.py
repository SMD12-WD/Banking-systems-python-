weather = int(input("What is the weather in your area ? "))
unit = input("Celsius(C) or Fahrenheit(F): ").upper()
if unit == "C":
    converted = (weather * 9 / 5) + 32
    print(f"The Temperature in Fahrenheit is {converted} ")
    if weather >= 32:
        print("you have got a hot day ahead")
    if weather <= 18:
        print("you have a cold day ahead")
if unit == "F":
    converted_2 = (weather - 32) * 5/9
    print(f"The Temperature in Degress Celsuis  is {converted_2} ")
    if weather >= 91:
        print("you have got a hot day ahead")
    elif weather <= 64:
        print("you have a cold day ahead")
print("Enjoy the rest of your day")













