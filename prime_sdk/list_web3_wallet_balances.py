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
from prime_sdk.utils import PaginationParams, append_query_param, append_pagination_params, Pagination
from prime_sdk.model import OnchainBalance, DefiBalances

@dataclass
class ListWeb3WalletBalancesRequest:
    portfolio_id: str
    wallet_id: str
    visibility_statuses: Optional[str] = None
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListWeb3WalletBalancesResponse(BaseResponse):
    balances: List[OnchainBalance] = None
    pagination: Pagination = None
    defi_balances: List[DefiBalances] = None


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_web3_wallet_balances(self, request: ListWeb3WalletBalancesRequest) -> ListWeb3WalletBalancesResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/web3_balances"

        query_params = append_query_param("", 'visibility_statuses', request.visibility_statuses)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListWeb3WalletBalancesResponse(**response.json())
