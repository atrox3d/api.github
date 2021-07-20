from helpers.exports import parse_exports

try:
    variables = parse_exports("data/github_export")
except KeyError as ke:
    raise SystemExit(f"FATAL| {ke}")

try:
    user = variables["GH_USER"]
    token = variables["GH_REPO_TOKEN"]
    api = variables["GH_API"]
    privaterepos = variables["GH_PRIVATE_REPOS_URL"]
    publicrepos = variables["GH_PUBLIC_REPOS_URL"]
    print(f"{user         = }")
    print(f"{token        = }")
    print(f"{api          = }")
    print(f"{privaterepos = }")
    print(f"{publicrepos  = }")
except KeyError as ke:
    raise SystemExit(f"FATAL| missing variable {ke}")
