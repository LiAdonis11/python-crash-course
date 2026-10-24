def make_album(artist_name, artist_album):
    album = {'name' : artist_name, 'album':artist_album}
    
    # if number_of_songs is not None:
    #     album['songs'] = number_of_songs
    return album
        
while True:
    print("Enter 'quit' to quit the program")
        
    artist = input("Enter the name of the artist: ")
    if artist == 'quit':
        break
    title = input("Enter its album: ")
    if title == 'quit':
        break
            
    album = make_album(artist,title)
    print(album)
    





# albums = make_album('radiohead', 'pablo honey')
# print(albums)
# albums = make_album('amy winehouse', 'back to black', 11)
# print(albums)



    