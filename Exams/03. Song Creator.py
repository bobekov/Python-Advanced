def add_songs(*args):
    result = {}
    for title, text in args:
        if title not in result:
            result[title] = []
        if text:
            result[title].extend(text)

    songs = []
    for key, value in result.items():
        songs.append('- ' + key)
        if value:
            songs.extend(value)

    return '\n'.join(songs)