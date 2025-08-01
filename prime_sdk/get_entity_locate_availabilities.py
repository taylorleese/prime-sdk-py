# Copyright 2025-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from typing import Optional, List
from prime_sdk.base_response import BaseResponse
from prime_sdk.client import Client
from prime_sdk.credentials import Credentials
from prime_sdk.model import LocateAvailability
from prime_sdk.utils import append_query_param


@dataclass
class GetEntityLocateAvailabilitiesRequest:
    entity_id: str
    locate_date: Optional[str] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetEntityLocateAvailabilitiesResponse(BaseResponse):
    locates: List[LocateAvailability] = None


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def get_entity_locate_availabilities(self, request: GetEntityLocateAvailabilitiesRequest) -> GetEntityLocateAvailabilitiesResponse:
        path = f"/entities/{request.entity_id}/locates_availability"
        query_params = append_query_param("", "locate_date", request.locate_date)
        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return GetEntityLocateAvailabilitiesResponse(**response.json())
