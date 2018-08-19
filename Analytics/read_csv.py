import csv


# put in there csv file, which need to analysis
path = 'videos.csv'

def read_csv(path):

    with open(path) as f:
        
        data = csv.reader(f)
        
        video_count = int()
        views = int()
        likes = int()
        dislikes = int()

        for line in data:
            
            if line != []:
                video_count += 1
                views += int(line[1])
                likes += int(line[2])
                dislikes += int(line[3])     
                           
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


data = read_csv(path)    
print_inf(data)
