from dataclasses import dataclass


@dataclass
class Temperature:
    __fahrenheit:float = 32.0
    __celsius:float = 0.0


    def getFahrenheit(self):
        return round(self.__fahrenheit, 2)
    
    def getCelsius(self):
        
        return round(self.__celsius, 2)

    def setFahrenheit(self,fahrenheit):
        self.__celsius = (5/9 * (fahrenheit-32))
        self.__fahrenheit = fahrenheit

    def setCelsius(self, celsius):
        self.__celsius = celsius
        self.__fahrenheit = ((celsius * 9/5) + 32)
        



# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    temp = Temperature()
    for f in range(0, 212, 40):
        temp.setFahrenheit(f)
        print(f"{temp.getFahrenheit()} Fahrenheit equals {temp.getCelsius()} Celsius")
    
    for c in range(0, 100, 20):
        temp.setCelsius(c)
        print(f"{temp.getCelsius()} Celsius equals {temp.getFahrenheit()} Fahrenheit")

# if this module is the main module, call the main function
# to test the other functions
if __name__ == "__main__":
    main()

