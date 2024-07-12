# Define the transport fleet management system

class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, registration_number, make, model, seats):
        super().__init__(registration_number, make, model)
        self.seats = seats

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles in the fleet.")
        else:
            print("List of vehicles:")
            for vehicle in self.vehicles:
                if isinstance(vehicle, Car):
                    print(f"Car - Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Seats: {vehicle.seats}")
                elif isinstance(vehicle, Truck):
                    print(f"Truck - Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Cargo Capacity: {vehicle.cargo_capacity}")
                elif isinstance(vehicle, Motorcycle):
                    print(f"Motorcycle - Registration: {vehicle.registration_number}, Make: {vehicle.make}, Model: {vehicle.model}, Engine Capacity: {vehicle.engine_capacity}")

    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                if isinstance(vehicle, Car):
                    print(f"Car found - Make: {vehicle.make}, Model: {vehicle.model}, Seats: {vehicle.seats}")
                elif isinstance(vehicle, Truck):
                    print(f"Truck found - Make: {vehicle.make}, Model: {vehicle.model}, Cargo Capacity: {vehicle.cargo_capacity}")
                elif isinstance(vehicle, Motorcycle):
                    print(f"Motorcycle found - Make: {vehicle.make}, Model: {vehicle.model}, Engine Capacity: {vehicle.engine_capacity}")
                return
        print(f"Vehicle with registration number {registration_number} not found.")

# Main program
fleet = Fleet()

# Adding vehicles
car1 = Car("ABC123", "Toyota", "Camry", 5)
truck1 = Truck("DEF456", "Ford", "F150", "1000 kg")
motorcycle1 = Motorcycle("GHI789", "Honda", "CBR600", "600 cc")
fleet.add_vehicle(car1)
fleet.add_vehicle(truck1)
fleet.add_vehicle(motorcycle1)

# Demonstrating functionalities
fleet.display_vehicles()
fleet.search_vehicle("DEF456")
