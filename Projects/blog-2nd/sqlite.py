import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect("instance/posts.db")  # 파일명 변경 필요
cursor = conn.cursor()

# 테이블 조회
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
# print("Tables:", tables)

# 특정 테이블의 데이터 조회
table_name = "users"  # 테이블 이름 변경 필요

cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
count = cursor.fetchone()[0]
print(f"Total rows in {table_name}: {count}")

cursor.execute(f"SELECT * FROM {table_name}")
rows = cursor.fetchall()

# 데이터 출력
for row in rows:
    print(row)

# 연결 종료
conn.close()
