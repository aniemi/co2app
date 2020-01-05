from flask import Flask, render_template, request, redirect
from forms import dataForm
import requests
from data import get_json, get_major_powers_emissions, update_databases

def get_json_for_template(country, per_capita): 
    if per_capita: 
        return api_per_capita(country)
    else: 
        return api_kt(country)

def major_powers_api():
    return calculate_major_powers()

def api_kt(country): 
    return get_json(country, true_for_kt=True)

def api_per_capita(country): 
    return get_json(country, true_for_kt=False)

def get_form(): 
    return dataForm()

def index(): 
    return render_template("index.html", form=get_form())

def requested_country():
    form = get_form()
    country = request.form.get('country')
    per_capita = request.form.get('per_capita')
    if form.validate_on_submit(): 
        return render_template("index.html", form=form, json=get_json_for_template(country, per_capita))
    else: 
        index()

# clean up
def major_powers():
    return render_template("major_powers.html", form=get_form(), china_emissions=get_json_for_template("China", False), russia_emissions=get_json_for_template("Russian Federation", False), france_emissions=get_json_for_template("France", False), uk_emissions=get_json_for_template("United Kingdom", False), usa_emissions=get_json_for_template("United States", False))