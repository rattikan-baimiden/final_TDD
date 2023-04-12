from function import calculate

order = str(input("Enter your order :"))
amount = input("Enter amount of order :")
try:
    try:
        amount = int(amount)
    except:
        amount = float(amount)
except:
    amount = str(amount)
glass = str(input("Do you have glass y/n :"))

result = calculate(order,amount,glass)
print(result)
