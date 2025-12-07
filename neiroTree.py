# def fruits(size, thickness):
#     if size < 5:
#         return "apple"
#     if thickness <1:
#         return "apple"
#     else:
#         return "orange"


data =[]

row = {"size": 4, "tol": 1.3, "name": "orange"}
data.append(row)
row = {"size": 1, "tol": 0.1, "name": "apple"}
data.append(row)

row = {"size": 4, "tol": 0.4, "name": "apple"}
data.append(row)

row = {"size": 0.1, "tol": 2, "name": "orange"}
data.append(row)

row = {"size": 2, "tol": 1.3, "name": "orange"}
data.append(row)

row = {"size": 2, "tol": 1.5, "name": "oragne"}
data.append(row)

for i in data:
    # print(i)
    print(f"Размер - {i["size"]}, Толщина - {i["tol"]}, Это - {i["name"]}")