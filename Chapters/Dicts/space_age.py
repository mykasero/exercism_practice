class SpaceAge:
    def __init__(self, seconds):
        self.orbit_time = {"Mercury": 0.2408467, "Venus": 0.61519726,
                           "Earth": 1.0, "Mars": 1.8808158,
                           "Jupiter": 11.862615, "Saturn": 29.447498,
                           "Uranus": 84.016846, "Neptune": 164.79132}
        self.time_sec = seconds
        self.earth_time = float(self.time_sec) / (60 * 60 * 24 * 365.25)
        print(self.earth_time)

    def on_earth(self):
        years_earth = round(self.earth_time, 2)
        print(years_earth)
        return years_earth

    def on_mercury(self):
        years = self.earth_time / self.orbit_time["Mercury"]
        years = round(years, 2)
        return years

    def on_venus(self):
        years = self.earth_time / self.orbit_time["Venus"]
        years = round(years, 2)
        return years

    def on_mars(self):
        years = self.earth_time / self.orbit_time["Mars"]
        years = round(years, 2)
        return years

    def on_jupiter(self):
        years = self.earth_time / self.orbit_time["Jupiter"]
        years = round(years, 2)
        return years

    def on_saturn(self):
        years = self.earth_time / self.orbit_time["Saturn"]
        years = round(years, 2)
        return years

    def on_uranus(self):
        years = self.earth_time / self.orbit_time["Uranus"]
        years = round(years, 2)
        return years

    def on_neptune(self):
        years = self.earth_time / self.orbit_time["Neptune"]
        years = round(years, 2)
        return years