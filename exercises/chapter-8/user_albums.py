# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.
def make_album(artist, album_title, tracks=0):
    """Returns a dictionary containing information about an album."""

    album = {
        'artist': artist.title(),
        'album': album_title.title()
    }

    if tracks:
        album['tracks'] = tracks
    
    return album

while True:
    print("\nInput an album below \n(type 'q' to quit)")
    artist =  input("Artist name: ")
    if artist == 'q':
        break

    album_title = input("Album title: ")
    if album_title == 'q':
        break

    album = make_album(artist, album_title)
    print("\n")
    print(album)