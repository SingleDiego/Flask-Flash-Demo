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
    error = None
    # 以下代码模拟登陆功能
    if request.method == 'POST':
        # 登录失败
        if request.form['username'] != 'admin' or \
                request.form['password'] != '123456':
            error = '登录失败！'
        # 登陆成功
        else:
            # 消息闪现功能，现在可以在 index 页面读取到反馈的信息
            flash('你已成功登录！')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run()