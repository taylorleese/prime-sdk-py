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

"""
Unified Prime SDK Client

This module provides a unified interface to the Coinbase Prime SDK,
consolidating all the individual client imports into a single class.

The Prime SDK requires importing individual client classes from each module,
which results in 70+ imports and naming conflicts since each module exports
a class named "PrimeClient".

This wrapper simplifies usage:
    from prime_sdk.prime_client import PrimeClient
    from prime_sdk.credentials import Credentials
    from prime_sdk.list_portfolios import ListPortfoliosRequest

    client = PrimeClient(credentials)
    portfolios = client.list_portfolios(ListPortfoliosRequest())
"""

from prime_sdk.credentials import Credentials

# Import all request and response types
from prime_sdk.accept_quote import AcceptQuoteRequest, AcceptQuoteResponse
from prime_sdk.cancel_entity_futures_sweep import CancelEntityFuturesSweepRequest, CancelEntityFuturesSweepResponse
from prime_sdk.cancel_order import CancelOrderRequest, CancelOrderResponse
from prime_sdk.create_address_book_entry import CreateAddressBookEntryRequest, CreateAddressBookEntryResponse
from prime_sdk.create_conversion import CreateConversionRequest, CreateConversionResponse
from prime_sdk.create_new_locates import CreateNewLocateRequest, CreateNewLocateResponse
from prime_sdk.create_onchain_address_book_entry import CreateOnchainAddressBookEntryRequest, CreateOnchainAddressBookEntryResponse
from prime_sdk.create_onchain_transaction import CreateOnchainTransactionRequest, CreateOnchainTransactionResponse
from prime_sdk.create_order import CreateOrderRequest, CreateOrderResponse
from prime_sdk.create_order_preview import CreateOrderPreviewRequest, CreateOrderPreviewResponse
from prime_sdk.create_portfolio_allocations import CreatePortfolioAllocationsRequest, CreatePortfolioAllocationsResponse
from prime_sdk.create_portfolio_net_allocations import CreatePortfolioNetAllocationsRequest, CreatePortfolioNetAllocationsResponse
from prime_sdk.create_quote import CreateQuoteRequest, CreateQuoteResponse
from prime_sdk.create_stake import CreateStakeRequest, CreateStakeResponse
from prime_sdk.create_transfer import CreateTransferRequest, CreateTransferResponse
from prime_sdk.create_unstake import CreateUnstakeRequest, CreateUnstakeResponse
from prime_sdk.create_wallet import CreateWalletRequest, CreateWalletResponse
from prime_sdk.create_wallet_address import CreateWalletAddressRequest, CreateWalletAddressResponse
from prime_sdk.create_withdrawal import CreateWithdrawalRequest, CreateWithdrawalResponse
from prime_sdk.delete_onchain_address_group import DeleteOnchainAddressGroupRequest, DeleteOnchainAddressGroupResponse
from prime_sdk.get_activity import GetActivityRequest, GetActivityResponse
from prime_sdk.get_address_book import GetAddressBookRequest, GetAddressBookResponse
from prime_sdk.get_allocation_by_id import GetAllocationByIdRequest, GetAllocationByIdResponse
from prime_sdk.get_entity_activity import GetEntityActivityRequest, GetEntityActivityResponse
from prime_sdk.get_entity_fcm_balance import GetEntityFcmBalanceRequest, GetEntityFcmBalanceResponse
from prime_sdk.get_entity_locate_availabilities import GetEntityLocateAvailabilitiesRequest, GetEntityLocateAvailabilitiesResponse
from prime_sdk.get_entity_payment_method import GetEntityPaymentMethodRequest, GetEntityPaymentMethodResponse
from prime_sdk.get_entity_positions import GetEntityPositionsRequest, GetEntityPositionsResponse
from prime_sdk.get_margin_information import GetMarginInformationRequest, GetMarginInformationResponse
from prime_sdk.get_net_allocations_by_netting_id import GetNetAllocationsByNettingIdRequest, GetNetAllocationsByNettingIdResponse
from prime_sdk.get_order import GetOrderRequest, GetOrderResponse
from prime_sdk.get_portfolio import GetPortfolioRequest, GetPortfolioResponse
from prime_sdk.get_portfolio_buying_power import GetBuyingPowerRequest, GetBuyingPowerResponse
from prime_sdk.get_portfolio_commission import GetPortfolioCommissionRequest, GetPortfolioCommissionResponse
from prime_sdk.get_portfolio_credit_information import GetPortfolioCreditInformationRequest, GetPortfolioCreditInformationResponse
from prime_sdk.get_portfolio_withdrawal_power import GetPortfolioWithdrawalPowerRequest, GetPortfolioWithdrawalPowerResponse
from prime_sdk.get_trade_finance_tiered_pricing_fees import GetTradeFinanceTieredPricingFeesRequest, GetTradeFinanceTieredPricingFeesResponse
from prime_sdk.get_transaction import GetTransactionRequest, GetTransactionResponse
from prime_sdk.get_wallet import GetWalletRequest, GetWalletResponse
from prime_sdk.get_wallet_balance import GetWalletBalanceRequest, GetWalletBalanceResponse
from prime_sdk.get_wallet_deposit_instructions import GetWalletDepositInstructionsRequest, GetWalletDepositInstructionsResponse
from prime_sdk.list_activities import ListActivitiesRequest, ListActivitiesResponse
from prime_sdk.list_aggregate_entity_positions import ListAggregateEntityPositionsRequest, ListAggregateEntityPositionsResponse
from prime_sdk.list_assets import ListAssetsRequest, ListAssetsResponse
from prime_sdk.list_entity_activities import ListEntityActivitiesRequest, ListEntityActivitiesResponse
from prime_sdk.list_entity_balances import ListEntityBalancesRequest, ListEntityBalancesResponse
from prime_sdk.list_entity_futures_sweeps import ListEntityFuturesSweepsRequest, ListEntityFuturesSweepsResponse
from prime_sdk.list_entity_payment_methods import ListEntityPaymentMethodsRequest, ListEntityPaymentMethodsResponse
from prime_sdk.list_entity_positions import ListEntityPositionsRequest, ListEntityPositionsResponse
from prime_sdk.list_existing_locates import ListExistingLocatesRequest, ListExistingLocatesResponse
from prime_sdk.list_interest_accruals import ListInterestAccrualsRequest, ListInterestAccrualsResponse
from prime_sdk.list_interest_accruals_for_portfolio import ListInterestAccrualsForPortfolioRequest, ListInterestAccrualsForPortfolioResponse
from prime_sdk.list_invoices import ListInvoicesRequest, ListInvoicesResponse
from prime_sdk.list_margin_call_summaries import ListMarginCallSummariesRequest, ListMarginCallSummariesResponse
from prime_sdk.list_margin_conversions import ListMarginConversionsRequest, ListMarginConversionsResponse
from prime_sdk.list_onchain_address_groups import ListOnchainAddressGroupsRequest, ListOnchainAddressGroupsResponse
from prime_sdk.list_open_orders import ListOpenOrdersRequest, ListOpenOrdersResponse
from prime_sdk.list_order_fills import ListOrderFillsRequest, ListOrderFillsResponse
from prime_sdk.list_orders import ListOrdersRequest, ListOrdersResponse
from prime_sdk.list_portfolio_allocations import ListPortfolioAllocationsRequest, ListPortfolioAllocationsResponse
from prime_sdk.list_portfolio_balances import ListPortfolioBalancesRequest, ListPortfolioBalancesResponse
from prime_sdk.list_portfolio_fills import ListPortfolioFillsRequest, ListPortfolioFillsResponse
from prime_sdk.list_portfolio_transactions import ListPortfolioTransactionsRequest, ListPortfolioTransactionsResponse
from prime_sdk.list_portfolio_users import ListPortfolioUsersRequest, ListPortfolioUsersResponse
from prime_sdk.list_portfolios import ListPortfoliosRequest, ListPortfoliosResponse
from prime_sdk.list_products import ListProductsRequest, ListProductsResponse
from prime_sdk.list_users import ListUsersRequest, ListUsersResponse
from prime_sdk.list_wallet_addresses import ListWalletAddressesRequest, ListWalletAddressesResponse
from prime_sdk.list_wallet_transactions import ListWalletTransactionsRequest, ListWalletTransactionsResponse
from prime_sdk.list_wallets import ListWalletsRequest, ListWalletsResponse
from prime_sdk.list_web3_wallet_balances import ListWeb3WalletBalancesRequest, ListWeb3WalletBalancesResponse
from prime_sdk.schedule_entity_futures_sweep import ScheduleEntityFuturesSweepRequest, ScheduleEntityFuturesSweepResponse
from prime_sdk.set_auto_sweep import SetAutoSweepRequest, SetAutoSweepResponse
from prime_sdk.update_onchain_address_book import UpdateOnchainAddressBookRequest, UpdateOnchainAddressBookResponse

