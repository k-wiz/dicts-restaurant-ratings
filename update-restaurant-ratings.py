import sys
import random

filename = sys.argv[1]

user_name = raw_input('Hello, what is your name? ')
restaurant_ratings = {}

def return_restaurant_rating_dictionary(filename):
    """Returns resturant ratings from file as a dictionary. """

    the_file = open(filename)

    for line in the_file:
        line = line.rstrip()
        ratings = line.split(":")

        restaurant_name = ratings[0]
        rating = ratings[1]
        restaurant_ratings[restaurant_name] = rating

    return restaurant_ratings

def print_alph_restaurant_ratings(restaurant_dict): 
    """ Prints restaurant ratings, alphabetized by restaurant name. """  

    for restaurant_name, rating in sorted(restaurant_dict.items()):
        # print "{} is rated at {}.".format(restaurant_name,
        #                                   rating)

        
        restaurant_name = restaurant_dict.items[0]
        rating = restaurant_dict.items[1]

        print restaurant_name, rating



restaurant_dict = return_restaurant_rating_dictionary(filename)

# random_restaurant = random.choice(restaurant_dict[key])

# print random_restaurant

print_alph_restaurant_ratings(restaurant_dict)
