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
from prime_sdk.base_response import BaseResponse
from prime_sdk.client import Client
from typing import Optional, List
from datetime import datetime
from prime_sdk.credentials import Credentials
from prime_sdk.utils import PaginationParams, append_query_param, append_pagination_params, Pagination
from prime_sdk.enums import ActivityLevel
from prime_sdk.model import Activity


@dataclass
class ListEntityActivitiesRequest:
    entity_id: str
    activity_level: Optional[ActivityLevel] = None
    symbols: Optional[str] = None
    categories: Optional[str] = None
    statuses: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListEntityActivitiesResponse(BaseResponse):
    activities: List[Activity] = None
    pagination: Pagination = None


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_entity_activities(self, request: ListEntityActivitiesRequest) -> ListEntityActivitiesResponse:
        path = f"/entities/{request.entity_id}/activities"

        query_params = append_query_param("", 'activity_level', request.symbols)
        query_params = append_query_param(query_params, 'symbols', request.symbols)
        query_params = append_query_param(query_params, 'categories', request.categories)
        query_params = append_query_param(query_params, 'statuses', request.statuses)

        if request.start_time:
            query_params = append_query_param(
                query_params,
                'start_time',
                request.start_time.isoformat() + 'Z')
        if request.end_time:
            query_params = append_query_param(
                query_params,
                'end_time',
                request.end_time.isoformat() + 'Z')

        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListEntityActivitiesResponse(**response.json())
