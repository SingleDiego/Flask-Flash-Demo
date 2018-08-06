from flask import (
    Flask, 
    flash,  # 消息闪现
    redirect, 
    render_template, 
    request, url_for
    )

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 以下代码模拟登陆功能
    if request.method == 'POST':
        # 登录失败
        if request.form['username'] != 'admin' or \
                request.form['password'] != '123456':
            # 在闪现的消息中带上分类 'error'
            flash(u'登录失败！', 'error')
        # 登陆成功
        else:
            # 消息闪现功能，现在可以在 index 页面读取到反馈的信息
            flash(u'你已成功登录！')
            return redirect(url_for('index'))
    return render_template('login.html')

if __name__ == "__main__":
    app.run()