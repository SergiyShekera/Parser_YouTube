import csv


def write_csv(data):
    
    with open('videos.csv', 'a') as f:
        
        order = ['name', 'views', 'like', 'dislike','duration', 'url']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)
