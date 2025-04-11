class Superhero:
    def __init__(self, name, real_name, power, city):
        self.name = name
        self.real_name = real_name
        self.power = power
        self.city = city

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def __str__(self):
        return f"Name: {self.name}, Real Name: {self.real_name}, Power: {self.power}, City: {self.city}"


class FlyingSuperhero(Superhero):
    def __init__(self, name, real_name, power, city, flight_speed):
        super().__init__(name, real_name, power, city)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} mph!"

    def use_power(self):
        return f"{self.name} soars through the sky using {self.power}!"

    def __str__(self):
        return f"{super().__str__()}, Flight Speed: {self.flight_speed} mph"
    
   
batman = Superhero("Batman", "Bruce Wayne", "Gadgets and Intelligence", "Gotham")
print(batman.introduce())
print(batman.use_power())
print(batman)


superman = FlyingSuperhero("Superman", "Clark Kent", "Super Strength", "Metropolis", 500)
print(superman.introduce())
print(superman.use_power())
print(superman.fly())
print(superman)



