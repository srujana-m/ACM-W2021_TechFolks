from flask import Flask,flash, redirect, url_for, request,render_template
from flask import session
from flask_sqlalchemy import SQLAlchemy
from mail import alert_mail
from sample import check

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/vita'
db = SQLAlchemy(app)

class vitalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email_id = db.Column(db.String(100))

@app.route('/')
def success():
   return render_template('landing.html')

@app.route('/home')
def home():
   return render_template('index.html') 

@app.route('/mainn')
def mainn():
   return render_template('landing.html')


@app.route('/formm',methods = ['POST', 'GET'])
def formm():
   if request.method=='POST':
      d={}
      name = request.form['name']
      age = int(request.form['age'])
      em = request.form['email']
      x=request.form.getlist('sym')
      d=check(x)
      alert_mail(em,d,name)
      
      return render_template('result.html',di=d)
      
   return render_template('formm.html')
   



@app.route('/login',methods = ['POST', 'GET'])
def login():

   msg = ''
   if 'user' in session and session['user']=='admin':
        return render_template('home.html')

   if request.method=='POST':
      username=request.form.get('username')
      userpass=request.form.get('password')
      log=vitalog.query.filter_by(username=username,password=userpass).first()
      if log is not None:
         msg='Logged in successfully !!'
         return render_template('chooseui.html',msg=msg)

   return render_template('index.html')


@app.route('/register',methods = ['POST','GET'])
def register():
   if(request.method=='POST'):
      username = request.form.get('username')
      password = request.form.get('password')
      email_id = request.form.get('email_id')
      entry=vitalog(username=username,password=password,email_id=email_id)
      db.session.add(entry)
      db.session.commit()

   return render_template('index.html')




@app.route('/Nutrition_Landing',methods = ['POST','GET'])
def land_func():
   return render_template('nutrition_landing.html')

@app.route('/about',methods = ['POST','GET'])
def about():
   return render_template('about.html') 

@app.route('/options',methods = ['POST','GET'])
def option_func():
   return render_template('boxes.html')    


@app.route('/Mental_Landing',methods = ['POST','GET'])
def mental_func():
   return render_template('mental_landing.html')   

@app.route('/workout_landing',methods = ['POST','GET'])
def workout_func():
   return render_template('workout_landing.html')      

@app.route('/Articles',methods = ['POST','GET'])
def articles():
   return render_template('Articles.html') 

@app.route('/mindfulness',methods = ['POST','GET'])
def mindfulness():
   return render_template('mindfullness.html')    

@app.route('/meditation',methods = ['POST','GET'])
def meditation():
   return render_template('meditation.html') 


@app.route('/sleep',methods = ['POST','GET'])
def sleep():
   return render_template('sleep.html')    

@app.route('/exercise',methods = ['POST','GET'])
def exercise():
   return render_template('exercise.html')    

@app.route('/todo',methods = ['POST','GET'])
def todo():
   return render_template('to-do.html')      


@app.route('/stress_relief',methods = ['POST','GET'])
def stress():
   return render_template('stress.html') 

@app.route('/BMI',methods = ['POST','GET'])
def bmi_func():
   return render_template('calculator.html')    

@app.route('/health_chat',methods = ['POST','GET'])
def health_chat():
   return render_template('health_chat.html') 

@app.route('/nutrition_chat',methods = ['POST','GET'])
def nutrition_chat():
   return render_template('nutrition_chat.html') 


@app.route('/diet_plan',methods = ['POST','GET'])
def diet():
   if request.method == 'POST':
      val1 = int(request.form['height'])
      val2 = int(request.form['weight'])
      result = round(val2/(val1/100*val1/100),2)
      if result<18.5:
         return render_template('underweight.html',result = result)
      elif result>=18.5 and result<25:
          return render_template('normalweight.html',result = result)
      elif result>=25 and result<30:
         return render_template('overweight.html',result = result)  
      else:
         return render_template('obesity.html',result = result)

if __name__ == '__main__':
   app.run(debug = True)