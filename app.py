from flask import Flask, jsonify
from scraper import scrape_data

app = Flask(__name__)


@app.route('/user/<string:username>')
def index(username):
    result = scrape_data(username)
    if result == None:
        return jsonify({
            'error': 'Account Not Found!'
        }), 404
    return jsonify(
        result
    ), 200


if __name__ == '__main__':
    app.run()
