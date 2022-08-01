# Backpack
# We can carry 2.5kg
# Maximize the weight limit utilized
# Maximizing the value of the items

# - Items
#   - Bottle of water
#     - Weight: 0.680389 kg
#     - Value:  15
#   - Snacks
#     - Weight: 0.136078 kg
#     - Value:  8
#   - Hat
#     - Weight: 0.453592 kg
#     - Value:  10
#   - Sunglasses
#     - Weight: 0.3175147 kg
#     - Value:  10
#   - Camera
#     - Weight: 0.907185 kg
#     - Value:  9
#   - Umbrella
#     - Weight: 1.36078 kg
#     - Value:  2
#   - Laptop
#     - Weight: 1.13398 kg
#     - Value: 5
# total weight of items - 4.9895187 kg


# - [0, 1, 1, 0, 0, 1, 0]
# - Snacks, hat, umbrella
# - 1.95045 kg
# - 20
# - [1, 1, 0, 1, 0, 0, 1]
# - bottle of water, snacks, sunglasses, and laptop
# - 2.2679617 kg
# - 38


class Item:
  def __init__(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value
  # END init method
# END Item class

items = []

items.append( Item('Bottle of Water', 0.680389, 15) )
items.append( Item('Snacks', 0.136078, 8) )
items.append( Item('Hat', 0.453592, 10) )
items.append( Item('Sunglasses', 0.3175147, 10) )
items.append( Item('Camera', 0.907185, 9) )
items.append( Item('Umbrella', 1.36078, 2) )
items.append( Item('Laptop', 1.13398, 5) )