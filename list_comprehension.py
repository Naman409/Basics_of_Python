# multiples = []
# for x in range(1,11):
#     multiples.append(x*7)

# print(multiples)

# Same thing can be done just in one line by list comprehension done as below -

multiples = [7*x for x in range(1,11)]
print(multiples)