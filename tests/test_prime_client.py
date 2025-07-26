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

import unittest
from unittest.mock import Mock, patch
from prime_sdk import PrimeClient
from prime_sdk.credentials import Credentials
from prime_sdk.list_portfolios import ListPortfoliosRequest, ListPortfoliosResponse
from prime_sdk.get_order import GetOrderRequest, GetOrderResponse
from prime_sdk.create_order import CreateOrderRequest, CreateOrderResponse


class TestPrimeClient(unittest.TestCase):
    def setUp(self):
        self.credentials = Credentials(
            access_key="test_access_key",
            passphrase="test_passphrase",
            signing_key="test_signing_key",
            portfolio_id="test_portfolio_id",
            entity_id="test_entity_id",
            svc_account_id="test_svc_account_id"
        )
        self.client = PrimeClient(self.credentials)

    def test_client_initialization(self):
        """Test that PrimeClient initializes all sub-clients properly"""
        self.assertIsNotNone(self.client._list_portfolios)
        self.assertIsNotNone(self.client._get_order)
        self.assertIsNotNone(self.client._create_order)
        self.assertIsNotNone(self.client._cancel_order)
        self.assertIsNotNone(self.client._list_assets)
        self.assertIsNotNone(self.client._list_products)
        self.assertIsNotNone(self.client._list_wallets)
        self.assertIsNotNone(self.client._get_wallet)
        self.assertIsNotNone(self.client._create_wallet)
        self.assertIsNotNone(self.client._create_withdrawal)

    def test_property_access(self):
        """Test that properties return bound methods"""
        # Properties should return the bound methods of underlying clients
        self.assertTrue(callable(self.client.list_portfolios))
        self.assertTrue(callable(self.client.get_order))
        self.assertTrue(callable(self.client.create_order))
        self.assertTrue(callable(self.client.cancel_order))
        self.assertTrue(callable(self.client.list_assets))
        self.assertTrue(callable(self.client.list_products))
        self.assertTrue(callable(self.client.list_wallets))
        self.assertTrue(callable(self.client.get_wallet))
        self.assertTrue(callable(self.client.create_wallet))
        self.assertTrue(callable(self.client.create_withdrawal))

    @patch('prime_sdk.list_portfolios.PrimeClient.list_portfolios')
    def test_list_portfolios_method(self, mock_list_portfolios):
        """Test the list_portfolios method calls the underlying client correctly"""
        # Mock response
        mock_response = ListPortfoliosResponse(portfolios=[])
        mock_list_portfolios.return_value = mock_response
        
        # Make request
        request = ListPortfoliosRequest()
        response = self.client.list_portfolios(request)
        
        # Verify
        mock_list_portfolios.assert_called_once_with(request)
        self.assertEqual(response, mock_response)

    @patch('prime_sdk.get_order.PrimeClient.get_order')
    def test_get_order_method(self, mock_get_order):
        """Test the get_order method calls the underlying client correctly"""
        # Mock response
        mock_response = GetOrderResponse()
        mock_get_order.return_value = mock_response
        
        # Make request
        request = GetOrderRequest(order_id="test_order_id", portfolio_id="test_portfolio_id")
        response = self.client.get_order(request)
        
        # Verify
        mock_get_order.assert_called_once_with(request)
        self.assertEqual(response, mock_response)

    @patch('prime_sdk.create_order.PrimeClient.create_order')
    def test_create_order_method(self, mock_create_order):
        """Test the create_order method calls the underlying client correctly"""
        # Mock response
        mock_response = CreateOrderResponse()
        mock_create_order.return_value = mock_response
        
        # Make request
        from prime_sdk.enums import OrderSide, OrderType
        request = CreateOrderRequest(
            portfolio_id="test_portfolio_id",
            side=OrderSide.BUY,
            client_order_id="test_order_123",
            product_id="BTC-USD",
            type=OrderType.MARKET
        )
        response = self.client.create_order(request)
        
        # Verify
        mock_create_order.assert_called_once_with(request)
        self.assertEqual(response, mock_response)

    def test_all_clients_initialized(self):
        """Test that all expected client properties are initialized"""
        expected_clients = [
            'accept_quote', 'cancel_entity_futures_sweep', 'cancel_order',
            'create_address_book_entry', 'create_conversion', 'create_new_locates',
            'create_onchain_address_book_entry', 'create_onchain_transaction',
            'create_order', 'create_order_preview', 'create_portfolio_allocations',
            'create_portfolio_net_allocations', 'create_quote', 'create_stake',
            'create_transfer', 'create_unstake', 'create_wallet', 'create_wallet_address',
            'create_withdrawal', 'delete_onchain_address_group', 'get_activity',
            'get_address_book', 'get_allocation_by_id', 'get_entity_activity',
            'get_entity_fcm_balance', 'get_entity_locate_availabilities',
            'get_entity_payment_method', 'get_entity_positions', 'get_margin_information',
            'get_net_allocations_by_netting_id', 'get_order', 'get_portfolio',
            'get_portfolio_buying_power', 'get_portfolio_commission',
            'get_portfolio_credit_information', 'get_portfolio_withdrawal_power',
            'get_trade_finance_tiered_pricing_fees', 'get_transaction', 'get_wallet',
            'get_wallet_balance', 'get_wallet_deposit_instructions', 'list_activities',
            'list_aggregate_entity_positions', 'list_assets', 'list_entity_activities',
            'list_entity_balances', 'list_entity_futures_sweeps', 'list_entity_payment_methods',
            'list_entity_positions', 'list_existing_locates', 'list_interest_accruals',
            'list_interest_accruals_for_portfolio', 'list_invoices', 'list_margin_call_summaries',
            'list_margin_conversions', 'list_onchain_address_groups', 'list_open_orders',
            'list_order_fills', 'list_orders', 'list_portfolio_allocations',
            'list_portfolio_balances', 'list_portfolio_fills', 'list_portfolio_transactions',
            'list_portfolio_users', 'list_portfolios', 'list_products', 'list_users',
            'list_wallet_addresses', 'list_wallet_transactions', 'list_wallets',
            'list_web3_wallet_balances', 'schedule_entity_futures_sweep', 'set_auto_sweep',
            'update_onchain_address_book'
        ]
        
        for client_name in expected_clients:
            self.assertTrue(hasattr(self.client, client_name), f"Client missing property: {client_name}")
            self.assertIsNotNone(getattr(self.client, client_name), f"Client property is None: {client_name}")


if __name__ == '__main__':
    unittest.main()