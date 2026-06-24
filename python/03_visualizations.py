#!/usr/bin/env python3
"""
Generate visualization dashboard for A/B test results.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

print("=" * 60)
print("GENERATING VISUALIZATIONS")
print("=" * 60)

# Load data
daily_df = pd.read_csv('data/daily_metrics.csv')
user_df = pd.read_csv('data/user_events.csv')

daily_df['date'] = pd.to_datetime(daily_df['date'])

# Setup
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (16, 12)
colors = ['#2196F3', '#4CAF50']
camp_names = ['Campaign A\n(Banner Ads)', 'Campaign B\n(Influencer Video)']

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Marketing Campaign A/B Test Results\nJune 1-30, 2024', 
             fontsize=18, fontweight='bold', y=0.995)

# --- Chart 1: Conversion Rate Comparison ---
ax1 = axes[0, 0]
conv_rates = []
for camp_id in [1, 2]:
    camp_data = daily_df[daily_df['campaign_id'] == camp_id]
    conv_rate = (camp_data['conversions'].sum() / camp_data['clicks'].sum() * 100)
    conv_rates.append(conv_rate)

bars = ax1.bar(camp_names, conv_rates, color=colors, edgecolor='black', linewidth=1.2, width=0.6)
ax1.set_ylabel('Conversion Rate (%)', fontsize=12, fontweight='bold')
ax1.set_title('Conversion Rate Comparison', fontsize=14, fontweight='bold')
ax1.set_ylim(0, max(conv_rates) * 1.3)
for bar, rate in zip(bars, conv_rates):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f'{rate:.2f}%', ha='center', fontsize=13, fontweight='bold')

# --- Chart 2: Daily Revenue Trend ---
ax2 = axes[0, 1]
for camp_id, color, label in [(1, '#2196F3', 'Campaign A'), (2, '#4CAF50', 'Campaign B')]:
    camp_data = daily_df[daily_df['campaign_id'] == camp_id].sort_values('date')
    ax2.plot(camp_data['date'], camp_data['revenue'], color=color, label=label, 
             linewidth=2.5, marker='o', markersize=4, alpha=0.8)
ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
ax2.set_ylabel('Daily Revenue ($)', fontsize=12, fontweight='bold')
ax2.set_title('Daily Revenue Trend', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11, loc='upper left')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True, alpha=0.3)

# --- Chart 3: ROI Comparison ---
ax3 = axes[1, 0]
roi_values = []
for camp_id in [1, 2]:
    camp_data = daily_df[daily_df['campaign_id'] == camp_id]
    spend = camp_data['spend'].sum()
    revenue = camp_data['revenue'].sum()
    roi = (revenue - spend) / spend * 100
    roi_values.append(roi)

bars = ax3.bar(camp_names, roi_values, color=colors, edgecolor='black', linewidth=1.2, width=0.6)
ax3.set_ylabel('ROI (%)', fontsize=12, fontweight='bold')
ax3.set_title('Return on Investment (ROI)', fontsize=14, fontweight='bold')
ax3.axhline(y=0, color='black', linewidth=0.8)
ax3.set_ylim(min(0, min(roi_values) * 1.1), max(roi_values) * 1.15)
for bar, roi in zip(bars, roi_values):
    y_pos = bar.get_height() + (max(roi_values) * 0.05)
    ax3.text(bar.get_x() + bar.get_width()/2, y_pos,
             f'{roi:.1f}%', ha='center', fontsize=13, fontweight='bold')

# --- Chart 4: Cost Per Acquisition ---
ax4 = axes[1, 1]
cpa_values = []
for camp_id in [1, 2]:
    camp_data = daily_df[daily_df['campaign_id'] == camp_id]
    spend = camp_data['spend'].sum()
    conv = camp_data['conversions'].sum()
    cpa = spend / conv if conv > 0 else 0
    cpa_values.append(cpa)

bars = ax4.bar(camp_names, cpa_values, color=colors, edgecolor='black', linewidth=1.2, width=0.6)
ax4.set_ylabel('Cost Per Acquisition ($)', fontsize=12, fontweight='bold')
ax4.set_title('Cost Per Acquisition (CPA)', fontsize=14, fontweight='bold')
ax4.set_ylim(0, max(cpa_values) * 1.3)
for bar, cpa in zip(bars, cpa_values):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'${cpa:.2f}', ha='center', fontsize=13, fontweight='bold')

plt.tight_layout()

# Save figure
import os
os.makedirs('output', exist_ok=True)
output_path = 'output/ab_test_results.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"✅ Visualization saved to: {output_path}")

plt.close()

# Generate summary statistics table
print(f"\n📊 SUMMARY STATISTICS")
print("=" * 80)

summary_data = []
for camp_id, camp_name in [(1, 'Campaign A (Banner)'), (2, 'Campaign B (Influencer)')]:
    camp_daily = daily_df[daily_df['campaign_id'] == camp_id]
    camp_users = user_df[user_df['campaign_id'] == camp_id]
    
    total_spend = camp_daily['spend'].sum()
    total_revenue = camp_daily['revenue'].sum()
    total_clicks = camp_daily['clicks'].sum()
    total_conversions = camp_daily['conversions'].sum()
    roi = (total_revenue - total_spend) / total_spend * 100 if total_spend > 0 else 0
    cpa = total_spend / total_conversions if total_conversions > 0 else 0
    roas = total_revenue / total_spend if total_spend > 0 else 0
    ctr = total_clicks / camp_daily['impressions'].sum() * 100
    conv_rate = total_conversions / total_clicks * 100 if total_clicks > 0 else 0
    aov = total_revenue / total_conversions if total_conversions > 0 else 0
    
    summary_data.append({
        'Campaign': camp_name,
        'Clicks': f'{int(total_clicks):,}',
        'Conversions': f'{int(total_conversions):,}',
        'Conv Rate': f'{conv_rate:.2f}%',
        'Spend': f'${total_spend:,.2f}',
        'Revenue': f'${total_revenue:,.2f}',
        'CPA': f'${cpa:.2f}',
        'AOV': f'${aov:.2f}',
        'ROAS': f'{roas:.2f}x',
        'ROI': f'{roi:.1f}%'
    })

summary_df = pd.DataFrame(summary_data)
print(summary_df.to_string(index=False))
print("=" * 80)

print("\n✅ Visualization dashboard complete!")
print("=" * 60)
