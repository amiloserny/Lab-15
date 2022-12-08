#Amanda Miloserny and Cathy Doherty
class Fabric:
    def __init__(self, countryOfOrigin, color):
        self.countryOfOrigin = countryOfOrigin
        self.color = color

    def __str__(self):
        return self.countryOfOrigin + "("+ str(self.color) + ")"

p1 = Fabric("Ireland", "green")
print(p1)
