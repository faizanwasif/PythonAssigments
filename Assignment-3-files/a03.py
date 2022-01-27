
def chocolatePrice(ali_budget, bashir_budget):
    while bashir_budget:
        ali_budget, bashir_budget = bashir_budget, ali_budget%bashir_budget
        
    return ali_budget


def calculateProfit(ali_budget, bashir_budget):
    if ali_budget == 0 or bashir_budget == 0:
        return "Not Possible"
    
    if type(ali_budget) == float:
        ali_budget = round(ali_budget)
    
    if type(bashir_budget) == float:
        bashir_budget = round(bashir_budget)
        
    if type(ali_budget) == int and type(bashir_budget) == int:
    
        price = chocolatePrice(ali_budget, bashir_budget)
        
        aliChocolates = ali_budget/price 
        bashirChocolates = bashir_budget/price
        
        bashirProfit, aliProfit = 0, 0
        
        if aliChocolates > bashirChocolates:
            bashirProfit = bashirChocolates * price * 2
            aliProfit = aliChocolates * price * 1.5
            
        elif aliChocolates < bashirChocolates:
            bashirProfit = bashirChocolates * price * 1.5
            aliProfit = aliChocolates * price * 2
        
        return max(bashirProfit, aliProfit)
            
    else:
        return "Not Possible"





