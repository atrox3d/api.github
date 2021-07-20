def parse_exports(filepath):
    """
        parse a text file containing at least 3 exports or key=value pairs

        - *URL*=value
        - *USER*=value
        - *TOKEN*=value
    """
    url = user = token = None
    with open(filepath) as gh:
        for line in gh:
            line = line.strip()
            if "URL" in line.upper():
                varname, url = line.split('=')
            if "USER" in line.upper():
                varname, user = line.split('=')
            if "TOKEN" in line.upper():
                varname, token = line.split('=')
    if not all((url, user, token)):
        raise ValueError("exports file must contain *URL*, *USER*, *TOKEN* variables")
    return url, user, token
