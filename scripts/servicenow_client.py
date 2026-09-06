"""Minimal ServiceNow REST client for MayaBank labs.
Never commit credentials. Production auth should be adapted to enterprise policy.
"""
from __future__ import annotations
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ServiceNowClient:
    def __init__(self) -> None:
        self.instance = os.environ["SN_INSTANCE"].rstrip("/")
        self.username = os.environ["SN_USERNAME"]
        self.password = os.environ["SN_PASSWORD"]
        self.verify = os.getenv("SN_VERIFY_TLS", "true").lower() == "true"

    def post(self, path: str, payload: dict, timeout: int = 30) -> dict:
        url = f"{self.instance}{path}"
        r = requests.post(
            url,
            json=payload,
            auth=(self.username, self.password),
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=timeout,
            verify=self.verify,
        )
        r.raise_for_status()
        return r.json()

    def get(self, path: str, params: dict | None = None, timeout: int = 30) -> dict:
        url = f"{self.instance}{path}"
        r = requests.get(url, params=params, auth=(self.username, self.password),
                         headers={"Accept": "application/json"}, timeout=timeout,
                         verify=self.verify)
        r.raise_for_status()
        return r.json()
