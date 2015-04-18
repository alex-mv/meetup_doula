from flask import Flask, render_template, redirect, request, flash, g, session as flask_session
import os

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']



if __name__ == "__main__":
	app.run(debug=True)