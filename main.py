from clothes import Clothing, Wardrobe, ClothingType


if __name__ == "__main__":
    wardrobe = Wardrobe()

    shirt1 = Clothing("Shirt 2", "Formal shirt", "Closet", "White", "L", ClothingType.SHIRT)
    shirt2 = Clothing("Shirt 1", "Casual shirt", "Closet", "Blue", "M", ClothingType.SHIRT)
    jeans1 = Clothing("Jeans 1", "Blue jeans", "Closet", "Blue", "L", ClothingType.JEANS)
    jacket1 = Clothing("Jacket 1", "Winter jacket", "Coat rack", "Black", "L", ClothingType.JACKET)

    shirt2.add_new_param("Bad whether")

    wardrobe.add_clothing(shirt1)
    wardrobe.add_clothing(shirt2)
    wardrobe.add_clothing(jeans1)
    wardrobe.add_clothing(jacket1)

    wardrobe.sort_clothing_by_size()

    for clothing in wardrobe.clothing_list:
        print(clothing)
    if wardrobe.are_going_out():
        print("You are ready to go out!")
    else:
        print("You are not ready to go out.")
        
