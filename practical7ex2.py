
t= (1, 2, 3, 4, 2, 3, 5, 6, 2)
count_dict = {}
repeated_items = []

for item in t:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

for item, count in count_dict.items():
        if count > 1:
            repeated_items.append(item)
print("Repeated items in the tuple:", repeated_items)
