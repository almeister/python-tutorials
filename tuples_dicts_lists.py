### Tuples

## What are tuples?
# Tuples represent an immutable (unchangeable) record of elements that can
# be heterogeneous (different types), separated by commas.

# Tuples can contain 0 or more elements, eg: (name, age)
id_card = ("Link", 17)

# An empty tuple (phone_number)
secondary_contact = ()

# A tuple with one element only
lute_box_prizes = ("Gold coins",)

## Where are tuples used?
# Tuples are useful for passing data records around, especially simple ones
# where a class would be over-kill, eg:

# Positional coordinates (x, y, z)
coordinates = (0, 1, 1)
print("coordinates: " + str(coordinates))


# For reference, a coordinates class could look like this:
class Coordinates:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# And this is how you would instantiate a Coordinates object
coords = Coordinates(0, 2, 3)

## How are tuples used?
# Unpacking into variables, eg:
x, y, z = coordinates
print("Unpacked coordinates:")
print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))

# Accessing elements by index, eg:
name = id_card[0]
print("Name from id_card is: " + name)

# Tuples can also be named, to make them more readable, eg:
from collections import namedtuple

# Define the new named tuple type, NamedCoordinates
NamedCoordinates = namedtuple("NamedCoordinates", "x y z")

# Instantiate a new NamedCoordinates
named_coords = NamedCoordinates(0, 2, 3)
print(named_coords)

# Access elements by attribute like a class (named tuples only)
print("x attribute of named_coords is: " + str(named_coords.x))
print("y attribute of named_coords is: " + str(named_coords.y))
print("z attribute of named_coords is: " + str(named_coords.z))


### Dictionaries

## What
# Dictionaries are a mapped data type or set of 'key: value' pairs, eg:

# user_id: name
users = {1: "Alex Kidd", 2: "Hestu Raddler"}

## Where
# Dictionaries are used wherever you want to represent various data with titles, eg: in tracking user data

user_data = {"name": "Link", "age": 15, "gender": "male", "nationality": "Hylian",
             "games_played": ["Super Mario Bros", "Tabletop Simulator"]}
print(user_data)

## How
# Storing a new / changing an existing value
user_data["age"] = 17
user_data["last_login"] = "02/10/2021 03:30:34"
print(user_data)

# Retrieving a value
user_name = user_data["name"]
print(user_name)

# Checking if a key already exists
if (user_data["nationality"] != None):
    print("user_data already has nationality: " + user_data["nationality"])

# Deleting a key:value pair
del user_data["games_played"]
print(user_data)

# Convert keys to a list
user_data_list = list(user_data)
print(user_data_list)

# Iterate over key and values in a loop using dict.items()
for key, value in user_data.items():
    print(key + " : " + str(value))


### Lists

## What are lists?
# A list is a mutable (changeable) sequence of values which in Python can heterogeneous, eg:

players = ["Player-1", "AI-1", "Player-2"]
print(players)

## Where
# Lists are usually used where you want to store homogenous (same type) data, then easily iterate and change it, eg:
friends_online = ["Benjy", "Murphy", "Artem"]

## How

# Count

# Get length
if (len(friends_online)):
    print(friends_online)

# Append

# Remove or pop

# Concatenate

# Iterate

# Access / Replace

# All other Sequence operations, eg: sort
# https://docs.python.org/3/library/stdtypes.html?highlight=lists#typesseq-common
