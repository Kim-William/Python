# import csv

# with open("pandas practic\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("pandas practic\weather_data.csv")
# temperatures = data["temp"]
# print(temperatures)

# print (type(data))
# print (type(data["day"]))
# print (type(data["temp"]))
# print (type(data["condition"]))

# print (f"{data['day'][0]} - {type(data['day'][0])}")
# print (f"{data['temp'][0]} - {type(data['temp'][0])}")
# print (f"{data['condition'][0]} - {type(data['condition'][0])}")


# print (f"{data['day'][1]} - {type(data['day'][1])}")
# print (f"{data['temp'][1]} - {type(data['temp'][1])}")
# print (f"{data['condition'][1]} - {type(data['condition'][1])}")


# data_dict = data.to_dict()

# print(data_dict)

# data_xml = data.to_xml()
# print(data_xml)

# data_json = data.to_json()
# print(data_json)

# temp_list = data['temp'].to_list()
# print(f"average temperatures(list): {round(sum(temp_list)/len(temp_list),2)}")

# temp_avg = round(data['temp'].mean(),2)
# print(f"average temperatures(series): {temp_avg}")

# print(f"Max : {data['temp'].max()}")
# print(data['condition'])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.condition == "Rain"])
# monday = data[data.day == "Monday"]
# # print(monday.condition)
# # (0°C × 9/5) + 32 = 32°F
# monday_temp = int(monday.temp) * 9/5 + 32
# print(monday_temp)

#create a dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angla", "Kim"],
#     "scores": [76, 56, 65, 80]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv(r'pandas practic\new_data.csv')


data = pandas.read_csv('pandas practic\Squirrel_data.csv')

data_primary_fur_color = data['Primary Fur Color']
gray_squirrel_count = len(data_primary_fur_color[data['Primary Fur Color'] == 'Gray'])

black_squirrel_count = len(data_primary_fur_color[data['Primary Fur Color'] == 'Black'])

cinnamon_squirrel_count = len(data_primary_fur_color[data['Primary Fur Color'] == 'Cinnamon'])


print(f"{gray_squirrel_count} | {black_squirrel_count} | {cinnamon_squirrel_count}")


data_dict = {
    "Fur Color":["Gray", "Black", "Cinnamon"],
    "Count":[gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('pandas practic\squirrel_count.csv')