# Marketing A/B Test Data Explanation & Power BI Details

## PART A: UNDERSTANDING YOUR DATA

---

## 1. THE THREE TABLES EXPLAINED

### Table 1: CAMPAIGNS
**Purpose:** Store campaign metadata and budget information

```
campaign_id (PK) | campaign_name              | campaign_type | channel          | start_date | end_date   | budget
─────────────────┼────────────────────────────┼───────────────┼──────────────────┼────────────┼────────────┼───────────
1                | Summer Sale Banner Ads     | Display       | Google Display   | 2024-06-01 | 2024-06-30 | 50,000.00
2                | Influencer Video Campaign  | Video Ad      | Instagram/TikTok | 2024-06-01 | 2024-06-30 | 50,000.00
```

**Fields Explained:**
- `campaign_id`: Unique identifier (links to other tables)
- `campaign_name`: Human-readable name for reporting
- `campaign_type`: Type of ad (Display, Video, Search, etc.)
- `channel`: Platform where ads run (Google, Facebook, Instagram, etc.)
- `start_date`: Campaign launch date
- `end_date`: Campaign end date
- `budget`: Total allocated budget for campaign

**In Power BI:** Use for filtering and labeling visuals

---

### Table 2: DAILY_METRICS (Most Important!)
**Purpose:** Aggregated daily performance data per campaign

```
date       | campaign_id | impressions | clicks | conversions | spend      | revenue
───────────┼─────────────┼─────────────┼────────┼─────────────┼────────────┼────────────
2024-06-01 | 1           | 118,956     | 1,952  | 47          | 1,665.42   | 3,055.00
2024-06-01 | 2           | 179,243     | 5,234  | 220         | 1,663.55   | 18,040.00
2024-06-02 | 1           | 121,043     | 1,843  | 48          | 1,671.33   | 3,120.00
2024-06-02 | 2           | 182,654     | 5,876  | 248         | 1,658.02   | 20,304.00
...        | ...         | ...         | ...    | ...         | ...        | ...
```

**Fields Explained:**
- `date`: Date of metrics (30 days: June 1-30)
- `campaign_id`: Links to campaigns table
- `impressions`: Times your ad was shown
  - Example: 118,956 means 118k+ people saw the ad
- `clicks`: People who clicked on the ad
  - Click-Through Rate (CTR) = clicks / impressions
- `conversions`: People who completed purchase after clicking
  - Conversion Rate = conversions / clicks
- `spend`: Money spent on ads that day ($)
- `revenue`: Money earned from sales ($)

**Sample Calculations from Daily Data:**
```
Day 1, Campaign A:
- CTR = 1,952 clicks / 118,956 impressions = 1.64%
- Conversion Rate = 47 conversions / 1,952 clicks = 2.41%
- CPC = $1,665.42 spend / 1,952 clicks = $0.85
- CPA = $1,665.42 spend / 47 conversions = $35.43
- ROAS = $3,055.00 revenue / $1,665.42 spend = 1.84x
- ROI = ($3,055 - $1,665.42) / $1,665.42 = 83.4%
```

**30-Day Totals (Sample):**
```
Campaign A (Banner Ads):
- Total Impressions: ~3.6 million
- Total Clicks: ~53,550
- Total Conversions: ~1,345
- Total Spend: $50,057
- Total Revenue: $86,414
- Avg Daily Revenue: $2,880

Campaign B (Influencer Video):
- Total Impressions: ~5.4 million
- Total Clicks: ~149,302
- Total Conversions: ~6,350
- Total Spend: $50,349
- Total Revenue: $514,139
- Avg Daily Revenue: $17,138
```

---

### Table 3: USER_EVENTS (Granular Data)
**Purpose:** Individual user-level action tracking

