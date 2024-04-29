
brand = {
    "name":"Zara",
    "creation_date" : 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes" : ["men", "women", "children", "home"],
    "international_competitors" : ["Gap", "H&M", "Benetton" ],
    "number_stores": 2,
    "major_color" : {"France": "blue", 
                    "Spain": "red", 
                    "US": "pink,green"},
}

brand["country_creation"]="Spain"

brand.pop("creation_date")

last_international_competitor = brand["international_competitors"][-1]
print("Last international competitor:", last_international_competitor,"\n")

us_major_colors = brand["major_color"]["US"]
print("Major clothes colors in the US:", us_major_colors,"\n")

num_key_value_pairs = len(brand)
print("Number of key-value pairs:", num_key_value_pairs,"\n")

keys = list(brand.keys())
print("Keys of the dictionary:", keys,"\n")


more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)

print("Number of stores:", brand["number_stores"])
