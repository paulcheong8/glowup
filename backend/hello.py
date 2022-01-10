from flask import Flask, request, jsonify
import logging
import json_log_formatter
import connection
from connection import Postgres
import requests

app = Flask(__name__)

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='/var/log/my-log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

db = Postgres()

@app.route('/')
def hello_world():
    nickname = db.get_username(1)
    print("this is the nickname: ", nickname)
    logger.info('Processing default request logger')
    return 'Hello world!'


# @app.route('/test')
# def test_endpoint():
#     # app.logger.info("Testing endpoints.........")
#     logger.info('Processing default request logger')
#     current_span = tracer.current_span()
#     body =    {"key":"value"}

#     if current_span:
#         # customer_id -> 254889
#         print("current span")
#         print(current_span)
#         current_span.set_tag("body", body)    
#     print("Testing endpointss.........")

#     response = requests.get("https://anapioficeandfire.com/api/characters/583")
#     print(response)
#     external_api_endpoint()
#     return "Test endpoint"

@app.route('/external_api')
def external_api_endpoint():
    # app.logger.info("Testing external api endpoint.........")
    response = requests.get("https://anapioficeandfire.com/api/books/1")
    print(response) 

# create post
@app.route("/createpost/", methods=['POST'])
def create_post():
    try:
        post_object = request.json
        db.create_post(post_object)
        logger.info('Created post')
        return "Created post"
    except Exception as e:
        logger.error("Failed to create post: ", str(e))
        return "Failed to create post"

# create comment
@app.route("/createcomment/", methods=['POST'])
def create_comment():
    try:
        comment_object = request.json
        db.create_comment(comment_object)
        logger.info('Created comment')
        return "created comment"
    except Exception as e:
        logger.error("Failed to create comment: ", str(e))
        return "Failed to create comment"

# create view
# request body will contain post_id and user_id in json object 
@app.route("/createview/", methods=['POST'])
def create_view():
    try:
        view_object = request.json
        db.create_view(view_object)
        logger.info('Created view')
        return "created view"
    except Exception as e:
        logger.error("Failed to create view: ", str(e))
        return "Failed to create view"

# create user 
@app.route("/createuser/", methods=['POST'])
def create_user(): 
    try:
        user_obj = request.json
        db.create_user(user_obj)
        logger.info('Created user')
        return "created user"
    except Exception as e:
        logger.error("Failed to create user: ", str(e))
        return "Failed to create user"
    
# login
@app.route("/login", methods=['POST'])
def login(): 
    login_obj = request.json

    return

# read posts
@app.route("/getposts", methods=['GET'])
def get_posts():
    try:
        post_id = request.args.get('post_id')
        posts = db.get_posts(post_id)
        logger.info('Get posts')
        return jsonify({'posts': posts})
    except Exception as e:
        logger.error("Failed to get posts: ", str(e))
        return "Failed to get posts"
    # return posts

# read posts
@app.route("/getcomments", methods=['GET'])
def get_comments():
    try:
        post_id = request.args.get('post_id')
        comments = db.get_comments(post_id)
        logger.info('Get comments')
        return jsonify({'comments': comments})
    except Exception as e:
        logger.error("Failed to get comments: ", str(e))
        return "Failed to get comments"
    # return posts

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)