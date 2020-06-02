# Command-line program that takes two arguments "start date" and "End date",
# and outputs a list of 6-month Euribor rates

# Euribor 6 months rates list
Euribor_6m_Rates = ['2019.12.02 -0.345', '2020.01.02 -0.323', '2020.02.03 -0.338',
                    '2020.03.02 -400', '2020.04.01 -0.276', '2020.05.04 -0.157']

# Assigning the arguments with its corresponding item in the list
Start_date = Euribor_6m_Rates[0]
End_date = Euribor_6m_Rates[5]

# Printing out the information about the start and end date to the screen
print("Start date is 2019.12.02 and end date is 2020.05.04")
print("Please type in the date format as shown : yyyy.mm.dd")

# print(Start_date)
# print(End_date)

# User input the two given arguments to get the list of 6 months Euribor rates
start = input("Enter Start date: ")
End = input("Enter End date: ")

# Print the output to the screen.
print("Euribor 6-months rates are: ", Euribor_6m_Rates)
