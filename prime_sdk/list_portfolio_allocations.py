# Copyright 2024-present Coinbase Global, Inc.
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
from datetime import datetime
from prime_sdk.base_response import BaseResponse
from prime_sdk.enums import OrderSide
from prime_sdk.client import Client
from prime_sdk.credentials import Credentials
from prime_sdk.utils import PaginationParams, append_query_param, append_pagination_params, Pagination
from prime_sdk.model import Allocation


@dataclass
class ListPortfolioAllocationsRequest:
    portfolio_id: str
    start_date: datetime
    product_ids: Optional[str] = None
    order_side: Optional[OrderSide] = None
    end_date: Optional[datetime] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListPortfolioAllocationsResponse(BaseResponse):
    allocations: List[Allocation] = None
    pagination: Pagination = None


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_portfolio_allocations(self, request: ListPortfolioAllocationsRequest) -> ListPortfolioAllocationsResponse:
        path = f"/portfolios/{request.portfolio_id}/allocations"

        query_params = append_query_param("", 'product_ids', request.product_ids)
        query_params = append_query_param(query_params, 'order_side', request.order_side)

        if request.start_date:
            query_params = append_query_param(query_params, 'start_date', request.start_date.isoformat() + 'Z')
        if request.end_date:
            query_params = append_query_param(query_params, 'end_date', request.end_date.isoformat() + 'Z')

        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioAllocationsResponse(**response.json())
