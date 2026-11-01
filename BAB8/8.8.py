def make_album(artist, title, tracks=None):
    """Return a dictionary describing a music album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album
 
 
while True:
    print("\nPlease tell me about an album.")
    print("(Enter 'q' at any time to quit)")
 
    artist = input("Artist name: ")
    if artist == 'q':
        break
 
    title = input("Album title: ")
    if title == 'q':
        break
 
    album = make_album(artist, title)
    print(album)
 