from helpers.exports import parse_exports
from helpers.api import GithubApi

try:
    # variables = parse_exports("data/github_export")
    # print(json.dumps(variables, indent=4))
    gh = GithubApi.from_export("data/github_export")
except KeyError as ke:
    raise SystemExit(f"FATAL| {ke}")

response = gh.api_call(url=gh.private_repos)
print(gh.get_totalpages(response))
