# Power BI Export Scripts & Data Samples

## QUICK START: EXPORT DATA FOR POWER BI

### Method 1: Docker Command Line (Fastest)

**Step 1: Open Command Prompt or PowerShell**

**Step 2: Run these commands (one at a time):**

#### Export Campaigns Table
```bash
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY campaigns TO STDOUT WITH CSV HEADER" > campaigns.csv
```

#### Export Daily Metrics Table
```bash
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY daily_metrics TO STDOUT WITH CSV HEADER" > daily_metrics.csv
```

#### Export User Events Table
```bash
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY user_events TO STDOUT WITH CSV HEADER" > user_events.csv
```

**Result:** Three CSV files appear in your current folder

---

### Method 2: Using Adminer Web UI

**Step 1: Open http://localhost:8080**

**Step 2: Login with credentials:**
- Server: `postgres`
- User: `marketing_user`
- Password: `marketing_pass`
- Database: `marketing_ab_test`

**Step 3: For each table:**
- Click table name in left sidebar
- Click "Export" button (top right)
- Choose "CSV" format
- Click "Export"
- File downloads automatically

---

### Method 3: Direct SQL Query (Advanced)

**In PgAdmin or psql:**

```sql
-- Export campaigns
COPY campaigns TO '/tmp/campaigns.csv' WITH CSV HEADER;

-- Export daily metrics
COPY daily_metrics TO '/tmp/daily_metrics.csv' WITH CSV HEADER;

-- Export user events
COPY user_events TO '/tmp/user_events.csv' WITH CSV HEADER;
```

Then copy files from container:
```bash
docker cp marketing_db:/tmp/campaigns.csv .
docker cp marketing_db:/tmp/daily_metrics.csv .
docker cp marketing_db:/tmp/user_events.csv .
```

---

## DATA SAMPLES FOR REFERENCE

### Sample 1: CAMPAIGNS TABLE
```
campaign_id,campaign_name,campaign_type,channel,start_date,end_date,budget
1,Summer Sale Banner Ads,Display Banner,Google Display,2024-06-01,2024-06-30,50000.00
2,Influencer Video Campaign,Video Ad,Instagram/TikTok,2024-06-01,2024-06-30,50000.00
```

---

### Sample 2: DAILY_METRICS TABLE (First 10 rows)
```
date,campaign_id,impressions,clicks,conversions,spend,revenue
2024-06-01,1,118956,1952,47,1665.42,3055.00
2024-06-01,2,179243,5234,220,1663.55,18040.00
2024-06-02,1,121043,1843,48,1671.33,3120.00
2024-06-02,2,182654,5876,248,1658.02,20304.00
2024-06-03,1,119234,1876,45,1667.89,2925.00
2024-06-03,2,178912,5245,216,1671.05,17712.00
2024-06-04,1,120654,1954,51,1672.11,3315.00
2024-06-04,2,181234,5312,228,1664.23,18684.00
2024-06-05,1,118765,1823,42,1668.45,2730.00
2024-06-05,2,179876,5876,252,1660.77,20664.00
```

---

### Sample 3: USER_EVENTS TABLE (First 20 rows)
```
user_id,campaign_id,event_date,clicked,converted,order_value
1,1,2024-06-01,true,true,64.50
2,1,2024-06-01,true,false,0.00
3,2,2024-06-01,true,true,82.15
4,1,2024-06-01,true,true,65.75
5,2,2024-06-01,true,false,0.00
6,1,2024-06-01,true,true,63.45
7,2,2024-06-01,true,true,81.25
8,1,2024-06-01,true,false,0.00
9,2,2024-06-01,true,true,79.95
10,1,2024-06-01,true,true,66.20
11,2,2024-06-01,true,false,0.00
12,1,2024-06-01,true,true,62.85
13,2,2024-06-01,true,true,83.40
14,1,2024-06-01,true,false,0.00
15,2,2024-06-01,true,true,81.75
16,1,2024-06-01,true,true,65.30
17,2,2024-06-01,true,false,0.00
18,1,2024-06-01,true,true,63.95
19,2,2024-06-01,true,true,80.50
20,1,2024-06-01,true,true,64.80
```

---

## SUMMARY STATISTICS FOR POWER BI VALIDATION

### Expected Results After Import

**Once you import data into Power BI, verify these totals:**

#### Campaign A (Banner Ads)
```
Total Impressions:        3,634,789
Total Clicks:            53,550
Total Conversions:        1,345
Conversion Rate:          2.51%

Total Spend:             $50,057.47
Total Revenue:           $86,414.23
Net Profit:              $36,356.76

Cost Per Click:          $0.93
Cost Per Acquisition:    $37.22
Average Order Value:     $64.25

Click-Through Rate:      1.47%
ROAS:                    1.73x
ROI:                     72.6%
```

