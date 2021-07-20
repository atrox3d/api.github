import os
import json


def set_plainvars(filepath):
    variables = {}
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
                    variables[name] = value
    return variables


def set_expandedvars(filepath):
    variables = {}
    with open(filepath) as gh:
        for line in gh:
            line = line.strip()
            if "$" in line:
                if "export" in line and "=" in line:
                    export, line = line.split(" ")

                if "=" in line:
                    name, value = line.split("=")
                    # print(name, value)
                    os.environ[name] = os.path.expandvars(value)
                    value = os.environ[name]
                    # print(name, value)
                    variables[name] = value
    return variables


def parse_exports(filepath):
    variables = {}
    variables.update(set_plainvars(filepath))
    variables.update(set_expandedvars(filepath))

    return variables


if __name__ == '__main__':
    variables = parse_exports("../data/github_export")
    print(json.dumps(variables, indent=4))
