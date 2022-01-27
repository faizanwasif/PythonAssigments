def openLocks(number_of_lockers , number_of_students):### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
    if number_of_students < 0:
        return None
    if (number_of_lockers) == 0:
        return(0)

    if number_of_students == 1:
        for i in range(1 , number_of_lockers+1):
            return(number_of_lockers)

    for j in range(1 , number_of_lockers + 1):
        if (j == number_of_lockers) or (j % number_of_lockers == 0):
            return(0)
        else:
            return(1)
#### End OF MARKER







def mostTouchableLocker(number_of_lockers , number_of_students):### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
    if number_of_students == 0:
        return 0
    if (number_of_lockers or number_of_students) < 0:
        return None
    
    a = 0
    for i in range(1, number_of_lockers + 1):
        for z in range(1, number_of_students+1):
            if i % number_of_students == 0:
                a += 1
                
    return(a)

#### End OF MARKER

