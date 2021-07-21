import json

from helpers.exports import parse_exports
from helpers import api

try:
    # variables = parse_exports("data/github_export")
    # print(json.dumps(variables, indent=4))
    gh = api.GithubApi.from_export("data/github_export")
except KeyError as ke:
    raise SystemExit(f"FATAL| {ke}")

data = gh.get_repos(visibility=api.REPOS_PUBLIC, print_url=True)
# print(f"{len(data)}")
#
# for d in data:
#     for k in d.keys():
#         print(k, d[k], type(d[k]))
count = 0
for d in data:
    print("private" if d["private"] else "public", d["clone_url"])
    count += 1
print(f"total: {count}")
