#obtaining how much gas their gas tank holds
print("Hello, im here to calculate your miler per gallon (MPG) or miles per liter (MPL)")
#asking what type of unit meausre thier gas tank uses
volume_used = str(input("Is your tank in liters or gallons?"))
#going through if they are using liters
while volume_used == str("liters"):
    liters_conf = input("would you like to convert to gallons?")
    if liters_conf == str("yes") or str("y") or str("Y"):
#obtaining how many liters their tank holds
        liters = int(float(input("How many liters does your tank hold?")))
#made it so the value cannot be 0 or a negative number. If it is it redos the code until a positive number is inputted
    while liters <= 0:
      print("redo")     
      liters = int(float(input("How many liters does your tank hold?")))
    liters *= .264172
#gives calculation of liters to gallons
    gal = f"You have {liters} gallons in your gas tank"
    print(gal)
if volume_used == str("gallons") or str("Gallons"):
    gal_conf = int(float(input("How many gallons does your tank hold?")))
    while gal_conf <= 0:
        print("redo")
        gal_conf = int(float(input("How many gallons does your tank hold?")))