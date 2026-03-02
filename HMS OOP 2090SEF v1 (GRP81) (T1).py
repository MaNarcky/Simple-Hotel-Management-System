#By CHIAN Makeiyle P., DGW Mackie H. and LIU Keyang (Group 81)
#Version 1 (March 2) | OOP-based application development | Task 1
#OOP Project on Hotel Managment System
#Created for COMP2090SEF 2026 Spring Term

from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, room_number, price, capacity):
        self.room_number = room_number
        self.price = price
        self.capacity = capacity
        self.is_occupied = False
    
    @abstractmethod
    def get_room_type(self):
        pass
    
    def __str__(self):
        return f"{self.get_room_type()} #{self.room_number} - ${self.price}/night"

class StandardRoom(Room):
    def get_room_type(self):
        return "Standard Room"

class DeluxeRoom(Room):
    def __init__(self, room_number, price, capacity, has_balcony=True):
        super().__init__(room_number, price, capacity)
        self.has_balcony = has_balcony
    
    def get_room_type(self):
        return "Deluxe Room"

class Suite(Room):
    def __init__(self, room_number, price, capacity, has_jacuzzi=False):
        super().__init__(room_number, price, capacity)
        self.has_jacuzzi = has_jacuzzi
    
    def get_room_type(self):
        return "Suite"
    
class Guest:
    def __init__(self, guest_id, name, email, phone):
        self._guest_id = guest_id
        self._name = name
        self._email = email
        self._phone = phone
        self._loyalty_points = 0
    
    #Getter
    @property
    def guest_id(self):
        return self._guest_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def loyalty_points(self):
        return self._loyalty_points
    
    #Setter with validation
    def add_loyalty_points(self, points):
        if points > 0:
            self._loyalty_points += points
    
    def use_loyalty_points(self, points):
        if points <= self._loyalty_points:
            self._loyalty_points -= points
            return True
        return False
    
    def __str__(self):

        return f"Guest {self._name} (ID: {self._guest_id})"
