from abc import ABCMeta, abstractmethod 
 

#Creador de carro  
class Car(metaclass=ABCMeta): 
    def __init__(self): 
        self.name = None 
        self.maxSpeed = None 
         
    def __str__(self): 
        return "name is {:s}, maxSpeed is {:s}".format(self.name, self.maxSpeed) 

#Tipos de carros         
class SportsCar(Car): 
    def __init__(self): 
        self.name = "Deportivo" 
        self.maxSpeed = "250 km/hr" 
         
class FamilyCar(Car): 
    def __init__(self): 
        self.name = "Familiar" 
        self.maxSpeed = "150 km/hr" 


#Creador de objeto (fabrica + carro)              
class AbstractFactory(metaclass=ABCMeta): 
    def __init__(self): 
        self.manufacturer = None 
 
    def __str__(self): 
        return "manufacturer is {:s}".format(self.manufacturer) 
         
    @abstractmethod 
    def createCar(self, carType): pass 
     
    @staticmethod           
    def get_factory(factoryName): 
        if factoryName == "vw": 
            return VWFactory() 
        elif factoryName == "mb": 
            return MBFactory() 
             
        raise TypeError("Unknown Factory") 
         
#Tipos (clases) de fabricas
class VWFactory(AbstractFactory): 
    def __init__(self): 
        self.manufacturer = "VolksWagen" 
 
    def createCar(self, carType): 
        self.car = None 
        if carType == "sports": 
            self.car =  SportsCar(); 
        elif carType == "family": 
            self.car =  FamilyCar(); 
        else: 
            print("Car type {:s} is not defined".format(carType)) 
        return self.car  
             
    def doSomething(self): 
        print(self.car) 

class MBFactory(AbstractFactory): 
    def __init__(self): 
        self.manufacturer = "Mercedez Benz" 
 
    def createCar(self, carType): 
        self.car = None 
        if carType == "sports": 
            self.car =  SportsCar(); 
        elif carType == "family": 
            self.car =  FamilyCar(); 
        else: 
            print("Car type {:s} is not defined".format(carType)) 
        return self.car  
             
    def doSomething(self): 
        print(self.car) 

    
#Implementacion             
if __name__ == "__main__": 
    myFactory = AbstractFactory.get_factory("mz") 

    print(myFactory) 
     
    s = myFactory.createCar("sports") 
    f = myFactory.createCar("family") 
     
    print(s) 
    print(f) 
     

