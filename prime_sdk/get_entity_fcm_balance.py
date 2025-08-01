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
from typing import List, Optional
from prime_sdk.credentials import Credentials


@dataclass
class GetEntityFcmBalanceRequest:
    entity_id: str
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class GetEntityFcmBalanceResponse(BaseResponse):
    portfolio_id: str = None
    cfm_usd_balance: str = None
    unrealized_pnl: str = None
    daily_realized_pnl: str = None
    excess_liquidity: str = None
    futures_buying_power: str = None
    initial_margin: str = None
    maintenance_margin: str = None
    clearing_account_id: str = None    


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)
        
    def get_entity_fcm_balance(self, request: GetEntityFcmBalanceRequest) -> GetEntityFcmBalanceResponse:
        path = f"/entities/{request.entity_id}/futures/balance_summary"
        response = self.client.request("GET", path, allowed_status_codes=request.allowed_status_codes)
        return GetEntityFcmBalanceResponse(**response.json())
