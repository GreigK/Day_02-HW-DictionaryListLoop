from unicodedata import name


united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.

#united_kingdom.update[1]["capital": "Cardiff"]


# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
#united_kingdom.append = {
# 	"name": "Nothern Ireland",
# 	"population": [1811000],
# 	"capital": "belfast",
# }

print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.
for place in united_kingdom:
   print({place["name"]})

# 4. Use a loop to find the total population of the UK.
total_folk = 0

for persons in united_kingdom:
    total_folk += persons["population"]
    persons["population"] = 0


print({total_folk})
print(total_folk)