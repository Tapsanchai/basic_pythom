# เรียกใช้งาน Lib
from flask import Flask, request, render_template

# สร้างตัวแปล เรียกชื่อของ Flask
app = Flask(__name__)

list_name = ['parew','kuma','max','yohoho']
# สร้าง Function & Route เพื่อรับ-ส่งข้อมูล
# -------------------------------------------------------
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html',results=list_name)

@app.route('/post', methods=['POST'])
def post():
    print(request.args)
    name = request.args.get('name')
    return "message POST", "name is " + name

@app.route('/query', methods=['POST'])
def query():
    print("request =",request.args)
    name = request.args.get('name')
    return "message Query [POST] " + "name is " + name

@app.route('/form', methods=['POST'])
def form_data():
    data_name = request.form.get("name")
    data_age = request.form.get("age")
    return "data = " + data_name + "," + data_age

@app.route('/user/<user_id>', methods=['POST'])
def get_user(user_id):
    return "User ID: " + user_id


# -------------------------------------------------------


# ตรวจสอบความถูกต้อง และให้แสดงผลเว็บไซต์ url ที่กำหนด 
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=8080)