#### Campaign B (Influencer Video)
```
Total Impressions:        5,389,234
Total Clicks:            149,302
Total Conversions:        6,350
Conversion Rate:          4.25%

Total Spend:             $50,348.90
Total Revenue:           $514,139.07
Net Profit:              $463,790.17

Cost Per Click:          $0.34
Cost Per Acquisition:    $7.93
Average Order Value:     $80.97

Click-Through Rate:      2.77%
ROAS:                    10.21x
ROI:                     921.2%
```

---

## POWER BI IMPORT CHECKLIST

- [ ] Downloaded all 3 CSV files (or connected to PostgreSQL)
- [ ] Opened Power BI Desktop
- [ ] Imported campaigns.csv
- [ ] Imported daily_metrics.csv
- [ ] Imported user_events.csv
- [ ] Created relationships:
  - [ ] daily_metrics.campaign_id → campaigns.campaign_id
  - [ ] user_events.campaign_id → campaigns.campaign_id
- [ ] Created 14 DAX measures
- [ ] Built executive summary page
- [ ] Built detailed analysis page
- [ ] Built statistics summary page
- [ ] Added slicers (campaign, date range)
- [ ] Applied color theme
- [ ] Saved file as "Marketing_AB_Test_Dashboard.pbix"
- [ ] Tested all filters work correctly
- [ ] Published to Power BI Service (optional)

---

## ADVANCED SQL QUERIES FOR DEEPER ANALYSIS

### Query 1: Day-by-Day Performance
```sql
SELECT 
    d.date,
    c.campaign_name,
    d.impressions,
    d.clicks,
    d.conversions,
    ROUND(d.spend::NUMERIC, 2) AS spend,
    ROUND(d.revenue::NUMERIC, 2) AS revenue,
    ROUND(CAST(d.clicks AS NUMERIC) / NULLIF(d.impressions, 0) * 100, 2) AS ctr_pct,
    ROUND(CAST(d.conversions AS NUMERIC) / NULLIF(d.clicks, 0) * 100, 2) AS conversion_pct,
    ROUND((d.revenue - d.spend) / NULLIF(d.spend, 0) * 100, 2) AS daily_roi_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
ORDER BY d.date DESC, c.campaign_id;
```

**Use in Power BI:** Create new table for daily drilldown visualizations

---

### Query 2: Weekly Performance Comparison
```sql
SELECT 
    c.campaign_name,
    DATE_TRUNC('week', d.date)::DATE AS week_start,
    SUM(d.impressions) AS week_impressions,
    SUM(d.clicks) AS week_clicks,
    SUM(d.conversions) AS week_conversions,
    ROUND(SUM(d.spend), 2) AS week_spend,
    ROUND(SUM(d.revenue), 2) AS week_revenue,
    ROUND(CAST(SUM(d.conversions) AS NUMERIC) / NULLIF(SUM(d.clicks), 0) * 100, 2) AS week_conv_rate,
    ROUND((SUM(d.revenue) - SUM(d.spend)) / NULLIF(SUM(d.spend), 0) * 100, 2) AS week_roi_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
GROUP BY c.campaign_name, DATE_TRUNC('week', d.date)
ORDER BY c.campaign_id, DATE_TRUNC('week', d.date) DESC;
```

---

### Query 3: User Conversion Breakdown
```sql
SELECT 
    c.campaign_name,
    COUNT(DISTINCT ue.user_id) AS total_users,
    SUM(CASE WHEN ue.converted THEN 1 ELSE 0 END) AS conversions,
    ROUND(100.0 * SUM(CASE WHEN ue.converted THEN 1 ELSE 0 END) / 
          COUNT(DISTINCT ue.user_id), 2) AS conversion_rate_pct,
    ROUND(AVG(CASE WHEN ue.converted THEN ue.order_value ELSE 0 END), 2) AS avg_converted_value,
    ROUND(SUM(ue.order_value), 2) AS total_customer_value
FROM user_events ue
JOIN campaigns c ON ue.campaign_id = c.campaign_id
GROUP BY c.campaign_name;
```

---

### Query 4: Top Performing Days
```sql
SELECT 
    d.date,
    c.campaign_name,
    d.conversions,
    ROUND(d.revenue, 2) AS daily_revenue,
    ROUND(d.spend, 2) AS daily_spend,
    ROUND((d.revenue - d.spend) / NULLIF(d.spend, 0) * 100, 2) AS daily_roi_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
ORDER BY d.revenue DESC
LIMIT 10;
```

---

### Query 5: Efficiency Metrics Comparison
```sql
SELECT 
    c.campaign_name,
    ROUND(SUM(d.spend) / NULLIF(SUM(d.impressions), 0) * 1000, 2) AS cpm,
    ROUND(SUM(d.spend) / NULLIF(SUM(d.clicks), 0), 2) AS cpc,
    ROUND(SUM(d.spend) / NULLIF(SUM(d.conversions), 0), 2) AS cpa,
    ROUND(SUM(d.revenue) / NULLIF(SUM(d.spend), 0), 3) AS roas,
    ROUND(AVG(d.revenue / NULLIF(d.conversions, 0)), 2) AS aov
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
GROUP BY c.campaign_name;
```

