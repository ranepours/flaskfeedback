from models import db, User, Feedback
from app import app

db.drop_all()
db.create_all()

u1 = User(username='koolKat',
        password='MIC4theC4T',
        first_name='jade',
        last_name='bratz',
        email='bratzrbratz@gmail.com')
u2 = User(username='angelc',
        password='809CC',
        first_name='cloe',
        last_name='bratz',
        email='soccergirl@yahoo.com')
u3 = User(username='bunnyboo23',
        password='dulc3ygab',
        first_name='sasha',
        last_name='bratz',
        email='passion4fashion@gmail.com')
u4 = User(username='pretty_princess',
        password='bubbi1956',
        first_name='yasmin',
        last_name='bratz',
        email='shoelover@gmail.com')
u5 = User(username='SPlCE',
        password='phoebe992',
        first_name='roxxi',
        last_name='bratz',
        email='callmespice@yahoo.com')
db.session.add_all([u1,u2,u3,u4,u5])
db.session.commit()

f1 = Feedback(title='',content='',username='')
f2 = Feedback(title='',content='',username='')
f3 = Feedback(title='',content='',username='')
f4 = Feedback(title='',content='',username='')
f5 = Feedback(title='',content='',username='')
db.session.add_all([f1,f2,f3,f4,f5])
db.session.commit()