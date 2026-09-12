from flask import Flask
app = Flask(__name__)


@app.rout("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AutoEngineer</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"
    </head>
    <body>
       <h1>Welcome to AutoEngineer</h1>
       <p>Find a trusted automobile engineer near you.</p>
       
       <button>Request an Engineer</button>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)      