try:
    file = open('aaa.txt')
except FileNotFoundError as error_message:
    print(f'Error : {error_message}')
else:
    content = file.read()
    print(content)
    file.close()
    file = None
finally:
    print('Close')
