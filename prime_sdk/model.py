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
from typing import List
from prime_sdk.enums import NetworkType


@dataclass
class Address:
    name: str
    address: str
    chain_ids: List[str]


@dataclass
class AddressGroup:
    id: str
    name: str
    network_type: NetworkType
    addresses: List[Address]
    added_at: str


@dataclass
class Portfolio:
    id: str
    name: str
    entity_id: str
    organization_id: str
    entity_name: str


@dataclass
class PortfolioUser:
    id: str
    name: str
    email: str
    portfolio_id: str
    entity_id: str
    role: str


@dataclass
class User:
    id: str
    name: str
    email: str
    entity_id: str
    role: str


@dataclass
class Network:
    id: str
    type: str


@dataclass
class Blockchain:
    address: str
    account_identifier: str
    network: Network


@dataclass
class AssetNetwork:
    network: Network
    name: str
    max_decimals: str
    default: bool
    trading_supported: bool
    vault_supported: bool
    prime_custody_supported: bool
    destination_tag_required: bool
    network_link: str


@dataclass
class Asset:
    name: str
    symbol: str
    decimal_precision: str
    trading_supported: bool
    explorer_url: str
    networks: List[AssetNetwork]
  

@dataclass
class ConsensusMetadata:
    approval_deadline: str
    has_passed_consensus: bool


@dataclass
class TransactionsMetadata:
    consensus: ConsensusMetadata


@dataclass
class AccountMetadata:
    consensus: ConsensusMetadata


@dataclass
class UserAction:
    action: str
    user_id: str
    timestamp: str


@dataclass
class Activity:
    id: str
    reference_id: str
    category: str
    type: str
    secondary_type: str
    status: str
    created_by: str
    title: str
    description: str
    user_actions: List[UserAction]
    transactions_metadata: TransactionsMetadata = None
    account_metadata: AccountMetadata = None
    symbols: List[str] = None
    created_at: str = None
    updated_at: str = None
    hierarchy_type: str = None


@dataclass
class ActivityResponse:
    activity: Activity


@dataclass
class Add:
    id: str
    name: str
    avatar_url: str


@dataclass
class Address:
    id: str
    currency_symbol: str
    name: str
    address: str
    account_identifier: str
    account_identifier_name: str
    state: str
    explorer_link: str
    last_used_at: str
    added_at: str
    added_by: Add
    type: str
    counterparty_id: str


@dataclass
class Destination:
    leg_id: str
    portfolio_id: str
    allocation_base: str
    allocation_quote: str
    fees_allocated_leg: str


@dataclass
class Allocation:
    root_id: str
    reversal_id: str
    allocation_completed_at: str
    user_id: str
    product_id: str
    side: str
    avg_price: str
    base_quantity: str
    quote_value: str
    fees_allocated: str
    status: str
    source: str
    order_ids: List[str]
    destinations: List[Destination]
    netting_id: str


@dataclass
class Details:
    id: str
    symbol: str
    payment_method_type: str
    name: str
    account_number: str
    bank_code: str
    

@dataclass
class Position:
    product_id: str
    side: str
    number_of_contracts: str
    daily_realized_pnl: str
    unrealized_pnl: str
    current_price: str
    avg_entry_price: str
    expiration_time: str


@dataclass
class Order:
    id: str
    user_id: str
    portfolio_id: str
    product_id: str
    side: str
    client_order_id: str
    type: str
    base_quantity: str
    quote_value: str
    limit_price: str
    start_time: str
    expiry_time: str
    status: str
    time_in_force: str
    created_at: str
    filled_quantity: str
    filled_value: str
    average_filled_price: str
    commission: str
    exchange_fee: str
    historical_pov: str
    stop_price: str
    net_average_filled_price: str
    user_context: str
    client_product_id: str


@dataclass
class Commission:
    type: str
    rate: str
    trading_volume: str


@dataclass
class AmountDue:
    currency: str
    amount: str
    due_date: str

@dataclass
class PostTradeCredit:
    portfolio_id: str
    currency: str
    limit: str
    utilized: str
    available: str
    frozen: str
    frozen_reason: str
    amounts_due: List[AmountDue]
    enabled: str
    adjusted_credit_utilized: str
    adjusted_portfolio_equity: str


@dataclass
class TransferLocation:
    type: str
    value: str


@dataclass
class EstimatedNetworkFees:
    lower_bound: str
    upper_bound: str


@dataclass
class Collection:
    name: str


@dataclass
class Item:
    name: str


