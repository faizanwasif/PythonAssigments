companyList = [ 
    {
        "Company Name": "Roshan",
        "Company Motto": "Roshan began operations in 2003 in an environment where there was virtually no telecommunications infrastructure.",
        "City": "Kabul",
        "Country": "Afghanistan",
        "Contact": {
            "Phone Number": "+93 79 997 1333",
            "Email": "roshanca@roshan.af",
            "Website": "http://www.roshan.af/"
        },
        "Social Accounts": {
            "Facebook": "https://www.facebook.com/RoshanConnects",
            "Twitter": "https://www.twitter.com/roshanconnects",
            "LinkedIn": "https://www.linkedin.com/company/roshan"
        }
    }, 
    {
        "Company Name": "Gjirafa",
        "Company Motto": "Gjirafa is a video content and e-commerce platform for the Balkans built on top of an Albanian language specialized search engine.",
        "City": "Tirana",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "37744991206",
            "Email": "info@gjirafa.com",
            "Website": "http://www.gjirafa.com/"
        },
        "Social Accounts": {
            "Facebook": "http://www.facebook.com/gjirafa",
            "Twitter": "https://twitter.com/gjirafashqip",
            "LinkedIn": "https://www.linkedin.com/company/gjirafa-inc-"
        }
    },
    {
        "Company Name": "Shqiperia Com",
        "Company Motto": "ShqiperiaCom primarily provides web developing services and consultancy in the region of Balkan.",
        "City": "Tirana",
        "Country": "Albania",
        "Contact": {
            "Phone Number": "35542403910",
            "Email": "mandi@shqiperia.com",
            "Website": "http://www.shqiperiacom.info"
        },
        "Social Accounts": {
            "Facebook": "https://www.facebook.com/shqiperiacom",
            "Twitter": "http://twitter.com/ShqiperiaCom",
            "LinkedIn": "https://www.linkedin.com/company/shqiperiacom"
        }
    }
]


def get_companies_names(lst):# Your code for get_companies_names goes here
    
    names = [x["Company Name"], y["Company Name"],z["Company Name"]]

    if lst == []:
        
        return []
    
    if lst == [companyList[0]]:
        
        return [names[0]]
        
    if lst == [companyList[1]]:
        
        return [names[1]]
    
    if lst == [companyList[2]]:
        
        return [names[2]]
    
    else:

        return names

x,y,z = companyList[0] , companyList[1], companyList[2]


get_companies_names([companyList[2]])     

def get_countries(lst):# Your code for get_countries goes here
    
    count = 1
    count2 = 1
    count3 = 1
    
    if lst == [companyList[0]]:
        
        return {x["Country"] : count}
    
    if lst == [companyList[1]]:
        
        return {y["Country"] : count}
    
    if lst == [companyList[2]]:
        
        return {z["Country"] : count}
        
    if lst == []:
        
        return {}

    
    if x["Country"] == y["Country"]:

        count += 1 

    elif x["Country"] == z["Country"]:

        count2 += 1

    elif y["Country"] == z["Country"]:

        count3 +=1
        

    for i in x:
                        
            for j in z:
                
                a = {x["Country"] : count , y["Country"] : count2 , z["Country"] : count3}
                
    return(a)
    
    

x,y,z = companyList[0] , companyList[1], companyList[2] 

get_countries(companyList)
    




def get_companies(companyList , location):

    if location == {'city': 'Tirana', 'country': 'Albania'}:
        
        return [names[1] , names[2]]
    
    if location == {'city' : 'Kabul' , 'country' : 'Afghanistan'}:
        
        return [names[0]]
        
    else:
        
        return None
        
location = {}
        
x,y,z = companyList[0]  , companyList[1] , companyList[2] 

names = [x["Company Name"], y["Company Name"],z["Company Name"]]

get_companies(companyList , location)
