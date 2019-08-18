def route_index():
    data = None
    with open("/home/evi/codecool/web/1stSIassignment/data.csv", "r") as myfile:
        data = [line.strip().split(";") for line in myfile]
    return data

print(route_index())