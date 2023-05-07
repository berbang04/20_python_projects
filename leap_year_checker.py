print("welcome to leap year checker: ")
leap_years=[]
i=1982
while(i<2023):
    leap_years.append(i)
    i=i+4
print(leap_years)    
def leap_checker():
    year=int(input("enter your year to check, if it is leap: "))    
    if year in leap_years:
        print(year ,": is a leap year")
    else:
        print(year ,": is not a leap year")    
leap_checker()        