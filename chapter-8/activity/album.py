def make_album(artist_name, artist_album, number_of_songs=None):
    album = {'name' : artist_name, 'album':artist_album}
    if number_of_songs is not None:
        album['songs'] = number_of_songs
    return album

albums = make_album('radiohead', 'pablo honey')
print(albums)
albums = make_album('amy winehouse', 'back to black', 11)
print(albums)
albums = make_album('kendrick lamar', 'good kid')
print(albums)


    