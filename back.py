import flask

flask_app = flask.Flask(__name__)

@flask_app.route('/')
def root():
    return flask.redirect('/front/')

@flask_app.route('/front/')
def front_index():
    return flask.send_from_directory('front', "index.html")

@flask_app.route('/front/<path:filename>')
def front_file(filename):
    return flask.send_from_directory('front', filename)

if __name__ == "__main__":
    flask_app.run(debug=True)
