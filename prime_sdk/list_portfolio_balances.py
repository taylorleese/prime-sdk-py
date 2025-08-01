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
from prime_sdk.base_response import BaseResponse
from prime_sdk.client import Client
from prime_sdk.credentials import Credentials
from prime_sdk.enums import BalanceType
from prime_sdk.utils import PaginationParams, append_query_param, append_pagination_params
from prime_sdk.model import Balance, BalanceWithHolds
from dataclasses import asdict
import dataclasses
import json


@dataclass
class ListPortfolioBalancesRequest:
    portfolio_id: str
    symbols: Optional[str] = None
    balance_type: Optional[BalanceType] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListPortfolioBalancesResponse(BaseResponse):
    balances: List[Balance] = None
    type: str = None
    trading_balances: BalanceWithHolds = None
    vault_balances: BalanceWithHolds = None
    prime_custody_balances: BalanceWithHolds = None


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_portfolio_balances(self, request: ListPortfolioBalancesRequest) -> ListPortfolioBalancesResponse:
        path = f"/portfolios/{request.portfolio_id}/balances"

        query_params = append_query_param("", 'symbols', request.symbols)
        query_params = append_query_param(query_params, 'balance_type', request.balance_type)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListPortfolioBalancesResponse(**response.json())