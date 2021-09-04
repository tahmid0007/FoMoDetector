from googleapiclient.discovery import build
from datetime import datetime,timedelta
from csv import writer

viewCount = 0
commentCount = 0
likeCount = 0

today = datetime.utcnow()
temp = today - timedelta(days = 5) #always bigger
after = temp.isoformat() + 'Z'
 
temp_before = today - timedelta(days = 1) # 1 means upto yesterday, always smaller
before = temp_before.isoformat() + 'Z'

key = "YOUR_YOUTUBE_API_KEY"
youtube = build('youtube','v3',developerKey = key)

id_George = "UCI7M65p3A-D3P4v5qW8POxQ"
id_Banter = "UCN9Nj4tjXbVTLYWN0EKly_Q"
id_altdaily = "UCbLhGKVY-bJPcawebgtNfbw"
id_moon = "UCc4Rz_T9Sb1w5rqqo9pL1Og"

id = id_George

###################### LAST 5 DAYS DATA AVG VIEW ... #######################################################
data = youtube.search().list(part = "snippet", channelId = id,order = "date", type = "video", maxResults=200, publishedBefore = before, publishedAfter = after).execute()

for item in data['items']:
    vdoId = item['id']['videoId']
    stat = youtube.videos().list(part = "contentDetails,statistics", id = vdoId).execute()
    
    viewCount = viewCount + int(stat['items'][0]['statistics']['viewCount'])
    commentCount = commentCount + int(stat['items'][0]['statistics']['commentCount'])
    likeCount = likeCount + int(stat['items'][0]['statistics']['likeCount'])

list_data = [int(viewCount/len(data['items'])),int(commentCount/len(data['items'])),int(likeCount/len(data['items']))]
    
with open('george.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(list_data)  
    f_object.close()


id = id_Banter

data = youtube.search().list(part = "snippet", channelId = id,order = "date", type = "video", maxResults=200, publishedBefore = before, publishedAfter = after).execute()

for item in data['items']:
    vdoId = item['id']['videoId']
    stat = youtube.videos().list(part = "contentDetails,statistics", id = vdoId).execute()
    
    viewCount = viewCount + int(stat['items'][0]['statistics']['viewCount'])
    commentCount = commentCount + int(stat['items'][0]['statistics']['commentCount'])
    likeCount = likeCount + int(stat['items'][0]['statistics']['likeCount'])

list_data = [int(viewCount/len(data['items'])),int(commentCount/len(data['items'])),int(likeCount/len(data['items']))]
    
with open('banter.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(list_data)  
    f_object.close()
