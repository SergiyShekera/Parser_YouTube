from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class MyTable(Base):
        
        __tablename__ = 'youtube_table'

        id = Column(Integer, primary_key=True)
        name = Column(Text)
        views = Column(Integer)
        like = Column(Integer)
        dislike = Column(Integer)
        duration = Column(Text)
        url = Column(Text)
       
        def __init__(self, name, views, like, dislike, duration, url):
            
                self.name = name
                self.views = views
                self.like = like 
                self.dislike = dislike 
                self.duration = duration
                self.url = url

        def __repr__(self):
                return "<MyTable(%s, %s, %s, %s, %s, %s)>" % (
                        self.name, self.views,
                        self.like, self.dislike,
                        self.duration, self.url
                        )


def connect_to_database():
    
    try:
            
        engine = create_engine('postgresql://postgres:root@localhost/test_db')
        Session = sessionmaker(bind=engine)
        session = Session()
        
        data = {'engine' : engine,
                'session' :session}
        
        return data

    except:
            
        print('Fail to connect to the database')
        
           
engine = connect_to_database()
engine = engine['engine']

Base.metadata.create_all(engine)


def write_database(data):

    session = connect_to_database()
    session = session['session']
        
    try:
            
        new_record = MyTable(
            name = data['name'],
            views = data['views'],
            like = data['like'],
            dislike = data['dislike'],
            duration = data['duration'],
            url = data['url'],
            )
        
        session.add(new_record)
        session.commit()
        
    except:
            
        print('fail when put in database')


        
