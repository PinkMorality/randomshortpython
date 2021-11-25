import csv

total_population = 0
total_area = 0

with open("C:\Users\Aditya\AppData\Roaming\JetBrains\PyCharmCE2020.3\scratches\population redestribute delta.csv", newline="") as csvfile:
    dict1 = csv.DictReader(csvfile)
    dict2 = csv.DictReader(csvfile)

    # for row in dict1:
    #     population = float(row.get("Population"))
    #     area = float(row.get("Area"))
    #     density = population/area
    #     #print(area)
    #     #print(population)
    #     population = float(population)
    #     total_population += population
    #     total_area += area
    average_density = 7910157000/122162000

    def change_population(c_pop, c_den, c_area):
        delta_pop = average_density*c_area - c_pop
        return delta_pop


    print(f"{total_population} people, {total_area} km2")
    # for row in dict1:
    #     population = float(row.get("Population"))
    #     area = float(row.get("Area"))
    #     density = population/area
    #     print(area)
    #     print(population)
    #     population = float(population)
    #     total_population += population
    #     total_area += area

    for row in dict2:
        population = float(row.get("Population"))
        area = float(row.get("Area"))
        density = float(row.get("Density"))
        change = change_population(population, density, area)
        population2 = str(population + change)
        row.update({"Population": population2})
        row.setdefault("Change",change)
        print(f"{row}")
