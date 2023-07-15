from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def search_page():
    return 'Search Page'

@app.route('/recipe')
def get_recipe():
    recipe_id = request.args['id']
    return 'Recipe Page'

if __name__ == '__main__':
    app.run()