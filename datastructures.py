


# Empty list
fruits = ["apple", "banana", "orange"]

# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")      # Add to end
fruits.insert(1, "kiwi")    # Insert at position

# Remove items
fruits.remove("banana")     # Remove by value
last = fruits.pop()        # Remove and return last
del fruits[0]              # Remove by index

# Dictionary------
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
person["age"]

person["license"] = True

del person["license"] 
 





 # Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20




# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}