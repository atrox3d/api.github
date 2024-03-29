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

VISIBILITY = api.REPOS_ALL
if params.private:
    VISIBILITY = api.REPOS_PRIVATE
elif params.public:
    VISIBILITY = api.REPOS_PUBLIC

PRINT_URL = params.printurl

data = gh.get_repos(visibility=VISIBILITY, print_url=PRINT_URL)
# print(f"{len(data)}")
#
# for d in data:
#     for k in d.keys():
#         print(k, d[k], type(d[k]))
if params.filter:
    data = [item[params.field] for item in data if params.filter.lower() in item[params.field].lower()]
else:
    data = [item[params.field] for item in data]

count = 0
for d in data:
    # print("private" if d["private"] else "public", d["clone_url"])
    print(d)
    count += 1

if params.count:
    print(f"total: {count}")
