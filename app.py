from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer,rating,comments)
        if customer == '' or dealer == '' or rating == '' or comments == '':
            return render_template('index.html', message='Please enter required fileds')

        # return render_template('success.html', customer)
        return render_template('success.html', customer=customer)


if __name__ == '__main__':
    app.debug = True
    app.run()