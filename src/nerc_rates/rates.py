import requests
import yaml

from .models import Rates

DEFAULT_URL = "https://raw.githubusercontent.com/knikolla/nerc-rates/main/rates.yaml"


def load_from_url(url=DEFAULT_URL) -> Rates:
    r = requests.get(url, allow_redirects=True)
    # Using the BaseLoader prevents conversion of numeric
    # values to floats and loads them as strings.
    config = yaml.safe_load(r.content.decode("utf-8"))
    return Rates.model_validate(config)


def load_from_file() -> Rates:
    with open("rates.yaml", "r") as f:
        # Using the BaseLoader prevents conversion of numeric
        # values to floats and loads them as strings.
        config = yaml.safe_load(f)
    return Rates.model_validate(config)
