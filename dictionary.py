# file_counts = {"txt":20 ,"jpg":15,"png":10,"css":25}
# print(type(file_counts))
# print(file_counts["txt"])
# print("jpg" in file_counts)
# print("html" in file_counts)
# The below method is used to add key value pair of js and 10 into file_counts
# file_counts["js"] = 10
# If we add a new key which exists , then the value of that key gets replaced with the new key as shown below
# file_counts["jpg"] = 17
# To delete a key value pair we use del key word as shown below
# del file_counts["png"]
# print(file_counts)

# Iteration in Dictionary
# We use .items() method to iterate both key and value as shown below
# for extention,num in file_counts.items():
#     print("{} files with {} extention".format(num,extention))

# To access keys and values we can use the following methods
# print(file_counts.keys())
# print(file_counts.values())

# for value in file_counts.values():
#     print(value)

# def count_letters(text):
#     result = {}
#     for letter in text.lower():
#         if letter not in result:
#             result[letter]=0
#         result[letter] += 1
#     return result

# print(count_letters("Naman"))

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)