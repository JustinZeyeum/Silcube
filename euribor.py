# Command-line program that takes two arguments "start date" and "End date",
# and outputs a list of 6-month Euribor rates

# importing the url and reading the data for Euribor 6 months rates list

from six.moves.urllib.request import urlopen
Link = "https://www.euribor-rates.eu/umbraco/api/euriborpageapi/highchartsdata?series[0]=3"
response = urlopen(Link)
Euribor_6m_Rates = response.read()
# Assigning the arguments with its corresponding item in the list
Start_date = Euribor_6m_Rates[0]
End_date = Euribor_6m_Rates[142]

# Printing the length of the data
print(len(Euribor_6m_Rates))
# Printing the 6-months rates between the start and end date.
print(Euribor_6m_Rates[0:142])

