from flask import Flask , request ,render_template
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def fun():
    a=datetime.now()
    print("time is=",a)
    return render_template('index.html',a=a);
    # jinga ...{{}}
@app.route('/h')
def home():
    return "Hello, Flask! abc"

# @app.route('/status/<name>')
# def status(name):
#     print(f"Received request for status of {name}")
#     return {"status": "OK", "code": 200, "name": name}

@app.route('/login')
def login():
    name = request.values.get('name')
    password = request.values.get('password')
    print(f"Login attempt with name: {name} and password: {password}")
    userdata = {"status": "Logged In", "code": 200, "name": name, "password": password}
    return userdata;
if __name__ == '__main__':
    app.run(debug=True)  # debug=True for development purposes

# serving tamplates