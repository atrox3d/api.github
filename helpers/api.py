import requests


def api_call(url, user, token, params=None, headers=None):
    response = requests.get(url, auth=(user, token), params=params, headers=headers)
    response.raise_for_status()
    # rheaders = response.headers
    # print(json.dumps(dict(rheaders), indent=4))
    # print(rheaders.get('link'))
    return response
