def calculateArea(width,length):### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
    
    area = length * width
    
    return area     

#### End OF MARKER



def checkTilesFit(plot_width, plot_length, tile_width, tile_length):### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
    
    tile_area = calculateArea(tile_length , tile_width)
    
    
    plot_area = calculateArea(plot_length , plot_width)
     
    y = plot_length % tile_length
    z = plot_width % tile_width
    a = plot_width % tile_length
    b = plot_length % tile_width
    
        
    if a == 0 and b==0:
    
    	return True
    	
    elif z == 0 and y ==0:
    	
    	return True

    else:
        
        return False

#### End OF MARKER 
    
   
def calculateTiles(plot_width, plot_length, tile_width , tile_length):### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ### 
    

    
    if type(plot_width)== str:
            
        return "Invalid Input"
    
    elif (plot_width) == 0:
        
        return None
    
    
    elif type(plot_length) == str:
        
        return "Invalid Input"
    
    elif (plot_length) == 0:
        
        return None
    
    elif type(tile_width) == str:
        
        return "Invalid Input"
    
    elif (tile_width) == 0:
        
        return None
    
    elif type(tile_length) == str:
        
        return "Invalid Input"
    
    elif (tile_length) == 0:
        
        return None
        

    if checkTilesFit(plot_width, plot_length, tile_width, tile_length) :
        
        tile_area = calculateArea(tile_length , tile_width)
    
        plot_area = calculateArea(plot_length , plot_width)      
    
        return plot_area / tile_area
     
    else:
         
        return "Not Possible" 
            
#### End OF MARKER
            
            
                                





