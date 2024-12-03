from src.client.client import WeatherResponse


def format_response(response: WeatherResponse, location: str) -> str:
    """
    Neatly format the weather response as an f string, also includes mark down formatting provided by rich, currently only output
    the temp that it feels like and the actual temperature alongside the current condition
    :param location: location requested for by the user
    :param response: weather response returned higher up by the client
    :return: neatly formatted string to output to terminal
    """
    return (f"{choose_icon(response)} Currently it [bold]feels[/bold] like {round(int(response.feels_like_c))} °[bold cyan]C[/bold cyan] in [bold salmon1]{location}[/bold salmon1].\n "
            f" * It is actually {round(int(response.temp_c))} °[bold cyan]C[/bold cyan].\n"
            f"  * It's [bold]{str.lower(response.condition["text"])}[/bold].")


def choose_icon(response: WeatherResponse) -> str:
    """

    :param response:
    :return:
    """
    match str.lower(response.condition["text"]):
        case "sunny":
            return ":sunny:"
        case "clear":
            return ":crescent_moon:"
        case "cloudy" | "partly cloudy" | "overcast":
            return ":cloud:"
        case "rain":
            return ":cloud_rain:"
        case "thunder":
            return ":thunder_cloud_rain:"
        case "snow":
            return ":snowflake:"
        case _:
            return ":mount_fuji:"


