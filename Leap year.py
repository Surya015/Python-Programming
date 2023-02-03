a=int(input("Enter the year:"))
if( a%400 ==0 and 100 !=0 or a%4==0):
    print('It year is a leap year')
else:
    print("It year is not a leap year")
