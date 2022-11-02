Year =int(input("Enter the year to be checked:"))
if(Year % 4 == 0 and Year % 100 != 0 or Year % 400==0):
   print("The Year is a leap year")
else:
   print("The Year is not a leap year")
   
