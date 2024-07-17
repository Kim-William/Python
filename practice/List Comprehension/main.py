

# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]

# print(f"numbers: {numbers}\nnew_numbers: {new_numbers}")

# name = "WoongKeol"
# letters_list = [letter for letter in name]
# print(letters_list)

# aaa = [ n*2 for n in range(1,5)]
# print(aaa)

# names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
# short_names = [n for n in names if len(n) < 5]
# print(short_names)
# long_names = [n.upper() for n in names if len(n) > 5]
# print(long_names)

# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)

# # input <= 1,1,2,3,5,8,13,21,34,55
# list_of_strings = input().split(',')
# result = [int(str_value) for str_value in list_of_strings if int(str_value) %2 == 0]
# print(result)


# with open(r'List Comprehension\file1.txt') as file:
#   first_file = file.readlines()
# first_numbers = [int(n) for n in first_file]

# with open(r'List Comprehension\file2.txt') as file:
#   second_file = file.readlines()
# second_numbers = [int(n) for n in second_file]

# result = [n for n in first_numbers if n in second_numbers]

# result_2 = [int(n) for n in first_file if n in second_file]

# print(result_2)