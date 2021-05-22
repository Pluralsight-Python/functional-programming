"""
    Examples of advanced comprehensions: Multi-input comprehension and Nested Comprehension
"""

if __name__ == '__main__':
    # All integer coordinates in Cartesian 3D space upto given point.
    # Multi-input comprehension
    upto = (1, 1, 2)
    coords = [(x, y, z) for x in range(upto[0] + 1) for y in range(upto[1] + 1) for z in range(upto[2] + 1)]
    print(coords)

    # Nested Comprehension
    places = {"Gurgaon", "Lucknow", "Shimla", "Kannauj"}
    letter_set = [{letter for letter in place} for place in places]
    print(letter_set)

