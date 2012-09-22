import csv

from flask import Flask, render_template


app = Flask(__name__)


def parse_csv(filename):
    """Read data from a CSV.
    This will return a list of dictionaries, with key-value pairs corresponding
    to each column in the parsed csv.
    """
    with open(filename, 'rb') as f:
        return list(csv.DictReader(f))


@app.route('/')
def hello_world():
    pins = list(parse_csv("data/pins.csv"))
    categories = list(parse_csv("data/categories.csv"))
    return render_template('index.html', *locals())

if __name__ == '__main__':
    app.run(debug=True)
