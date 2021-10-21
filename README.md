# Calculate your z score!

This is a barebones API providing 1 endpoint to caluclate your zscore, built using Python and FastAPI 🔧

# Steps to run locally

1. Clone/download the remote repo to your local env
2. Open terminal in root directory of the project
3. $ make install
4. $ make run
5. Go to 127.0.0.1/docs

IMPORTANT: CHECK .ENVEXAMPLE and CREATE .env IN ROOT with your db credentials (POSTGRES)

# Interact with API
You will be presented with 1 PUT endpoint - /calculate/get_zscore

Here the request expects your financial data as a nested list of json objects, below is an example:

```
{"financials": [ 
{"year": 2020, "ebit": 123.45, "equity": 234.56, "retained_earnings": 345.67, "sales": 
1234.56, "total_assets": 345.67, "total_liabilities": 456.78}, 
{"year": 2019, "ebit": 122.63, "equity": 224.56, "retained_earnings": 325.33, "sales": 
1214.99, "total_assets": 325.04, "total_liabilities": 426.78}, 
{"year": 2018, "ebit": 120.17, "equity": 214.06, "retained_earnings": 225.00, "sales": 
1204.01, "total_assets": 305.11, "total_liabilities": 426.78}, 
{"year": 2017, "ebit": 118.23, "equity": 204.96, "retained_earnings": 125.97, "sales": 
1200.00, "total_assets": 290.75, "total_liabilities": 426.78}, 
{"year": 2016, "ebit": 116.05, "equity": 234.56, "retained_earnings": 105.11, "sales": 
1010.82, "total_assets": 250.13, "total_liabilities": 426.78}]}
```

You will get a response containing the data.

# Still to do - i.e branches and PR's
1. Setup logging, sentry, newrelic
2. Setup alembic for migrations
5. Pylint/conf file for testing
6. Dockerise in preparations for containers management, k8s

# Branches & PR's
1. Create branch as normal
2. Upon PR Github will run pylint against code to ensure clean code across the board
