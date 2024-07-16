import os
# 현재 작업 디렉터리 출력
print("Current working directory:", os.getcwd())

# 파일 경로 확인
file_path = os.path.join(os.getcwd(), 'ddd\my_file.txt')
print("File path:", file_path)

# 파일이 존재하는지 확인 후 열기
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
else:
    print("The file 'my_file.txt' does not exist.")