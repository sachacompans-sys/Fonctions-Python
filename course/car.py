class Car:
    def __init__(self, model:str, brand:str, power:int, fuel_tank:float):
        self.fuel_tank = fuel_tank
        self.model = model
        self.brand = brand
        self.power = power
        self.is_strarted = False
    
    def start(self):
        if not self.is_strarted :
            self.is_strarted = True
            print(f'La {self.brand} a démarré')
        else:
            print(f'La {self.brand}')

    def stop(self):
        if self.is_strarted :
            self.is_strarted = False
            print (f'La {self.brand} est arrété')
        else :
            print(f'La {self.brand} a deja démarré')

    def forward(self, distance:float):
        if self.is_strarted :
            print(f'la {self.brand} avance de {distance}km')
            self.fuel_tank -= 0.15*distance
        else:
            print(f'La {self.brand} n\'avance pas')

    
        


ferrari = Car('488', 'Ferrari', 800, 60)
ferrari.start()
print(ferrari.fuel_tank)
ferrari.forward(50)
print(ferrari.fuel_tank)
ferrari.stop()