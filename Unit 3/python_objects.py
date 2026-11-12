# Python objects are digital representations of things
# that can interact with one another

# Objects are collectons of data that we use tp
# characterize things.

# example - A car is a object/ "thing"
# characteristitics of a car: engine,tires,battery,seats.

# when we want to make an object, we need to use a class
# class keyword = object maker

# the class name ALWAYS is capitalized / Pascal case
class Car:
    # This function describes the characteristics of the car.
    def __init__(self, color, year, model, engine, pushTostart):
        self.color = color
        self.year = year
        self.model = model
        self.engine = engine
        self.pushTostart = pushTostart

    # Methods are functions that exist inside the object.
    def start(self):
        # Start the vehicle when push-to-start is enabled.
        if self.pushTostart:
            pass

    def accelerate(self):
        # When the gas pedal is pressed, move the vehicle.
        pass

    def brake(self):
        # When the brake pedal is pressed, engage the brakes.
        pass


