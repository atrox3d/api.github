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
        # self.response = None

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

    def api_call(self, url, params=None, headers=None, auth=None):
        # kwargs = (lambda **kargs: kargs)(headers=headers, auth=auth)
        auth = auth or (self.user, self.token)
        kwargs = {name: value for name, value in locals().items() if name not in ["self", "url"] and value}
        # response = requests.get(
        #     url,
        #     auth=(self.user, self.token),
        #     params=params,
        #     headers=headers
        # )
        response = requests.get(
            url,
            **kwargs
        )
        response.raise_for_status()
        self.response = response
        return response

    def get_repos(self, visibility=REPOS_ALL, per_page=100):
        _json = []
        nextpage = 1
        while nextpage:
            params = dict(visibility=visibility, per_page=per_page, page=nextpage)
            if visibility == REPOS_PUBLIC:
                response = self.api_call(self.public_repos, params=params)
            else:
                response = self.api_call(self.private_repos, params=params)
            _json.extend(response.json())
            nextpage = self.nextpage(response)
        return _json

    @staticmethod
    def nextpage(response):
        try:
            link = response.headers["link"]
            regex = "([0-9]+)>; rel=\"next\""
            search = re.search(regex, link)
            # print(f"{link=}")
            # print(f"{regex=}")
            # print(f"{search=}")
            # print(f"{search.groups()=}")
            page, = search.groups()
            # print(f"nextpage: {page}")
            # exit()
            return int(page)
        except (KeyError, AttributeError):
            # print(f"nextpage: {False}")
            return False

    @staticmethod
    def get_totalpages(response):
        try:
            link = response.headers["link"]
            regex = "([0-9]+)>; rel=\"last\""
            search = re.search(regex, link)
            pages, = search.groups()
            return int(pages)
        except KeyError:
            return 1
