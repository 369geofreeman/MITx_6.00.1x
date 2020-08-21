# Hash Table Exercise 2:

# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
# Figure out data structure that is best for this problem


jan_weather = {}

with open('nyc_weather.csv', 'r') as f:
    for line in f:
        data = line.split(',')
        try:
            jan_weather[data[0]] = int(data[1])
        except:
            print('No value in this line')


# What was the temperature on Jan 9?
print(jan_weather['Jan 9'])

# What was the temperature on Jan 4?
print(jan_weather['Jan 4'])

# Figure out data structure that is best for this problem
print('Converting nyc_weather.csv to a dictonary and accessing it directly in O(1) is the fastest')
