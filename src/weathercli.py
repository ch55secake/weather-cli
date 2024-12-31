from typing import Annotated

import rich
import typer as t

from src.client.client import WeatherClient, WeatherResponse
from src.config.config import does_config_file_exist, initialize_config, get_config
from src.output.output import format_response

app: t.Typer = t.Typer()

@app.command(
    help="Will create a new yaml configuration file, at the path $HOME/.config/weather-cli/config.yaml, this stores only "
         "the api key for weather api.",
    short_help="creates a new yaml configuration file",
)
def init(api_key: Annotated[str, t.Argument()], filepath: Annotated[str, t.Option()] = f".config/weather-cli/config.yml"):
    """
    Command to init configuration file at provided path and with provided key.
    :param api_key: api key that is to be saved
    :param filepath: the filepath to initialize configuration file at
    :return: nothing
    """
    if not does_config_file_exist(filepath=filepath):
        initialize_config(api_key=api_key)

@app.command(
    help="Fetch current weather information for a given area, relies on the weather api key that has to be already created, "
         "so please make sure that you have already run `weather-cli init <key>`, location will always default to London. Only outputs as celsius",
    short_help="fetch current weather information for a given area",
)
def get(location: Annotated[str, t.Argument()] = "London", json: Annotated[bool, t.Option()] = False):
    """
    Command to get the current weather information for a given area, relies on the weather api key
    :param location: provide the location to fetch weather information for
    :param json: whether to output as json
    :return: a string containing the current weather information
    """
    api_key: str = get_config().api_key
    weather_client: WeatherClient = WeatherClient()
    current_forecast: WeatherResponse = weather_client.get_data(location=location, api_key=api_key)
    if json:
        rich.print_json(data=str(current_forecast.json()))
    else:
        rich.print(format_response(current_forecast, location=location))


def main():
   app()

if __name__ == "__main__":
   main()