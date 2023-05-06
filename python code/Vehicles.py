class Vehicle:
    def __init__(self,b,x,y):
        self.__year_manufactured = b
        self.engine_displacement_volume = int()
        self.colour = str()
        self.gear_system = str()
        self.fuel_type = str()
        self.__previous_owners = x
        self.__mileage = y
        self.model = str()
    def __del__(self):
        obj = self.model
    def __call__(self):
        return {'name':self.model,'year of manufacture':self.__year_manufactured,'colour':self.colour,'transmission':self.gear_system,'fuel':self.fuel_type,'Engine displacement':self.engine_displacement_volume,'mileage':self.__mileage}
    def get__Year_manufactured(self):
        print(self.__year_manufactured)
    def age(self,a):
        #a = 2023, current year
        age = a - self.__year_manufactured
        return age
    def set__Previous_owners(self,__previous_owners,vehicle_sold):
        #number of previous owners will change with each successfull trade
        vehicle_sold == 1 or 0
        if vehicle_sold == 1:
            __previous_owners = __Previous_owners + 1
        else:
            __previous_owners = __previous_owners 
        self.__previous_owners = __previous_owners
    def get__Previous_owners(self):
        return self.__previous_owners
    def set__Mileage(self,mileage,distance):
        #driving a vehicle increases its mileage
        #mileage is mileage before driving
        #distance is distance covered in metres when driving
        if distance>0:
            mileage = mileage + distance
        else:
            mileage = mileage
        self.__mileage = mileage
    def get__Mileage(self):
        print(self.__mileage//1000,'kilometres')
class Car(Vehicle):
    body_type = 'monocoque'
    maximum_passenger = 7
    maximum_load_kilo = 1000
    purpose = 'personal navigation and taxi'
    def __init__(self,b,x,y):
        Vehicle.__init__(self,b,x,y)
class Sedan(Car):
    maximum_passenger = 5
    trunk_door = 'horizontal when closed'
    doors = 4
    trunk_space = 'limited'
    rear_screen = 'not attached to trunk-door'
    def __init__(self,b,x,y):
        Car.__init__(self,b,x,y)
class Hatchback(Car):
    trunk_door = 'hatch opening upwards'
    rear_screen = 'attached to trunk-door'
    tailgate = 'steeply sloping'
    accesories = 'speed improvement'
class SUV(Car):
    body_type = 'body-on-frame chasis'
    drive_type = '4WD'
    accesories = 'off-road modification and speed improvement'
class Crossover(Car):
    drive_type = '2WD'
    accesories = 'city traffic modification and speed improvement'
class Stationwagon(Car):
    trunk_space = 'large'
    ground_clearence = 'increased for country navigation'
    trunk_door = 'hatch opening upwards'
    rear_screen = 'attached to trunk-door'
class Coupe(Car):
    interior_space = 'less than 33 cubic feet'
    doors = 2
    rear_seat = 'present'
    accesories = 'speed improvement'
class Roadster(Car):
    doors = 2
    rear_seat = 'absent'
    cargo_space = 'negligible'
    roof_type = 'retractable roof'
    accesories = 'speed improvement'
class Convertible(Car):
    roof_type = 'retractable roof'
    trunk_space = 'limited'
    rear_seat = 'present'
class Microcar(Car):
    body_size = 'small'
    accessories = 'city traffic navigation'
    doors = 2
    cargo_space = 'negligible'
class Limo(Car):
    body_size = 'longer than normal cars'
    accessories = 'super comfort enhancement'
class Pickup(Vehicle):
    cabin_area = 'enclosed'
    cargo_area = 'separated from cabin'
    purpose = 'cargo transport'
    def __init__(self,b,x,y):
        Vehicle.__init__(self,b,x,y)
class Single_cab(Pickup):
    doors = 2
    cabin_area = 'small, has front seats only'
class Double_cab(Pickup):
    doors = 4
    cabin_area = 'large, has front and rear seats'
class Ute(Pickup):
    body_type = 'monocoque'
    cabin_area = 'large, has front and rear seats'
class Van(Vehicle):
    cargo_area = 'not separated from cabin'
    body = 'encloses cabin and cargo area'
    purpose = 'cargo and/or passenger transport'
    def __init__(self,b,x,y):
        Vehicle.__init__(self,b,x,y)
class Bus(Vehicle):
    cargo_area = 'large and not separated from cabin'
    body = 'encloses cabin and cargo area'
    purpose = 'cargo and/or passenger transport'
    def __init__(self,b,x,y):
        Vehicle.__init__(self,b,x,y)
class Singledeck(Bus):
    passenger_space = 'one deck'
class Minibus(Bus):
    passenger_space = 'one deck'
    maximum_passengers = 38
class Articulatedbus(Bus):
    passenger_compartments = 'more than one, joined by pivot joints'
class Doubledeck(Bus):
    passenger_space = 'two decks'
class Truck(Vehicle):
    purpose = 'cargo transport'
    cabin_area = 'enclosed'
    cargo_area = 'large and separated from cabin'
    def __init__(self,b,x,y):
        Vehicle.__init__(self,b,x,y)

vehiclelist = []
vehicle1 = Sedan(2015,8,30000)
vehicle1.model = 'Hyundai Elantra'
vehicle1.colour = 'red'
vehicle1.engine_displacement_volume = 1.6
vehicle1.gear_system = 'automatic'
vehicle1.fuel_type = 'petrol'
vehicle1.__mileage = 30000000
if vehicle1.age(2023)>8 or vehicle1.get__Previous_owners()>5:
    del vehicle1
else:
    vehiclelist.append(vehicle1())
vehicle2 = Truck(2020,3,2105)
vehicle2.model = 'Kenworth W990'
vehicle2.colour = 'white'
vehicle2.engine_displacement_volume = 12.9
vehicle2.gear_system = 'manual'
vehicle2.fuel_type = 'diesel'
vehicle2.__mileage = 2105000
if vehicle2.age(2023)>8 or vehicle2.get__Previous_owners()>5:
    del vehicle2
else:
    vehiclelist.append(vehicle2())
vehicle3 = Minibus(2021,1,162555)
vehicle3.model = 'Iveco Daily'
vehicle3.colour = 'white'
vehicle3.engine_displacement_volume = 3.0
vehicle3.gear_system = 'manual'
vehicle3.fuel_type = 'diesel'
vehicle3.__mileage = 162555000
if vehicle3.age(2023)>8 or vehicle3.get__Previous_owners()>5:
    del vehicle3
else:
    vehiclelist.append(vehicle3())
vehicle3.maximum_passengers =31
vehicle4 = Van(2019,2,30000)
vehicle4.model = 'Nissan NV350 Urvan'
vehicle4.colour = 'Silver'
vehicle4.engine_displacement_volume = 2.5 
vehicle4.gear_system = 'manual'
vehicle4.fuel_type = 'diesel'
vehicle4.__mileage = 30000000
if vehicle4.age(2023)>8 or vehicle4.get__Previous_owners()>5:
    del vehicle4
else:
    vehiclelist.append(vehicle4())
vehicle5 = Microcar(2016,4,900)
vehicle5.model = 'Renault Twizy'
vehicle5.colour = 'grey'
vehicle5.engine_displacement_volume = 0
vehicle5.gear_system = 'automatic'
vehicle5.fuel_type = 'electricity'
vehicle5.__mileage = 900000
if vehicle5.age(2023)>8 or vehicle5.get__Previous_owners()>5:
    del vehicle5
else:
    vehiclelist.append(vehicle5())
vehicle6 = Crossover(2018,3,27345)
vehicle6.model = 'Mazda CX-5'
vehicle6.colour = 'white'
vehicle6.engine_displacement_volume = 2.5
vehicle6.gear_system = 'Automatic'
vehicle6.fuel_type = 'petrol'
vehicle6.__mileage = 27345000
if vehicle6.age(2023)>8 or vehicle6.get__Previous_owners()>5:
    del vehicle6
else:
    vehiclelist.append(vehicle6())
vehicle7 = Hatchback(2010,2,123456)
vehicle7.model = 'Kia Rio'
vehicle7.colour = 'blue'
vehicle7.engine_displacement_volume = 1.6
vehicle7.gear_system = 'Automatic'
vehicle7.fuel_type = 'petrol'
vehicle7.__mileage = 123456000
if vehicle7.age(2023)>8 or vehicle7.get__Previous_owners()>5:
    del vehicle7
else:
    vehiclelist.append(vehicle7())
vehicle8 = Double_cab(2017,3,30000)
vehicle8.model = 'Toyota Hilux'
vehicle8.colour = 'white'
vehicle8.engine_displacement_volume = 2.4
vehicle8.gear_system = 'manual'
vehicle8.fuel_type = 'diesel'
vehicle8.__mileage = 30000000
if vehicle8.age(2023)>8 or vehicle8.get__Previous_owners()>5:
    del vehicle8
else:
    vehiclelist.append(vehicle8())
vehicle9 = Hatchback(2020,1,333456)
vehicle9.model = 'Subaru Impreza'
vehicle9.colour = 'blue'
vehicle9.engine_displacement_volume = 2.0 
vehicle9.gear_system = 'manual'
vehicle9.fuel_type = 'petrol'
vehicle9.__mileage = 333456000
if vehicle9.age(2023)>8 or vehicle9.get__Previous_owners()>5:
    del vehicle9
else:
    vehiclelist.append(vehicle9())
vehicle10 = SUV(2023,0,0)
vehicle10.model = 'Nissan Armada'
vehicle10.colour = 'black'
vehicle10.engine_displacement_volume = 5.6
vehicle10.gear_system = 'semi-auto'
vehicle10.fuel_type = 'petrol'
vehicle10.__mileage = 900
if vehicle10.age(2023)>8 or vehicle10.get__Previous_owners()>5:
    del vehicle10
else:
    vehiclelist.append(vehicle10())
for i in range(len(vehiclelist)):
    for j in range(len(vehiclelist)):
        if vehiclelist[j]['year of manufacture']<vehiclelist[i]['year of manufacture']:
            temp = vehiclelist[i]
            vehiclelist[i] = vehiclelist[j]
            vehiclelist[j] = temp
    vehiclelist1 = vehiclelist
print(vehiclelist1)
vehiclelist2 = [[i for i in vehiclelist if i['mileage']<=5000],[i for i in vehiclelist if i['mileage']>5000 and i['mileage']<=100000],[i for i in vehiclelist if i['mileage']>100000 and i['mileage']<=200000],[i for i in vehiclelist if i['mileage']>200000 and i['mileage']<=300000],[i for i in vehiclelist if i['mileage']>300000 and i['mileage']<=400000],[i for i in vehiclelist if i['mileage']>400000]]        
print(vehiclelist2)
bestvehicles = [i for i in vehiclelist1 if i['year of manufacture']==vehiclelist1[0]['year of manufacture']]
for i in bestvehicles:
    optimumvehicle = bestvehicles[0]
    if i['mileage']<bestvehicles[0]['mileage']:
        optimumvehicle = i
    print('The optimum car is',i['name'],i['year of manufacture'])
