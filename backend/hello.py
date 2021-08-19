from flask import Flask, request, jsonify
import connection
from connection import Postgres

app = Flask(__name__)

db = Postgres()

@app.route('/')
def hello_world():
    nickname = db.get_username(1)
    print("this is the nickname: ", nickname)
    return 'Hello world!'

@app.route("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)

@app.route("/details", methods=['POST'])
def get_book_details():
    author=request.json['author']
    published=request.args.get('published')
    return "Author : {}, Published: {}".format(author,published)

# create post
@app.route("/createpost/", methods=['POST'])
def create_post():
    post_object = request.json
    db.create_post(post_object)
    return "created post"

# create view
# request body will contain post_id and user_id in json object 
@app.route("/createview/", methods=['POST'])
def create_view():
    view_object = request.json
    db.create_view(view_object)
    return "created view"

# create user 
@app.route("/createuser/", methods=['POST'])
def create_user(): 
    user_obj = request.json
    db.create_user(user_obj)
    return "created user"
    

# read posts
@app.route("/getposts", methods=['GET'])
def get_posts():
    post_id = request.args.get('post_id')
    posts = db.get_posts(post_id)
    return jsonify({'posts': posts})
    # return posts


# date_object = datetime.strptime(date_string, "%d %b %Y %H:%M:%S")
# export FLASK_APP=hello.py
# flask run --host=0.0.0.0 --port=80