```
user_id | campaign_id | event_date | clicked | converted | order_value
────────┼─────────────┼────────────┼─────────┼───────────┼─────────────
1       | 1           | 2024-06-01 | TRUE    | TRUE      | 64.50
2       | 1           | 2024-06-01 | TRUE    | FALSE     | 0.00
3       | 2           | 2024-06-01 | TRUE    | TRUE      | 82.15
4       | 1           | 2024-06-01 | TRUE    | TRUE      | 65.75
5       | 2           | 2024-06-01 | TRUE    | FALSE     | 0.00
...     | ...         | ...        | ...     | ...       | ...
```

**Fields Explained:**
- `user_id`: Unique person (202,852 total users tracked)
- `campaign_id`: Which campaign they saw
- `event_date`: Date they clicked ad
- `clicked`: Did they click? (always TRUE in this table)
- `converted`: Did they purchase?
- `order_value`: How much they spent ($)

**Statistical Analysis from User Data:**
```
Campaign A Users:
- 53,550 total clicks
- 1,345 conversions
- Conversion Rate: 2.51%
- Avg Order Value: $64.25

Campaign B Users:
- 149,302 total clicks
- 6,350 conversions
- Conversion Rate: 4.25%
- Avg Order Value: $80.97

Difference:
- Campaign B has 74% higher conversion rate
- Campaign B has 26% higher average order value
- Campaign B has 2.79x more total conversions
```

---

## PART B: KEY METRICS EXPLAINED

### 1. IMPRESSIONS
**Definition:** Number of times your ad appeared on screen

**Why it matters:** 
- Shows reach/visibility
- Base for all other metrics

**Example:**
- Campaign A: 3.6M impressions (seen 3.6 million times)
- Campaign B: 5.4M impressions (seen 5.4 million times)

---

### 2. CLICKS
**Definition:** People who clicked on your ad

**Why it matters:**
- Shows interest level
- Measures ad appeal

**Calculation:**
```
Campaign A: 53,550 clicks from 3.6M impressions = 1.64% click rate
Campaign B: 149,302 clicks from 5.4M impressions = 2.91% click rate
```

**Insight:** Campaign B's click rate is 78% higher (people more engaged)

---

### 3. CONVERSIONS
**Definition:** People who clicked AND completed purchase

**Why it matters:**
- Actual business outcome
- What you're really measuring in A/B test

**Calculation:**
```
Campaign A: 1,345 conversions from 53,550 clickers = 2.51% conversion rate
Campaign B: 6,350 conversions from 149,302 clickers = 4.25% conversion rate
```

**Insight:** Campaign B converts 1.69x better (more buyers per clicker)

---

### 4. SPEND (Cost)
**Definition:** Money spent on ads

**Why it matters:**
- Budget constraint
- Cost efficiency metric

**Daily Breakdown:**
```
Campaign A: $50,057 over 30 days = $1,669 per day
Campaign B: $50,349 over 30 days = $1,678 per day
(Equal budgets, which is the point of A/B testing)
```

---

### 5. REVENUE (Income)
**Definition:** Total money earned from sales

**Why it matters:**
- Top-line business metric
- Directly shows ROI

**Comparison:**
```
Campaign A: $86,414 revenue
Campaign B: $514,139 revenue
Difference: Campaign B earned 496% MORE revenue
```

**Per Conversion Revenue (AOV - Average Order Value):**
```
Campaign A: $86,414 / 1,345 conversions = $64.25 per order
Campaign B: $514,139 / 6,350 conversions = $80.97 per order
```

---

### 6. CLICK-THROUGH RATE (CTR)
**Formula:** (Clicks / Impressions) × 100

**Campaign A:** (53,550 / 3,600,000) × 100 = 1.49%
**Campaign B:** (149,302 / 5,400,000) × 100 = 2.77%

**What it means:**
- Campaign A: Out of 100 people who saw the ad, ~1-2 clicked
- Campaign B: Out of 100 people who saw the ad, ~2-3 clicked
- Campaign B gets 86% more clicks per impression

**Good CTR Ranges:**
- Display ads: 0.5-2% (Campaign A is good)
- Video ads: 2-5% (Campaign B is excellent)

---

### 7. CONVERSION RATE
**Formula:** (Conversions / Clicks) × 100

