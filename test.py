from app import db
from app.models import User, Post

u = User(username='john', email='john@example.com')
db.session.add(p)
db.session.commit()
 
users = User.query.all()
users
for u in users:
    print(u.id, u.username)

u = User.query.get(1)
p = Post(body='my first post!', author=u)

# get all posts written by a user
u = User.query.get(1)
u

posts = u.posts.all()
posts
users = User.query.all()
for u in users:
    db.session.delete(u)
posts = Post.query.all()
for p in posts:
    db.session.delete(p)
db.session.commit()


u = User(username='1', email='1male@example.com')
u.set_password('1')
db.session.add(u)
db.session.commit()