@dataclass
class AssetChange:
    type: str
    symbol: str
    amount: str
    collection: Collection
    item: Item


@dataclass
class MatchMetadata:
    reference_id: str
    settlement_date: str


@dataclass
class Web3TransactionMetadata:
    label: str
    confirmed_asset_changes: List[AssetChange]


@dataclass
class TransactionMetadata:
    match_metadata: MatchMetadata
    web3_transaction_metadata: Web3TransactionMetadata


@dataclass
class RiskAssessment:
    compliance_risk_detected: bool
    security_risk_detected: bool


@dataclass
class OnchainDetails:
    signed_transaction: str
    risk_assessment: RiskAssessment
    chain_id: str
    nonce: str
    replaced_transaction_id: str
    destination_address: str
    skip_broadcast: bool
    failure_reason: str
    signing_status: str


@dataclass
class Transaction:
    id: str
    wallet_id: str
    portfolio_id: str
    type: str
    status: str
    symbol: str
    created_at: str
    completed_at: str
    amount: str
    transfer_from: TransferLocation
    transfer_to: TransferLocation
    network_fees: str
    fees: str
    fee_symbol: str
    blockchain_ids: List[str]
    transaction_id: str
    destination_symbol: str
    estimated_network_fees: EstimatedNetworkFees
    network: str
    estimated_asset_changes: List[AssetChange]
    metadata: TransactionMetadata
    idempotency_key: str
    onchain_details: OnchainDetails
    network_info: Network


@dataclass
class Balance:
    symbol: str
    amount: str
    holds: str
    bonded_amount: str
    reserved_amount: str
    unbonding_amount: str
    unvested_amount: str
    pending_rewards_amount: str
    past_rewards_amount: str
    bondable_amount: str
    withdrawable_amount: str
    fiat_amount: str
    unbondable_amount: str


@dataclass
class CryptoInstructions:
    id: str
    name: str
    type: str
    address: str
    account_identifier: str
    account_identifier_name: str
    network: Network


@dataclass
class FiatInstructions:
    id: str
    name: str
    type: str
    account_number: str
    routing_number: str
    reference_code: str


@dataclass
class Instructions:
    crypto_instructions: CryptoInstructions
    fiat_instructions: FiatInstructions


@dataclass
class Wallet:
    id: str
    name: str
    symbol: str
    type: str
    created_at: str
    address: str
    visibility: str
    network: Network


@dataclass
class RequestedAmount:
    currency: str
    amount: str


@dataclass
class Sweeps:
    id: str
    requested_amount: RequestedAmount
    should_sweep_all: bool
    status: str
    scheduled_time: str


@dataclass
class InvoiceItem:
    description: str
    currency_symbol: str
    invoice_type: str
    rate: float
    quantity: float
    price: float
    average_auc: float
    total: float


@dataclass
class Invoices:
    id: str
    billing_month: int
    billing_year: int
    due_date: str
    invoice_number: str
    state: str
    usd_amount_paid: float
    usd_amount_owed: float
    invoice_items: List[InvoiceItem]


@dataclass
class Fill:
    id: str
    order_id: str
    product_id: str
    client_product_id: str
    side: str
    filled_quantity: str
    filled_value: str
    price: str
    time: str
    commission: str
    venue: str


@dataclass
class BalanceWithHolds:
    total: str
    holds: str


@dataclass
class RfqProductDetails:
    tradable: bool
    min_notional_size: str
    max_notional_size: str


@dataclass
class Product:
    id: str
    base_increment: str
    quote_increment: str
    base_min_size: str
    quote_min_size: str
    base_max_size: str
    quote_max_size: str
    permissions: List[str]
    price_increment: str
    rfq_product_details: RfqProductDetails


@dataclass
class DefiBalances:
    network: str
    protocol: str
    net_usd_value: str


@dataclass
class OnchainBalance:
    asset: Asset
    amount: str
    visibility_status: str


@dataclass
class MarketRate:
    symbol: str
    rate: str


@dataclass
class AssetBalance:
    portfolio_id: str
    symbol: str
    amount: str
    notional_amount: str
    conversion_rate: str


@dataclass
class TfLoan:
    portfolio_id: str
    symbol: str
    amount: str
    notional_amount: str
    due_date: str


@dataclass
class PmLoan:
    portfolio_id: str
    symbol: str
    amount: str
    notional_amount: str
    due_date: str


@dataclass
class ShortCollateral:
    portfolio_id: str
    symbol: str
    amount: str
    notional_amount: str
    due_date: str


