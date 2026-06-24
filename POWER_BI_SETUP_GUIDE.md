# Marketing A/B Test - Power BI Setup Guide

## Overview
This guide walks you through connecting your PostgreSQL database to Power BI and creating a comprehensive A/B test dashboard.

---

## PART 1: PREPARE YOUR DATA SOURCE

### Step 1: Export Data from PostgreSQL to CSV (Optional but Recommended)

**Option A: Export from Docker Container**
```bash
# Daily metrics
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY daily_metrics TO STDOUT WITH CSV HEADER" > daily_metrics_export.csv

# User events
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY user_events TO STDOUT WITH CSV HEADER" > user_events_export.csv

# Campaigns
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY campaigns TO STDOUT WITH CSV HEADER" > campaigns_export.csv
```

**Option B: Use Adminer Web UI**
1. Open http://localhost:8080
2. Login: Server=`postgres`, User=`marketing_user`, Password=`marketing_pass`
3. Select `marketing_ab_test` database
4. For each table (campaigns, daily_metrics, user_events):
   - Click table name
   - Click "Export" button
   - Choose CSV format
   - Save file

**Option C: Direct PostgreSQL Connection (Recommended)**
- Keep the Docker containers running
- Power BI will connect directly to PostgreSQL on localhost:5432

---

## PART 2: CONNECT TO DATA IN POWER BI

### Step 2A: Direct PostgreSQL Connection (Recommended)

1. **Open Power BI Desktop**

2. **Go to: Home → Get Data → Databases → PostgreSQL Database**

3. **Enter Connection Details:**
   - Server: `localhost` (or `127.0.0.1`)
   - Database: `marketing_ab_test`
   - Data Connectivity mode: **Import** (recommended)

4. **Enter Credentials:**
   - Username: `marketing_user`
   - Password: `marketing_pass`

5. **Select Tables:**
   - ☑ campaigns
   - ☑ daily_metrics
   - ☑ user_events
   - Click **Load**

6. **Wait for data to load** (may take 1-2 minutes)

### Step 2B: CSV Import (If Direct Connection Fails)

1. **For each CSV file:**
   - Home → Get Data → Text/CSV
   - Select the file (daily_metrics_export.csv, user_events_export.csv, campaigns_export.csv)
   - Click **Load**

---

## PART 3: CREATE DATA MODEL

### Step 3: Set Up Relationships

1. **Go to: Model view** (left sidebar)

2. **Create Relationships:**
   - **daily_metrics → campaigns**
     - From: `daily_metrics.campaign_id`
     - To: `campaigns.campaign_id`
     - Click **Create**

   - **user_events → campaigns**
     - From: `user_events.campaign_id`
     - To: `campaigns.campaign_id`
     - Click **Create**

3. **Verify relationships:** You should see connection lines between tables

4. **Back to Report view** (left sidebar)

---

## PART 4: CREATE CALCULATED COLUMNS & MEASURES

### Step 4: Add Measures for Analysis

1. **Click on `daily_metrics` table** in Fields panel

2. **Home → New Measure** and add each:

#### Measure 1: Total Revenue
```DAX
Total Revenue = SUM(daily_metrics[revenue])
```

#### Measure 2: Total Spend
```DAX
Total Spend = SUM(daily_metrics[spend])
```

#### Measure 3: Total Conversions
```DAX
Total Conversions = SUM(daily_metrics[conversions])
```

#### Measure 4: Total Clicks
```DAX
Total Clicks = SUM(daily_metrics[clicks])
```

#### Measure 5: Total Impressions
```DAX
Total Impressions = SUM(daily_metrics[impressions])
```

#### Measure 6: Click-Through Rate (%)
```DAX
CTR % = DIVIDE([Total Clicks], [Total Impressions], 0) * 100
```

#### Measure 7: Conversion Rate (%)
```DAX
Conversion Rate % = DIVIDE([Total Conversions], [Total Clicks], 0) * 100
```

#### Measure 8: Cost Per Click (CPC)
```DAX
CPC = DIVIDE([Total Spend], [Total Clicks], 0)
```

#### Measure 9: Cost Per Acquisition (CPA)
```DAX
CPA = DIVIDE([Total Spend], [Total Conversions], 0)
```

