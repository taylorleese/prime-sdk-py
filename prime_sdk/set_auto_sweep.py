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

from dataclasses import dataclass, asdict

from prime_sdk.base_response import BaseResponse
from prime_sdk.client import Client
from typing import List, Optional
from prime_sdk.credentials import Credentials


@dataclass
class SetAutoSweepRequest:
    entity_id: str
    auto_sweep: bool
    allowed_status_codes: Optional[List[int]] = None


@dataclass
class SetAutoSweepResponse(BaseResponse):
    success: bool = None


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)
        
    def set_auto_sweep(self, request: SetAutoSweepRequest) -> SetAutoSweepResponse:
        path = f"/entities/{request.entity_id}/futures/auto_sweep"
        body = {k: v for k, v in asdict(request).items() if v is not None}
        response = self.client.request("POST", path, body=body, allowed_status_codes=request.allowed_status_codes)
        return SetAutoSweepResponse(**response.json())
