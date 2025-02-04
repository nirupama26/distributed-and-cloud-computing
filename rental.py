from Pyro5.api import Daemon, serve

class rental(object):
    def __init__(self):
        self.users = {}   # Dictionary to store users {username: phonenumber}
        self.manufacturers = {} # Dictionary to store manufacturers {manufacturer_name: manufacturer_country}
        self.cars_not_rented = []   # List to store rental cars not rented yet
        self.cars_rented = {}  # Dictionary to store rented cars {car_model: user_name}

    def add_user(self, user_name, user_number):
        if user_name not in self.users:
            self.users[user_name] = user_number
            return True
        else:
            return False


#    def return_users(self):
#        return self.users

    def return_users(self):
        user_info_str = "User Information:\n"
        for user_name, user_number in self.users.items():
            user_info_str += f"Name: {user_name}, Contact Number: {user_number}\n"
        return user_info_str


    def add_manufacturer(self, manufacturer_name, manufacturer_country):
        if manufacturer_name not in self.manufacturers:
            self.manufacturers[manufacturer_name] = manufacturer_country
            return True
        else:
            return False
    
    def return_manufacturers(self):
        manufacturer_info_str = "Manufacturer Information:\n"
        for manufacturer_name, manufacturer_country in self.manufacturers.items():
            manufacturer_info_str += f"Name: {manufacturer_name}, Country: {manufacturer_country}\n"
        return manufacturer_info_str

    def add_rental_car(self, manufacturer_name, car_model):
        self.cars_not_rented.append((manufacturer_name, car_model))
 
    def return_cars_not_rented(self):
        not_rented_info = "Rental Cars Currently Not Rented:\n"
        for car in self.cars_not_rented:
            manufacturer_name, car_model = car
            not_rented_info += f"Manufacturer: {manufacturer_name}, Model: {car_model}\n"
        return not_rented_info


    def rent_car(self, user_name, car_model, year, month, day):

        # Check if the user exists
        if user_name not in self.users:
            return 0  # User does not exist
      
        # Check if the car model exists
        car_available = False
        for car in self.cars_not_rented:
            if car[1] == car_model:
                car_available = True
                break

        if not car_available:
            return 0  # Car model not available for rent

        # Check if the car is already rented
        rented_cars = self.return_cars_rented()
        for rented_car in rented_cars:
            if rented_car[1] == car_model:
                return 0  # Car already rented

        # Check if the date is valid
        try:
            rental_date = datetime.date(year, month, day)
        except ValueError:
            return 0  # Invalid date

        # If all checks passed, rent the car to the user
        self.cars_not_rented.remove((car[0], car[1]))  # Remove the rented car from cars_not_rented list
        return 1  # Car rented successfully

    def return_cars_rented(self):
        rented_info = "Rented Cars:\n"
        for car_model, user_name in self.cars_rented.items():
            rented_info += f"Manufacturer: {self.get_manufacturer(car_model)}, Model: {car_model}, Rented by: {user_name}\n"
        return rented_info

    def end_rental(self, user_name, car_model, year, month, day):
        # Check if the car model exists in rented cars
        if car_model not in self.cars_rented:
            return 0  # Car not found

        # Check if the user rented this car
        if self.cars_rented[car_model][0] != user_name:
            return 0  # User did not rent this car

        # Check if the rental date matches the specified date
        rental_date = self.cars_rented[car_model][1]
        specified_date = datetime.date(year, month, day)
        if rental_date != specified_date:
            return 0  # Rental date does not match specified date

        # Remove the car from the rented cars dictionary
        del self.cars_rented[car_model]
        return 1  # Car returned successfully   

    def delete_car(self, car_model):
        self.cars_not_rented = [car for car in self.cars_not_rented if car[1] != car_model]

    def delete_user(self, user_name):
        # Check if the user has rented any cars
        if any(user_name == user[0] for user in self.rented_cars):
            return 0  # User has rented a car, cannot be deleted

        # Remove the user from the users dictionary
        if user_name in self.users:
            del self.users[user_name]
            return 1  # User deleted successfully
        else:
            return 0  # User not found

    def user_rental_date(self, user_name, start_year, start_month, start_day, end_year, end_month, end_day):
        rental_cars = []
        start_date = datetime.date(start_year, start_month, start_day)
        end_date = datetime.date(end_year, end_month, end_day)
        
        # Iterate through rented cars to find the ones rented by the specified user within the specified date range
        for car_model, (rented_user, rental_date, return_date) in self.cars_rented.items():
            if rented_user == user_name and start_date <= rental_date <= end_date and start_date <= return_date <= end_date:
                rental_cars.append((car_model, rental_date, return_date))
        
        return rental_cars
    



# Create an instance of the rental class
#rental_object = rental()

# Create a Pyro5 daemon
#daemon = Daemon()

# Register the rental_object with the name server
#serve({rental_object: "example.rental"}, daemon=daemon, use_ns=True)

# Start the daemon to handle incoming requests
#daemon.requestLoop()

if __name__ == "__main__":
    daemon = Daemon()
    serve({rental: "example.rental"}, daemon=daemon, use_ns=True)
