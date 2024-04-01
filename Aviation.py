# Developed by: Joseph Maltese
# Date: 2023-03-31
# Description: This program defines a class called Aviation, which is used to create Aviation objects. When used in
# conjunction with Airport and Flight objects, and text files containing related data, Aviation objects can be used
# to obtain relevant information regarding possible flights. For example, methods exist in ths class to display
# information regarding all the existing flights to or from a specific city or country. This program utilizes both the
# Flight and Airport classes previously created in order to obtain/store relevant information. Various methods exist
# within the class, including constructors, accessors, mutators, methods which read data from text files and stores the
# data accordingly, and other methods which check data and produce possible outcomes. This class can be used to aid in
# the development of an aviation system which controls and displays information regarding flights around the world.

# Import everything from both the Flight and Airport classes.
from Flight import *
from Airport import *

# Defines the Aviation class
class Aviation:
    # Defines the constructor, which takes no parameters other than self. When an Aviation object is declared, this
    # method executes.
    def __init__(self):
        # Declares each instance variable

        # Defines the instance variable _allAirports, and initializes it as an empty list. This variable will store all
        # the information from the text file about airports, storing them as Airport objects.
        self._allAirports = []
        # Defines the instance variable _allFlights, and initializes it as an empty dictionary. This variable will store
        # all the information from the text file about flights, storing them as flight objects.
        self._allFlights = {}
        # Defines the instance variable _allCountries, and initializes it as an empty dictionary. This variable will
        # store all the information from the text file about countries, storing it with its country as the key, and the
        # associated continent as the value of the key.
        self._allCountries = {}

    # Defines the accessor method which returns the instance variable _allAirports, which is a list storing airport
    # objects. This conveys information about all the existing airports from the text files.
    def getAllAirports(self):
        return self._allAirports

    # Defines the accessor method which returns the instance variable _allFlights, which is a dictionary storing flight
    # numbers as keys, and their associated Flight objects as values.
    def getAllFlights(self):
        return self._allFlights

    # Defines the accessor method which returns the instance variable _allCountries, which is a dictionary storing
    # country names as keys, and continents as the associated values.
    def getAllCountries(self):
        return self._allCountries

    # Defines the mutator method which changes the value of the instance variable _allAirports. Takes a list, airports,
    # as a parameter, and sets the instance variable equal to it.
    def setAllAirports(self, airports):
        if isinstance(airports, list):
            self._allAirports = airports
        else:
            raise Exception('airports parameter must be a list.')

    # Defines the mutator method which changes the value of the instance variable _allFlights. Takes a dictionary,
    # flights, as a parameter, and sets the instance variable equal to it.
    def setAllFlights(self, flights):
        if isinstance(flights, dict):
            self._allFlights = flights
        else:
            raise Exception('flights parameter must be a dictionary.')

    # Defines the mutator method which changes the value of the instance variable _allCountries. Takes a dictionary,
    # countries, as a parameter, and sets the instance variable equal to it.
    def setAllCountries(self, countries):
        if isinstance(countries, dict):
            self._allCountries = countries
        else:
            raise Exception('countries parameter must be a dictionary.')

    # Defines a method, loadData, to read data from text files. Other than self, there are 3 parameters taken by this
    # method. The parameters are an airport data text file, a flight data text file, and a country data text file.
    def loadData(self, airportFile, flightFile, countriesFile):
        self._allAirports = []
        self._allFlights = {}
        self._allCountries = {}

        # Try statement which attempts to read from the text files.
        try:
            # With statement which opens the file storing country information, reads from it, and closes it when
            # finished. Gives the file the variable name countriesText.
            with open(countriesFile, 'r', encoding='utf8') as countriesText:

                # Reads the first line from the file and stores it as a string in the line variable.
                line = countriesText.readline()

                # While the line variable is not equal to an empty string (the end of the file has not been reached),
                # this while loop will continue to iterate.

                while line != '':
                    # Checks if the line is a blank line. If so, this branch executes and the line gets skipped.
                    if line == '\n':
                        # Reads the next line in the file.
                        line = countriesText.readline()
                        # Continues to the start of the while loop.
                        continue

                    # Strips the whitespace from both ends of the line and splits the data from the line into a list
                    # using the comma as a delimiter.
                    line = line.strip().split(',')
                    # For loop that iterates for each element in the list created in the previous line.
                    for element in range(len(line)):
                        # Strips each element in the list of its whitespace on each side.
                        line[element] = line[element].strip()

                    # Alters the dictionary instance variable so that the 0th element (country) in the list is a key in
                    # the dictionary, and the 1st element (continent) is its associated value.
                    self._allCountries[line[0]] = line[1]

                    # Reads the next line in the text file.
                    line = countriesText.readline()

            # With statement which opens the file storing airport information, reads from it, and closes it when
            # finished. Gives the file the variable name airportsText.
            with open(airportFile, 'r', encoding='utf8') as airportsText:

                # Reads the first line in the text, storing it as a string in the line variable.
                line = airportsText.readline()

                # While the line variable is not equal to an empty string (the end of the file has not been reached),
                # this while loop will continue to iterate.
                while line != '':
                    # Checks if the line is a blank line. If so, this branch executes and the line gets skipped.
                    if line == '\n':
                        # Reads the next line in the file.
                        line = airportsText.readline()
                        # Continues to the start of the while loop.
                        continue

                    # Splits the data from the line into a list using the comma as a delimiter.
                    line = line.strip().split(',')
                    # For loop that iterates for each element in the list created in the previous line.
                    for element in range(len(line)):
                        # Strips each element in the list of its whitespace on each side.
                        line[element] = line[element].strip()

                    # Since the country is in the 1st index position in the list created, this accesses the countries
                    # associated continent through the dictionary stored in the instance variable _allCountries
                    continent = self._allCountries[line[1]]

                    # Creates an airport object using the data from the line as arguments, since the airport code is the
                    # 0th element of the list, the city is the 2nd index, and the country is the 1st index. Appends this
                    # airport object to the instance variable _allAirports, which is a list of Airport objects.
                    self._allAirports.append(Airport(line[0], line[2], line[1], continent))

                    # Reads the next line in the text file.
                    line = airportsText.readline()

            # With statement which opens the file storing flight information, reads from it, and closes it when
            # finished. Gives the file the variable name flightsText.
            with open(flightFile, 'r', encoding='utf8') as flightsText:

                # Reads the first line in the text, storing it as a string in the line variable.
                line = flightsText.readline()

                # While the line variable is not equal to an empty string (the end of the file has not been reached),
                # this while loop will continue to iterate.
                while line != '':
                    # Checks if the line is a blank line. If so, this branch executes and the line gets skipped.
                    if line == '\n':
                        # Reads the next line in the file.
                        line = flightsText.readline()
                        # Continues to the start of the while loop.
                        continue

                    # Strips the whitespace from both ends of the line and splits the data from the line into a list
                    # using the comma as a delimiter.
                    line = line.strip().split(',')

                    # For loop that iterates for each element in the list created in the previous line.
                    for element in range(len(line)):
                        # Strips each element in the list of its whitespace on each side.
                        line[element] = line[element].strip()

                    # Try statement which tries to add the flight information to the dictionary of flights.
                    try:
                        # If the origin airport code does not exist as a key in the dictionary _allFlights, this branch
                        # executes.
                        if line[1] not in self._allFlights:
                            # Creates a key in the dictionary with the origin airport code, and initializes it as an
                            # empty list.
                            self._allFlights[line[1]] = []
                            # Appends a flight object using the flight information from the line as arguments to the
                            # list associated with the given key. Obtains the origin and destination airport objects
                            # using the getAirportByCode method since the airport codes are given on the line.
                            self._allFlights[line[1]].append(Flight(line[0], self.getAirportByCode(line[1]), self.getAirportByCode(line[2])))
                        # If the origin airport code already exists as a key in the dictionary, this branch executes.
                        else:
                            # Appends a flight object using the flight information from the line as arguments to the
                            # list associated with the given key. Obtains the origin and destination airport objects
                            # using the getAirportByCode method since the airport codes are given on the line.
                            self._allFlights[line[1]].append(Flight(line[0], self.getAirportByCode(line[1]), self.getAirportByCode(line[2])))
                    # Except statement which catches any errors that occur when trying to access the Airport objects
                    # used as arguments when creating each flight object. Tells the user that the airport code listed on
                    # the line could not be found.
                    except:
                        print('Could not find airport in line')

                    line = flightsText.readline()
            # If everything occurred properly without error, returns true.
            return True

        # If any unforeseen errors occur when reading from the text file, this except statement catches it and returns
        # false.
        except:
            return False

    # Defines a method which obtains an Airport object associated with a given airport code. Takes a code as a parameter
    # and finds the related Airport object.
    def getAirportByCode(self, code):
        # Boolean that indicates the object has not yet been found.
        found = False
        # Iterates through each Airport object in the list of all airports.
        for airport in self._allAirports:
            # If the airport code associated with the current Airport object is equal to the given code, then the
            # required object has been found. This branch executes.
            if airport.getCode() == code:
                # Returns the airport object.
                return airport

        # If the object is not found in the list of airports, returns -1
        if not found:
            return -1

    # Method that finds all flights associated with a given city. If either the origin or destination is the given city,
    # the flight gets added to a list of flights.
    def findAllCityFlights(self, city):
        # List which stores all the flights that either originate or land in the given city.
        flightList = []

        # Iterates through each key in the dictionary of flights.
        for airport in self._allFlights:
            # Iterates through each element of the list of flight objects associated with each key.
            for flight in self._allFlights[airport]:
                # If the city of the origin airport is equal to the given city or the city of the destination airport is
                # equal to the given city, this branch executes.
                if city == flight.getOrigin().getCity() or city == flight.getDestination().getCity():
                    # Adds the flight object to the list of flights
                    flightList.append(flight)
        # Return the list of associated flight objects.
        return flightList

    # Defines a method which finds a specific flight when given the flight number.
    def findFlightByNo(self,flightNo):
        # Boolean that indicates that the flight has not been found.
        found = False

        # Iterates through each key in the dictionary of flights.
        for airport in self._allFlights:
            # Iterates through each element of the list of flight objects associated with each key.
            for flight in self._allFlights[airport]:
                # If the flight number of the current flight object is equal to the given flight number, this branch
                # executes.
                if flightNo == flight.getFlightNumber():
                    # Flight is found
                    found = True
                    # returns the flight object.
                    return flight
        # If the flight object is not found in the list of all flights, returns -1.
        if not found:
            return -1

    # Method which finds all flights associated with a given country. If the flight lands in or takes off from the
    # given country, the flight gets added to a list of flights.
    def findAllCountryFlights(self, country):
        # Creates an empty list of flights associated with the given country,
        flightList = []
        # Creates an empty list of cities found in the given country.
        listOfCitiesInCountry = []

        # Iterates through each airport object in the list of airports
        for airport in self._allAirports:
            # If the country related to the current Airport object is equal to the given country, this branch executes.
            if airport.getCountry() == country:
                # Adds the city related to the current Airport object to the list of cities within the country.
                listOfCitiesInCountry.append(airport.getCity())

        # Iterates through each key in the dictionary of flights.
        for airport in self._allFlights:
            # Iterates through each element of the list of flight objects associated with each key.
            for flight in self._allFlights[airport]:
                # If the city of the origin airport is in the list of cities in the country or the city of the
                # destination airport is in the list of cities in the country, this branch executes.
                if flight.getOrigin().getCity() in listOfCitiesInCountry or flight.getDestination().getCity() in listOfCitiesInCountry:
                    # Adds the Flight object to the list of flights.
                    flightList.append(flight)
        # Returns the list of flights.
        return flightList

    # Defines a method that tries to find a direct flight from the given origin airport to the given destination
    # airport. If a direct flight cannot be found, a connecting flight with one intermediate airport is found. If a
    # connecting flight cannot be found, -1 is returned. Two airport objects are taken as parameters in this method.
    def findFlightBetween(self, origAirport, destAirport):

        # If both given arguments are Airport objects, this branch executes.
        if isinstance(origAirport, Airport) == True and isinstance(destAirport, Airport) == True:
            # Boolean that indicates that a direct flight has not yet been found
            foundDirect = False

            # Iterates through each key in the dictionary of flights.
            for airport in self._allFlights:
                # Iterates through each element of the list of flight objects associated with each key.
                for flight in self._allFlights[airport]:
                    # If the city of the given origin Airport object is equal to the city of the origin airport
                    # of the current flight, this branch executes.
                    if origAirport.getCity() == flight.getOrigin().getCity():
                        # If the city of the given destination Airport object is equal to the city of the destination
                        # airport of the current flight, this branch executes.
                        if destAirport.getCity() == flight.getDestination().getCity():
                            # A direct flight has been found, so foundDirect is set to true.
                            foundDirect = True
                            # Returns a string displaying the direct flight, including the flight number, as well as the
                            # code of the origin and destination airports.
                            return f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"

            # If a direct flight is not found in the list of all flights, this branch executes. Searches for a
            # connecting flight.
            if foundDirect == False:

                # Creates an empty set which will store possible connecting airports.
                possibleConnectingAirports = set()
                # Boolean that indicates that at least one connecting flight has not been found yet.
                foundAtLeastOneConnecting = False

                # Iterates through each key in the dictionary of flights.
                for airport1 in self._allFlights:
                    # Iterates through each element of the list of flight objects associated with each key.
                    for flight1 in self._allFlights[airport1]:
                        # If the city of the given origin Airport object is equal to the city of the origin airport of
                        # the current Flight object, this branch executes.
                        if origAirport.getCity() == flight1.getOrigin().getCity():
                            # The midpoint of the flight (connecting airport) is set equal to the destination airport
                            # of the current flight.
                            midPoint = flight1.getDestination()

                            # Iterates again through each key in the dictionary of flights.
                            for airport2 in self._allFlights:
                                # Iterates through each element of the list of flight objects associated with each key.
                                for flight2 in self._allFlights[airport2]:
                                    # If the current midpoint airport is equal to the origin airport of the current
                                    # flight, this branch executes.
                                    if midPoint == flight2.getOrigin():
                                        # If the city of the given destination Airport is equal to the city of the
                                        # destination Airport of the current flight, this branch executes.
                                        if destAirport.getCity() == flight2.getDestination().getCity():
                                            # A possible connecting flight has been found, so the airport code of the
                                            # origin airport of the current flight (the midpoint airport) is added to
                                            # the set of possible connecting airports.

                                            # possibleConnectingAirports.add(flight2.getOriginCode())
                                            possibleConnectingAirports.add(flight2.getOrigin().getCode())

                                            # FoundAtLeastOneConnecting is set to true, because a connecting flight has
                                            # been found.
                                            foundAtLeastOneConnecting = True
                # If at least one possible connecting flight has been found, this branch executes.
                if foundAtLeastOneConnecting:
                    # Returns the set of possible connecting airports.
                    return possibleConnectingAirports
                # Otherwise, if no possible flights are found, this branch executes and returns -1.
                else:
                    return -1
        # If not both of the given arguments are Airport objects, this branch executes.
        else:
            # A type error is raised telling the user that both the arguments must be Airport objects.
            raise TypeError("The origin and destination must be Airport objects")

    # Method which finds the return flight of a given flight.
    def findReturnFlight(self, firstFlight):
        # Swaps the origin and destination cities in order to find the correct returning flight.

        # Defines a variable which stores the city of the destination airport of the given flight object. This will
        # become the origin city of the return flight.
        origin = firstFlight.getDestination().getCity()
        # Defines a variable which stores the city of the origin airport of the given flight object. This will become
        # the destination city of the return flight.
        destination = firstFlight.getOrigin().getCity()

        # Boolean indicating the return flight has not yet been found.
        found = False

        # Iterates through each key in the dictionary of flights.
        for airport in self._allFlights:
            # Iterates through each element of the list of flight objects associated with each key.
            for flight in self._allFlights[airport]:
                # If the city of the origin Airport object of the current Flight object is equal to the origin city of
                # the desired return flight, and the city of the destination Airport object of the current Flight object
                # is equal to the destination city of the desired return flight, this branch executes.
                if origin == flight.getOrigin().getCity() and destination == flight.getDestination().getCity():
                    # Found is set to true because a return flight has been found.
                    found = True
                    # Returns the current flight.
                    return flight
        # If no possible return flight is found in the list of all flights, -1 is returned.
        if not found:
            return -1

    # Defines a method which finds flights which cross a given ocean. An ocean name is taken as an argument. If no
    # flights are found that cross the given ocean, -1 is returned.
    def findFlightsAcross(self, ocean):
        # Creates an empty list of countries found in the green zone
        countriesInGreenZone = []
        # Creates an empty list of countries found in the red zone
        countriesInRedZone = []
        # Creates an empty list of countries found in the blue zone
        countriesInBlueZone = []
        # Creates an empty set that will store flights which cross the given ocean.
        flightSet = set()
        # Boolean that indicates that at least one flight that crosses the given ocean has not been found.
        foundAtLeastOne = False

        # Loops through every key in the dictionary of countries.
        for country in self._allCountries:
            # If the continent associated with the current country is equal to North America or South America, this
            # branch executes.
            if self._allCountries[country].upper() == 'NORTH AMERICA' or self._allCountries[country].upper() == 'SOUTH AMERICA':
                # The current country is added to the list of countries in the green zone.
                countriesInGreenZone.append(country)
            # If the continent associated with the current country is equal to Asia or Australia, this
            # branch executes.
            elif self._allCountries[country].upper() == 'ASIA' or self._allCountries[country].upper() == 'AUSTRALIA':
                # The current country is added to the list of countries in the red zone.
                countriesInRedZone.append(country)
            # If the continent associated with the current country is equal to Europe or Africa, this
            # branch executes.
            elif self._allCountries[country].upper() == 'EUROPE' or self._allCountries[country].upper() == 'AFRICA':
                # The current country is added to the list of countries in the blue zone.
                countriesInBlueZone.append(country)

        # Iterates through each key in the dictionary of flights.
        for airport in self._allFlights:
            # Iterates through each element of the list of flight objects associated with each key.
            for flight in self._allFlights[airport]:

                # Sets two variables equal to the city of the origin and destination airports, respectively.
                originCountry = flight.getOrigin().getCountry()
                destinationCountry = flight.getDestination().getCountry()

                # If the given ocean equals 'pacific', this branch executes.
                if ocean.lower() == 'pacific':
                    # Executes if the origin country is in the red zone.
                    if originCountry in countriesInRedZone:
                        # Executes if the destination country is in the green zone.
                        if destinationCountry in countriesInGreenZone:
                            # Adds the flight number of the current flight to the set of flights which cross the given
                            # ocean.
                            flightSet.add(flight.getFlightNumber())
                            # At least one flight that crosses the given ocean has been found.
                            foundAtLeastOne = True
                    # Executes if the origin country is in the green zone.
                    elif originCountry in countriesInGreenZone:
                        # Executes if the destination country is in the red zone.
                        if destinationCountry in countriesInRedZone:
                            # Adds the flight number of the current flight to the set of flights which cross the given
                            # ocean.
                            flightSet.add(flight.getFlightNumber())
                            # At least one flight that crosses the given ocean has been found.
                            foundAtLeastOne = True
                # Otherwise, this executes if the given ocean is 'atlantic'
                elif ocean.lower() == 'atlantic':
                    # Executes if the origin country is in the blue zone.
                    if originCountry in countriesInBlueZone:
                        # Executes if the destination country is in the green zone.
                        if destinationCountry in countriesInGreenZone:
                            # Adds the flight number of the current flight to the set of flights which cross the given
                            # ocean.
                            flightSet.add(flight.getFlightNumber())
                            # At least one flight that crosses the given ocean has been found.
                            foundAtLeastOne = True
                    # Executes if the origin country is in the green zone.
                    elif originCountry in countriesInGreenZone:
                        # Executes if the destination country is in the blue zone.
                        if destinationCountry in countriesInBlueZone:
                            # Adds the flight number of the current flight to the set of flights which cross the given
                            # ocean.
                            flightSet.add(flight.getFlightNumber())
                            # At least one flight that crosses the given ocean has been found.
                            foundAtLeastOne = True
        # If at least one flight has been found that crosses the given ocean, this branch executes, which returns the
        # set of flights that cross the given ocean.
        if foundAtLeastOne:
            return flightSet
        # Otherwise, if not flights are found, this branch executes, which returns -1.
        else:
            return -1