import psycopg2
from datetime import datetime, time
from flask import jsonify

import logging
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='/var/log/my-log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

class Postgres(object):
    _instance = None

    def __new__(cls):
        if (cls._instance is None):
            cls._instance = object.__new__(cls)
            dbname = "glowupdb"
            host = "ec2-44-197-226-89.compute-1.amazonaws.com"
            password = "password"
            port = "5432"
            user="postgres"
            db_config = {
                "dbname": dbname,
                "host": host,
                "password": password,
                "port": port,
                "user": user,
            }
            try: 
                logger.info("connecting to db")
                print("connecting to db")
                connection = Postgres._instance.connection = psycopg2.connect(**db_config)
                cursor = Postgres._instance.cursor = connection.cursor()
            except Exception as error:
                logger.info("Error: connection not established {}".format(error))
                print("Error: connection not established {}".format(error))
                Postgres._instance = None
            else:
                logger.info("connection established")
                print("connection established")

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def get_username(self, user_id):
        query = "select nickname from public.users where user_id={}".format(user_id)
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
            return results

    def get_user_id(self, nickname):
        query = "select user_id from public.users where nickname='{}'".format(nickname)
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            print(type(results))
        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
            return results[0][0]      

    # create post
    def create_post(self, post_object):
        
        nickname = post_object['nickname']
        user_id = self.get_user_id(nickname)
        title = post_object['title']
        advice = post_object['advice']   
        selectedCategory = post_object['selectedCategory']     
        query = "insert into public.posts (user_id, title, advice, category) values ({}, '{}', '{}', '{}')".format(user_id, title, advice, selectedCategory)
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
             print("post created")
             return

    # create comment
    def create_comment(self, comment_object):
        post_id = comment_object['post_id']
        nickname = comment_object['nickname']
        print(nickname)
        user_id = self.get_user_id(nickname)
        print(user_id)
        comment = comment_object['comment']   
        query = "insert into public.comments (post_id, user_id, comment) values ({}, {}, '{}')".format(post_id, user_id, comment)
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
             print("comment created")
             return             

    # create view
    def create_view(self, view_object):
        post_id = view_object['post_id']
        user_id = view_object['user_id']
        query = "insert into public.views (post_id, user_id) values ({}, '{}')".format(post_id, user_id)
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
             print("view created")
             return        

    def create_like(self, like_object):
        comment_id = like_object['comment_id']
        user_id = like_object['user_id']
        query = "insert into public.likes (user_id, comment_id) values ({}, '{}')".format(user_id, comment_id)
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
             print("like created")
             return              

    # create user
    def create_user(self, user_object):
        nickname = user_object['nickname']
        email = user_object['email']
        organisation = user_object['organisation']
        password = user_object['password']
        print(password)
        query = "insert into public.users (nickname, email, organisation, password) values ('{}', '{}', '{}', crypt('{}', gen_salt('bf')))".format(nickname, email, organisation, password)
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
             print("view created")
             return             

    # login 
    def login(self, login_object):
        return

    # read posts
    def get_posts(self, post_id = None):
        if post_id != None:
            query = '''select p.post_id, p.user_id, nickname, organisation, title, advice, category, p.created_date, coalesce(b.num_views, 0) num_views, coalesce(c.num_comments, 0) num_comments
                        from public.users u 
                        inner join 
                        public.posts p on u.user_id = p.user_id
                        left join 
                        (select post_id, count(*) as num_views from public.views group by post_id) as b
                        on p.post_id=b.post_id
                        left join 
                        (select post_id, count(*) as num_comments from public.comments group by post_id) as c
                        on p.post_id=c.post_id where p.post_id={}'''.format(post_id)
        else:
            query = '''select p.post_id, p.user_id, nickname, organisation, title, advice, category, p.created_date, coalesce(b.num_views, 0), coalesce(c.num_comments, 0)
                        from public.users u 
                        inner join 
                        public.posts p on u.user_id = p.user_id
                        left join 
                        (select post_id, count(*) as num_views from public.views group by post_id) as b
                        on p.post_id=b.post_id
                        left join 
                        (select post_id, count(*) as num_comments from public.comments group by post_id) as c
                        on p.post_id=c.post_id
                        order by num_views asc
                        '''
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            posts = []
            for result in results:
                created_date = result[7]
                timestamp = datetime.timestamp(created_date)
                # created_date = created_date[5:25]
                # created_date_object = datetime.strptime(created_date, "%d %b %Y %H:%M:%S")
                # time_diff = abs((datetime.now() - created_date_object))
                time_diff = abs((datetime.now() - created_date))
                time_posted = 0

                # if more than a day, show DD Mmm
                if time_diff.days > 0: 
                    time_posted = created_date.strftime("%d %b, %Y")
                # if more than 59min, show h
                elif time_diff.seconds > 3600: 
                    time_posted = time_diff.seconds // 3600 
                    time_posted = str(time_posted) + "h"
                elif time_diff.seconds > 60: 
                    time_posted = time_diff.seconds // 60
                    time_posted = str(time_posted) + "min"
                else: 
                    time_posted = time_diff.seconds 
                    time_posted = str(time_posted) + "s"

                post = {
                    "post_id": result[0],
                    "user_id": result[1],
                    "nickname": result[2],
                    "organisation": result[3],
                    "title": result[4],
                    "advice": result[5],
                    "category": result[6],
                    "created_date": timestamp,
                    "numViews": result[8],
                    "numComments": result[9],
                    "timePosted": time_posted
                }
                posts.append(post)

        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
            # return jsonify({'posts': posts})
            return posts


    # read posts
    def get_comments(self, post_id):
        query = '''
            select comment_id, post_id, c.user_id, comment_reply_id, c.created_date, comment, nickname, organisation 
            from public.comments c
            inner join
            public.users u on c.user_id=u.user_id
            where post_id={}      
            order by created_date desc
        '''.format(post_id)

        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            comments = []
            for result in results:
                created_date = result[4]
                timestamp = datetime.timestamp(created_date)
                time_diff = abs((datetime.now() - created_date))
                time_posted = 0

                # if more than a day, show DD Mmm
                if time_diff.days > 0: 
                    time_posted = created_date.strftime("%d %b, %Y")
                # if more than 59min, show h
                elif time_diff.seconds > 3600: 
                    time_posted = time_diff.seconds // 3600 
                    time_posted = str(time_posted) + "h"
                elif time_diff.seconds > 60: 
                    time_posted = time_diff.seconds // 60
                    time_posted = str(time_posted) + "min"
                else: 
                    time_posted = time_diff.seconds 
                    time_posted = str(time_posted) + "s"

                comment = {
                    "comment_id": result[0],
                    "post_id": result[1],
                    "user_id": result[2],
                    "comment_reply_id": result[3],
                    "comment": result[5],
                    "nickname": result[6],
                    "organisation": result[7],
                    "created_date": timestamp,
                    # "numViews": result[8],
                    # "numComments": result[9],
                    "timePosted": time_posted
                }
                comments.append(comment)

        except Exception as error:
            print('error executing query "{}", error:{}'.format(query, error))
            return None
        else:
            # return jsonify({'posts': posts})
            return comments