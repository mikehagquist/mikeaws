#!/usr/bin/env python3

'''
Copyright 2018, Victoria S. Yanovich, yanovich.net
Licensed under the Eiffel Forum License 2.
This cross compares the current IMDb Top 250 movies of all times with what
is available on streaming platforms.
* Amazon Prime
    ./movies.py amp
* Netflix
    ./movies.py nfx
* Hulu
    ./movies.py hlu
'''

from justwatch import JustWatch
import sys

just_watch = JustWatch(country='US')

list_of_movies = """The Shawshank Redemption (1994)
The Godfather (1972)
The Godfather: Part II (1974)
The Dark Knight (2008)
12 Angry Men (1957)
Schindler's List (1993)
The Lord of the Rings: The Return of the King (2003)
Pulp Fiction (1994)
The Good, the Bad and the Ugly (1966)
Fight Club (1999)
The Lord of the Rings: The Fellowship of the Ring (2001)
Forrest Gump (1994)
Star Wars: Episode V - The Empire Strikes Back (1980)
Inception (2010)
The Lord of the Rings: The Two Towers (2002)
One Flew Over the Cuckoo's Nest (1975)
Goodfellas (1990)
The Matrix (1999)
Seven Samurai (1954)
Avengers: Infinity War (2018)
City of God (2002)
Star Wars: Episode IV - A New Hope (1977)
Se7en (1995)
The Silence of the Lambs (1991)
It's a Wonderful Life (1946)
Life Is Beautiful (1997)
The Usual Suspects (1995)
Spirited Away (2001)
Saving Private Ryan (1998)
Léon: The Professional (1994)
The Green Mile (1999)
Interstellar (2014)
American History X (1998)
Psycho (1960)
City Lights (1931)
Once Upon a Time in the West (1968)
Casablanca (1942)
Modern Times (1936)
The Intouchables (2011)
The Pianist (2002)
The Departed (2006)
Terminator 2 (1991)
Back to the Future (1985)
Raiders of the Lost Ark (1981)
Rear Window (1954)
Whiplash (2014)
Gladiator (2000)
The Lion King (1994)
The Prestige (2006)
Memento (2000)
Apocalypse Now (1979)
Alien (1979)
The Great Dictator (1940)
Cinema Paradiso (1988)
Grave of the Fireflies (1988)
Sunset Boulevard (1950)
Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)
The Lives of Others (2006)
Paths of Glory (1957)
The Shining (1980)
Django Unchained (2012)
WALL·E (2008)
Coco (2017)
Princess Mononoke (1997)
American Beauty (1999)
The Dark Knight Rises (2012)
Witness for the Prosecution (1957)
Oldboy (2003)
Aliens (1986)
Once Upon a Time in America (1984)
Das Boot (1981)
Citizen Kane (1941)
Vertigo (1958)
North by Northwest (1959)
Braveheart (1995)
Reservoir Dogs (1992)
Star Wars: Episode VI - Return of the Jedi (1983)
Your Name (2016)
M (1931)
Dangal (2016)
Requiem for a Dream (2000)
Amadeus (1984)
Like Stars on Earth (2007)
Amélie (2001)
Lawrence of Arabia (1962)
A Clockwork Orange (1971)
Eternal Sunshine of the Spotless Mind (2004)
Double Indemnity (1944)
Taxi Driver (1976)
2001: A Space Odyssey (1968)
3 Idiots (2009)
Toy Story (1995)
Singin' in the Rain (1952)
Full Metal Jacket (1987)
To Kill a Mockingbird (1962)
Inglourious Basterds (2009)
Bicycle Thieves (1948)
The Sting (1973)
The Kid (1921)
Toy Story 3 (2010)
Good Will Hunting (1997)
Snatch (2000)
The Hunt (2012)
Monty Python and the Holy Grail (1975)
For a Few Dollars More (1965)
Scarface (1983)
L.A. Confidential (1997)
The Apartment (1960)
Metropolis (1927)
A Separation (2011)
Rashomon (1950)
Indiana Jones and the Last Crusade (1989)
Up (2009)
Yojimbo (1961)
All About Eve (1950)
Batman Begins (2005)
Some Like It Hot (1959)
Unforgiven (1992)
The Treasure of the Sierra Madre (1948)
Downfall (2004)
Die Hard (1988)
Heat (1995)
My Father and My Son (2005)
Raging Bull (1980)
Ikiru (1952)
The Great Escape (1963)
Incendies (2010)
The Third Man (1949)
Children of Heaven (1997)
Pan's Labyrinth (2006)
Chinatown (1974)
My Neighbor Totoro (1988)
Three Billboards Outside Ebbing, Missouri (2017)
Judgment at Nuremberg (1961)
Ran (1985)
Howl's Moving Castle (2004)
The Secret in Their Eyes (2009)
The Gold Rush (1925)
The Bridge on the River Kwai (1957)
On the Waterfront (1954)
Lock, Stock and Two Smoking Barrels (1998)
A Beautiful Mind (2001)
The Seventh Seal (1957)
Inside Out (2015)
Casino (1995)
Room (2015)
Mr. Smith Goes to Washington (1939)
The Elephant Man (1980)
The Wolf of Wall Street (2013)
V for Vendetta (2005)
Blade Runner (1982)
Warrior (2011)
Wild Strawberries (1957)
The General (1926)
Dial M for Murder (1954)
Trainspotting (1996)
Sherlock Jr. (1924)
No Country for Old Men (2007)
Gone with the Wind (1939)
The Sixth Sense (1999)
There Will Be Blood (2007)
Gran Torino (2008)
Fargo (1996)
The Deer Hunter (1978)
The Thing (1982)
Incredibles 2 (2018)
Finding Nemo (2003)
The Big Lebowski (1998)
Come and See (1985)
Kill Bill: Vol. 1 (2003)
Cool Hand Luke (1967)
Rebecca (1940)
Shutter Island (2010)
Tokyo Story (1953)
Sunrise (1927)
Hacksaw Ridge (2016)
Mary and Max (2009)
How to Train Your Dragon (2010)
Gone Girl (2014)
The Bandit (1996)
Wild Tales (2014)
Into the Wild (2007)
Life of Brian (1979)
It Happened One Night (1934)
Andrei Rublev (1966)
Jurassic Park (1993)
Platoon (1986)
In the Name of the Father (1993)
Stand by Me (1986)
Rang De Basanti (2006)
The Grand Budapest Hotel (2014)
Network (1976)
Hotel Rwanda (2004)
The Passion of Joan of Arc (1928)
Stalker (1979)
Ben-Hur (1959)
The Wages of Fear (1953)
The Truman Show (1998)
Persona (1966)
Rush (2013)
12 Years a Slave (2013)
Memories of Murder (2003)
Million Dollar Baby (2004)
Mad Max: Fury Road (2015)
The 400 Blows (1959)
Spotlight (2015)
Logan (2017)
Before Sunrise (1995)
Amores Perros (2000)
Hachi: A Dog's Tale (2009)
Blade Runner 2049 (2017)
Prisoners (2013)
Butch Cassidy and the Sundance Kid (1969)
The Princess Bride (1987)
Nausicaä of the Valley of the Wind (1984)
Catch Me If You Can (2002)
Harry Potter and the Deathly Hallows: Part 2 (2011)
Rocky (1976)
The Maltese Falcon (1941)
La La Land (2016)
The Grapes of Wrath (1940)
Barry Lyndon (1975)
Monsters, Inc. (2001)
The Nights of Cabiria (1957)
Donnie Darko (2001)
A Wednesday (2008)
Diabolique (1955)
Gandhi (1982)
The Terminator (1984)
Paper Moon (1973)
La Haine (1995)
Groundhog Day (1993)
The Wizard of Oz (1939)
Touch of Evil (1958)
Dead Poets Society (1989)
Jaws (1975)
The Bourne Ultimatum (2007)
In the Mood for Love (2000)
The Help (2011)
8½ (1963)
Annie Hall (1977)
Guardians of the Galaxy (2014)
Before Sunset (2004)
The Best Years of Our Lives (1946)
Paris, Texas (1984)
Pirates of the Caribbean: The Curse of the Black Pearl (2003)
Beauty and the Beast (1991)
The Battle of Algiers (1966)
Gangs of Wasseypur (2012)
Dog Day Afternoon (1975)"""

list_of_movies = list_of_movies.split('\n')


provider = str(sys.argv[1])
out=''

print ("Searching for: " + provider)

for movie in list_of_movies:
    results_by_providers = just_watch.search_for_item(query=movie,
                                                      providers=[provider],
                                                      content_types=['movie'])
    out = 'n'
    if len(results_by_providers['items']) > 0:
        for result in results_by_providers['items']:
            if result['title'] == movie[:-7] and \
                    result['original_release_year'] == int(movie[-5:-1]):
                out = 'y'

    print(out)