import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    user_agent = flask.request.headers.get('User-Agent')
    return "<p>Your browser is %s<p>" %user_agent

@app.route("/alt")
def alt():
    return "alternate page"

@app.route("/name/<name>")
def helloName(name):
    return '<h1>hello, %s<h1>' %name

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')