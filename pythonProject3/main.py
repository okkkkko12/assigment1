from datetime import datetime, timedelta

#create an airport class
class Airport:
    def __init__(self, name, city, country):
        self._name = name
        self._city = city
        self._country = country

    # Getters and setters for name
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    # Getters and setters for city
    def getCity(self):
        return self._city

    def setCity(self, city):
        self._city = city

    # Getters and setters for country
    def getCountry(self):
        return self._country

    def setCountry(self, country):
        self._country = country

    def find_flights(self):
        pass  # this pass function retrieve flight information about flights departing from or arriving at this airport.

#create a flight class
class Flight:
    def __init__(self, number, airline, departure_date, departure_time, arrival_time, ):
        self._number = number
        self._airline = airline
        self._departure_date = departure_date
        self._departure_time = departure_time
        self._arrival_time = arrival_time

    # Getters and setters for flight number
    def get_number(self):
        return self._number

    def set_number(self, number):
        self._number = number

    # Getters and setters for airline
    def get_airline(self):
        return self._airline

    def set_airline(self, airline):
        self._airline = airline

    # Getters and setters for departure_date
    def get_departure_date(self):
        return self._departure_date

    def set_departure_date(self, departure_date):
        self._departure_date = departure_date

    # Getters and setters for departure_time
    def get_departure_time(self):
        return self._departure_time

    def set_departure_time(self, departure_time):
        self._departure_time = departure_time

    # Getters and setters for arrival_time
    def get_arrival_time(self):
        return self._arrival_time

    def set_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time

    def is_flight_full(self):
        pass  # this function checks if the flight capacity,whether it's fully booked or not.

#create a boardin gpass class
class BoardingPass:
    def __init__(self, airline, flight_number, date, departure_time, boarding_time, seat, departure_airport,
                 arrival_airport, passenger_name, gate, terminal, electronic_ticket, arrival_time):
        self._airline = airline
        self._flight_number = flight_number
        self._date = date
        self._departure_time = departure_time
        self._boarding_time = boarding_time
        self._seat = seat
        self._departure_airport = departure_airport
        self._arrival_airport = arrival_airport
        self._passenger_name = passenger_name
        self._gate = gate
        self._terminal = terminal
        self._electronic_ticket = electronic_ticket
        self._arrival_time = arrival_time

    # Getters and setters for airline
    def getairline(self):
        return self._airline

    def setairline(self, airline):
        self._airline = airline

    # Getters and setters for flight_number
    def get_flight_number(self):
        return self._flight_number

    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    # Getters and setters for date
    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    # Getters and setters for departure_time
    def get_departure_time(self):
        return self._departure_time

    def set_departure_time(self, departure_time):
        self._departure_time = departure_time

    # Getters and setters for seat
    def get_seat(self):
        return self._seat

    def set_seat(self, seat):
        self._seat = seat

    # Getters and setters for boarding_time
    def get_boarding_time(self):
        return self._boarding_time

    def set_boarding_time(self, boarding_time):
        self._boarding_time = boarding_time

    # Getters and setters for departure_airport
    def get_departure_airport(self):
        return self._departure_airport

    def set_departure_airport(self, departure_airport):
        self._departure_airport = departure_airport

    # Getters and setters for arrival_airport
    def get_arrival_airport(self):
        return self._arrival_airport

    def set_arrival_airport(self, arrival_airport):
        self._arrival_airport = arrival_airport

    # Getters and setters for passenger_name
    def get_passenger_name(self):
        return self._passenger_name

    def set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    # Getters and setters for gate
    def get_gate(self):
        return self._gate

    def set_gate(self, gate):
        self._gate = gate

    # Getters and setters for terminal
    def get_terminal(self):
        return self._terminal

    def set_terminal(self, terminal):
        self._terminal = terminal

    # Getters and setters for electronic ticket number
    def get_electronic_ticket(self):
        return self._electronic_ticket

    def set_electronic_ticket(self, electronic_ticket):
        return self._electronic_ticket

    # Getters and setters for the arrival time
    def get_arrival_time(self):
        return self._arrival_time

    def set_arrival_time(self, arrival_time):
        return self._arrival_time

    def is_valid(self):
        pass  # this pass function Checks if the boarding pass is valid for the flight or not.

#create a passenger class
class Passenger:
    def __init__(self, first_name, last_name, ticket_number, phone_number, email, passport_number):
        self._first_name = first_name
        self._last_name = last_name
        self._ticket_number = ticket_number
        self._phone_number = phone_number
        self._email = email
        self._passport_number = passport_number

    # Getters and setters for first_name
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    # Getters and setters for last_name
    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    # Getters and setters for ticket_number
    def get_ticket_number(self):
        return self._ticket_number

    def set_ticket_number(self, ticket_number):
        self._ticket_number = ticket_number

    # Getters and setters for phone_number
    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    # Getters and setters for email
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    # Getters and setters for passport_number
    def get_passport_number(self):
        return self._passport_number

    def set_passport_number(self, passport_number):
        self._passport_number = passport_number

    def check_in(self):
        pass  # this pass function check the passenger into their flight.

    def print_boarding_passes(self):
        pass  # this pass function Prints all boarding passes for the passenger's upcoming flights.


# Create objects of all the identified classes
departure_airport = Airport("Chicago O'Hare International Airport", "Chicago", "USA")
arrival_airport = Airport("John F. Kennedy International Airport", "New York City", "USA")
flight = Flight("NA4321", "NATIONAL AIRLINE", datetime(2020, 12, 6), "11:40", "13:30")
passenger = Passenger("JAMES", "SMITH", "629", "8383672383", "JAMES@gmail.com", "ABCDEF123456")
boarding_pass = BoardingPass(
    airline=flight.get_airline(),
    flight_number=flight.get_number(),
    date=flight.get_departure_date().strftime("%d %b %y"),
    departure_time=flight.get_departure_time(),
    arrival_time="13:30",
    boarding_time="11:20",
    seat="09A",
    departure_airport=departure_airport.getName(),
    arrival_airport=arrival_airport.getName(),
    passenger_name=f"{passenger.get_first_name()} {passenger.get_last_name()}",
    gate="03",
    terminal="2 ",
    electronic_ticket=passenger.get_ticket_number()
)

# Displaying the boarding pass details
print("Boarding Pass")
print("----------------")
print("Passenger:", boarding_pass.get_passenger_name())
print("From:", departure_airport.getCity())
print("To:", arrival_airport.getCity())
print("Flight:", boarding_pass.get_flight_number())
print("Date:", boarding_pass.get_date())
print("Time:", boarding_pass.get_departure_time())
print("Arrival Time:", boarding_pass.get_arrival_time())
print("Gate:", boarding_pass.get_gate())
print("Seat:", boarding_pass.get_seat())
print("Boarding Till:", boarding_pass.get_boarding_time())
print("Terminal:", boarding_pass.get_terminal())
print("Electronic Ticket:", boarding_pass.get_electronic_ticket())