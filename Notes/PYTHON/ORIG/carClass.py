
class Car():
    """ A simple attempt to represent a car """
    
    def __init__(self,make,model,year):
        """ Initialize all attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neatly formated descriptive name """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ Print a statement showing car mileage """
        print("This car has " + str(self.odometer_reading) + " Miles on it")

    def update_odometer(self,mileage):
        """ Set the odometer reading to the given value """
        """ Reject the change if it attempt to roll the odometer back """
        if(mileage >= self.odometer_reading):
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer")

    def increment_odometer(self,miles):
        """ Add the given amount to the odometer reading """
        self.odometer_reading += miles

class Battery():
    """ A simpliest attempt to model a batery for electric model car """

    def __init__(self,battery_size=60):
        """Initialize the batery attributes """
        self.battery_size = battery_size
        
    def describe_battery(self):
        """ print a statement describring the batery size...""" 
        print("This car has a " + str(self.battery_size) + "-kWH batery.")

    def get_range(self):
        """ Print a statement about the range this batery provide """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on full charge"
        print(message)

class ElectricCar(Car):
    """ Model aspect of a car ,specifix to electric vehicle """
    def __init__(self,make,model,year):
        """ Initial attributes of parent class. """
        """ Then initialize attributes specific to electric Cars """
        super().__init__(make,model,year)
        self.battery = Battery()


