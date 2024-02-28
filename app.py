import flask
import hijridate


app = flask.Flask(__name__)
if __name__ == '__main__':
    app.run()


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/main', methods=['POST'])
def main():
    date = flask.request.values.get('date').split('-')
    year, month, day = [int(i) for i in date]
    hijri = hijridate.Gregorian(year, month, day).to_hijri()
    return f'<p>{hijri.day}  {hijri.month_name("en")}[{hijri.month}]  {hijri.year}</p>'


@app.errorhandler(Exception)
def error(e):
    return '<p>💀 ERROR 💀</p>'
