# names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {
#     'Alex':89,
#     'Bath':23,
#     ,
#     ,
#     ,

# }
# import random
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)
# passed_students = {name:score for (name,score) in student_scores.items() if score > 50}
# print(passed_students)


# input <= What is the Airspeed Velocity of an Unladen Swallow?
# sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
# dict_len = {word:len(word) for word in sentence.split()}
# print(dict_len)


# weather_c = eval('{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}')
# weather_f = {day:(temp * 9/5 + 32) for (day,temp) in weather_c.items()}
# print(weather_f)


# student_dict ={
#     "student":['Angela', 'Kim', 'Lily'],
#     "score":[56,76,44]
# }
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key,value) in student_data_frame.items():
#     print(value)

# for (index, row) in student_data_frame.iterrows():
#     print(row)
#     print(row.student)
#     if row.student == 'Angela':
#         print(row.score)

