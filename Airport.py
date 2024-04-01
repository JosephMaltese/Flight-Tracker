# Developed by: Joseph Maltese
# Date: 2023-03-30
# Description: This program creates a class called Airport, which is used to create Airport objects. Airport objects
# contain information through their instance variables regarding the airport code, city, country, and continent of each
# Airport object. This class defines several methods which can act upon Aiport objects, such as getCode(), which returns
# the airport code of the Airport object. There are a number of both accessor and mutator methods, meant to either
# return information from an instance variable, or alter information in an instance variable. This class will be called
# and utilized in the other two python files for this assignment, Flight.py, and Aviation.py.

# Defines the class Airport, which encompasses all airport objects.
class Airport:
    # Define the constructor, which takes self, the airport code, the airport city, country and continent as the
    # parameters.
    def __init__(self, code, city, country, continent):
        # Define instance variables for each Airport objects airport code,city,country, and continent. Initialize them
        # to the values given as arguments when the Airport object is defined.
        self._code = code
        self._city = city
        self._country = country
        self._continent = continent

    # Defines the special method which is used when the str() or print() operators/functions are called on an Airport
    # object. When one tries to print an Airport object or convert it to a string, the string defined in this method is
    # returned.
    def __repr__(self):
        # Returns a string including the code of the Airport object, as well as both the city and country of the Airport
        # in parentheses. Accesses these values from the corresponding instance variables of the object.
        return str(self._code) + f" ({self._city}, {self._country})"

    # Defines the accessor method which obtains the airport code and returns it. Obtains this value from the _code
    # instance variable of the Airport object.
    def getCode(self):
        # Returns the airport code
        return self._code
    # Defines the accessor method which obtains the city of the airport and returns it. Obtains this value from the
    # _city instance variable of the Airport object.
    def getCity(self):
        # Returns the city in which the airport is located.
        return self._city

    # Defines the accessor method which obtains the country of the airport and returns it. Obtains this value from the
    # _country instance variable of the Airport object.
    def getCountry(self):
        # Returns the country in which the airport is located.
        return self._country

    # Defines the accessor method which obtains the continent of the airport and returns it. Obtains this value from the
    # _continent instance variable of the Airport object.
    def getContinent(self):
        # Returns the continent in which the airport is located.
        return self._continent
    # Defines the mutator method which alters the city of the airport. It does this by changing the value of the _city
    # instance variable of the Airport object.
    def setCity(self, city):
        # Changes the city in which the airport is located
        self._city = city

    # Defines the mutator method which alters the country of the airport. It does this by changing the value of the
    # _country instance variable of the Airport object.
    def setCountry(self,country):
        # Changes the country in which the airport is located.
        self._country = country

    # Defines the mutator method which alters the continent of the airport. It does this by changing the value of the
    # _continent instance variable of the Airport object.
    def setContinent(self,continent):
        # Changes the country in which the airport is located.
        self._continent = continent



