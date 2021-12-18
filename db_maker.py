from my_flask_app import db
from my_flask_app.models import Post, User

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

db.drop_all()
db.create_all()

user1 = User(
    username="testperson",
    email="test@test.com",
)


post1 = Post(title="Post 1", content="1contentcontentcontent", author_id=1)
post2 = Post(title="Post 2", content="2contentcontentcontent", author_id=1)


db.session.add(user1)
db.session.add(post1)
db.session.add(post2)

db.session.commit()
