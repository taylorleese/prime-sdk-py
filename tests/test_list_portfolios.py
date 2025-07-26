import unittest
from prime_sdk.list_portfolios import ListPortfoliosResponse
from prime_sdk.model import Portfolio


class TestListPortfoliosResponse(unittest.TestCase):
    def test_list_portfolios_response_parsing(self):
        # Mock portfolio data
        mock_portfolios = [
            {
                "id": "fake-portfolio-id-123",
                "name": "CryptoBalances",
                "entity_id": "fake-entity-id",
                "organization_id": "fake-org-id",
                "entity_name": "Sample Prime Entity"
            }
        ]

        # Create response with proper structure
        response = ListPortfoliosResponse(portfolios=mock_portfolios)

        # Verify the portfolios were parsed correctly
        self.assertIsInstance(response.portfolios, list)
        self.assertEqual(len(response.portfolios), 1)
        self.assertIsInstance(response.portfolios[0], Portfolio)

        portfolio = response.portfolios[0]
        self.assertEqual(portfolio.id, "fake-portfolio-id-123")
        self.assertEqual(portfolio.name, "CryptoBalances")
        self.assertEqual(portfolio.entity_id, "fake-entity-id")
        self.assertEqual(portfolio.organization_id, "fake-org-id")
        self.assertEqual(portfolio.entity_name, "Sample Prime Entity")

    def test_list_portfolios_empty_list(self):
        # Test empty portfolios list
        response = ListPortfoliosResponse(portfolios=[])
        self.assertEqual(len(response.portfolios), 0)

    def test_list_portfolios_none(self):
        # Test None portfolios
        response = ListPortfoliosResponse(portfolios=None)
        self.assertIsNone(response.portfolios)


if __name__ == '__main__':
    unittest.main()
