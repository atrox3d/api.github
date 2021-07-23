import json

from helpers.exports import parse_exports
from helpers import api
from helpers import options

DEFAULT_EXPORTFILE = "data/github_export"


params = options.parse_arguments()

if params.templateurlpublic:
    api.TEMPLATE_PRIVATE_REPOS_URL = params.templateurlpublic
if params.templateurlprivate:
    api.TEMPLATE_PRIVATE_REPOS_URL = params.templateurlprivate

if params.exportfile:
    """precedence over all params"""
    try:
        gh = api.GithubApi.from_export(params.exportfile)
    except KeyError as ke:
        raise SystemExit(f"FATAL| {ke}")
elif all((params.user, params.token)):
    """only if we have minimal params"""
    gh = api.GithubApi(
        params.user,
        params.token,
        params.urlapi,
    )
else:
    """fallback to default exporfile"""
    try:
        gh = api.GithubApi.from_export(DEFAULT_EXPORTFILE)
    except KeyError as ke:
        raise SystemExit(f"FATAL| {ke}")
    """and override"""
    gh.update(
        params.user or gh.user,
        params.token or gh.token,
        params.urlapi or gh.urlapi
    )

VISIBILITY = params.visibility or api.REPOS_ALL
PRINT_URL = params.print_url or True

data = gh.get_repos(visibility=VISIBILITY, print_url=PRINT_URL)
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