**Campaign A:** (1,345 / 53,550) × 100 = 2.51%
**Campaign B:** (6,350 / 149,302) × 100 = 4.25%

**What it means:**
- Campaign A: Out of 100 clickers, ~2-3 make purchase
- Campaign B: Out of 100 clickers, ~4-5 make purchase
- Campaign B converts 69% better

**Good Conversion Rate Ranges:**
- E-commerce: 1-3% (Campaign A is average)
- High-intent: 3-5% (Campaign B is strong)

---

### 8. COST PER CLICK (CPC)
**Formula:** Spend / Clicks

**Campaign A:** $50,057 / 53,550 = $0.93 per click
**Campaign B:** $50,349 / 149,302 = $0.34 per click

**What it means:**
- Campaign A costs $0.93 for each click
- Campaign B costs $0.34 for each click
- Campaign B is 64% cheaper per click (more efficient)

**Why?** Influencer ads naturally get more clicks, so cost spreads across more clicks

---

### 9. COST PER ACQUISITION (CPA)
**Formula:** Spend / Conversions

**Campaign A:** $50,057 / 1,345 = $37.22 per conversion
**Campaign B:** $50,349 / 6,350 = $7.93 per conversion

**What it means:**
- To get 1 customer via Campaign A costs $37.22
- To get 1 customer via Campaign B costs $7.93
- Campaign B is 79% cheaper to acquire customers

**Insight:** This is THE key metric for ROI. Lower is better.

**Benchmark:**
- Acceptable: $25-50 per customer (Campaign A borderline)
- Excellent: $5-15 per customer (Campaign B is here!)

---

### 10. AVERAGE ORDER VALUE (AOV)
**Formula:** Revenue / Conversions

**Campaign A:** $86,414 / 1,345 = $64.25 per order
**Campaign B:** $514,139 / 6,350 = $80.97 per order

**What it means:**
- Average customer spends $64.25 (Campaign A)
- Average customer spends $80.97 (Campaign B)
- Campaign B customers spend 26% more per order

**Insight:** Influencer marketing attracts better-quality customers (or shows different products)

---

### 11. RETURN ON AD SPEND (ROAS)
**Formula:** Revenue / Spend

**Campaign A:** $86,414 / $50,057 = 1.73x
**Campaign B:** $514,139 / $50,349 = 10.21x

**What it means:**
- For every $1 spent on Campaign A, earn $1.73 back
- For every $1 spent on Campaign B, earn $10.21 back
- Campaign B generates 490% more value per dollar spent

**Interpretation:**
```
ROAS < 1.0 = Losing money
ROAS 1.0-1.5 = Break-even (not good)
ROAS 1.5-3.0 = Healthy (what you want)
ROAS 3.0-5.0 = Excellent
ROAS > 5.0 = Exceptional

Campaign A: 1.73x = Good
Campaign B: 10.21x = Exceptional!
```

---

### 12. RETURN ON INVESTMENT (ROI)
**Formula:** (Revenue - Spend) / Spend × 100

**Campaign A:** ($86,414 - $50,057) / $50,057 × 100 = 72.6%
**Campaign B:** ($514,139 - $50,349) / $50,349 × 100 = 921.2%

**What it means:**
- Campaign A brings back $0.73 profit for every $1 spent
- Campaign B brings back $9.21 profit for every $1 spent
- Campaign B is 1169% more profitable

**Business Impact:**
```
If you had $100,000 budget:
Campaign A profit: $100,000 × 72.6% = $72,600 profit
Campaign B profit: $100,000 × 921.2% = $921,200 profit

Difference: $848,600 additional profit by choosing Campaign B
```

---

### 13. COST PER THOUSAND IMPRESSIONS (CPM)
**Formula:** (Spend / Impressions) × 1000

**Campaign A:** ($50,057 / 3,600,000) × 1000 = $13.91 CPM
**Campaign B:** ($50,349 / 5,400,000) × 1000 = $9.32 CPM

