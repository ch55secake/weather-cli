from typing import Annotated

import rich
import typer as t

from client.client import WeatherClient, WeatherResponse
from config.config import does_config_file_exist, initialize_config, get_config

app: t.Typer = t.Typer()

@app.command()
def init(api_key: Annotated[str, t.Argument()], filepath: Annotated[str, t.Option()] = f".config/weather-cli/config.yml"):
    if not does_config_file_exist(filepath=filepath):
        initialize_config(api_key=api_key, filepath=filepath)

@app.command()
def get(location: Annotated[str, t.Argument()] = "London", json: Annotated[bool, t.Option()] = False):
    api_key: str = get_config().key()
    weather_client: WeatherClient = WeatherClient()
    current_forecast: WeatherResponse = weather_client.get_data(location=location, api_key=api_key)
    if json:
        rich.print_json(current_forecast.json())
    else:
        rich.print(f"It currently feels like {current_forecast.feels_like_c} at {location} and it is {current_forecast.condition["text"]}")


if __name__ == "__main__":
   app()