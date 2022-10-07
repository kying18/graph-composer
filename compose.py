"""
Implemented Markov Chain Composer by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

"""
Empty Compose Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import os
import re
import string
import random

from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'rb') as f:
        text = f.read().decode("utf-8")

        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    words = words[:1000]
    return words

def make_graph(words):
    g = Graph()
    previous_word = None
    

    for word in words:
        word_vertex = g.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex
    
    g.generate_probability_mappings()
    return g

        
def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

def main(artist):
    words = []

    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)

    g = make_graph(words)

    composition = compose(g, words, 100)
    return ' '.join(composition)

#made new function in order that all function can work
def mainw():
    words = get_words_from_text(choice+'/hp_sorcerer_stone.txt')
    g = make_graph(words)

    composition = compose(g, words, 100)
    return ' '.join(composition)

if __name__ == '__main__':
    #user input
    choice = input('Select folder you wanna graph: texts or song ')
    if choice == 'song':
        artist = input('Put Your Artist Name: alan_warker, armin_van_buuren, avicii, billie_eilish, celine_dion, drake, green_day, halsey, Lady_Gaga, linkin_park, queen, taylor_swift ')
        print(main(artist))
    elif choice == 'texts':
        print(mainw())
    else:
        quit()

    #made replay game
    while True:
        again = input('Still wanna try? (Y/n) ')
        if again == 'Y' or again == 'y':
            choice = input('Select folder you wanna graph: texts or song ')
            if choice == 'song':
                artist = input('Put Your Artist Name: alan_warker, armin_van_buuren, avicii, billie_eilish, celine_dion, drake, green_day, halsey, Lady_Gaga, linkin_park, queen, taylor_swift ')
                print(main(artist))
            elif choice == 'texts':
                print(mainw())
            else:
                quit()
        else:
            quit()
