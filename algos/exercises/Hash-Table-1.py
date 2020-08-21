# Hash Table


# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

jan_weather = []

with open('nyc_weather.csv', 'r') as fle:
    for line in fle:
        data = line.split(',')
        try:
            jan_weather.append(int(data[1]))
        except:
            print('invalid line')


# What was the average temperature in first week of Jan
week_1 = sum(jan_weather[:7])/7
print(week_1)

# What was the maximum temperature in first 10 days of Jan
print(max(jan_weather))


fle.close()
