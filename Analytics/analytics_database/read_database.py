from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from MyTable import MyTable


def connect_to_database():
    
    try:      
        engine = create_engine('postgresql://postgres:root@localhost/test_db')
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    except:
        print('Fail to connect to the database')
        
        

def read_database(session):

    records = session.query(MyTable.name,
                            MyTable.views,
                            MyTable.like,
                            MyTable.dislike)

    video_count = int()
    views = int()
    likes = int()
    dislikes = int()

    for i in records:
        video_count += 1
        views += int(i[1])
        likes += int(i[2])
        dislikes += int(i[3])        
        
    data = {
        'video_count': video_count,
        'views': views,
        'likes': likes,
        'dislikes': dislikes,
        }    
        
    return data


def print_inf(data):
    
    print('all videos = ' + str(data['video_count']))
    print('sum of views = ' + str(data['views']))
    print('sum of likes = ' + str(data['likes']))
    print('sum of dislikes = ' + str(data['dislikes']))



session = connect_to_database()
data = read_database(session)    
print_inf(data)