# Import all individual clients with aliases
from prime_sdk.accept_quote import PrimeClient as AcceptQuoteClient
from prime_sdk.cancel_entity_futures_sweep import PrimeClient as CancelEntityFuturesSweepClient
from prime_sdk.cancel_order import PrimeClient as CancelOrderClient
from prime_sdk.create_address_book_entry import PrimeClient as CreateAddressBookEntryClient
from prime_sdk.create_conversion import PrimeClient as CreateConversionClient
from prime_sdk.create_new_locates import PrimeClient as CreateNewLocatesClient
from prime_sdk.create_onchain_address_book_entry import PrimeClient as CreateOnchainAddressBookEntryClient
from prime_sdk.create_onchain_transaction import PrimeClient as CreateOnchainTransactionClient
from prime_sdk.create_order import PrimeClient as CreateOrderClient
from prime_sdk.create_order_preview import PrimeClient as CreateOrderPreviewClient
from prime_sdk.create_portfolio_allocations import PrimeClient as CreatePortfolioAllocationsClient
from prime_sdk.create_portfolio_net_allocations import PrimeClient as CreatePortfolioNetAllocationsClient
from prime_sdk.create_quote import PrimeClient as CreateQuoteClient
from prime_sdk.create_stake import PrimeClient as CreateStakeClient
from prime_sdk.create_transfer import PrimeClient as CreateTransferClient
from prime_sdk.create_unstake import PrimeClient as CreateUnstakeClient
from prime_sdk.create_wallet import PrimeClient as CreateWalletClient
from prime_sdk.create_wallet_address import PrimeClient as CreateWalletAddressClient
from prime_sdk.create_withdrawal import PrimeClient as CreateWithdrawalClient
from prime_sdk.delete_onchain_address_group import PrimeClient as DeleteOnchainAddressGroupClient
from prime_sdk.get_activity import PrimeClient as GetActivityClient
from prime_sdk.get_address_book import PrimeClient as GetAddressBookClient
from prime_sdk.get_allocation_by_id import PrimeClient as GetAllocationByIdClient
from prime_sdk.get_entity_activity import PrimeClient as GetEntityActivityClient
from prime_sdk.get_entity_fcm_balance import PrimeClient as GetEntityFcmBalanceClient
from prime_sdk.get_entity_locate_availabilities import PrimeClient as GetEntityLocateAvailabilitiesClient
from prime_sdk.get_entity_payment_method import PrimeClient as GetEntityPaymentMethodClient
from prime_sdk.get_entity_positions import PrimeClient as GetEntityPositionsClient
from prime_sdk.get_margin_information import PrimeClient as GetMarginInformationClient
from prime_sdk.get_net_allocations_by_netting_id import PrimeClient as GetNetAllocationsByNettingIdClient
from prime_sdk.get_order import PrimeClient as GetOrderClient
from prime_sdk.get_portfolio import PrimeClient as GetPortfolioClient
from prime_sdk.get_portfolio_buying_power import PrimeClient as GetPortfolioBuyingPowerClient
from prime_sdk.get_portfolio_commission import PrimeClient as GetPortfolioCommissionClient
from prime_sdk.get_portfolio_credit_information import PrimeClient as GetPortfolioCreditInformationClient
from prime_sdk.get_portfolio_withdrawal_power import PrimeClient as GetPortfolioWithdrawalPowerClient
from prime_sdk.get_trade_finance_tiered_pricing_fees import PrimeClient as GetTradeFinanceTieredPricingFeesClient
from prime_sdk.get_transaction import PrimeClient as GetTransactionClient
from prime_sdk.get_wallet import PrimeClient as GetWalletClient
from prime_sdk.get_wallet_balance import PrimeClient as GetWalletBalanceClient
from prime_sdk.get_wallet_deposit_instructions import PrimeClient as GetWalletDepositInstructionsClient
from prime_sdk.list_activities import PrimeClient as ListActivitiesClient
from prime_sdk.list_aggregate_entity_positions import PrimeClient as ListAggregateEntityPositionsClient
from prime_sdk.list_assets import PrimeClient as ListAssetsClient
from prime_sdk.list_entity_activities import PrimeClient as ListEntityActivitiesClient
from prime_sdk.list_entity_balances import PrimeClient as ListEntityBalancesClient
from prime_sdk.list_entity_futures_sweeps import PrimeClient as ListEntityFuturesSweepsClient
from prime_sdk.list_entity_payment_methods import PrimeClient as ListEntityPaymentMethodsClient
from prime_sdk.list_entity_positions import PrimeClient as ListEntityPositionsClient
from prime_sdk.list_existing_locates import PrimeClient as ListExistingLocatesClient
from prime_sdk.list_interest_accruals import PrimeClient as ListInterestAccrualsClient
from prime_sdk.list_interest_accruals_for_portfolio import PrimeClient as ListInterestAccrualsForPortfolioClient
from prime_sdk.list_invoices import PrimeClient as ListInvoicesClient
from prime_sdk.list_margin_call_summaries import PrimeClient as ListMarginCallSummariesClient
from prime_sdk.list_margin_conversions import PrimeClient as ListMarginConversionsClient
from prime_sdk.list_onchain_address_groups import PrimeClient as ListOnchainAddressGroupsClient
from prime_sdk.list_open_orders import PrimeClient as ListOpenOrdersClient
from prime_sdk.list_order_fills import PrimeClient as ListOrderFillsClient
from prime_sdk.list_orders import PrimeClient as ListOrdersClient
from prime_sdk.list_portfolio_allocations import PrimeClient as ListPortfolioAllocationsClient
from prime_sdk.list_portfolio_balances import PrimeClient as ListPortfolioBalancesClient
from prime_sdk.list_portfolio_fills import PrimeClient as ListPortfolioFillsClient
from prime_sdk.list_portfolio_transactions import PrimeClient as ListPortfolioTransactionsClient
from prime_sdk.list_portfolio_users import PrimeClient as ListPortfolioUsersClient
from prime_sdk.list_portfolios import PrimeClient as ListPortfoliosClient
from prime_sdk.list_products import PrimeClient as ListProductsClient
from prime_sdk.list_users import PrimeClient as ListUsersClient
from prime_sdk.list_wallet_addresses import PrimeClient as ListWalletAddressesClient
from prime_sdk.list_wallet_transactions import PrimeClient as ListWalletTransactionsClient
from prime_sdk.list_wallets import PrimeClient as ListWalletsClient
from prime_sdk.list_web3_wallet_balances import PrimeClient as ListWeb3WalletBalancesClient
from prime_sdk.schedule_entity_futures_sweep import PrimeClient as ScheduleEntityFuturesSweepClient
from prime_sdk.set_auto_sweep import PrimeClient as SetAutoSweepClient
from prime_sdk.update_onchain_address_book import PrimeClient as UpdateOnchainAddressBookClient


