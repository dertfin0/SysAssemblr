def check() -> bool:
    from requests import get
    try:
        req = get("https://www.google.com/")
        return req.status_code == 200
    except ConnectionError:
        return False