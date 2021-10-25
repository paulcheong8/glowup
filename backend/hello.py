from flask import Flask, request, jsonify
import logging
import json_log_formatter
# from pythonjsonlogger import jsonlogger
import connection
from connection import Postgres

app = Flask(__name__)

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='/var/log/my-log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

logger.info('Sign up', extra={'referral_code': '52d6ce'})

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

db = Postgres()

@app.route('/')
def hello_world():
    app.logger.info('Processing default request')
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
    logger.info('Created post')
    return "created post"

# create comment
@app.route("/createcomment/", methods=['POST'])
def create_comment():
    comment_object = request.json
    db.create_comment(comment_object)
    logger.info('Created comment')
    return "created comment"

# create view
# request body will contain post_id and user_id in json object 
@app.route("/createview/", methods=['POST'])
def create_view():
    view_object = request.json
    db.create_view(view_object)
    logger.info('Created view')
    return "created view"

# create user 
@app.route("/createuser/", methods=['POST'])
def create_user(): 
    user_obj = request.json
    db.create_user(user_obj)
    logger.info('Created user')
    return "created user"
    
# login
@app.route("/login", methods=['POST'])
def login(): 
    login_obj = request.json

    return

# read posts
@app.route("/getposts", methods=['GET'])
def get_posts():
    post_id = request.args.get('post_id')
    posts = db.get_posts(post_id)
    logger.info('Get posts')
    return jsonify({'posts': posts})
    # return posts

# read posts
@app.route("/getcomments", methods=['GET'])
def get_comments():
    post_id = request.args.get('post_id')
    comments = db.get_comments(post_id)
    logger.info('Get comments')
    return jsonify({'comments': comments})
    # return posts

# date_object = datetime.strptime(date_string, "%d %b %Y %H:%M:%S")
# export FLASK_APP=hello.py
# flask run --host=0.0.0.0 --port=80

# app.run(host='localhost', port=80, debug=True)

if __name__ == '__main__':
    print('here')
    app.run(host='0.0.0.0', port=80)