import requests
import random
import sqlite3


response = requests.get("https://restcountries.com/v3.1/all")
countries = response.json()


selected_countries = random.sample(countries, 10)


country_data = []
for country in selected_countries:
    name = country.get("name", {}).get("common", "N/A")
    capital = country.get("capital", ["N/A"])[0] if country.get("capital") else "N/A"
    flag = country.get("flags", {}).get("png", "N/A")
    subregion = country.get("subregion", "N/A")
    population = country.get("population", "N/A")
    country_data.append((name, capital, flag, subregion, population))


conn = sqlite3.connect('countries.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY,
    name TEXT,
    capital TEXT,
    flag TEXT,
    subregion TEXT,
    population INTEGER
)
''')


cursor.executemany('''
INSERT INTO countries (name, capital, flag, subregion, population)
VALUES (?, ?, ?, ?, ?)
''', country_data)


conn.commit()
conn.close()

print("10 random countries have been inserted into the database.")