**What it means:**
- Showing ads to 1000 people costs $13.91 (Campaign A)
- Showing ads to 1000 people costs $9.32 (Campaign B)
- Campaign B is 33% cheaper on reach

---

### 14. NET PROFIT
**Formula:** Revenue - Spend

**Campaign A:** $86,414 - $50,057 = $36,357 profit
**Campaign B:** $514,139 - $50,349 = $463,790 profit

**What it means:**
- Campaign A nets $36.4k profit
- Campaign B nets $463.8k profit
- Campaign B is 12.7x more profitable

---

## PART C: STATISTICAL SIGNIFICANCE

### THE A/B TEST QUESTION
**Question:** Is Campaign B *actually* better, or just lucky?

**Answer:** Two-Proportion Z-Test

```
STATISTICAL RESULTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Campaign A Conversion Rate: 2.41%
Campaign B Conversion Rate: 4.20%
Difference: 1.79 percentage points
Relative Lift: 74% improvement

Z-Statistic: 18.72
P-value: < 0.0001 (extremely significant)
95% Confidence Interval: [1.60%, 1.97%]

CONCLUSION: Campaign B is definitively better
(99.99% confidence, not just random luck)
```

### WHAT THIS MEANS
- **P-value < 0.05:** Result is statistically significant (we reject null hypothesis)
- **P-value < 0.0001:** Result is highly statistically significant
- **Confidence Interval doesn't cross 0:** Difference is real

### STATISTICAL POWER
```
Power: 100% (exceeds 80% threshold)
Sample Size Required: 1,544 per group
Actual Sample Size: 53,550 (Campaign A), 149,302 (Campaign B)
Status: More than adequately powered
```

**Translation:** We have massive sample sizes, so results are rock solid.

---

## PART D: POWER BI VISUALIZATION STRATEGY

### Dashboard Purpose
**Goal:** Enable stakeholders to quickly see:
1. ✅ Campaign B is clearly superior
2. ✅ All key metrics at a glance
3. ✅ Visual proof via multiple angles
4. ✅ Data is statistically valid
5. ✅ Business recommendation is sound

### Visualization Choices & Why

#### 1. CARDS (Key Metrics)
**Why:** 
- Immediate eye-catching numbers
- No mental math required
- Best for C-level executives

**Metrics to show:**
- Revenue (biggest differentiator)
- ROI % (most important for business)
- Conversion Rate % (core A/B test metric)
- CPA (cost efficiency)

---

#### 2. CLUSTERED COLUMN CHART (Revenue vs Spend)
**Why:**
- Shows absolute difference clearly
- Easy to compare two campaigns
- Revenue towers over spend

**What it shows:**
```
Campaign A: 3 bars (Revenue, Spend, Profit)
Campaign B: 3 bars (Revenue is MUCH taller)
Visual Impact: Campaign B dominates
```

---

#### 3. LINE CHART (Daily Trends)
**Why:**
- Shows consistency over time
- Trending up/down visible
- Timeline context

**What it shows:**
```
Green line (Campaign B): Always above blue line
Pattern: Campaign B consistent winner across all 30 days
```

---

#### 4. COLUMN CHART (Conversion Rate)
**Why:**
- Directly shows A/B test result
- Percentage easy to understand
- Data labels for precision

**What it shows:**
```
Campaign A bar: 2.51%
Campaign B bar: 4.25%
Visual: B is clearly taller (69% higher)
```

---

#### 5. MATRIX/TABLE (All Metrics)
**Why:**
- Complete reference
- Allows sorting/filtering
- For analysts to deep-dive

**Rows:** Campaign names
**Columns:** All KPIs (Clicks, Conversions, Spend, Revenue, CPA, ROAS, ROI, etc.)

---

#### 6. FUNNEL CHART (Conversion Funnel)
**Why:**
- Shows drop-off at each stage
- Visual representation of optimization
- Identifies where to improve

**Stages:**
```
Campaign A: 3.6M → 53K → 1.3K (steep drop-off)
Campaign B: 5.4M → 149K → 6.3K (better retention)
```

