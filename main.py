from helpers.exports import parse_exports
from helpers.api import api_call, get_totalpages

try:
    variables = parse_exports("data/github_export")
    # print(json.dumps(variables, indent=4))
except KeyError as ke:
    raise SystemExit(f"FATAL| {ke}")

response = api_call(url=variables.private_repos, user=variables.user, token=variables.token)
print(get_totalpages(response))
