user={}
name=input("what is your name:")
age=input("what is your name:")
fav_movie=input('your favorite movie seperated by comma:').split(',')
fav_songs=input('your favorite songs seperated by comma:').split(',')
user['name']=name
user['age']=age
user['fav_movie']=fav_movie
user['fav_songs']=fav_songs
for i,j in user.items():
    print(f"{i}:{j}")