def fruits(tuple_of_fruits):
    output = {}
    for fruit in tuple_of_fruits:
        if fruit.get("shape") == "sphere" and 300 <= fruit.get("mass") <= 600 and 100 <= fruit.get("volume") <= 500:
            if fruit.get("name") in output:
                output[fruit.get("name")] += 1
                continue
            output[fruit.get("name")] = 1

    return output


print(fruits((
    {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
    {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})))
