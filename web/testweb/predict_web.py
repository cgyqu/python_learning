from flask import Flask, request

app = Flask(__name__)  #创建Flask类的实例，第一个参数是模块或者包的名称
app.config['JSON_AS_ASCII'] = False  # 支持中文显示


@app.route('/', methods=['GET', 'POST'])  # 使用methods参数处理不同HTTP方法
def home():
    return 'Hello, Flask'


@app.route('/predict', methods=['GET', 'POST'])  # 使用methods参数处理不同HTTP方法
def predict():
    return {"data": [11, 23, 42]}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="7000", debug=True)