---

#### 7. SCATTER PLOT (Spend Efficiency)
**Why:**
- Shows efficiency frontier
- Revenue vs Spend relationship
- Bubble size = profit

**Interpretation:**
```
Campaign B: High spend, even higher revenue (upper right)
Campaign A: High spend, lower revenue (lower left)
```

---

## PART E: KEY INSIGHTS FROM DATA

### Finding 1: Volume Difference
```
Campaign B generates 2.79x more conversions:
Campaign A: 1,345 conversions
Campaign B: 6,350 conversions

Why? Better targeting, more engaging creative, influencer trust
```

### Finding 2: Quality Difference
```
Campaign B has higher AOV (+26%):
Campaign A: $64.25 average order
Campaign B: $80.97 average order

Why? Influencer followers have higher purchasing power
```

### Finding 3: Efficiency Difference
```
Campaign B costs 79% less to acquire customer:
Campaign A: $37.22 CPA
Campaign B: $7.93 CPA

Why? More conversions spread costs across more buyers
```

### Finding 4: Profitability Difference
```
Campaign B is 12.7x more profitable:
Campaign A: $36,357 net profit
Campaign B: $463,790 net profit

Why? Combination of all above factors
```

---

## PART F: BUSINESS RECOMMENDATIONS

### IMMEDIATE ACTION (Week 1)
```
1. PAUSE Campaign A (Banner Ads)
   - Performance is acceptable but inferior
   - Budget being wasted
   - Cost: Opportunity loss of $36k/month

2. DOUBLE Campaign B budget to $100k
   - Still highly profitable at scale
   - Test audience expansion
   - Expected profit: $900k+/month
```

### MEDIUM TERM (Month 2-3)
```
3. TEST Campaign B variations
   - Different influencers
   - Different product angles
   - Different landing pages
   - Goal: Find optimal version

4. A/B TEST Campaign B itself
   - Creative variant 1 vs 2
   - Audience segment 1 vs 2
   - Landing page 1 vs 2

5. MONITOR for diminishing returns
   - Watch CPA as budget scales
   - May decrease (more efficient) or increase (market saturation)
   - Track weekly performance
```

### LONG TERM (Quarter 2)
```
6. EXPAND winning formula
   - Roll out to new platforms
   - Test similar influencers
   - Expand audience size

7. QUARTERLY RETEST
   - Market dynamics change
   - Refresh validation quarterly
   - Stay competitive
```

---

## PART G: POWER BI SPECIFIC CALCULATIONS

### All DAX Formulas Used

```DAX
// Aggregations
Total Revenue = SUM(daily_metrics[revenue])
Total Spend = SUM(daily_metrics[spend])
Total Conversions = SUM(daily_metrics[conversions])
Total Clicks = SUM(daily_metrics[clicks])
Total Impressions = SUM(daily_metrics[impressions])

// Rates (as percentages)
CTR % = DIVIDE([Total Clicks], [Total Impressions], 0) * 100
Conversion Rate % = DIVIDE([Total Conversions], [Total Clicks], 0) * 100

// Costs (per unit)
CPC = DIVIDE([Total Spend], [Total Clicks], 0)
CPA = DIVIDE([Total Spend], [Total Conversions], 0)
CPM = DIVIDE([Total Spend], [Total Impressions], 0) * 1000

// Efficiency Ratios
ROAS = DIVIDE([Total Revenue], [Total Spend], 0)
ROI % = DIVIDE(([Total Revenue] - [Total Spend]), [Total Spend], 0) * 100

// Average Value
AOV = DIVIDE([Total Revenue], [Total Conversions], 0)

// Profit
Net Profit = [Total Revenue] - [Total Spend]
```

### Filter Contexts
- Campaign filter affects all metrics
- Date filter affects daily trends
- Channel filter optional (both same channel in this case)

---

**Ready to build your Power BI dashboard! Follow the steps in POWER_BI_SETUP_GUIDE.md**