@dataclass
class PortfolioStressTriggered:
    amount: str
    add_on_type: str


@dataclass
class PmAssetInfo:
    symbol: str
    amount: str
    price: str
    notional_amount: str
    asset_tier: str
    margin_eligible: bool
    base_margin_requirement: str
    base_margin_requirement_notional: str
    adv_30d: str
    hist_5d_vol: str
    hist_30d_vol: str
    hist_90d_vol: str
    volatility_addon: str
    liquidity_addon: str
    total_position_margin: str
    short_nominal: str
    long_nominal: str


@dataclass
class MarginSummary:
    entity_id: str
    margin_equity: str
    margin_requirement: str
    excess_deficit: str
    pm_credit_consumed: str
    tf_credit_limit: str
    tf_credit_consumed: str
    tf_adjusted_asset_value: str
    tf_adjusted_liability_value: str
    tf_adjusted_credit_consumed: str
    tf_adjusted_equity: str
    frozen: bool
    frozen_reason: str
    tf_enabled: bool
    pm_enabled: bool
    market_rates: List[MarketRate]
    asset_balances: List[AssetBalance]
    tf_loans: List[TfLoan]
    pm_loans: List[PmLoan]
    short_collateral: List[ShortCollateral]
    gross_market_value: str
    net_market_value: str
    long_market_value: str
    non_marginable_long_market_value: str
    short_market_value: str
    gross_leverage: str
    net_exposure: str
    portfolio_stress_triggered: PortfolioStressTriggered
    pm_asset_info: List[PmAssetInfo]
    pm_credit_limit: str
    pm_margin_limit: str
    pm_margin_consumed: str


@dataclass
class MarginCall:
    id: str
    initial_notional_amount: str
    outstanding_notional_amount: str
    created_at: str
    due_at: str


@dataclass
class WithdrawalPower:
    symbol: str
    amount: str


@dataclass
class BuyingPower:
    portfolio_id: str
    base_currency: str
    quote_currency: str
    base_buying_power: str
    quote_buying_power: str


@dataclass
class ConversionDetail:
    symbol: str
    tf_balance: str
    notional_tf_balance: str
    converted_balance: str
    notional_converted_balance: str
    interest_rate: str
    conversion_rate: str


@dataclass
class ShortCollateral:
    old_balance: str
    new_balance: str
    loan_interest_rate: str
    collateral_interest_rate: str


@dataclass
class Conversion:
    conversion_details: List[ConversionDetail]
    short_collateral: ShortCollateral
    conversion_datetime: str
    portfolio_id: str


@dataclass
class Accrual:
    accrual_id: str
    date: str
    portfolio_id: str
    symbol: str
    loan_type: str
    interest_rate: str
    nominal_accrual: str
    notional_accrual: str
    conversion_rate: str
    loan_amount: str
    benchmark: str
    benchmark_rate: str
    spread: str
    rate_type: str
    loan_amount_notional: str
    nominal_open_borrow_sod: str
    notional_open_bnorrow_sod: str


@dataclass
class Reference:
    id: str
    type: str


@dataclass
class Position:
    symbol: str
    long: str
    short: str
    reference: Reference


@dataclass
class MarginSummaryRecord:
    conversion_datetime: str
    conversion_date: str
    margin_summary: MarginSummary


@dataclass
class Balance:
    symbol: str
    long_amount: str
    long_notional: str
    short_amount: str
    short_notional: str


@dataclass
class LocateAvailability:
    symbol: str
    quantity: str
    rate: str


@dataclass
class Locate:
    locate_id: str
    entity_id: str
    portfolio_id: str
    symbol: str
    requested_amount: str
    interest_rate: str
    status: str
    approved_amount: str
    conversion_date: str
    created_at: str
    locate_date: str


@dataclass
class MarginCallRecord:
    margin_call_id: str
    initial_notional_amount: str
    outstanding_notional_amount: str
    created_at: str
    due_at: str


@dataclass
class MarginInformation:
    margin_call_records: List[MarginCallRecord]
    margin_summary: MarginSummary


@dataclass
class AmountDue:
    currency: str
    amount: str
    due_date: str


@dataclass
class PostTradeCredit:
    portfolio_id: str
    currency: str
    limit: str
    utilized: str
    available: str
    frozen: bool
    frozen_reason: str
    amounts_due: List[AmountDue]
    enabled: bool
    adjusted_credit_utilized: str
    adjusted_portfolio_equity: str


@dataclass
class Fee:
    symbol: str
    fee: str
