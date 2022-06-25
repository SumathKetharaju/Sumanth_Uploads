class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
        # self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    #     # return (self.get_temperature() * 1.8) + 32
    #
    # # Making Getters and Setter methods
    #
    # # getter method
    # def get_temperature(self):
    #     print("Getting value...")
    #     return self._temperature
    #
    # # setter method
    # def set_temperature(self, value):
    #     print("Setting value...")
    #     if value < -273.15:
    #         raise ValueError("Temperature below -273.15 is not possible.")
    #     self._temperature = value

    # temperature = property(get_temperature, set_temperature)

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# human = Celsius()
human = Celsius(37)
print(f"The Human Temperature before change is --> {human.temperature}")
# print(f"The Human Temperature before change is --> {human.get_temperature()}")
print(f"The Human Temperature in fahrenheit before changing the temperature is --> {human.to_fahrenheit()}")

# human.temperature = 37
human.temperature = -300

print(f"The Human Temperature after change is --> {human.temperature}")
# print(f"The Human Temperature after change is --> {human.set_temperature(-300)}")
print(f"The Human Temperature in fahrenheit after changing the temperature --> {human.to_fahrenheit()}")



