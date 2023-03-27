from function import calculate

order = str(input("Enter your order :"))
amount = int(input("Enter amount of order :"))
glass = str(input("Do you have glass y/n :"))

result = calculate(order,amount,glass)
print(result)
# result = display_month(input_number)
# print(result)
