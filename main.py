# Open the text file containing the list of countries
with open('countries.txt', 'r') as file:
    # Read all lines from the file and store them in a list
    countries = file.readlines()

# Remove any extra whitespace (like newline characters) from each line
countries = [country.strip() for country in countries]

# Get the count of countries
country_count = len(countries)

# Output the number of countries
print(f"There are {country_count} countries listed.")
print(countries[6])
print(countries[76])
print(len([w for w in input().split() if len(w) > 5]))
