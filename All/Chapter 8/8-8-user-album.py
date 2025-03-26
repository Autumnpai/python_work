def make_album(artist, album, songs=None):
    """
    make a dictionary of an album
    lines
    lines
    """
    album_dict = {}
    album_dict['artist'] = artist.title()
    album_dict['album'] = album.title()
    if songs:
        album_dict['songs'] = songs
    return album_dict

while True:
    artist = input('Please give me the name of the artist ("q" for quit): ')
    if artist == 'q':
        break
    album = input('Please give me the title of the ablum ("q" for quit): ')
    if album == 'q':
        break
    print(make_album(artist, album))


# print(album1)
# print(album2)
# print(album3)