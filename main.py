import json

from helpers.exports import parse_exports
from helpers import api

try:
    # variables = parse_exports("data/github_export")
    # print(json.dumps(variables, indent=4))
    gh = api.GithubApi.from_export("data/github_export")
except KeyError as ke:
    raise SystemExit(f"FATAL| {ke}")

data = gh.get_repos(visibility=api.REPOS_ALL)
print(f"{len(data)}")