#### Measure 10: Return on Ad Spend (ROAS)
```DAX
ROAS = DIVIDE([Total Revenue], [Total Spend], 0)
```

#### Measure 11: Return on Investment (ROI %)
```DAX
ROI % = DIVIDE(([Total Revenue] - [Total Spend]), [Total Spend], 0) * 100
```

#### Measure 12: Net Profit
```DAX
Net Profit = [Total Revenue] - [Total Spend]
```

#### Measure 13: Average Order Value (AOV)
```DAX
AOV = DIVIDE([Total Revenue], [Total Conversions], 0)
```

#### Measure 14: Cost Per Thousand Impressions (CPM)
```DAX
CPM = DIVIDE([Total Spend], [Total Impressions], 0) * 1000
```

---

## PART 5: CREATE VISUALIZATIONS

### Page 1: Executive Summary Dashboard

#### Card 1: Campaign Names
- Visualization: **Card**
- Field: `campaigns[campaign_name]`
- (Create 2 cards, one per campaign)

#### Card 2: Total Revenue by Campaign
- Visualization: **Card**
- Field: `[Total Revenue]`
- Filters: Campaign A & B (separate cards)
- Format: Currency

#### Card 3: ROI % by Campaign
- Visualization: **Card**
- Field: `[ROI %]`
- Filters: Campaign A & B (separate cards)
- Format: Percentage

#### Card 4: Conversion Rate by Campaign
- Visualization: **Card**
- Field: `[Conversion Rate %]`
- Filters: Campaign A & B (separate cards)
- Format: Percentage

### Visualization 1: Campaign Performance Comparison (Clustered Bar Chart)

**Settings:**
- X-axis: `campaigns[campaign_name]`
- Y-axis: Add multiple:
  - `[Total Revenue]` (Blue)
  - `[Total Spend]` (Orange)
  - `[Net Profit]` (Green)
- Title: "Revenue vs Spend vs Profit by Campaign"
- Format: Set Y-axis to Currency

### Visualization 2: Daily Revenue Trend (Line Chart)

**Settings:**
- X-axis: `daily_metrics[date]`
- Y-axis: `[Total Revenue]`
- Legend: `campaigns[campaign_name]`
- Title: "Daily Revenue Trend"
- Line style: Smooth

### Visualization 3: Conversion Rate Comparison (Clustered Column Chart)

**Settings:**
- X-axis: `campaigns[campaign_name]`
- Y-axis: `[Conversion Rate %]`
- Color: By campaign
- Data labels: On
- Title: "Conversion Rate Comparison (%)"

### Visualization 4: ROI Comparison (Gauge)

**Settings:**
- Value: `[ROI %]`
- Filters: Use two gauges (one per campaign)
- Min value: 0
- Max value: 1000
- Title: "ROI % - Campaign A" (and B)

### Visualization 5: Key Metrics Table (Matrix)

**Settings:**
- Rows: `campaigns[campaign_name]`
- Values:
  - `[Total Clicks]`
  - `[Total Conversions]`
  - `[Conversion Rate %]`
  - `[Total Spend]`
  - `[Total Revenue]`
  - `[CPA]`
  - `[ROAS]`
  - `[ROI %]`
- Title: "Complete Performance Metrics"
- Format numbers appropriately

---

### Page 2: Deep Dive Analysis

### Visualization 6: Funnel Chart (Impressions → Clicks → Conversions)

**Settings:**
- Category: `campaigns[campaign_name]`
- Values (in order):
  - `[Total Impressions]`
  - `[Total Clicks]`
  - `[Total Conversions]`
- Title: "Marketing Funnel"
- Format: Show percentages

### Visualization 7: Cost Metrics Comparison (Clustered Bar)

**Settings:**
- X-axis: `campaigns[campaign_name]`
- Y-axis: Add multiple:
  - `[CPC]` (Cost Per Click)
  - `[CPA]` (Cost Per Acquisition)
  - `[CPM]` (Cost Per 1000 Impressions)
- Title: "Cost Efficiency Metrics"
- Data labels: On

### Visualization 8: Revenue Distribution by Campaign (Pie Chart)

**Settings:**
- Legend: `campaigns[campaign_name]`
- Values: `[Total Revenue]`
- Data labels: Show percentages
- Title: "Revenue Distribution"

### Visualization 9: Daily Conversions Trend (Area Chart)

