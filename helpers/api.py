import requests
import re

from helpers.exports import parse_exports

try:
    variables = parse_exports("data/github_export")
    # print(json.dumps(variables, indent=4))
except KeyError as ke:
    raise SystemExit(f"FATAL| {ke}")


def api_call(url, user, token, params=None, headers=None):
    response = requests.get(url, auth=(user, token), params=params, headers=headers)
    response.raise_for_status()
    return response


def get_repos(usr, filter=None):
    pass


def get_totalpages(response):
    link = response.headers["link"]
    regex = "([0-9]+)>; rel=\"last\""
    search = re.search(regex, link)
    pages, = search.groups()
    return int(pages)
