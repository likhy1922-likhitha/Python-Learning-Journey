# write a program using function to convert
# celsius to fahrent
def conversion():
    # cel =5*(f-32)/9
    fah = (cel/5)*9+32
    return fah
cel = int(input("Enter the celsuius: "))

print(f"{cel} is connverted to fahrent {conversion()}")