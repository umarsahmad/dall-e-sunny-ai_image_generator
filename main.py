from flask import Flask, jsonify
from config import key # create a config.py file and in it give your openai api key for dall e image generator.
import openai
from flask import render_template

openai.api_key = key

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', )
  
@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=5, size="256x256") 
  print(response)
  return jsonify(response)


app.run(host='0.0.0.0', port=81)

key = "give the repl key here"

