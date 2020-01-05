from flask import g
import pandas as pd
import sqlite3
import requests
import pandas_datareader as pdr
from pandas_datareader import data, wb

DATABASE = 'wp_data.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None: 
        db = g._database = sqlite3.connect(DATABASE, isolation_level=None)
    return db

def read_database(query, params):
    return pd.read_sql_query(query, con=get_db(), params=params)

def get_country_emissions_as_kt(country):
    query = "SELECT year, co2_kt FROM co2_table WHERE country=?;"
    param = (country,)
    return read_database(query, param)

def get_country_population(country): 
    query = "SELECT year, population FROM population_table WHERE country=?;"
    param = (country,)
    return read_database(query, param)

def get_world_bank_api_data_to_db(): 
    co2_data_to_db()
    pop_data_to_db()

def co2_data_to_db(): 
    co2_data = pdr.wb.download(country='all', indicator='EN.ATM.CO2E.KT', start='1960', end='2019')
    co2_data.columns = ['co2_kt']
    co2_data.to_sql('co2_table', con=get_db(), if_exists='replace')

def pop_data_to_db():
    pop_data = pdr.wb.download(indicator='SP.POP.TOTL', country='all', start='1960', end='2019')
    pop_data.columns = ['population']
    pop_data.to_sql('population_table', con=get_db(), if_exists='replace')