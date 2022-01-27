def chocolatePrice(ali_budget,bashir_budget):### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###

    while(bashir_budget):
       ali_budget , bashir_budget = bashir_budget, (ali_budget % bashir_budget)
    return ali_budget

#### End OF MARKER





def calculateProfit(ali_budget,bashir_budget): ### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
     
    if type(ali_budget) == str or type(bashir_budget) == str:
        
        return "Not Possible"
        
    if (ali_budget) == 0 or (bashir_budget) == 0:
        
        return "Not Possible"
        
    elif (type(ali_budget) or type(bashir_budget) == float or int):
        
        a = round(ali_budget) 
        b = round(bashir_budget)

        
        if (a > b):
            
            c = int(a * (3/2))
            d = (b * 2)
            
            
            return min(a , b)
        
        else:
            c = (a * 2)
            d = int(b * (3/2))
            
            return min(a , b)  

#### End OF MARKER


