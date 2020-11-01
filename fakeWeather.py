import random
def fakeWeather():
    dayLike = random.choice(["sunny", "cloudy", "rainy", "foggy", "chilly", "hot"])
    temperature = random.randint(32,90)
    print("It is a", dayLike, "day, and the temperature is",str(temperature) + "F")


# Driver code
fakeWeather()
fakeWeather()
fakeWeather()