**Settings:**
- X-axis: `daily_metrics[date]`
- Y-axis: `[Total Conversions]`
- Legend: `campaigns[campaign_name]`
- Area styling: Stacked
- Title: "Daily Conversions Trend"

### Visualization 10: Spend Efficiency (Scatter)

**Settings:**
- X-axis: `[Total Spend]`
- Y-axis: `[Total Revenue]`
- Legend: `campaigns[campaign_name]`
- Size: `[Net Profit]`
- Title: "Spend Efficiency Analysis"

---

### Page 3: Statistical Summary

### Visualization 11: Summary Stats Text Box

Add a Text Box with:
```
A/B TEST RESULTS SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CAMPAIGN PERFORMANCE

Campaign A: Banner Ads
• Clicks: 53,550 | Conversions: 1,345 | Conv Rate: 2.51%
• Spend: $50,057 | Revenue: $86,414 | ROI: 72.6%

Campaign B: Influencer Video
• Clicks: 149,302 | Conversions: 6,350 | Conv Rate: 4.25%
• Spend: $50,349 | Revenue: $514,139 | ROI: 921.2%

STATISTICAL SIGNIFICANCE
• Z-statistic: 18.72 (Highly Significant)
• P-value: < 0.0001 (reject null hypothesis)
• Relative Lift: 74% improvement
• Statistical Power: 100%

RECOMMENDATION: Scale Campaign B immediately
```

### Visualization 12: Monthly Trend (if using 30-day data)

**Settings:**
- X-axis: `daily_metrics[date]` (grouped by day)
- Y-axis: `[ROI %]`
- Legend: `campaigns[campaign_name]`
- Title: "Daily ROI Trend"

---

## PART 6: ADD INTERACTIVITY

### Step 5: Add Slicers

1. **Insert → Slicer**

2. **Slicer 1: Campaign Filter**
   - Field: `campaigns[campaign_name]`
   - Apply to all visuals on page
   - Title: "Select Campaign"

3. **Slicer 2: Date Range Filter**
   - Field: `daily_metrics[date]`
   - Style: Between
   - Title: "Date Range"

4. **Slicer 3: Channel Filter** (Optional)
   - Field: `campaigns[channel]`
   - Title: "Select Channel"

---

## PART 7: FORMAT & POLISH

### Step 6: Apply Formatting

1. **For all card visuals:**
   - Format → Card → Data label size: 28pt
   - Category label: Campaign name
   - Show title: Yes

2. **For all charts:**
   - Title font size: 14pt, Bold
   - Legend position: Top
   - Data labels: ON for comparisons

