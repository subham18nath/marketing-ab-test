# Marketing Campaign ROI & A/B Testing

An end-to-end data analytics project that compares two marketing campaigns, proves which one wins with a statistical A/B test, and visualizes the result in an executive Power BI dashboard.

> **TL;DR:** Campaign B (Influencer Video) beat Campaign A (Banner Ads) on every business metric, and the difference is **statistically significant (p < 0.001)**. Recommendation: shift budget to Campaign B.

---

## 📋 Project Overview

| | |
|---|---|
| **Company (scenario)** | TechGear Direct — e-commerce electronics retailer |
| **Test period** | June 2024 (30 days) |
| **Budget** | $50,000 per campaign |
| **Campaign A (Control)** | Static Banner Ads — Display Network |
| **Campaign B (Treatment)** | Influencer Video Ads — Social Media |
| **Goal** | Determine which campaign delivers better ROI and whether the difference is statistically significant |

---

## ❓ Business Question

Which campaign is mathematically more successful — measured by efficiency (CPA), profitability (ROI/ROAS), and statistical rigor — and where should the next marketing dollar go?

---

## 🛠️ Tech Stack

- **Python** (pandas, numpy, scipy/statsmodels) — synthetic data generation + statistical testing
- **SQL** (MySQL / PostgreSQL) — schema design and analytical KPI queries
- **Power BI Desktop** — interactive executive dashboard with DAX measures
- **Statistics** — two-proportion z-test, p-value, confidence interval, power analysis

---


---

## 🗄️ Data

Two synthetic datasets generated with Python (`numpy` seeded for reproducibility):

- **`daily_metrics.csv`** — one row per campaign per day: `date`, `campaign_id`, `impressions`, `clicks`, `conversions`, `spend`, `revenue`.
- **`user_events.csv`** — one row per click (user): `user_id`, `campaign_id`, `event_date`, `clicked`, `converted`, `order_value`.

---

## 🔍 Analysis Workflow

1. **Generate** realistic synthetic data in Python (different CTR, conversion, and AOV distributions per campaign).
2. **Query** core KPIs in SQL — conversion rate, CPA, CPC, CPM, ROAS, ROI, net profit.
3. **Test** the difference in conversion rates with a two-proportion z-test in Python.
4. **Visualize** everything in a Power BI executive dashboard.
5. **Recommend** a budget decision backed by the numbers.

---

## 📈 Key Results

| Metric | Campaign A (Banner) | Campaign B (Influencer) | Winner |
|---|---|---|---|
| Conversion Rate | 2.50% | 4.20% | **B (+68%)** |
| Cost Per Acquisition | $37.04 | $7.87 | **B (-79%)** |
| Avg Order Value | $65.00 | $82.00 | **B (+26%)** |
| ROAS | 1.76x | 10.41x | **B** |
| ROI | 75.5% | 941.4% | **B** |

**Statistical validation:** Z ≈ 14.5 · p < 0.0001 · 95% CI does not contain 0 · statistical power ≈ 100%.

---

## ✅ Recommendation

Scale **Campaign B (Influencer Video)** immediately. The evidence is overwhelming (p < 0.0001) that it outperforms banner ads on every metric. Reallocating Campaign A's budget to Campaign B is projected to generate substantial additional net profit over the same period. Sunset Campaign A, iterate on influencer creative, and retest quarterly.

---

## 🚀 How to Run



---

## 🎯 Skills Demonstrated

- A/B testing methodology & hypothesis testing
- Statistical rigor: p-values, confidence intervals, effect size, power analysis
- SQL: aggregation, joins, conditional aggregation, KPI derivation
- Revenue/ROI thinking: ROAS, CPA, ROI, AOV, net profit
- Data visualization & DAX in Power BI
- Business communication: data → decision

---

*Built as a portfolio project to demonstrate an end-to-end analytics workflow: data → SQL → statistics → visualization → business recommendation.*
