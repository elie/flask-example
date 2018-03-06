from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []

@app.route('/')
def root():
  return render_template("students.html", students=students)

@app.route('/students/new')
def new():
  return render_template("new.html")

@app.route("/students")
def index():
  new_student = request.args.get("first")
  students.append(new_student)
  return redirect(url_for('root'))

# make a route for /rithm
@app.route('/rithm')
def say_hi():
  return "Hello class!"

@app.route('/instructor/<name>')
def elie(name):
  return render_template("instructor.html", instructor_name=name, numbers=[1,2,3,4])

@app.route('/sum/<int:num1>/<int:num2>')
def add(num1, num2):
  total = num1 + num2
  return f"{total}"

if __name__ == '__main__':
  app.run(debug=True, port=3000)






