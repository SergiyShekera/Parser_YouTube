from sqlalchemy import Column, Integer, Text
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
