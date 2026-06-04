#programmm to calculate the electricity bill
units = int(input("Enter units: "))

#for low category
if units <= 100:
    bill = units * 5
    category = "Low"
    
#for medium category
elif units <= 200:
    bill = units * 7
    category = "Medium"
# find high category
else:
    bill = units * 10
    category = "High"

print("Units Consumed =", units)
print("Total Bill = ₹", bill)
print("Category =", category)
