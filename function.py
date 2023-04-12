def calculate(order,amount,glass):
    sum = 0
    if type(amount) == int:
        if amount >= 1:
            if order == "espresso" or order == "cappuccino" or order == "late" or order == "mocha":
                if order == "espresso":
                    sum = 55 * amount
                elif order == "cappuccino":
                    sum = 60 * amount
                elif order == "late":
                    sum = 65 * amount
                elif order == "mocha":
                    sum = 70 * amount
            else:
                return "Please input order espresso, cappuccino, late, mocha" 

            if glass == "y":
                sum = sum -5
                return sum 
            elif glass == "n":
                return sum 
            else:
                return "Please input glass y/n"

        elif amount < 1:
            return "Please input amount integer"

    elif type(amount) == str or type(amount) == float :
        return "Please input amount integer"
