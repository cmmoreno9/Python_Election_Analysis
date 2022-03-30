counties = ["Arapahoe", "Denver", "Jefferson"]
counties_list = []
print(counties_list)
counties [0]
len(counties)
counties[0:2]
counties[0:1]
counties.append("El Paso")
print(counties_list)
counties.insert(2, "El Paso")
print(counties_list)
counties.remove("El Paso")
print(counties_list)
counties.pop(3)
print(counties_list)
counties[2] = "El Paso"
print(counties_list)
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
print(counties_tuple[1])
counties_dict = {}
counties_dict["Arapahoe"]= 422829
print(counties_dict)
counties_dict["Denver"]= 463353
counties_dict["Jefferson"]= 432438
print(counties_dict)
len(counties_dict)
counties_dict.items()
print ((counties_dict).keys())
print (counties_dict['Arapahoe'])
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
counties = ["Arapahoe", "Denver", "Jefferson"]
if ("El Paso") in counties:
    print("El Paso is in the list of countries")
else:
    print("El Paso is not the list of counties")
if ("Arapahoe") in counties and ("El Paso") in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if ("Arapahoe") in counties or ("El Paso") in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:print("Arapahoe and El Paso are not in the list of counties.")
for county in counties:
    print(county)
for county_dict in voting_data:
   for value in county_dict.values():
        print(value)
        