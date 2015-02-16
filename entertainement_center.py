import media
import fresh_tomatoes

# Create Instances of Movie class
being_there = media.Movie("Being There",
                          "1979",
                          "8.1",
                          "A simple, sheltered gardener becomes an unlikely trusted adviser to a powerful businessman and an insider in Washington politics.",
                          "http://upload.wikimedia.org/wikipedia/en/9/9b/Original_movie_poster_for_Being_There.jpg",
                          "https://www.youtube.com/watch?v=oOOghKacg40")

whiplash = media.Movie("Whiplash",
                       "2014",
                       "8.7",
                       "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
                       "http://upload.wikimedia.org/wikipedia/en/thumb/0/01/Whiplash_poster.jpg/220px-Whiplash_poster.jpg",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

phoebe_in_wonderland = media.Movie("Phoebe in Wonderland",
                                   "2008",
                                   "7.2",
                                   "Confounded by her clashes with the seemingly rule-obsessed world, a troubled young girl seeks enlightenment from her unconventional drama teacher.",
                                   "http://www.impawards.com/2009/posters/phoebe_in_wonderland.jpg",
                                   "https://www.youtube.com/watch?v=7OCJi6_lxAQ")

her = media.Movie("Her",
                  "2013",
                  "8",
                  "A lonely writer develops an unlikely relationship with his newly purchased operating system that's designed to meet his every need.",
                  "http://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
                  "https://www.youtube.com/watch?v=WzV6mXIOVl4")

hugo_cabret = media.Movie("Hugo Cabret",    
                          "2011",
                          "7.6",
                          "Set in 1930s Paris, an orphan who lives in the walls of a train station is wrapped up in a mystery involving his late father and an automaton.",
                          "http://upload.wikimedia.org/wikipedia/en/7/73/Hugo_Poster.jpg",
                          "https://www.youtube.com/watch?v=iQNkETGfA6k")
gravity = media.Movie("Gravity",
                      "2013",
                      "8",
                      "A medical engineer and an astronaut work together to survive after a catastrophe destroys their shuttle and leaves them adrift in orbit.",
                      "http://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")

# Populate list with Movie instances
my_movies = [being_there, whiplash, phoebe_in_wonderland, her, hugo_cabret, gravity]

# Create and open html page to display my_movies list
fresh_tomatoes.open_movies_page(my_movies)

