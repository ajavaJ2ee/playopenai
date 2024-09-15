import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def exception_handler (function):
    def exception_raised(*args, **kwargs):
        try:
            global okta_token_elevate
            global session
            global ELEVATE_BASE_URL
            session = requests.Session()


            retries = Retry(total=1, allowed_methods=['GET','POST','PUT'],backoff_factor=0, status_forcelist=500)
            session.mount (ELEVATE_BASE_URL, HTTPAdapter (max_retries=retries))
            response = function(*args, **kwargs)
            return response
        except Exception as EX:
            raise EX
    return exception_raised
