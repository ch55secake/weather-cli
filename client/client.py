import json
from dataclasses import dataclass

import requests as r
import rich as ri

from config.config import get_config


@dataclass
class WeatherResponse:
    """
    Dataclass representing a response from the Weather API
    """
    location: dict
    current: dict

    @property
    def condition(self) -> dict:
        return self.current["condition"]

    @property
    def wind_mph(self) -> float:
        return self.current["wind_mph"]

    @property
    def feels_like_c(self) -> float:
        return self.current["feelslike_c"]

    @property
    def feels_like_f(self) -> float:
        return self.current["feelslike_f"]

    @property
    def temp_c(self) -> float:
        return self.current["temp_c"]

    @property
    def temp_f(self) -> float:
        return self.current["temp_f"]

    def json(self):
        return json.loads(self.current["condition"])


class WeatherClient:

    def __init__(self):
        """
        Creates a new weather api client, can fetch weather data with this client
        """
        self.base_url = "https://api.weatherapi.com/v1/"
        self.headers: dict = { "Accept": "application/json" }

    def get_data(self, location: str, api_key: str) -> WeatherResponse:
        """
        Will fetch weather data from weather api, will map json received into WeatherResponse
        :param api_key: api_key to fetch weather data with
        :param location: provide location to get weather data from
        :return: WeatherResponse
        """
        try:
            response = r.get(f"{self.base_url}/current.json?key={api_key}q={location}", headers=self.headers).json()
            if response.ok:
                return WeatherResponse(**response)
        except Exception as e:
            ri.print(f"Error when fetching from weather api: {e}")


