from flask import Flask, render_template, request
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

OWN_EMAIL = "wkkim.blog@gmail.com"
OWN_PASSWORD = "etty xktp gaez ejrd"

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

  
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def smtp_setting(email, password, type=None):
  mail_type = None
  port = 587

  if type == 'naver':
    mail_type = 'smtp.naver.com'
  elif type == 'gmail':
    mail_type = 'smtp.gmail.com'
  else:
    mail_type = 'smtp.gmail.com'
    
  # SMTP 세션 생성
  smtp = smtplib.SMTP(mail_type, port)
  smtp.set_debuglevel(True)

  # SMTP 계정 인증 설정
  smtp.ehlo()
  smtp.starttls() # TLS 사용시 호출
  smtp.login(email, password) # 로그인

  return smtp

def send_email(name, email, phone, message):
    
    try:
        email_message = f"Subject:{name} Sent this Blog Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)
    except Exception as e:
        print('error', e)
    finally:
        print('email sent')

if __name__ == "__main__":
    app.run(debug=True)

