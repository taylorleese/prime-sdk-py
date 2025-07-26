# Prime Python SDK

## Overview

The *Prime Python SDK* is a sample library that demonstrates the usage of the [Coinbase Prime](https://prime.coinbase.com/) API via its [REST APIs](https://docs.cdp.coinbase.com/prime/reference). This SDK provides a structured way to integrate Coinbase Prime functionalities into your Python applications.

## Installation

```bash
pip install prime-sdk-py
```

For development:
```bash
git clone git@github.com:coinbase/prime-sdk-py.git
cd prime-sdk-py
pip install -e .
```

## License

The *Prime Python SDK* sample library is free and open source and released under the [Apache License, Version 2.0](LICENSE).

The application and code are only available for demonstration purposes.

## Usage

### Setting Up Credentials

To use the *Prime Python SDK*, initialize the [Credentials](prime_sdk/credentials.py) class with your Prime API credentials. This class is designed to facilitate the secure handling of sensitive information required to authenticate API requests.

Ensure that your API credentials are stored securely and are not hard-coded directly in your source code. The Credentials class supports creating credentials from a JSON string or directly from environment variables, providing flexibility and enhancing security.

#### Example Initialization:
```python
from prime_sdk.credentials import Credentials

credentials = Credentials.from_env("PRIME_CREDENTIALS")
```

#### Environment Variable Format: 

The JSON format expected for `PRIME_CREDENTIALS` is:

```
{
  "accessKey": "",
  "passphrase": "",
  "signingKey": "",
  "portfolioId": "",
  "svcAccountId": "",
  "entityId": ""
}
```

### Obtaining API Credentials 

Coinbase Prime API credentials can be created in the Prime web console under Settings -> APIs. While not immediately necessary for most endpoints, your entity ID can be retrieved by calling [List Portfolios](https://docs.cdp.coinbase.com/prime/reference/primerestapi_getportfolios).

### Making API Calls

#### Using the Unified PrimeClient (Recommended)

The SDK now provides a unified `PrimeClient` that consolidates all 70+ Prime API operations into a single class, eliminating the need to manage multiple imports:

```python
from prime_sdk import PrimeClient
from prime_sdk.credentials import Credentials
from prime_sdk.list_portfolios import ListPortfoliosRequest
from prime_sdk.create_order import CreateOrderRequest
from prime_sdk.enums import OrderSide, OrderType

# Initialize credentials
credentials = Credentials.from_env("PRIME_CREDENTIALS")
client = PrimeClient(credentials)

# List portfolios
portfolios = client.list_portfolios(ListPortfoliosRequest())
for portfolio in portfolios.portfolios:
    print(f"Portfolio: {portfolio.name} (ID: {portfolio.id})")

# Create an order
order_request = CreateOrderRequest(
    portfolio_id="your-portfolio-id",
    product_id="BTC-USD",
    side=OrderSide.BUY,
    type=OrderType.MARKET,
    base_quantity="0.001",
    client_order_id="unique-order-id"
)
order_response = client.create_order(order_request)

# Get wallet balance
from prime_sdk.get_wallet_balance import GetWalletBalanceRequest
balance = client.get_wallet_balance(
    GetWalletBalanceRequest(
        portfolio_id="your-portfolio-id",
        wallet_id="your-wallet-id",
        asset_id="BTC"
    )
)
```

#### Using Individual Client Classes

For backwards compatibility, you can still import individual client classes from their respective modules, though this requires managing naming conflicts since each module exports a class named `PrimeClient`:

```python
from prime_sdk.list_portfolios import PrimeClient as PortfoliosClient, ListPortfoliosRequest
from prime_sdk.create_order import PrimeClient as OrdersClient, CreateOrderRequest

credentials = Credentials.from_env("PRIME_CREDENTIALS")

# Need separate client instances for each operation
portfolios_client = PortfoliosClient(credentials)
orders_client = OrdersClient(credentials)

# Make API calls
portfolios = portfolios_client.list_portfolios(ListPortfoliosRequest())
```

### Supported Versions
The SDK is tested and confirmed to work with Python version 3.7 and newer.
