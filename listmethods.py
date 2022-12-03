# # append methodu listeye eleman eklemek için kullanılmaktadır.
# list = ["a",5,"b","bektas"]
# print("eleman eklenmemiş hali : {}".format(list))
# list.append("new_one")
# print("append ile eleman eklenmiş hali : {}".format(list)) # ['a', 5, 'b', 'bektas', 'new_one']

# #insert methodu ile append methodundan farklı olarak listedeki belirli bir indexe eleman ekleriz.
# list = ["a",5,"b","bektas"]
# print("eleman eklenmemiş hali : {}".format(list))
# list.insert(0,"new_one")
# print("insert ile eleman eklenmiş hali : {}".format(list)) # ['new_one', 'a', 5, 'b', 'bektas']

# #remove methodu ile liste içindeki herhangi bir elemanı silebiliriz.
# list = ["a",5,"b","bektas"]
# list.remove(5)
# print(list)   # ['a', 'b', 'bektas']

# # clear methodu ile ise listedeki tüm elemanları sileriz.
# list = ["a",5,"b","bektas"]
# list.clear()
# print(list)   # []

# list = ["a",5,"b","bektas"]
# print(10 in list)   #false

# list = ["a",5,"b","bektas"]
# print("bektas" in list)   #true

# Listede ne kadar eleman olduğunu bulmak için len methodu kullanılmaktadır.
list = ["a",5,"b","bektas"]
print(len(list))  #4
