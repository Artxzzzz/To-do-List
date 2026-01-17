class item: # Objeto item
    def __init__(self, name: str, hour: str, date: tuple, complete=False): # Init do item
        self.name = name # Nome
        self.hour = hour # Horário que foi feito
        self.date = date # Data
        self.complete = False

    def completeModule(self):
        self.complete = True

    def todict(self):
        return {
            "Name": self.name,
            "Hour": self.hour,
            "Date": self.date,
            "Complete": self.complete
        }
    
    @classmethod
    def fromdict(cls, data: dict):
        return cls(
            data["Name"],
            data["Hour"],
            data["Date"],
            data["Complete"]
        )