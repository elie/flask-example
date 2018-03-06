from flask import Flask, render_template

app = Flask(__name__)

# listen for HTTP requests to "/"

# 1 - specify the route and HTTP verb
@app.route('/')
# 2 - define a function to be run, when that route is reached
def root():
  return render_template("first.html")

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






