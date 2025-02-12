#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.

#month
month_num = int(input("What is the number of the month? "))

if month_num == 1:
    month_num = "January"
elif month_num == 2:
    month_num = "February"
elif month_num == 3:
    month_num = "March"
elif month_num == 4:
    month_num = "April"
elif month_num == 5:
    month_num = "May"
elif month_num == 6:
    month_num = "June"
elif month_num == 7:
    month_num = "July"
elif month_num == 8:
    month_num = "August"
elif month_num == 9:
    month_num = "September"
elif month_num == 10:
    month_num = "October"
elif month_num == 11:
    month_num = "November"
elif month_num == 12:
    month_num = "December"
#season
season = month_num
if month_num == "March" or month_num == "April" or month_num == "May":
    season = "Spring"
elif month_num == "June" or month_num == "July" or month_num == "August":
    season = "Summer"
elif month_num == "September" or month_num == "October" or month_num == "November":
    season = "Fall"
elif month_num == "December" or month_num == "January" or month_num == "February":
    season = "Winter"

print(f"The month is {month_num} and the season is {season}")