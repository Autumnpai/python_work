def make_album(artist, album, songs=None):
    """make a dictionary of an album"""
    album_dict = {}
    album_dict['artist'] = artist
    album_dict['album'] = album
    if songs:
        album_dict['songs'] = songs
    return album_dict

album1 = make_album('The Beatles', 'Abbey Road')
album2 = make_album('崔健', '一无所有', 10)
album3 = make_album('The Who', 'Who Are You', 9)

print(album1)
print(album2)
print(album3)

# I made some more

def display_album(album_dict):
    """Display the album information"""
    print("\n")
    for key, value in album_dict.items():
        print(f"{key.title()}: {value}")


display_album(album1)
display_album(album2)
display_album(album3)