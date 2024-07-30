from flask import Flask

app = Flask(__name__)

print(f'Running Module :{__name__}')

@app.route('/')
def hello_world():
    return 'hello, World!'

if __name__ == '__main__':
    app.run()