import sys
import argparse
import pydantic
import yaml

from .. import rates


def pydantic_to_github(err, rates_file):
    """Produce a github error annotation from a pydantic ValidationError"""
    for error in err.errors():
        print(f"::error file={rates_file},title=Validation error::{error['msg']}")


def yaml_to_github(err, rates_file):
    """Produce a github error annotation from a YAML ParserError"""
    line = err.problem_mark.line
    print(
        f"::error file={rates_file},line={line},title=Parser error::{err.context}: {err.problem}"
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument(
        "-g", "--github", action="store_true", help="Emit github workflow annotations"
    )
    p.add_argument("-u", "--url", action="store_true", help="Rate file is a url")
    p.add_argument("rates_file", default="rates.yaml", nargs="?")
    args = p.parse_args()

    try:
        if args.url:
            r = rates.load_from_url(args.rates_file)
        else:
            r = rates.load_from_file(args.rates_file)

        print(f"OK [{len(r.root)} entries]")
    except pydantic.ValidationError as err:
        if args.github:
            pydantic_to_github(err, args.rates_file)
        sys.exit(err)
    except yaml.parser.ParserError as err:
        if args.github:
            yaml_to_github(err, args.rates_file)
        sys.exit(err)
