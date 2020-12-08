from flask import Flask, render_template, request

import requests
from bs4 import BeautifulSoup as bs


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':

        customer = request.form['customer']
        r = requests.get(customer)
        soup = bs(r.content)

        first_header = soup.find_all('h2')
        result = soup.prettify()
        dealer = request.form['dealer']
        # rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer,rating,comments)
        if customer == '' or dealer or comments == '':
            return render_template('index.html', message='Please enter required fileds')

        # return render_template('success.html', customer)
        return render_template('success.html', customer=result, first_header=first_header)
        # return render_template('success.html', first = first_header)


if __name__ == '__main__':
    app.debug = True
    app.run()
