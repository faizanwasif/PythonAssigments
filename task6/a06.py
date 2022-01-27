## IMPORTS GO HERE
import os

## END OF IMPORTS


#### YOUR CODE FOR text_count FUNCTION GOES HERE ####
def text_count(directory , filename ,third = False ,fourth = False):
    count = 0
    
    directory = '.'
    
    filename = 'essay.txt'

    name = os.path.join(directory, filename)
    
    file = open( name , "r")
     
    for line in file:

        for word in line.split():

            if word:
                count+=1

    if third == True:
    
        count2 = 0

        directory = '.'
    
        filename = 'essay.txt'

        name = os.path.join(directory, filename)

        file = open(name , "r")

        for line in file:

            for word in line.split():

                if word.islower():

                    count2 += 1

        return(count2)
    
    if fourth == True:
        
        count3 = 0
        
        directory = '.'

        filename = 'essay.txt'

        name = os.path.join(directory, filename)
        
        file = open(name , "r")
    
        for line in file:
            
            for words in line:
        
                count3 += 1
        
        return(count3)
    
    else:
        return(count)
        
    file.close()

words = []

su = []
#text_count('directory' , 'filename' ,False , True)

#### End OF MARKER

#### YOUR CODE FOR copy_lines FUNCTION GOES HERE ####

def copy_lines(inpu , output , num_lines):
    
    directory = '.'
    
    filename = 'essay.txt'
    
    inpu = os.path.join(directory , filename)
    
    directory = '.'
    
    filename = 'out.txt'
    
    output = os.path.join(directory , filename)
    
    file1 = open(inpu , 'r')
    file2 = open(output , 'w+')
    a = []
    
    for lines in file1:
        
        c = lines
                 
        a.append(c)
            
        
    for lines2 in a[:num_lines]:
            
        x = lines2.strip()
               
        file2.write(x)
                            

    file1.close()
    file2.close()    
                            
copy_lines('file1','file2', 3)    
   
#### End OF MARKER



