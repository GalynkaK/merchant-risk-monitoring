import pandas as pd
import os

print(os.getcwd())  

df = pd.read_csv('data/transactions.csv')

# Preview data
print("Dataset preview:")
print(df.head())

# Check structure
print("\nInfo:")
print(df.info())

# --- Feature Engineering ---

# Fraud rate per merchant
fraud_rate = df.groupby('merchant_id')['is_fraud'].mean()

# Small transaction flag
df['is_small_tx'] = df['amount'] < 10

# Small transaction rate
small_tx_rate = df.groupby('merchant_id')['is_small_tx'].mean()

# Combine features
risk = pd.concat([fraud_rate, small_tx_rate], axis=1)
risk.columns = ['fraud_rate', 'small_tx_rate']

# Final risk score
risk['risk_score'] = (
    risk['fraud_rate'] * 0.5 +
    risk['small_tx_rate'] * 0.5
)

# Sort and display top risky merchants
top_risk = risk.sort_values('risk_score', ascending=False).head(5)

print("\nTop 5 risky merchants:")
print(top_risk)

top_risk.to_csv('../data/top_risk_merchants.csv')