You have been hired by a car rental company to build a distributed data storage 
system using a remote object paradigm that will allow one to store and access 
information relating to rental cars, manufacturers of cars and users who rent cars.
Each manufacturer has the following two associated pieces of information which 
should be stored in the system:
1. Manufacturer name. This is a string data type.
2. Manufacturer country which refers to the country in which the manufacturer is 
based (e.g. BMW is based in Germany). This is a string data type.
Each rental car has the following two associated pieces of information which should 
be stored in the system:
1. Car manufacturer name. This is a string data type.
2. Car model. This is a string data type.
Note, multiple cars with the same manufacturer and model can exist in the system. 
Each user has the following two associated pieces of information which should be 
stored in the system: 
1. User name. This is a string data type.
2. User contact phone number. This is a string data type.
Design and implement the above distributed data storage system using a remote 
object paradigm which allows employees of the car rental company to perform the 
following twelve tasks:
Task 1
Add a user to the system. Implement this using a method with the following header: 
def add_user(self, user_name, user_number) 
An example of calling this method is: 
rental_object.add_user(“Conor Reilly”, “123456”) 
You can assume that each user added to the system has a unique user name.
Task 2
Return all associated pieces of information relating to the collection of users currently 
stored in the system (i.e. a collection of user names and contact numbers). 
Implement this using a method with the following header: 
def return_users(self) 
An example of calling this method is: 
rental_object.return_users() 
The information returned by this method should have the property that it can be 
easily interpreted when displayed using the Python print function. That is, the output 
from the following print function should be easily interpreted and understood by a 
human reader: 
print(rental_object.return_users())
Task 3
Add a car manufacturer to the system. Implement this using a method with the 
following header: 
def add_manufacturer(self, manufacturer_name, manufacturer_country)
An example of calling this method is: 
rental_object.add_manufacturer(“BMW”, “Germany”)
You can assume that each manufacturer added to the system has a unique 
manufacturer name.
Task 4
Return all associated pieces of information relating to the collection of manufacturers 
currently stored in the system (i.e. a collection of manufacturer names and 
countries). Implement this using a method with the following header:
def return_manufacturers(self)
An example of calling this method is: 
rental_object.return_manufacturers()
The information returned by this method should have the property that it can be 
easily interpreted when displayed using the Python print function.
Task 5
Add a rental car to the system. Implement this using a method with the following 
header:
def add_rental_car(self, manufacturer_name, car_model)
An example of calling this method is: 
rental_object.add_rental_car(“BMW”, “3 Series”)
You can assume that the manufacturer in question has previously been added using 
the add_manufacturer method.
When a car is first added to the system it is initially not rented to any user. Multiple 
cars with the same manufacturer and model may be added to the system.
Task 6
Return all associated pieces of information relating to the collection of rental cars 
currently not rented (i.e. a collection of car manufacturers and models). Implement 
this using a method with the following header:
def return_cars_not_rented(self)
An example of calling this method is: 
rental_object.return_cars_not_rented()
The information returned by this method should have the property that it can be 
easily interpreted when displayed using the Python print function.
Task 7
Rent a car of a specified model to a specified user on a specified date. Implement 
this using a method with the following header:
def rent_car(self, user_name, car_model, year, month, day)
An example of calling this method is: 
rental_object.rent_car(“Conor Reilly”, “3 Series”, 2019, 1, 3)
You can assume that the user in question has previously been added using the 
add_user method. You can also assume that no two manufacturers will have a car 
with the same model name. Therefore, there will never exist any ambiguity regarding 
which car is being referred to.
Each rental car can only be rented to a single user at a time. For example, consider 
the case where there are two rental cars in the system with model equal to “3 Series” 
and both are currently rented. In this case another car with model equal to “3 Series” 
cannot be rented until one of the two above cars is returned or an additional car with 
model equal to “3 Series” is added to the system.
The year, month, day parameters are integer values greater than zero, integers in 
the interval (0, 12] and integers in the interval (0, 31] respectively.
The method rent_car should return a value of 1 if the car in question was
successfully rented. Otherwise, the method should return a value of 0.
Task 8
Return all associated pieces of information relating to the collection of cars currently 
rented (i.e. a collection of car manufacturers and models). Implement this using a 
method with the following header: 
def return_cars_rented(self)
An example of calling this method is: 
rental_object.return_cars_rented()
The information returned by this method should have the property that it can be 
easily interpreted when displayed using the Python print function.
Task 9
Return to the rental company, a rented car of a specified model by a specified user 
on a specified date; that is, set the status of the rental car in question from rented to 
not rented. Implement this using a method with the following header:
def end_rental(self, user_name, car_model, year, month, day)
An example of calling this method is: 
rental_object.end_rental(“Conor Reilly”, “3 Series”, 2019, 2, 4)
You can assume that the user has previously rented the car in question and this 
method call corresponds to them returning that car. You can also assume that a user
will only rent a single car of each model at any given time. Therefore, there will never 
exist any ambiguity regarding which car is being returned.
The year, month, day parameters are integer values greater than zero, integers in 
the interval (0, 12] and integers in the interval (0, 31] respectively.
Task 10
Delete from the system all rental cars of a specified model which are currently not 
rented. Rental cars that are currently rented should not be deleted. Implement this 
using a method with the following header:
def delete_car(self, car_model)
An example of calling this method is:
rental_object.delete_car(“3 Series”)
Task 11
Delete from the system a specified user. A user should only be deleted if they have 
never rented a car. Implement this using a method with the following header:
def delete_user(self, user_name)
An example of calling this method is: 
rental_object.delete_user(“Conor Reilly”)
You can assume that the user in question has previously been added using the 
add_user method and has not previously been deleted.
The method delete_user should return a value of 1 if the user in question was 
deleted. Otherwise, the method should return a value of 0.
Task 12
Return all rental cars (i.e. a collection of car manufacturers and models) a user 
previously has rented where the corresponding rental and return dates both lie 
between a specified start and end date inclusive.
Implement this using a method with the following header:
def user_rental_date(self, user_name, start_year, start_month, start_day, end_year, 
end_month, end_day)
An example of calling this method is:
rental_object.user_rental_date(“Conor Reilly”, 2010, 1, 1, 2029, 2, 1)
Note, the rental cars returned may contain duplicates if the user rented the car in 
question more than once.
You can assume that the user in question has previously been added using the 
add_user method.
The information returned by this method should have the property that it can be 
easily interpreted when displayed using the Python print function.
