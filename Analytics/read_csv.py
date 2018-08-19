import csv

def read_csv():

    # put in there csv file, which need to analysis
    with open('videos.csv') as f:
        
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
    
data = read_csv()

print('all videos = ' + str(data['video_count']))
print('all views = ' + str(data['views']))
print('all likes = ' + str(data['likes']))
print('all dislikes = ' + str(data['dislikes']))
