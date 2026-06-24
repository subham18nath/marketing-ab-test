#!/usr/bin/env python3
"""
Statistical A/B testing analysis for marketing campaigns.
"""

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

print("=" * 60)
print("A/B TEST STATISTICAL ANALYSIS")
print("=" * 60)

# Load data
user_df = pd.read_csv('data/user_events.csv')

# Campaign data
camp_a = user_df[user_df['campaign_id'] == 1]
camp_b = user_df[user_df['campaign_id'] == 2]

n_a = len(camp_a)
n_b = len(camp_b)
conversions_a = camp_a['converted'].sum()
conversions_b = camp_b['converted'].sum()
p_a = conversions_a / n_a
p_b = conversions_b / n_b

print(f"\n📊 CAMPAIGN SUMMARY")
print(f"Campaign A (Banner Ads)")
print(f"   Sample size:       {n_a:,}")
print(f"   Conversions:       {int(conversions_a):,}")
print(f"   Conversion rate:   {p_a:.4f} ({p_a*100:.2f}%)")

print(f"\nCampaign B (Influencer Video)")
print(f"   Sample size:       {n_b:,}")
print(f"   Conversions:       {int(conversions_b):,}")
print(f"   Conversion rate:   {p_b:.4f} ({p_b*100:.2f}%)")

# Two-proportion Z-test
pooled_p = (conversions_a + conversions_b) / (n_a + n_b)
se = np.sqrt(pooled_p * (1 - pooled_p) * (1/n_a + 1/n_b))
z_stat = (p_b - p_a) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

# 95% Confidence interval for difference
ci_lower = (p_b - p_a) - 1.96 * se
ci_upper = (p_b - p_a) + 1.96 * se

print(f"\n🔬 TWO-PROPORTION Z-TEST")
print(f"Absolute difference:       {p_b - p_a:.4f} ({(p_b-p_a)*100:.2f}%)")
print(f"Relative lift (B vs A):    {(p_b/p_a - 1)*100:.1f}%")
print(f"\nZ-statistic:               {z_stat:.4f}")
print(f"P-value:                   {p_value:.6f}")
print(f"95% CI for difference:     [{ci_lower*100:.2f}%, {ci_upper*100:.2f}%]")

if p_value < 0.05:
    print(f"\n✅ RESULT: Statistically SIGNIFICANT (p < 0.05)")
else:
    print(f"\n❌ RESULT: NOT significant (p ≥ 0.05)")

# Revenue analysis
daily_df = pd.read_csv('data/daily_metrics.csv')

print(f"\n💰 REVENUE & ROI ANALYSIS")

for camp_id, camp_name in [(1, 'Campaign A (Banner Ads)'), (2, 'Campaign B (Influencer)')]:
    camp_data = daily_df[daily_df['campaign_id'] == camp_id]
    total_spend = camp_data['spend'].sum()
    total_revenue = camp_data['revenue'].sum()
    conversions = camp_data['conversions'].sum()
    roi = (total_revenue - total_spend) / total_spend * 100 if total_spend > 0 else 0
    cpa = total_spend / conversions if conversions > 0 else 0
    roas = total_revenue / total_spend if total_spend > 0 else 0

    print(f"\n{camp_name}")
    print(f"   Total spend:       ${total_spend:,.2f}")
    print(f"   Total revenue:     ${total_revenue:,.2f}")
    print(f"   Conversions:       {int(conversions):,}")
    print(f"   CPA:               ${cpa:,.2f}")
    print(f"   ROI:               {roi:.1f}%")
    print(f"   ROAS:              {roas:.2f}x")

# Power analysis
print(f"\n⚡ STATISTICAL POWER ANALYSIS")

effect_size = proportion_effectsize(p_b, p_a)
power_analysis = NormalIndPower()
power = power_analysis.power(effect_size=effect_size, nobs1=n_a, alpha=0.05, ratio=n_b/n_a)

print(f"Effect size (Cohen's h):   {effect_size:.4f}")
print(f"Sample size (A):           {n_a:,}")
print(f"Sample size (B):           {n_b:,}")
print(f"Statistical power:         {power:.4f} ({power*100:.2f}%)")
print(f"Alpha:                     0.05")

if power >= 0.80:
    print(f"\n✅ Power ≥ 80% — Test is adequately powered")
else:
    print(f"\n⚠️  Power < 80% — Consider larger sample size")

required_n = power_analysis.solve_power(effect_size=effect_size, alpha=0.05, power=0.80)
print(f"\nMinimum sample needed per group (80% power): {int(required_n):,}")
print(f"Actual sample size:        {min(n_a, n_b):,}")
print(f"Status:                    {'✅ Sufficient' if min(n_a, n_b) >= required_n else '❌ Insufficient'}")

print("\n" + "=" * 60)
