import sys

filename = sys.argv[1]

def return_restaurant_rating_dictionary(filename):
    """Returns resturant ratings from file as a dictionary. """

    restaurant_ratings = {}

    the_file = open(filename)

    for line in the_file:
        line = line.rstrip()
        ratings = line.split(":")

        restaurant_name = ratings[0]
        rating = ratings[1]
        restaurant_ratings[restaurant_name] = rating

    return restaurant_ratings

restaurant_dict = return_restaurant_rating_dictionary(filename)

def print_alph_restaurant_ratings(restaurant_dict): 
    """ Prints restaurant ratings, alphabetized by restaurant name. """  

    for restaurant_name, rating in sorted(restaurant_dict.items()):
        print "{} is rated at {}.".format(restaurant_name,
                                          rating)


print_alph_restaurant_ratings(restaurant_dict)



