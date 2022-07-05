from operator import index


stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append('Edinburgh Waverly')

# # #2. Add "Glasgow Queen St" to the start of the list
stops[0] = 'Glasgow Queen St'

# # #3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")

# #4. Print out the index position of "Linlithgow"
index = stops.index('Linlithgow')

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")

#6. Delete "Cumbernauld" from the list by index
stops.remove('Cumbernauld')

#7. Print the number of stops there are in the list
number_stops = len(stops)

#8. Sort the list alphabetically
stops.sort()

#9. Reverse the positions of the stops in the list
stops.sort(reverse=True)

#10 Print out all the stops using a for loop
for stop in stops:
    print(stops)


print(stops)
print(index)
print(number_stops)