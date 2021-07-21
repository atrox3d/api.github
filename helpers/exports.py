import os
from string import Template
import json
from dataclasses import dataclass


@dataclass
class Variables:
    user = ""
    api = ""
    token = ""
    public_repos = ""
    private_repos = ""


def set_plainvars(filepath):
    _variables = {}
    with open(filepath) as gh:
        for line in gh:
            line = line.strip()
            if "$" not in line:
                if "export" in line and "=" in line:
                    export, line = line.split(" ")

                if "=" in line:
                    name, value = line.split("=")
                    # print(name, value)
                    os.environ[name] = value
                    _variables[name] = value
    return _variables


def set_expandedvars(filepath):
    _variables = {}
    with open(filepath) as gh:
        for line in gh:
            line = line.strip()
            if "$" in line:
                if "export" in line and "=" in line:
                    export, line = line.split(" ")

                if "=" in line:
                    name, value = line.split("=")
                    # print(name, value)
                    try:
                        expanded = Template(value).substitute(os.environ)
                        os.environ[name] = expanded
                        value = os.environ[name]
                        # print(name, value)
                        _variables[name] = value
                    except KeyError as ke:
                        raise KeyError(f"cannot expand {name}={value} with missing variable: {ke}")
    return _variables


def parse_exports(filepath):
    _variables = {}
    _variables.update(set_plainvars(filepath))
    _variables.update(set_expandedvars(filepath))

    variables = Variables()
    try:
        variables.user = _variables["GH_USER"]
        variables.token = _variables["GH_REPO_TOKEN"]
        variables.api = _variables["GH_API"]
        variables.private_repos = _variables["GH_PRIVATE_REPOS_URL"]
        variables.public_repos = _variables["GH_PUBLIC_REPOS_URL"]
    except KeyError as ke:
        raise SystemExit(f"FATAL| missing variable {ke}")

    return variables


if __name__ == '__main__':
    variables = parse_exports("../data/github_export")
    # print(json.dumps(variables, indent=4))
    print(variables.__dict__)