from flask import Flask, render_template

app = Flask(__name__, static_folder='templates/static')

@app.route('/')
def root():
    return render_template('index.html')

@app.route('projects')
def projects():
    return render_template('projects.html')

@app.route('projects/calculator')
def projects():
    return render_template('projects/calculator.html')

if __name__ == "__main__":
    app.run(debug=True)