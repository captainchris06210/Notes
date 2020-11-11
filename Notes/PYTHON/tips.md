                                        <ur PYTHON HOWTO>
                      
                 [< GO BACK](index.md)
                 
                 
# [CONDTIONS] #
                ##  IF CONDITIONNAL LOOP ##
                ```python
                        cars =('Audi','BMW','Subaru','Toyota']

                        for cars in cars:
                                if cars =='BMW':
                                        print(car.upper())
                ```
                ## CHEK INEQUALITY ## 
                ```python

                ```
                
                ```python
                ```
# [CLASSES] #

                 * Python 2.7 - classDog(object)
                ```python
                class Dog():
                    def __init__(self,name,age):
                        self.name = name
                        self.age = age
                    def sit(self):
                        print(self.name + " is sitting")

                    def roll_over(self):
                        print(self.name + " roll over!")



                my_dog = Dog('Willie',47)
                my_dog.sit()
                        ``` 
        
        ## MODIFYING ATTRIBUTE VALUE ##

                ```python
                class Car():
                    def __init__(self,make,model,year):
                        self.make = make
                        self.model = model
                        self.year = year
                        self.odometer_reading = 0

                    def read_odometer(self):
                        print("This car has " + str(self.odometer_reading) + " miles on it")
                    def update_odometer(self,mileage):
                        self.odometer_reading = mileage

                my_car = Car('Renault','Captur',2016)
                my_car.odometer_reading = 1000
                # OR my_car.update_odometer(1000)
                my_car.read_odometer()
                ```
        
        ## INHERITANCE ##
                ```python
                class ElectricCar(Car):
                    def __init__(self,make,model,year):
                        super().__init__(make,model,year)

                my_tesla = ElectricCar('tesla','model S',2016)
                my_tesla.update_odometer(100)
                print(my_tesla.read_odometer())
                ```
                
        ## IMPORT CLASS FROM OTHER FILE CARCLASS.PY ##
                ```python
                class Car
                from carClass import Car,ElectricCar 

                my_new_car = Car('Audi', 'A4',2016)
                print(my_new_car.get_descriptive_name())
                my_new_car.odometer_reading = 23
                my_new_car.read_odometer()

                my_Tesla = ElectricCar('tesla', 'model S',2016)
                print(my_Tesla.get_descriptive_name())
                my_Tesla.battery.describe_battery()
                my_Tesla.battery.get_range()
                ```
                
# [READ FILE AND SEARCH] #
                
                ```python
                def read_line_by_line(filename):
                    with open(filename) as file_object:
                        lines = file_object.readlines()

                        contents = ' '
                        for line in lines:
                            contents += line.rstrip()

                        print (contents)                                        """ Show entire file """
                        print (contents[0])  | (line[0])                        """ Show character by character """
                        print (lines[0])                                        """ Show entire line 0 """ 

                        if "<map_info>" in contents:                            """ Search occurence in contents """
                                print ("FOUND")
                        else: 
                            print("NOT FOUND")
              ```
              
# [CODE] #
   ```python
   ```
               
