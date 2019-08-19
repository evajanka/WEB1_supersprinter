def get_data_from_csv():
    with open("data.csv", "r") as myfile:
        data = [line.strip().split(";") for line in myfile]
    return data

