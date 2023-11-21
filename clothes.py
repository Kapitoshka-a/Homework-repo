from enum import Enum


class ClothingType(Enum):
    SHIRT = 1
    JEANS = 2
    JACKET = 3


class Clothing:
    def __init__(self, name, description, location, color, size, clothing_type):
        self.param = None
        self.name = name
        self.description = description
        self.location = location
        self.color = color
        self.size = size
        self.clothing_type = clothing_type

    def __str__(self):
        return (f"{self.name} ({self.clothing_type.name}), Description: {self.description}, Location: {self.location}, "
                f" Color: {self.color}, Size: {self.size}, Clothing type: {self.clothing_type}")

    def change(self, text):
        self.param = text


class Wardrobe:
    def __init__(self):
        self.clothing_list = []

    def add_clothing(self, clothing):
        self.clothing_list.append(clothing)

    def sort_clothing_by_size(self):
        self.clothing_list.sort(key=lambda x: x.size)

    def are_going_out(self):
        clothing_types = set(clothing.clothing_type for clothing in self.clothing_list)
        ready_to_go_out = len(clothing_types) > 3
        return ready_to_go_out
