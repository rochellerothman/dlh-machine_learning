#!/usr/bin/env python3
"""Retrieve home planets of all sentient Star Wars species."""

import requests


def sentientPlanets():
    """Return home planet names for all sentient species."""
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification")
            designation = species.get("designation")

            if classification == "sentient" or designation == "sentient":
                homeworld = species.get("homeworld")

                if homeworld:
                    planet_response = requests.get(homeworld)
                    planet_data = planet_response.json()
                    planets.append(planet_data.get("name"))

        url = data.get("next")

    return planets
