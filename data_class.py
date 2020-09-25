from dataclasses import dataclass


@dataclass
class Sailboat:
    """example of a data class that defines a sailboat.
    You can do this with a regular class, but rank and suit are repeated 3x to
    initialize the object.
    More info here: https://realpython.com/python-data-classes/"""
    make: str
    year: int
    length: int


sailboat = Sailboat('Catalina', '1992', '286')

print("The sailboat is a: {}{} made in {}".format(
    sailboat.make,
    sailboat.length,
    sailboat.year)
    )

print(sailboat == Sailboat('Catalina', '1992', '286'))