class PrimeClient:
    """
    Unified client for Coinbase Prime SDK operations.

    This class consolidates all individual PrimeClient imports into a single interface,
    avoiding the need to import from 70+ different modules.
    """

    def __init__(self, credentials: Credentials):
        """
        Initialize the unified Prime client with credentials.

        Args:
            credentials: Coinbase Prime API credentials
        """
        self.credentials = credentials
        
        # Initialize all client properties
        self._accept_quote = AcceptQuoteClient(credentials)
        self._cancel_entity_futures_sweep = CancelEntityFuturesSweepClient(credentials)
        self._cancel_order = CancelOrderClient(credentials)
        self._create_address_book_entry = CreateAddressBookEntryClient(credentials)
        self._create_conversion = CreateConversionClient(credentials)
        self._create_new_locates = CreateNewLocatesClient(credentials)
        self._create_onchain_address_book_entry = CreateOnchainAddressBookEntryClient(credentials)
        self._create_onchain_transaction = CreateOnchainTransactionClient(credentials)
        self._create_order = CreateOrderClient(credentials)
        self._create_order_preview = CreateOrderPreviewClient(credentials)
        self._create_portfolio_allocations = CreatePortfolioAllocationsClient(credentials)
        self._create_portfolio_net_allocations = CreatePortfolioNetAllocationsClient(credentials)
        self._create_quote = CreateQuoteClient(credentials)
        self._create_stake = CreateStakeClient(credentials)
        self._create_transfer = CreateTransferClient(credentials)
        self._create_unstake = CreateUnstakeClient(credentials)
        self._create_wallet = CreateWalletClient(credentials)
        self._create_wallet_address = CreateWalletAddressClient(credentials)
        self._create_withdrawal = CreateWithdrawalClient(credentials)
        self._delete_onchain_address_group = DeleteOnchainAddressGroupClient(credentials)
        self._get_activity = GetActivityClient(credentials)
        self._get_address_book = GetAddressBookClient(credentials)
        self._get_allocation_by_id = GetAllocationByIdClient(credentials)
        self._get_entity_activity = GetEntityActivityClient(credentials)
        self._get_entity_fcm_balance = GetEntityFcmBalanceClient(credentials)
        self._get_entity_locate_availabilities = GetEntityLocateAvailabilitiesClient(credentials)
        self._get_entity_payment_method = GetEntityPaymentMethodClient(credentials)
        self._get_entity_positions = GetEntityPositionsClient(credentials)
        self._get_margin_information = GetMarginInformationClient(credentials)
        self._get_net_allocations_by_netting_id = GetNetAllocationsByNettingIdClient(credentials)
        self._get_order = GetOrderClient(credentials)
        self._get_portfolio = GetPortfolioClient(credentials)
        self._get_portfolio_buying_power = GetPortfolioBuyingPowerClient(credentials)
        self._get_portfolio_commission = GetPortfolioCommissionClient(credentials)
        self._get_portfolio_credit_information = GetPortfolioCreditInformationClient(credentials)
        self._get_portfolio_withdrawal_power = GetPortfolioWithdrawalPowerClient(credentials)
        self._get_trade_finance_tiered_pricing_fees = GetTradeFinanceTieredPricingFeesClient(credentials)
        self._get_transaction = GetTransactionClient(credentials)
        self._get_wallet = GetWalletClient(credentials)
        self._get_wallet_balance = GetWalletBalanceClient(credentials)
        self._get_wallet_deposit_instructions = GetWalletDepositInstructionsClient(credentials)
        self._list_activities = ListActivitiesClient(credentials)
        self._list_aggregate_entity_positions = ListAggregateEntityPositionsClient(credentials)
        self._list_assets = ListAssetsClient(credentials)
        self._list_entity_activities = ListEntityActivitiesClient(credentials)
        self._list_entity_balances = ListEntityBalancesClient(credentials)
        self._list_entity_futures_sweeps = ListEntityFuturesSweepsClient(credentials)
        self._list_entity_payment_methods = ListEntityPaymentMethodsClient(credentials)
        self._list_entity_positions = ListEntityPositionsClient(credentials)
        self._list_existing_locates = ListExistingLocatesClient(credentials)
        self._list_interest_accruals = ListInterestAccrualsClient(credentials)
        self._list_interest_accruals_for_portfolio = ListInterestAccrualsForPortfolioClient(credentials)
        self._list_invoices = ListInvoicesClient(credentials)
        self._list_margin_call_summaries = ListMarginCallSummariesClient(credentials)
        self._list_margin_conversions = ListMarginConversionsClient(credentials)
        self._list_onchain_address_groups = ListOnchainAddressGroupsClient(credentials)
        self._list_open_orders = ListOpenOrdersClient(credentials)
        self._list_order_fills = ListOrderFillsClient(credentials)
        self._list_orders = ListOrdersClient(credentials)
        self._list_portfolio_allocations = ListPortfolioAllocationsClient(credentials)
        self._list_portfolio_balances = ListPortfolioBalancesClient(credentials)
        self._list_portfolio_fills = ListPortfolioFillsClient(credentials)
        self._list_portfolio_transactions = ListPortfolioTransactionsClient(credentials)
        self._list_portfolio_users = ListPortfolioUsersClient(credentials)
        self._list_portfolios = ListPortfoliosClient(credentials)
        self._list_products = ListProductsClient(credentials)
        self._list_users = ListUsersClient(credentials)
        self._list_wallet_addresses = ListWalletAddressesClient(credentials)
        self._list_wallet_transactions = ListWalletTransactionsClient(credentials)
        self._list_wallets = ListWalletsClient(credentials)
        self._list_web3_wallet_balances = ListWeb3WalletBalancesClient(credentials)
        self._schedule_entity_futures_sweep = ScheduleEntityFuturesSweepClient(credentials)
        self._set_auto_sweep = SetAutoSweepClient(credentials)
        self._update_onchain_address_book = UpdateOnchainAddressBookClient(credentials)

    # Client properties for direct access
    @property
    def accept_quote(self):
        return self._accept_quote.accept_quote

    @property
    def cancel_entity_futures_sweep(self):
        return self._cancel_entity_futures_sweep.cancel_entity_futures_sweep

    @property
    def cancel_order(self):
        return self._cancel_order.cancel_order

    @property
    def create_address_book_entry(self):
        return self._create_address_book_entry.create_address_book_entry

    @property
    def create_conversion(self):
        return self._create_conversion.create_conversion

    @property
    def create_new_locates(self):
        return self._create_new_locates.create_new_locate

    @property
    def create_onchain_address_book_entry(self):
        return self._create_onchain_address_book_entry.create_onchain_address_book_entry

    @property
    def create_onchain_transaction(self):
        return self._create_onchain_transaction.create_onchain_transaction

    @property
    def create_order(self):
        return self._create_order.create_order

    @property
    def create_order_preview(self):
        return self._create_order_preview.create_order_preview

    @property
    def create_portfolio_allocations(self):
        return self._create_portfolio_allocations.create_portfolio_allocations

    @property
    def create_portfolio_net_allocations(self):
        return self._create_portfolio_net_allocations.create_portfolio_net_allocations

    @property
    def create_quote(self):
        return self._create_quote.create_quote

    @property
    def create_stake(self):
        return self._create_stake.create_stake

    @property
    def create_transfer(self):
        return self._create_transfer.create_transfer

    @property
    def create_unstake(self):
        return self._create_unstake.create_unstake

    @property
    def create_wallet(self):
        return self._create_wallet.create_wallet

    @property
    def create_wallet_address(self):
        return self._create_wallet_address.create_wallet_address

    @property
    def create_withdrawal(self):
        return self._create_withdrawal.create_withdrawal

    @property
    def delete_onchain_address_group(self):
        return self._delete_onchain_address_group.delete_onchain_address_group

    @property
    def get_activity(self):
        return self._get_activity.get_activity

    @property
    def get_address_book(self):
        return self._get_address_book.get_address_book

    @property
    def get_allocation_by_id(self):
        return self._get_allocation_by_id.get_allocation_by_id

    @property
    def get_entity_activity(self):
        return self._get_entity_activity.get_entity_activity_by_activity_id

    @property
    def get_entity_fcm_balance(self):
        return self._get_entity_fcm_balance.get_entity_fcm_balance

    @property
    def get_entity_locate_availabilities(self):
        return self._get_entity_locate_availabilities.get_entity_locate_availabilities

    @property
    def get_entity_payment_method(self):
        return self._get_entity_payment_method.get_entity_payment_method

    @property
    def get_entity_positions(self):
        return self._get_entity_positions.get_entity_positions

    @property
    def get_margin_information(self):
        return self._get_margin_information.get_margin_information

    @property
    def get_net_allocations_by_netting_id(self):
        return self._get_net_allocations_by_netting_id.get_net_allocations_by_netting_id

    @property
    def get_order(self):
        return self._get_order.get_order

    @property
    def get_portfolio(self):
        return self._get_portfolio.get_portfolio

    @property
    def get_portfolio_buying_power(self):
        return self._get_portfolio_buying_power.get_buying_power

    @property
    def get_portfolio_commission(self):
        return self._get_portfolio_commission.get_portfolio_commission

    @property
    def get_portfolio_credit_information(self):
        return self._get_portfolio_credit_information.get_portfolio_credit_information

    @property
    def get_portfolio_withdrawal_power(self):
        return self._get_portfolio_withdrawal_power.get_portfolio_withdrawal_power

    @property
    def get_trade_finance_tiered_pricing_fees(self):
        return self._get_trade_finance_tiered_pricing_fees.get_trade_finance_tiered_pricing_fees

    @property
    def get_transaction(self):
        return self._get_transaction.get_transaction

    @property
    def get_wallet(self):
        return self._get_wallet.get_wallet

    @property
    def get_wallet_balance(self):
        return self._get_wallet_balance.get_wallet_balance

    @property
    def get_wallet_deposit_instructions(self):
        return self._get_wallet_deposit_instructions.get_wallet_deposit_instructions

    @property
    def list_activities(self):
        return self._list_activities.list_activities

    @property
    def list_aggregate_entity_positions(self):
        return self._list_aggregate_entity_positions.list_aggregate_entity_positions

    @property
    def list_assets(self):
        return self._list_assets.list_assets

    @property
    def list_entity_activities(self):
        return self._list_entity_activities.list_entity_activities

    @property
    def list_entity_balances(self):
        return self._list_entity_balances.list_entity_balances

    @property
    def list_entity_futures_sweeps(self):
        return self._list_entity_futures_sweeps.list_entity_futures_sweeps

    @property
    def list_entity_payment_methods(self):
        return self._list_entity_payment_methods.list_entity_payment_methods

    @property
    def list_entity_positions(self):
        return self._list_entity_positions.list_entity_positions

    @property
    def list_existing_locates(self):
        return self._list_existing_locates.list_existing_locates

    @property
    def list_interest_accruals(self):
        return self._list_interest_accruals.list_interest_accruals

    @property
    def list_interest_accruals_for_portfolio(self):
        return self._list_interest_accruals_for_portfolio.list_interest_accruals_for_portfolio

    @property
    def list_invoices(self):
        return self._list_invoices.list_invoices

    @property
    def list_margin_call_summaries(self):
        return self._list_margin_call_summaries.list_margin_call_summaries

    @property
    def list_margin_conversions(self):
        return self._list_margin_conversions.list_margin_conversions

    @property
    def list_onchain_address_groups(self):
        return self._list_onchain_address_groups.list_onchain_address_groups

    @property
    def list_open_orders(self):
        return self._list_open_orders.list_open_orders

    @property
    def list_order_fills(self):
        return self._list_order_fills.list_order_fills

    @property
    def list_orders(self):
        return self._list_orders.list_orders

    @property
    def list_portfolio_allocations(self):
        return self._list_portfolio_allocations.list_portfolio_allocations

    @property
    def list_portfolio_balances(self):
        return self._list_portfolio_balances.list_portfolio_balances

    @property
    def list_portfolio_fills(self):
        return self._list_portfolio_fills.list_portfolio_fills

    @property
    def list_portfolio_transactions(self):
        return self._list_portfolio_transactions.list_portfolio_transactions

    @property
    def list_portfolio_users(self):
        return self._list_portfolio_users.list_portfolio_users

    @property
    def list_portfolios(self):
        return self._list_portfolios.list_portfolios

    @property
    def list_products(self):
        return self._list_products.list_products

    @property
    def list_users(self):
        return self._list_users.list_users

    @property
    def list_wallet_addresses(self):
        return self._list_wallet_addresses.list_wallet_addresses

    @property
    def list_wallet_transactions(self):
        return self._list_wallet_transactions.list_wallet_transactions

    @property
    def list_wallets(self):
        return self._list_wallets.list_wallets

    @property
    def list_web3_wallet_balances(self):
        return self._list_web3_wallet_balances.list_web3_wallet_balances

    @property
    def schedule_entity_futures_sweep(self):
        return self._schedule_entity_futures_sweep.schedule_entity_futures_sweep

    @property
    def set_auto_sweep(self):
        return self._set_auto_sweep.set_auto_sweep

    @property
    def update_onchain_address_book(self):
        return self._update_onchain_address_book.update_onchain_address_book