3. **Color scheme:**
   - Campaign A (Banner): Blue (#2196F3)
   - Campaign B (Influencer): Green (#4CAF50)
   - Revenue: Gold (#FFD700)
   - Profit: Green (#00C853)

4. **Add page titles:**
   - Insert → Text Box
   - Page 1: "Executive Summary"
   - Page 2: "Detailed Analysis"
   - Page 3: "Statistical Insights"

---

## PART 8: CREATE DRILL-DOWN & TOOLTIPS

### Step 7: Enable Drill-Down

1. **On Daily Revenue Trend chart:**
   - Right-click → Add drill-through page
   - Drill-through fields: `campaigns[campaign_name]`, `daily_metrics[date]`
   - Create new page showing:
     - Daily metrics for selected campaign/date
     - User-level conversions for that day
     - Performance metrics

---

## PART 9: EXPORT & SHARE

### Step 8: Publish to Power BI Service

1. **File → Publish**
2. **Select workspace** where you want to publish
3. **Provide report name:** "Marketing A/B Test Dashboard"
4. **Share with team members:**
   - Power BI Service → Share button
   - Enter email addresses
   - Set permissions (View/Edit)

---

## SQL QUERIES FOR ADDITIONAL INSIGHTS

### Query 1: Daily Performance by Campaign
```sql
SELECT 
    d.date,
    c.campaign_name,
    d.impressions,
    d.clicks,
    d.conversions,
    ROUND(d.spend::NUMERIC, 2) AS spend,
    ROUND(d.revenue::NUMERIC, 2) AS revenue,
    ROUND(d.clicks::NUMERIC / NULLIF(d.impressions, 0) * 100, 2) AS ctr_pct,
    ROUND(d.conversions::NUMERIC / NULLIF(d.clicks, 0) * 100, 2) AS conversion_rate_pct,
    ROUND((d.revenue - d.spend) / NULLIF(d.spend, 0) * 100, 2) AS daily_roi_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
ORDER BY d.date DESC;
```

### Query 2: User-Level Conversion Analysis
```sql
SELECT 
    c.campaign_name,
    COUNT(DISTINCT ue.user_id) AS total_users,
    SUM(CASE WHEN ue.converted THEN 1 ELSE 0 END) AS conversions,
    ROUND(SUM(CASE WHEN ue.converted THEN 1 ELSE 0 END)::NUMERIC / 
          COUNT(DISTINCT ue.user_id) * 100, 2) AS conversion_rate_pct,
    ROUND(AVG(CASE WHEN ue.converted THEN ue.order_value ELSE 0 END), 2) AS avg_order_value
FROM user_events ue
JOIN campaigns c ON ue.campaign_id = c.campaign_id
GROUP BY c.campaign_name;
```

### Query 3: Week-over-Week Comparison
```sql
SELECT 
    c.campaign_name,
    EXTRACT(WEEK FROM d.date) AS week,
    SUM(d.impressions) AS weekly_impressions,
    SUM(d.clicks) AS weekly_clicks,
    SUM(d.conversions) AS weekly_conversions,
    ROUND(SUM(d.spend), 2) AS weekly_spend,
    ROUND(SUM(d.revenue), 2) AS weekly_revenue,
    ROUND((SUM(d.revenue) - SUM(d.spend)) / NULLIF(SUM(d.spend), 0) * 100, 2) AS weekly_roi_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
GROUP BY c.campaign_name, EXTRACT(WEEK FROM d.date)
ORDER BY week DESC;
```

---

## TROUBLESHOOTING

### Issue: Cannot connect to PostgreSQL from Power BI

**Solution:**
1. Ensure Docker container is running: `docker ps`
2. Verify PostgreSQL is accessible: `docker logs marketing_db`
3. Check firewall: Port 5432 should be open
4. Use CSV import method as fallback

### Issue: Data not refreshing

**Solution:**
1. Refresh data: Ctrl + R (or Home → Refresh)
2. Set refresh schedule: File → Options → Data Refresh
3. Recommended: Daily refresh at 2 AM

### Issue: Performance is slow

**Solution:**
1. Use **Import mode** instead of DirectQuery
2. Create aggregations on daily_metrics table
3. Reduce date range in slicers

---

## DASHBOARD LAYOUT RECOMMENDATION

### Page 1: Executive Summary (3 rows)
```
[Campaign A Cards]          [Campaign B Cards]
[Revenue vs Spend Chart]    [ROI Comparison]
[Daily Trend Line]          [Key Metrics Table]
```

### Page 2: Analysis (2 rows)
```
[Funnel Chart]              [Cost Metrics]
[Conversions Trend]         [Spend Efficiency]
```

### Page 3: Insights (1 row)
```
[Statistical Summary]       [ROI Trend]
```

---

## KEY METRICS TO MONITOR

| Metric | Good Range | Target | Campaign A | Campaign B |
|--------|-----------|--------|-----------|-----------|
| CTR % | 1-5% | > 2% | 1.64% | 2.91% |
| Conversion Rate % | 2-5% | > 3% | 2.51% | 4.25% |
| CPA | $10-$50 | < $20 | $37.22 | $7.93 |
| ROAS | 1.5x-5x | > 2x | 1.73x | 10.21x |
| ROI % | 50-200% | > 100% | 72.6% | 921.2% |

---

## NEXT STEPS

1. ✅ Connect to data (PostgreSQL or CSV)
2. ✅ Create calculated measures (DAX formulas)
3. ✅ Build visualizations (charts & cards)
4. ✅ Add interactivity (slicers & drill-through)
5. ✅ Format & theme (colors & fonts)
6. ✅ Publish to Power BI Service
7. ✅ Share with stakeholders
8. ✅ Set up automatic refresh schedule

---

## POWER BI FILE STRUCTURE

Save your Power BI file as:
```
Marketing_AB_Test_Dashboard.pbix
```

Backup location: Cloud (OneDrive/SharePoint)

---

**Questions?** Refer to Power BI docs: https://docs.microsoft.com/power-bi/
