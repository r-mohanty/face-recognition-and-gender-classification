from flask import Flask
from app import views

app = Flask(__name__)

# url
app.add_url_rule('/','faceapp',views.faceapp)
app.add_url_rule('/base','base',views.base)
app.add_url_rule('/gender','gender',views.gender,methods=['GET','POST'])
# 
if __name__ == "__main__":
    app.run(debug=True)