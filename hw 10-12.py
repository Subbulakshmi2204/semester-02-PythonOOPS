
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def displayVehicleInfo(self):
        print(f"Make:{self.make}\nModel:{self.model}\nYear:{self.year}")
class Car(Vehicle):
    def __init__(self,make,model,year,no_of_doors,trunk_capacity):
        Vehicle.__init__(self,make,model,year)
        self.no_of_doors=no_of_doors
        self.trunk_capacity=trunk_capacity
    def displayCarInfo(self):
        print(f"Number of doors:{self.no_of_doors}\nTrunk Capacity:{self.trunk_capacity}")
class Truck(Vehicle):
    def __init__(self,make,model,year,cargo_capacity,no_of_axles):
        Vehicle.__init__(self,make,model,year)
        self.cargo_capacity=cargo_capacity
        self.no_of_axles=no_of_axles
    def displayTruckInfo(self):
        print(f"Cargo Capacity:{self.cargo_capacity}\nNumber of axles:{self.no_of_axles}")
class PickupTruck(Car,Truck):
    def __init__(self,make,model,year,no_of_doors,trunk_capacity,cargo_capacity,no_of_axles):
        Car.__init__(self,make,model,year,no_of_doors,trunk_capacity)
        Truck.__init__(self,make,model,year,cargo_capacity,no_of_axles)
    def display(self):
        self.displayVehicleInfo()
        self.displayCarInfo()
        self.displayTruckInfo()
s=PickupTruck("SunDrive","Eclipse X5",2024,4,"450 litres","1200 litres",2)
s.display()

class Product:
    def __init__(self,p_Id,p_name,p_price):
        self.p_Id=p_Id
        self.p_name=p_name
        self.p_price=p_price
    def displayProductInfo(self):
        print(f"Product Id:{self.p_Id}\nProduct Name:{self.p_name}\nProduct Price:{self.p_price}")
class Electronics(Product):
    def __init__(self,p_Id,p_name,p_price,warranty,brand):
        Product.__init__(self,p_Id,p_name,p_price)
        self.warranty=warranty
        self.brand=brand
    def displayElectronicsInfo(self):
        self.displayProductInfo()
        print(f"Warranty Period:{self.warranty}\nBrand Name:{self.brand}")
class Clothing(Product):
    def __init__(self,p_Id,p_name,p_price,size,material):
        Product.__init__(self,p_Id,p_name,p_price)
        self.size=size
        self.material=material
    def displayClothingInfo(self):
        self.displayProductInfo()
        print(f"Size:{self.size}\nMaterial:{self.material}")
e=Electronics("E55","UltraSound Pro Headphones","$249","2 years","SonicWave")
e.displayElectronicsInfo()
c=Clothing("P55","Jean",800,"L","Cotton")
c.displayClothingInfo()
