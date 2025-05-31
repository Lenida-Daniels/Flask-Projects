<<<<<<< HEAD
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items=[
        {"id":1,"name":"phone","barcode":"893212299897","price":500},
        {"id":2,"name":"laptop","barcode":"123512699897","price":900},
        {"id":3,"name":"keyboard","barcode":"103275299997","price":150}
    ]
    return render_template("market.html",items=items)
"""
#Dynamic routing
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'
"""
if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
>>>>>>> 732726179e70cdb4e39b9c0b9b01780e1bbeb7f2
