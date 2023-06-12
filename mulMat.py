from flask import Flask


# If entrypoint is not defined in app.yaml, App Engine will look for an app
# called app in main.py.
app = Flask(_name_)


@app.route('/matrix')
def matrixMultiplication():
    a = [[4, 23, 7],
         [4, 9, 6],
         [2, 5, 5]]
    b = [[4, 9, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 23, 1]]
    c = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    la = len(a)
    lb = len(b)
    lb0 = len(b[0])
    for i in range(la):
        for j in range(lb0):
            for k in range(lb):
                c[i][j] += a[i][k] * b[k][j]

    return c


if _name_ == '_main_':
    app.run(host='127.0.0.1', port=8085, debug=True)