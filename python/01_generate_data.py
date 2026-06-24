#!/usr/bin/env python3
"""
Generate synthetic marketing campaign data for A/B testing.
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

print("=" * 60)
print("SYNTHETIC DATA GENERATION")
print("=" * 60)

# Configuration
DAYS = 30
DAILY_BUDGET_A = 50000 / DAYS  # $1,666.67/day
DAILY_BUDGET_B = 50000 / DAYS
np.random.seed(42)

print(f"\n📊 Generating {DAYS} days of campaign data...")
print(f"   Budget per day (both campaigns): ${DAILY_BUDGET_A:,.2f}")

# Generate dates
dates = [datetime(2024, 6, 1) + timedelta(days=i) for i in range(DAYS)]

# Generate daily metrics
data = []
for date in dates:
    # CAMPAIGN A - Banner Ads (lower CTR, lower conversion, lower AOV)
    impressions_a = np.random.poisson(120000)
    ctr_a = np.random.normal(0.015, 0.002)  # ~1.5% CTR
    clicks_a = int(impressions_a * max(ctr_a, 0))
    conv_rate_a = np.random.normal(0.025, 0.003)  # ~2.5% conversion
    conversions_a = int(clicks_a * max(conv_rate_a, 0))
    spend_a = DAILY_BUDGET_A + np.random.normal(0, 50)
    aov_a = np.random.normal(65, 8)
    revenue_a = conversions_a * max(aov_a, 0)

    # CAMPAIGN B - Influencer Video (higher CTR, higher conversion, higher AOV)
    impressions_b = np.random.poisson(180000)
    ctr_b = np.random.normal(0.028, 0.003)  # ~2.8% CTR
    clicks_b = int(impressions_b * max(ctr_b, 0))
    conv_rate_b = np.random.normal(0.042, 0.004)  # ~4.2% conversion
    conversions_b = int(clicks_b * max(conv_rate_b, 0))
    spend_b = DAILY_BUDGET_B + np.random.normal(0, 50)
    aov_b = np.random.normal(82, 10)
    revenue_b = conversions_b * max(aov_b, 0)

    data.append([date, 1, impressions_a, clicks_a, conversions_a, spend_a, revenue_a])
    data.append([date, 2, impressions_b, clicks_b, conversions_b, spend_b, revenue_b])

daily_df = pd.DataFrame(data, columns=[
    'date', 'campaign_id', 'impressions', 'clicks', 'conversions', 'spend', 'revenue'
])

print(f"✅ Generated {len(daily_df)} daily metric rows")

# Generate user-level data
print(f"\n👥 Generating user-level click/conversion data...")
users = []
user_id_counter = 1

for date in dates:
    row_a = daily_df[(daily_df['date'] == date) & (daily_df['campaign_id'] == 1)].iloc[0]
    row_b = daily_df[(daily_df['date'] == date) & (daily_df['campaign_id'] == 2)].iloc[0]

    # Campaign A users
    for _ in range(row_a['clicks']):
        converted = np.random.random() < (row_a['conversions'] / max(row_a['clicks'], 1))
        order_value = np.random.normal(65, 8) if converted else 0
        users.append([user_id_counter, 1, date, True, converted, max(order_value, 0)])
        user_id_counter += 1

    # Campaign B users
    for _ in range(row_b['clicks']):
        converted = np.random.random() < (row_b['conversions'] / max(row_b['clicks'], 1))
        order_value = np.random.normal(82, 10) if converted else 0
        users.append([user_id_counter, 2, date, True, converted, max(order_value, 0)])
        user_id_counter += 1

user_df = pd.DataFrame(users, columns=[
    'user_id', 'campaign_id', 'event_date', 'clicked', 'converted', 'order_value'
])

print(f"✅ Generated {len(user_df):,} user event rows")

# Save to CSV
os.makedirs('data', exist_ok=True)
daily_df.to_csv('data/daily_metrics.csv', index=False)
user_df.to_csv('data/user_events.csv', index=False)

print(f"\n📁 Files saved:")
print(f"   - data/daily_metrics.csv ({len(daily_df)} rows)")
print(f"   - data/user_events.csv ({len(user_df):,} rows)")

# Summary statistics
print(f"\n📊 CAMPAIGN A (Banner Ads)")
camp_a = daily_df[daily_df['campaign_id'] == 1]
print(f"   Total clicks:      {camp_a['clicks'].sum():,}")
print(f"   Total conversions: {camp_a['conversions'].sum():,}")
print(f"   Conversion rate:   {camp_a['conversions'].sum() / max(camp_a['clicks'].sum(), 1) * 100:.2f}%")
print(f"   Total spend:       ${camp_a['spend'].sum():,.2f}")
print(f"   Total revenue:     ${camp_a['revenue'].sum():,.2f}")

print(f"\n📊 CAMPAIGN B (Influencer Video)")
camp_b = daily_df[daily_df['campaign_id'] == 2]
print(f"   Total clicks:      {camp_b['clicks'].sum():,}")
print(f"   Total conversions: {camp_b['conversions'].sum():,}")
print(f"   Conversion rate:   {camp_b['conversions'].sum() / max(camp_b['clicks'].sum(), 1) * 100:.2f}%")
print(f"   Total spend:       ${camp_b['spend'].sum():,.2f}")
print(f"   Total revenue:     ${camp_b['revenue'].sum():,.2f}")

print("\n" + "=" * 60)
