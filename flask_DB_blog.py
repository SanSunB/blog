from flask import Flask, render_template, flash, request
from insert_jsonFile_toDB import *


app = Flask(__name__)

# Lunch the home page and get a title from the DB
@app.route('/')
def index():
        print("ddd")
        title1 = get_title()
        print("IN GUI", title1)
        return render_template("index.html", result=title1)

# Run the application
if __name__ == "__main__":
   app.run()
