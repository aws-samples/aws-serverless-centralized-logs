from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    print('hello world', flush=True)

    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80)