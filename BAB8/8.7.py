def make_album(artist, title, tracks=None):
    """Return a dictionary describing a music album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album
 
 
album_1 = make_album('fleetwood mac', 'rumours')
album_2 = make_album('daft punk', 'discovery')
album_3 = make_album('adele', '21')
album_4 = make_album('fleetwood mac', 'rumours', tracks=11)
 
print(album_1)
print(album_2)
print(album_3)
print(album_4)
 