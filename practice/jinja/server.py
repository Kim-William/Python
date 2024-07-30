# from flask import Flask,render_template
# import random
# import datetime

# app = Flask(__name__)

# @app.route('/')
# def home():
#     random_number = random.randint(1,10)
#     copy_year = datetime.datetime.today().year
#     print(copy_year)
#     return render_template('index.html', num=random_number, current_year = copy_year, name = 'Kim Woong Keol')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask,render_template
import requests

app  = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response=requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts, num=int(num))

@app.route('/guess/<name>')
def guess(name):
    gender_url = f'https://api.genderize.io?name={name}'
    age_url = f'https://api.agify.io?name={name}'

    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']

    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    return render_template('guess.html', guess_name=name, guess_age = age, guess_gender = gender)


if __name__ == '__main__':
    app.run(debug=True)