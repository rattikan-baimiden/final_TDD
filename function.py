def calculate(order,amount,glass):
    sum = 0
    if glass == "y" or glass == "n":
        if order == "espresso" and amount >= 1 :
            sum = 55 * amount
        elif order == "cappuccino" and amount >= 1:
            sum = 60 * amount
        elif order == "late" and amount >= 1:
            sum = 65 * amount
        elif order == "mocha" and amount >= 1:
            sum = 70 * amount
        else:
            return "order is wrong" 
    else:
        return "order is wrong" 

    if glass == "y":
        sum = sum -5

    return sum 

# def invalide_input(order,amount,glass):
#     if glass != "y" or glass != "n":
#         return "input glass y/n"
#     if amount != int or amount < 1:
#         return "input amount integer"
#     if order != "espresso" or order != "cappuccino" or order != "late" or order != "mocha":
#         return "input order espresso,cappuccino,late,mocha"









