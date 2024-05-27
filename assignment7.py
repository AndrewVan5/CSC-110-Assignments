import doctest


MusicScore = tuple[float, int, float, float]
'''
Type Alias for Music Track Score.
(Tempo, Popularity, Danceability, Energy)
'''


MusicInfo = tuple[str, str, str, int, list[int], MusicScore]
'''
Type Alias for Music Track Info.
(ID, Title, Artist, Duration, List of Genres, List of Scores)
'''

TITLE = 1
DURATION = 3
GENRES = 4
SCORE = 5
DANCE = 2

def multiply_by(los: list[str], loi: list[int]) -> None:
    
    '''
    Takes 2 lists and multiplies numbers in first list by corresponding numbers
    in second list. Doesn't return anything.
    
    >>> l = multiply_by(['hi', 4, 8], [2, 4, 8])
    >>> print(l)
    None
    '''
    if len(los) <= len(loi):
        for index in range(len(los)):
            los[index] *= loi[index]
    else:
        for index in range(len(loi)):
            los[index] *= loi[index]        
    
    

def create_scores(tempo: float, pop: int, dance: float, energy: float) -> tuple:
    
    '''
    Takes info of a track's score and compiles them together into a tuple.
    Takes 4 arguments and returns a tuple of values entered.
    
    >>> create_scores(79.124, 5, 0.518, 0.805)
    (79.124, 5, 0.518, 0.805)
    
    >>> create_scores(-74.241, 12, -0.824, -0.123)
    (-74.241, 12, -0.824, -0.123)
    '''
    
    MusicScore = (tempo, pop, dance, energy)
    
    return MusicScore
    
   
def create_music_track(id: str, title: str, artist: str, dur: str, log:
                       str, los: MusicScore) -> tuple:
    
    '''
    Takes info from a track and compiles them together into a tuple.
    Takes 6 arguments and returns a tuple of values entered.
    
    >>> create_music_track('001CyR8xqmmpVZFiTZJ5BC', \
    'She Knows How To Rock Me', 'Taj Mahal', 160107, '', \
    (90.048, 31, 0.826, 0.679)) # doctest: +NORMALIZE_WHITESPACE
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', \
    160107, [], (90.048, 31, 0.826, 0.679))
    
    >>> create_music_track('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, 'R&B:Rap:Pop', \
    (135.414, 55, 0.592, 0.569)) # doctest: +NORMALIZE_WHITESPACE
    ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
        '''
    returned_log = log.split(':')
    
    if log == '':
        returned_log = []
    
    MusicInfo = (id, title, artist, dur, returned_log, los)
    
    return MusicInfo


def get_titles(tracks: list[MusicInfo]) -> list[str]:
    
    '''
    Returns all titles of entered tracks in list.
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
    >>> tracks = [t1, t2, t3]
    >>> get_titles(tracks)
    ['Zangiefs Theme', 'She Knows How To Rock Me', 'SUMMER']
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', '', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', '5 Days', 'The Carters', \
    285200, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
    >>> tracks = [t1, t2, t3]
    >>> get_titles(tracks)
    ['', 'She Knows How To Rock Me', '5 Days']
    '''
    new_list = []
    index = 0
    
    for index in range(len(tracks)):
        new_list.append(tracks[index][TITLE])
        
    return new_list


def is_track_of_genre(tracks: MusicInfo, genre: str) -> bool:
    
    '''
    Returns whether track is same genre as entered genre.
    
    >>> tracks = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMEtrR', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> is_track_of_genre(tracks, 'Pop')
    True
    
    >>> tracks = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMEtrR', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> is_track_of_genre(tracks, 'Hip-hop')
    False
    '''
    index = 0
    
    for genre_value in tracks[GENRES]:
        
        if genre_value.lower() != genre.lower():
            index += 1
            
    return index != len(tracks[GENRES])
    
    
def get_length_of_playlist(tracks: list[MusicInfo]):
    
    '''
    Adds the duration of all tracks together and prints result in minutes,
    seconds, and milliseconds.
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
    >>> tracks = [t1, t2, t3]
    >>> get_length_of_playlist(tracks)
    (10, 14, 480)
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 257284, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 158143, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    525194, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
    >>> tracks = [t1, t2, t3]
    >>> get_length_of_playlist(tracks)
    (15, 40, 621)
    '''
    dur = 0
 
    for track in range(len(tracks)):
        
        dur += tracks[track][DURATION]
        
    total_mins = dur // 60000
    total_secs = (dur - (total_mins * 60000)) // 1000
    total_milli = (dur - ((total_mins + total_secs/60) * 60000)) //1  
        
    
        
    dur_tuple = (total_mins, total_secs, int(total_milli))
    
    return dur_tuple


def get_tracks_with_genre(tracks: list[MusicInfo], genre: str):
    
    '''
    Finds and returns info of tracks that include genre entered.
    
    >>> t1 = ('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', \
    250337, ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.78, 0.729))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> t4 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    
    >>> tracks = [t1, t2, t3, t4]
    
    >>> get_tracks_with_genre(tracks, 'pop') # doctest: +NORMALIZE_WHITESPACE
    [('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', 250337, \
    ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.78, 0.729)), \
    ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', 285200, \
    ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))]    
    '''
    new_list = []
    index = 0
    
    for index in range(len(tracks)):
        if is_track_of_genre(tracks[index], genre) == True:
            new_list.append(tracks[index])
        index += 1
        
    return new_list
    
    
    
def get_highest_danceability_score(lot: list[MusicInfo]) -> float:
    
    '''
    Takes a list of music tracks and returns the highest danceability
    score out of all 4 tracks.
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> t4 = ('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', \
    250337, ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.826, 0.729))
    
    >>> get_highest_danceability_score([t1, t2, t3, t4])
    0.826
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.123, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> t4 = ('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', \
    250337, ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.233, 0.729))
    
    >>> get_highest_danceability_score([t1, t2, t3, t4])
    0.617
    '''
    
    if lot == []:
        return 0
    
    else:
    
        largest = lot[0][SCORE][DANCE]
        index = 0
    
        for value in lot:
            if index < len(lot) and largest < lot[index][SCORE][DANCE]:
                largest = lot[index][SCORE][DANCE]
            
            index += 1
        
    return largest
                                        