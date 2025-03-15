class MeteorDataEntry:
    """Class representing a meteorite landing entry."""

    def __init__(self, name, id, nametype, recclass, mass, fall, year, reclat, reclong, geolocation, states, counties):
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong
        self.geolocation = geolocation
        self.states = states
        self.counties = counties

    def __str__(self):
        """Return a string representation of the meteorite entry."""
        return f"{self.name} ({self.year}, {self.mass}g)"
