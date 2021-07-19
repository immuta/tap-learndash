"""REST client handling, including LearnDashStream base class."""

import base64
import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.streams import RESTStream

#SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class LearnDashStream(RESTStream):
    """LearnDash stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"] + "/wp-json/ldlms/v2"

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")

        # Authentication
        raw_credentials = f"{self.config['username']}:{self.config['password']}"
        auth_token = base64.b64encode(raw_credentials.encode()).decode("ascii")
        headers["Authorization"] = f"Basic {auth_token}"

        return headers

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        resp_json = response.json()
        for row in resp_json:
            yield row
