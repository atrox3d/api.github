import requests
import re

from helpers.exports import parse_exports

REPOS_PRIVATE = "private"
REPOS_PUBLIC = "public"
REPOS_ALL = "all"

TEMPLATE_PUBLIC_REPOS_URL = "{api}/users/{user}/repos"
TEMPLATE_PRIVATE_REPOS_URL = "{api}/user/repos"


class GithubApi:

    def __init__(self, user, token, api, public_repos=None, private_repos=None):
        self.user = user
        self.token = token
        self.api = api
        self.public_repos = public_repos or TEMPLATE_PUBLIC_REPOS_URL.format(api=api, user=user)
        self.private_repos = private_repos or TEMPLATE_PRIVATE_REPOS_URL.format(api=api)
        self.response = None

    @classmethod
    def from_export(cls, export_path):
        try:
            variables = parse_exports(export_path)
            user = variables.user
            token = variables.token
            api = variables.api
            public_repos = variables.public_repos
            private_repos = variables.private_repos
            # response = None
            return cls(user, token, api, public_repos, private_repos)
        except KeyError as ke:
            raise SystemExit(f"FATAL| {ke}")

    def api_call(self, url, params=None, headers=None):
        response = requests.get(
            url,
            auth=(self.user, self.token),
            params=params,
            headers=headers
        )
        response.raise_for_status()
        self.response = response
        return response

    def get_repos(self, visibility=REPOS_ALL):
        pass

    @staticmethod
    def get_totalpages(response):
        link = response.headers["link"]
        regex = "([0-9]+)>; rel=\"last\""
        search = re.search(regex, link)
        pages, = search.groups()
        return int(pages)
