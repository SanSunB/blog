from flask import Flask, render_template, flash, request
from get_post_by_id import *


app = Flask(__name__)

# Lunch the home page and get a title from the DB
@app.route('/')
def index():
        # Get the post title
        post = get_post()
        title = post['title']

        # Lunch the page with the title as a variable
        return render_template("index.html", result=title)

# Run the application
if __name__ == "__main__":
   app.run()
