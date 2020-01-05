import pandas as pd
from database import get_country_emissions_as_kt, get_country_population, get_world_bank_api_data_to_db

def clean_emissions_as_kt(country):
    emissions = get_country_emissions_as_kt(country)
    emissions.set_index(['year'], inplace=True)
    emissions.sort_index(ascending=True, inplace=True)
    emissions = emissions["co2_kt"]
    return emissions

def clean_country_population(country): 
    population = get_country_population(country)
    population.set_index(['year'], inplace=True) 
    population.sort_index(ascending=True, inplace=True)
    population = population["population"]
    return population

def calculate_emissions_percapita(country):
    emissions_as_metric_tonnes = clean_emissions_as_kt(country) * 1000
    co2_mt_per_capita = emissions_as_metric_tonnes / clean_country_population(country)
    return co2_mt_per_capita

def get_major_powers_emissions(): 
    major_powers = ['China', 'Russian Federation', 'France', 'United Kingdom', 'United States']
    major_powers_data = []
    for country in major_powers:
        country_data = clean_emissions_as_kt(country)
        country_data.name = country
        major_powers_data.append(country_data)
    major_powers_data = pd.concat(major_powers_data, axis=1)
    return major_powers_data.to_json()

def get_json(country, true_for_kt): 
    if true_for_kt is True: 
        df_for_country = clean_emissions_as_kt(country).to_json()
        return df_for_country
    else: 
        df_for_country = calculate_emissions_percapita(country)
        return df_for_country.to_json()

def update_databases():
    try: 
        get_world_bank_api_data_to_db
        print("DB tables updated.")
    except: 
        print("Unable to update database.")