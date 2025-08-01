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
from prime_sdk.credentials import Credentials
from prime_sdk.utils import PaginationParams, append_query_param, append_pagination_params, Pagination
from prime_sdk.model import BlockchainAddress


@dataclass
class ListWalletAddressesRequest:
    portfolio_id: str
    wallet_id: str
    network_id: str
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class ListWalletAddressesResponse(BaseResponse):
    addresses: List[BlockchainAddress] = None
    pagination: Pagination = None


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_wallet_addresses(self, request: ListWalletAddressesRequest) -> ListWalletAddressesResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/addresses"

        query_params = append_query_param("", 'network_id', request.network_id)
        query_params = append_pagination_params(query_params, request.pagination)

        response = self.client.request("GET", path, query=query_params, allowed_status_codes=request.allowed_status_codes)
        return ListWalletAddressesResponse(**response.json())
