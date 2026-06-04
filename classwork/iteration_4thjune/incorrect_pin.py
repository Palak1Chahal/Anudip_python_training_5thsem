correct_pin = 1234

while (correct_pin):
    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Access Granted.")
        break
    else:
        print("Incorrect PIN. Try Again.")
