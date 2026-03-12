from flask import Flask, render_template   # this app will deploy on ec2
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'


if __name__ == "__main__":
    app.run(port=80)