**Result:**
```
campaign_name              | cpm   | cpc  | cpa   | roas  | aov
──────────────────────────┼───────┼──────┼───────┼───────┼──────
Summer Sale Banner Ads    | 13.78 | 0.93 | 37.22 | 1.73  | 64.25
Influencer Video Campaign | 9.34  | 0.34 | 7.93  | 10.21 | 80.97
```

---

## IMPORTING QUERIES INTO POWER BI

### Option A: Create Query in Power BI

1. **Home → Get Data → SQL Server**
2. **Enter:** Server: `localhost` | Database: `marketing_ab_test`
3. **Advanced Options → SQL statement**
4. **Paste query above**
5. **OK → Load**

### Option B: Create View in PostgreSQL

```sql
CREATE VIEW v_daily_performance AS
SELECT 
    d.date,
    c.campaign_name,
    d.impressions,
    d.clicks,
    d.conversions,
    ROUND(d.spend::NUMERIC, 2) AS spend,
    ROUND(d.revenue::NUMERIC, 2) AS revenue,
    ROUND(CAST(d.clicks AS NUMERIC) / NULLIF(d.impressions, 0) * 100, 2) AS ctr_pct,
    ROUND(CAST(d.conversions AS NUMERIC) / NULLIF(d.clicks, 0) * 100, 2) AS conversion_pct,
    ROUND((d.revenue - d.spend) / NULLIF(d.spend, 0) * 100, 2) AS daily_roi_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id;
```

Then import `v_daily_performance` view as table in Power BI

---

## DATA QUALITY CHECKS

Run these queries to validate data integrity:

### Check 1: Row Counts
```sql
SELECT 
    'campaigns' as table_name, COUNT(*) as row_count FROM campaigns
UNION ALL
SELECT 'daily_metrics', COUNT(*) FROM daily_metrics
UNION ALL
SELECT 'user_events', COUNT(*) FROM user_events;
```

**Expected:**
```
campaigns: 2 rows
daily_metrics: 60 rows (30 days × 2 campaigns)
user_events: 202,852 rows
```

### Check 2: Date Range
```sql
SELECT 
    MIN(date) as min_date,
    MAX(date) as max_date,
    COUNT(DISTINCT date) as unique_days
FROM daily_metrics;
```

**Expected:**
```
min_date: 2024-06-01
max_date: 2024-06-30
unique_days: 30
```

### Check 3: Spend Validation
```sql
SELECT 
    c.campaign_name,
    ROUND(SUM(d.spend), 2) AS total_spend,
    ROUND(50000.00, 2) AS budgeted
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
GROUP BY c.campaign_name;
```

**Expected:** Both campaigns spent ~$50,000 (actual: $50,057 and $50,349)

### Check 4: Conversion Logic
```sql
SELECT 
    c.campaign_id,
    COUNT(DISTINCT CASE WHEN ue.converted THEN ue.user_id END) as user_conversions,
    SUM(CASE WHEN d.date = ue.event_date THEN d.conversions ELSE 0 END) as daily_conversions
FROM campaigns c
JOIN user_events ue ON c.campaign_id = ue.campaign_id
JOIN daily_metrics d ON d.campaign_id = c.campaign_id
GROUP BY c.campaign_id;
```

---

## COMMON POWER BI ISSUES & FIXES

### Issue: Data not refreshing
**Fix:**
```
Power BI Desktop: Ctrl + R (manual refresh)
Power BI Service: Settings → Scheduled refresh (set daily)
```

### Issue: Slow loading times
**Fix:**
- Import mode instead of DirectQuery
- Reduce date range in slicers
- Create aggregations on daily_metrics

### Issue: Cannot connect to PostgreSQL
**Fix:**
1. Check Docker is running: `docker ps`
2. Verify container: `docker logs marketing_db`
3. Test connection: 
   ```bash
   psql -h localhost -U marketing_user -d marketing_ab_test
   ```
4. If fails, use CSV method instead

### Issue: Measures show blank/error
**Fix:**
- Check table relationships in Model view
- Verify DAX formula syntax
- Ensure aggregation is correct

---

## NEXT STEPS AFTER POWER BI SETUP

1. ✅ Build dashboard
2. ✅ Verify all data loads correctly
3. ✅ Test all slicers and filters
4. ✅ Save file
5. ✅ Publish to Power BI Service (optional)
6. ✅ Share with team
7. ✅ Set up refresh schedule
8. ✅ Create PDF exports for stakeholders
9. ✅ Schedule weekly data reviews
10. ✅ Monitor performance trends

---

**All data is ready to import. Start with POWER_BI_SETUP_GUIDE.md for step-by-step instructions!**
