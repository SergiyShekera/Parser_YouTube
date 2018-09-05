from get_csv_data import get_csv_data


# put in there csv files, which need to analysis
path_old = 'videos_old.csv'
path_new = 'videos_new.csv'

def comparison(path_old, path_new):

    data_old = get_csv_data(path_old)
    data_new = get_csv_data(path_new)

    video_count = data_new['video_count'] - data_old['video_count']

    views = data_new['views'] - data_old['views']

    likes = data_new['likes'] - data_old['likes']

    dislikes = data_new['dislikes'] - data_old['dislikes']
    
    if int(video_count) > 0:
        video_count = '+' + str(video_count)
        
    if int(views) > 0:
        views = '+' + str(views)
        
    if int(likes) > 0:
        likes = '+' + str(likes)
        
    if int(dislikes) > 0:
        dislikes = '+' + str(dislikes)

    data = {
        'video_count': video_count,
        'views': views,
        'likes': likes,
        'dislikes': dislikes,
        }

    return data


def print_comparsion_inf(data):
    
    print('video amount difference = ' + str(data['video_count']))
    print('video views difference = ' + str(data['views']))
    print('video likes difference = ' + str(data['likes']))
    print('video dislikes difference = ' + str(data['dislikes']))


data = comparison(path_old, path_new)
print_comparsion_inf(data)

