from flask import Flask, render_template, request
from app.views import views
import os
import datetime
from peewee import *
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv

load_dotenv()

# Retrieve database configuration from environment variables
db_name = os.getenv("MYSQL_DATABASE")
db_user = os.getenv("MYSQL_USER")
db_password = os.getenv("MYSQL_PASSWORD")
db_host = os.getenv("MYSQL_HOST")

if not db_name or not db_user or not db_password or not db_host:
    raise ValueError("Database configuration is missing in environment variables")

# Initialize database connection
mydb = MySQLDatabase(
    db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=3306
)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@views.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@views.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]
    return {'timeline_posts': posts}

@views.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_time_line_post(id):
    try:
        post = TimelinePost.get(TimelinePost.id == id)
        post.delete_instance()
        return {'message': 'Post deleted successfully'}
    except TimelinePost.DoesNotExist:
        return {'error': 'Post not found'}, 404

app = Flask(__name__)
app.register_blueprint(views)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
