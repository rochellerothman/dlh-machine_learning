#!/usr/bin/env python3
"""Retrieve starships that can hold a given number of passengers."""

import requests


def availableShips(passengerCount):
    """Return ships that can hold at least passengerCount passengers."""
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "unknown")
            passengers = passengers.replace(",", "")

            try:
                capacity = int(passengers)
            except ValueError:
                continue

            if capacity >= passengerCount:
                ships.append(ship.get("name"))

        url = data.get("next")

    return ships
