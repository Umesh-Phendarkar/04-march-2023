## This is Added for new Feature - for 2024 Year -- 

## This is a coming from Dev Branch -- Programmer - Umesh  

### This is a Python WebApplication ..
## This is going to Live on April 2023..


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello it is Python Here!...Enjoy your Coding..."

if __name__ == "__main__":
    app.run(host="0.0.0.0")
