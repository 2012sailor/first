import json
from flask import Flask
from flask import render_template
#使用3.0以上版本python能显示中文
app=Flask(__name__)

@app.route('/')
def test():
    return "nihao, flask"
    
@app.route('/first')
def first():
    a={"name":"菜鸟教程" , "url":"www.runoob.com" }
    return a

#from flask import render_template
@app.route('/index/')
@app.route('/index/<name>')
def index(name=None):
    return render_template('./index.html', name=name)
    
if __name__=='__main__':
    app.run()