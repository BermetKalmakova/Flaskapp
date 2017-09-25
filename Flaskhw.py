from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "<h2>Welcome</h2>"

@my_app.route('/name')
def name():
    return "<h1>My name is Bermet.</h1>"

@my_app.route('/end')
def start():
    return "<h2>Farewell</h2>"

if __name__ == '__main__':
    my_app.run()
    
