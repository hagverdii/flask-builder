import webbrowser
from threading import Timer
from flask import Flask, render_template

app = Flask(__name__, static_folder="./react/assets", template_folder="./react")


#python must be installed
#pip install flask
#pip install pyinstaller
#add react generated dist folder(in the same folder with this script) and rename it to "react" and run command below
#pyinstaller --onefile --add-data "react/assets;react/assets" --add-data "react/index.html;react" course_flask.py
#generated exe file will appear in newly generated dist folder
@app.route('/')
def index():
    return render_template('index.html')

def open_browser():
    webbrowser.open_new("http://127.0.0.1:80")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=False,port=80)