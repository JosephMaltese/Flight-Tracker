# Developed by: Joseph Maltese
# Date: 2023-03-30
# Description: This program defines a class called Flight which is used to create Flight objects. Flight objects store
# information through their instance variables regarding various available flights, including the flight number, the
# origin of the flight, and the destination of the flight. This program also utilizes the Airport class, as Airport
# objects are required as parameters when defining a Flight object. A number of methods are defined within the Flight
# class, including constructor, mutator, accessor, and various special methods. This class is also utilized in the
# other python file of this assignment, Aviation.py.

# Imports everything from the Airport class created in the Airport.py file.
from Airport import *

# Defines the Flight class, which encompasses all Flight objects.
class Flight:

    # Defines the constructor, which takes self, the flight number, the Airport object of the origin airport, and the
    # Airport object of the destination airport as parameters. When a Flight variable is created, this constructor
    # executes and establishes the instance variables of the Flight object.
    def __init__(self, flightNo, origAirport, destAirport):
        # Checks that origAirport and destAirport, given as arguments when a Flight object is created, are Airport
        # objects. They must be Airport objects. If so, this branch executes.
        if (isinstance(origAirport, Airport) == True) and (isinstance(destAirport,Airport)):
            # Checks that the flight number, given as an argument, is in the correct formatting, meaning 6 characters in
            # length, with the first 3 being letters, and the last 3 being numbers. If so, this branch executes.
            if (len(flightNo) == 6) and (flightNo[0:3].isalpha() == True) and (flightNo[4:6].isdigit() == True):
                # Defines the instance variables of the flight object. There are instance variables for the flight
                # number, origin airport object, destination airport object, and the codes of both the origin and
                # destination airports.
                self._flightNo = flightNo
                self._origin = origAirport
                self._destination = destAirport

            # If the flight number was not given in the correct format, this branch executes, raising an error that
            # tells the user that the flight number was given incorrectly.
            else:
                raise TypeError("The flight number format is incorrect")
        # If any of origAirport and destAirport are not Airport objects, this branch executes, raising an error that
        # tells the user that the statement is invalid because both the origin and destination must be Airport objects.
        else:
            raise TypeError("The origin and destination must be Airport objects")

    # Defines the special method which is used when the str() or print() operators/functions are called on a Flight
    # object. When one tries to print a Flight object or convert it to a string, the string defined in this method is
    # returned.
    def __repr__(self):
        # Calls the isDomesticFlight() method on the Flight object to check if the flight is domestic (within the same
        # country). If so, then this branch executes.
        if self.isDomesticFlight() == True:
            # Changes the domestOrInter variable to be equal to the string 'domestic'. This string will be used when
            # creating the string that will be returned from this method
            domestOrInter = 'domestic'
        # If the flight is not domestic, then this branch executes.
        else:
            # Changes the domestOrInter variable to the string 'international', since the flight is not domestic.
            domestOrInter = 'international'

        # Returns a string including the flight number of the Flight object, as well as the origin and destination
        # cities, and whether the flight is domestic or international.
        return f'Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()} [{domestOrInter}]'

    # Defines the special method that is used when the == operator is used to compare Flight objects. Allows one to
    # check if two Flight objects are the same (the same flight).
    def __eq__(self, other):
        # Checks that the other variable given as an argument is also a Flight object. If so, this branch executes.
        if isinstance(other, Flight) == True:
            # Checks if the _origin instance variable (which is the Airport object of the origin airport) of the first
            # Flight object is equal to the _origin instance variable of the second Flight object being compared. Also
            # checks that the destination Airport objects are equal. If both conditions are true, this branch executes
            # and returns true.
            if self._origin == other.getOrigin() and self._destination == other.getDestination():
                return True
            # If the two Flight objects do not have equal origin and destination Airport objects, this branch executes,
            # and returns false.
            else:
                return False
        # This branch executes and returns false if the other object is not a Flight object.
        else:
            return False

    # Defines an accessor method which obtains the flight number from the instance variable _flightNo of the Flight
    # object. Returns the flight number.
    def getFlightNumber(self):
        return self._flightNo

    # Defines an accessor method which obtains the origin airport, which is an Airport object. It is stored in the
    # _origin instance variable of the Flight object. Returns the origin airport.
    def getOrigin(self):
        return self._origin

    # Defines an accessor method which obtains the destination airport, which is an Airport object. It is stored in the
    # _destination instance variable of the Flight object. Returns the destination airport.
    def getDestination(self):
        return self._destination

    # Method which checks if a given Flight object is domestic (within the same country)
    def isDomesticFlight(self):
        # Uses the getCountry method to compare the country of the origin and destination airports. If they are equal,
        # then the flight is domestic, and this branch executes, returning true.
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        # If the flight is not domestic, this branch executes, returning false.
        else:
            return False

    # Defines a mutator method which changes the value of the _origin instance variable of the Flight object. The origin
    # of the flight should be an Airport object.
    def setOrigin(self, origin):
        if isinstance(origin, Airport) == True:
            self._origin = origin
        else:
            raise Exception('The origin must be an Airport object.')

    # Defines a mutator method which changes the value of the _destination instance variable of the Flight object. The
    # destination of the flight should be an Airport object.
    def setDestination(self, destination):
        if isinstance(destination, Airport):
            self._destination = destination
        else:
            raise Exception('The destination must be an Airport object.')