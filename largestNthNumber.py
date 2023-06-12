from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return """"
We Have a array of [1, 3, 4, 2, 6, 7, 7, 7, 9].
give a number after url/ between 1 - 9
"""


@app.route('/<int:n>')
def nthLargest(n):
    if(1 <= n <= 9):
        numbers = [1, 3, 4, 2, 6, 7, 7, 7, 9]
        numbers.sort()
        return str(n)+"th largest number from the given list is " + str(numbers[~n])
    else:
        return "Wrong input"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
