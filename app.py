from flask import Flask


app = Flask(__name__)

@app.route("/")


def index():
    script = server_document('')
    return render_template('index.html', script=script, template='Flask')

if __name__ == '__main__':
    app.run(port=8000)