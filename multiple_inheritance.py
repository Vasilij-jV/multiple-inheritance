# -*- confing: utf-8 -*-

class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def __init__(self):
        self.quantity = 0

    def horse_powers(self):
        return self.quantity


class Nissan(Car, Vehicle):
    vehicle_type = 'седан'
    price = 1500000

    def __init__(self):
        super().__init__()
        self.quantity = 400

    def horse_powers(self):
        return self.quantity


nissan = Nissan()
print(nissan.vehicle_type)
print(nissan.price)
