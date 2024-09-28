from src.hh_ru_api import HH_API
from unittest.mock import patch


@patch("requests.get")
def test_head_hunter_api_requests(test_requests_api):

    obj_api = HH_API()
    assert type(obj_api) is HH_API