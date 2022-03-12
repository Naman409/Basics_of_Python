fruits = ["Apple","Banana","Grapes","Watermelon"]
fruits.append("Kiwi")
# print(fruits)
fruits.insert(0,"Orange")
# if we insert element at the position more than the size of list , the element gets inserted at the end of the list without any error
fruits.insert(40,"Guava")
fruits.remove("Grapes")
fruits.pop(1)
fruits[2]="Strawberry"
print(fruits)


# list[i] = x Replaces the element at index i with x

# list.append(x) Inserts x at the end of the list

# list.insert(i, x) Inserts x at index i

# list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.

# list.remove(x) Removes the first occurrence of x in the list

# list.sort() Sorts the items in the list

# list.reverse() Reverses the order of items of the list

# list.clear() Removes all the items of the list

# list.copy() Creates a copy of the list

# list.extend(other_list) Appends all the elements of other_list at the end of list