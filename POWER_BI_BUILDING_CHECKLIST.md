# 🎯 POWER BI BUILD CHECKLIST - STEP-BY-STEP

## BEFORE YOU START
- [ ] Power BI Desktop installed
- [ ] PostgreSQL Docker running: `docker ps` shows `marketing_db`
- [ ] Downloaded all documentation files
- [ ] 15-20 minutes available

---

## PHASE 1: DATA EXPORT (5 minutes)

### Step 1: Open Terminal/PowerShell
- [ ] Windows: Open PowerShell or Command Prompt
- [ ] Mac: Open Terminal
- [ ] Navigate to project folder: `cd /path/to/marketing-ab-test`

### Step 2: Export Data
```bash
# Copy each command and paste into terminal (one at a time)

# Command 1: Export campaigns
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY campaigns TO STDOUT WITH CSV HEADER" > campaigns.csv

# Command 2: Export daily metrics
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY daily_metrics TO STDOUT WITH CSV HEADER" > daily_metrics.csv

# Command 3: Export user events
docker exec marketing_db psql -U marketing_user -d marketing_ab_test -c "\COPY user_events TO STDOUT WITH CSV HEADER" > user_events.csv
```

- [ ] campaigns.csv created (should be small ~200 bytes)
- [ ] daily_metrics.csv created (should be ~20 KB)
- [ ] user_events.csv created (should be ~15 MB)

---

## PHASE 2: POWER BI SETUP (30 seconds)

### Step 3: Launch Power BI Desktop
- [ ] Open Power BI Desktop application
- [ ] Click "Blank Report"
- [ ] You see empty white canvas

---

## PHASE 3: IMPORT DATA (3 minutes)

### Step 4: Import First CSV (Campaigns)
- [ ] **Home** tab → **Get Data** dropdown
- [ ] Click **Text/CSV**
- [ ] Browse to **campaigns.csv** → Open
- [ ] Data preview shows 2 rows (Campaign A and B)
- [ ] Click **Load**
- [ ] Wait for import complete (~10 seconds)

### Step 5: Import Second CSV (Daily Metrics)
- [ ] **Home** tab → **Get Data** dropdown
- [ ] Click **Text/CSV**
- [ ] Browse to **daily_metrics.csv** → Open
- [ ] Data preview shows 60 rows (30 days × 2 campaigns)
- [ ] Click **Load**
- [ ] Wait for import complete (~30 seconds)

### Step 6: Import Third CSV (User Events)
- [ ] **Home** tab → **Get Data** dropdown
- [ ] Click **Text/CSV**
- [ ] Browse to **user_events.csv** → Open
- [ ] Data preview shows 202,852 rows
- [ ] Click **Load**
- [ ] Wait for import complete (~2 minutes - this is the biggest file)

### After All Three Load
- [ ] Fields panel on right shows 3 tables
- [ ] Each table expandable with column names
- [ ] All data loaded successfully ✓

---

## PHASE 4: CREATE RELATIONSHIPS (2 minutes)

### Step 7: Access Model View
- [ ] Left sidebar: Click **Model** (icon looks like connected nodes)
- [ ] You see 3 tables displayed with columns
- [ ] No lines connecting them yet (we'll add those now)

### Step 8: Create Relationship 1
- [ ] **From:** daily_metrics table
- [ ] Drag **campaign_id** column
- [ ] Drop on **campaign_id** in campaigns table
- [ ] Relationship line appears connecting them
- [ ] Click **Create**

### Step 9: Create Relationship 2
- [ ] **From:** user_events table
- [ ] Drag **campaign_id** column
- [ ] Drop on **campaign_id** in campaigns table
- [ ] Relationship line appears
- [ ] Click **Create**

### Verify Relationships
- [ ] campaigns table is center (hub)
- [ ] Lines connect to both other tables
- [ ] Relationships look correct
- [ ] No error messages

### Step 10: Back to Report
- [ ] Left sidebar: Click **Report** view
- [ ] You're back to white canvas with empty page

---

## PHASE 5: CREATE MEASURES (8 minutes)

### Step 11: Create Aggregation Measures
- [ ] Select **daily_metrics** table in Fields panel
- [ ] **Home** → **New Measure**
- [ ] Name: `Total Revenue`
- [ ] Formula: `= SUM(daily_metrics[revenue])`
- [ ] Press **Enter**
- [ ] Repeat for all 5 aggregations:

```
Total Revenue = SUM(daily_metrics[revenue])
Total Spend = SUM(daily_metrics[spend])
Total Conversions = SUM(daily_metrics[conversions])
Total Clicks = SUM(daily_metrics[clicks])
Total Impressions = SUM(daily_metrics[impressions])
```

- [ ] All 5 measures created

### Step 12: Create Rate Measures
- [ ] **Home** → **New Measure**
- [ ] Name: `CTR %`
- [ ] Formula: `= DIVIDE([Total Clicks], [Total Impressions], 0) * 100`
- [ ] Press **Enter**
- [ ] Repeat for:

```
Conversion Rate % = DIVIDE([Total Conversions], [Total Clicks], 0) * 100
```

- [ ] 2 rate measures created

### Step 13: Create Cost Measures
- [ ] **Home** → **New Measure** for each:

```
CPC = DIVIDE([Total Spend], [Total Clicks], 0)
CPA = DIVIDE([Total Spend], [Total Conversions], 0)
CPM = DIVIDE([Total Spend], [Total Impressions], 0) * 1000
```

- [ ] 3 cost measures created

### Step 14: Create Efficiency Measures
- [ ] **Home** → **New Measure** for each:

```
ROAS = DIVIDE([Total Revenue], [Total Spend], 0)
ROI % = DIVIDE(([Total Revenue] - [Total Spend]), [Total Spend], 0) * 100
```

- [ ] 2 efficiency measures created

### Step 15: Create Additional Measures
- [ ] **Home** → **New Measure** for each:

```
AOV = DIVIDE([Total Revenue], [Total Conversions], 0)
Net Profit = [Total Revenue] - [Total Spend]
```

- [ ] 2 additional measures created

### Verify All Measures
- [ ] Select daily_metrics table
- [ ] Fields panel shows all 14 measures
- [ ] Each measure appears with sigma (Σ) icon
- [ ] No error messages

---

## PHASE 6: BUILD PAGE 1 - EXECUTIVE SUMMARY (12 minutes)

### Step 16: Create Campaign A Revenue Card
- [ ] **Insert** → **Card** (visualization)
- [ ] Card appears on canvas
- [ ] Drag **[Total Revenue]** to card
- [ ] Drag **campaigns[campaign_name]** to card filters
- [ ] Filter to **Campaign A** only
- [ ] Card shows: **$86,414**
- [ ] **Format** → Data label size: **28pt**
- [ ] Move to top-left of page

### Step 17: Create Campaign B Revenue Card
- [ ] **Insert** → **Card**
- [ ] Drag **[Total Revenue]** to card
- [ ] Drag **campaigns[campaign_name]** to card filters
- [ ] Filter to **Campaign B** only
- [ ] Card shows: **$514,139**
- [ ] **Format** → Data label size: **28pt**
- [ ] Move to top-right of page

### Step 18: Create Campaign A ROI Card
- [ ] **Insert** → **Card**
- [ ] Drag **[ROI %]** to card
- [ ] Drag **campaigns[campaign_name]** to card filters
- [ ] Filter to **Campaign A** only
- [ ] Card shows: **72.6%**
- [ ] Move to left side

### Step 19: Create Campaign B ROI Card
- [ ] **Insert** → **Card**
- [ ] Drag **[ROI %]** to card
- [ ] Drag **campaigns[campaign_name]** to card filters
- [ ] Filter to **Campaign B** only
- [ ] Card shows: **921.2%**
- [ ] Move to right side

### Step 20: Create Revenue vs Spend Chart
- [ ] **Insert** → **Clustered Column Chart**
- [ ] X-axis: **campaigns[campaign_name]**
- [ ] Y-axis: **[Total Revenue]** (blue column)
- [ ] Y-axis: Add **[Total Spend]** (orange column)
- [ ] Y-axis: Add **[Net Profit]** (green column)
- [ ] **Format** → Title: "Revenue vs Spend vs Profit"
- [ ] **Format** → Data labels: **ON**
- [ ] Move below cards

### Step 21: Create Daily Revenue Trend
- [ ] **Insert** → **Line Chart**
- [ ] X-axis: **daily_metrics[date]**
- [ ] Y-axis: **[Total Revenue]**
- [ ] Legend: **campaigns[campaign_name]**
- [ ] **Format** → Title: "Daily Revenue Trend"
- [ ] **Format** → Line style: **Smooth**
- [ ] Move to right side

### Step 22: Create Conversion Rate Comparison
- [ ] **Insert** → **Clustered Column Chart**
- [ ] X-axis: **campaigns[campaign_name]**
- [ ] Y-axis: **[Conversion Rate %]**
- [ ] **Format** → Title: "Conversion Rate Comparison (%)"
- [ ] **Format** → Data labels: **ON**
- [ ] Move to bottom

### Step 23: Create Metrics Table
- [ ] **Insert** → **Matrix**
- [ ] Rows: **campaigns[campaign_name]**
- [ ] Values:
  - [ ] [Total Clicks]
  - [ ] [Total Conversions]
  - [ ] [Conversion Rate %]
  - [ ] [Total Spend]
  - [ ] [Total Revenue]
  - [ ] [CPA]
  - [ ] [ROAS]
  - [ ] [ROI %]
- [ ] **Format** → Title: "Complete Performance Metrics"
- [ ] Move to bottom right

### Page 1 Complete ✓
- [ ] 4 cards (Revenue A, B, ROI A, B)
- [ ] 1 clustered column (Revenue vs Spend)
- [ ] 1 line chart (Daily trend)
- [ ] 1 column chart (Conversion rate)
- [ ] 1 matrix (Metrics table)
- [ ] Page layout looks professional

---

## PHASE 7: BUILD PAGE 2 - DEEP DIVE ANALYSIS (8 minutes)

### Step 24: Create New Page
- [ ] Right-click on page tab at bottom
- [ ] **Insert Page**
- [ ] Name: "Detailed Analysis"
- [ ] Click new page tab

### Step 25: Create Funnel Chart
- [ ] **Insert** → **Funnel Chart**
- [ ] Category: **campaigns[campaign_name]**
- [ ] Values (in order):
  - [ ] [Total Impressions]
  - [ ] [Total Clicks]
  - [ ] [Total Conversions]
- [ ] **Format** → Title: "Marketing Funnel"

### Step 26: Create Cost Metrics Chart
- [ ] **Insert** → **Clustered Bar Chart**
- [ ] Y-axis: **campaigns[campaign_name]**
- [ ] X-axis:
  - [ ] [CPC]
  - [ ] [CPA]
  - [ ] [CPM]
- [ ] **Format** → Title: "Cost Efficiency Metrics"
- [ ] **Format** → Data labels: **ON**

### Step 27: Create Scatter Plot
- [ ] **Insert** → **Scatter Chart**
- [ ] X-axis: **[Total Spend]**
- [ ] Y-axis: **[Total Revenue]**
- [ ] Legend: **campaigns[campaign_name]**
- [ ] Size: **[Net Profit]**
- [ ] **Format** → Title: "Spend Efficiency Analysis"

### Page 2 Complete ✓
- [ ] 3 visualizations created
- [ ] Page shows different perspectives

---

## PHASE 8: BUILD PAGE 3 - STATISTICS (3 minutes)

### Step 28: Create New Page
- [ ] Right-click on page tab
- [ ] **Insert Page**
- [ ] Name: "Statistical Insights"

### Step 29: Add Text Box with Findings
- [ ] **Insert** → **Text Box**
- [ ] Type:

```
A/B TEST RESULTS SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Campaign A (Banner Ads)
Conversions: 1,345 | Rate: 2.51%
Revenue: $86,414 | ROI: 72.6%

Campaign B (Influencer Video)
Conversions: 6,350 | Rate: 4.25%
Revenue: $514,139 | ROI: 921.2%

STATISTICAL VALIDATION
Z-statistic: 18.72
P-value: < 0.0001 (99.99% confidence)
Relative Lift: 74% (B is genuinely better)

RECOMMENDATION
Scale Campaign B immediately.
Projected additional profit: $400k+/month
```

- [ ] Text box created
- [ ] Formatted and readable

### Step 30: Add ROI Trend Chart
- [ ] **Insert** → **Line Chart**
- [ ] X-axis: **daily_metrics[date]**
- [ ] Y-axis: **[ROI %]**
- [ ] Legend: **campaigns[campaign_name]**
- [ ] **Format** → Title: "Daily ROI Trend"

### Page 3 Complete ✓
- [ ] Summary text added
- [ ] Trend chart added

---

## PHASE 9: ADD INTERACTIVITY (5 minutes)

### Step 31: Add Campaign Slicer
- [ ] **Insert** → **Slicer**
- [ ] Field: **campaigns[campaign_name]**
- [ ] Position: Top of Page 1
- [ ] **Format** → Title: "Select Campaign"

### Step 32: Add Date Range Slicer
- [ ] **Insert** → **Slicer**
- [ ] Field: **daily_metrics[date]**
- [ ] **Format** → Type: **Between**
- [ ] Position: Top of Page 1
- [ ] **Format** → Title: "Date Range"

### Step 33: Apply Slicers to Visuals
- [ ] Click Campaign slicer
- [ ] Hold Ctrl, click all charts/cards on Page 1
- [ ] Right-click → **Edit Interactions**
- [ ] Set to **Filter**
- [ ] Repeat for date slicer

### Step 34: Test Slicers Work
- [ ] Click Campaign A in slicer
- [ ] All visuals update (revenue drops to $86k)
- [ ] Click Campaign B in slicer
- [ ] All visuals update (revenue shows $514k)
- [ ] Click date range
- [ ] Trend charts update to show selected dates

### Interactivity Complete ✓
- [ ] Slicers work correctly
- [ ] All filters apply as expected

---

## PHASE 10: FORMATTING & POLISH (5 minutes)

### Step 35: Apply Color Theme
- [ ] **View** → **Themes** dropdown
- [ ] Choose **Blue Teal** or **Executive**
- [ ] All visuals get professional color scheme

### Step 36: Add Page Titles
- [ ] Each page: **Insert** → **Text Box**
- [ ] Page 1: "Executive Summary"
- [ ] Page 2: "Detailed Analysis"
- [ ] Page 3: "Statistical Insights"
- [ ] Format: Bold, 18pt font, centered

### Step 37: Final Visual Check
- [ ] [ ] All cards show correct values
- [ ] [ ] All charts render properly
- [ ] [ ] Colors are consistent
- [ ] [ ] Titles are readable
- [ ] [ ] Slicers work
- [ ] [ ] No error messages

### Formatting Complete ✓

---

## PHASE 11: SAVE & PUBLISH (3 minutes)

### Step 38: Save File
- [ ] **File** → **Save As**
- [ ] Name: **Marketing_AB_Test_Dashboard.pbix**
- [ ] Location: Desktop or Documents
- [ ] Click **Save**

### Step 39: Publish to Power BI Service (Optional)
- [ ] **File** → **Publish**
- [ ] Sign in with Power BI account
- [ ] Select workspace (or create new)
- [ ] Click **Select**
- [ ] Wait for publish complete
- [ ] Link shows: Power BI Service URL

### Step 40: Share Dashboard
- [ ] Open Power BI Service (if published)
- [ ] Find report
- [ ] Click **Share** button
- [ ] Enter email addresses
- [ ] Set permissions: **View** (most users)
- [ ] Click **Share**

### Publication Complete ✓

---

## VERIFICATION CHECKLIST

### Data Verification
- [ ] Campaigns card A shows: $86,414
- [ ] Campaigns card B shows: $514,139
- [ ] ROI card A shows: 72.6%
- [ ] ROI card B shows: 921.2%
- [ ] Conversion Rate A: 2.51%
- [ ] Conversion Rate B: 4.25%

### Functionality Verification
- [ ] Campaign slicer works (filters all pages)
- [ ] Date range slicer works (filters trend charts)
- [ ] All metrics table shows correct values
- [ ] Funnel chart shows decreasing values
- [ ] Scatter plot shows clear separation

### Visual Verification
- [ ] Campaign B revenue bar is ~6x taller than A
- [ ] Campaign B ROI bar is ~13x taller than A
- [ ] Green line (B) in trend chart above blue line (A)
- [ ] No blank/error messages
- [ ] Layout is professional

---

## TOTAL TIME INVESTMENT

| Phase | Task | Time |
|-------|------|------|
| 1 | Data Export | 5 min |
| 2 | Power BI Setup | 0.5 min |
| 3 | Import Data | 3 min |
| 4 | Create Relationships | 2 min |
| 5 | Create Measures | 8 min |
| 6 | Page 1 Visualizations | 12 min |
| 7 | Page 2 Visualizations | 8 min |
| 8 | Page 3 Summary | 3 min |
| 9 | Add Slicers | 5 min |
| 10 | Formatting | 5 min |
| 11 | Save & Publish | 3 min |
| | **TOTAL** | **~55 minutes** |

---

## TROUBLESHOOTING DURING BUILD

### Problem: CSV Import Fails
**Solution:**
1. Ensure CSV files are in current folder
2. Check file names exactly (case-sensitive)
3. Try importing one file at a time
4. Wait for import to complete before next

### Problem: Relationships Won't Create
**Solution:**
1. Ensure both tables are visible in Model view
2. Drag from exact column name (campaign_id)
3. Drop exactly on target column in other table
4. Should see a line appear

### Problem: Measures Show Blank
**Solution:**
1. Check table name is exact: `daily_metrics[revenue]`
2. Check column name exists in table
3. Verify no spelling mistakes
4. Copy formula exactly from documentation

### Problem: Cards/Charts Not Updating
**Solution:**
1. Ensure relationships are created correctly
2. Check slicers are not over-filtering
3. Try clicking on visual → Delete → Re-create
4. Refresh data: Ctrl + R

### Problem: Slow Performance
**Solution:**
1. Reduce user_events table (optional)
2. Use smaller date ranges initially
3. Refresh data manually instead of auto
4. Don't load all 202k user rows if not needed

---

## QUICK VICTORY INDICATORS

✅ **Your dashboard is successful when:**

1. **Cards display correct big numbers**
   - Campaign A: $86,414 revenue
   - Campaign B: $514,139 revenue
   - Difference is obvious

2. **Charts tell the story**
   - Revenue bar for B is taller
   - Daily trend line B above A consistently
   - Conversion rate clearly shows B winning

3. **Slicers work**
   - Click Campaign A → numbers drop to A values
   - Click Campaign B → numbers jump to B values
   - Date range filters update trends

4. **Metrics table is complete**
   - All 8 metrics visible
   - Values match card numbers
   - No errors or blanks

5. **Professional appearance**
   - Consistent colors
   - Clear titles
   - Readable fonts
   - Logical layout

---

**🎉 CONGRATULATIONS - YOUR POWER BI DASHBOARD IS COMPLETE!**

---

**Next: Share dashboard with stakeholders and prepare presentation with findings.**

**Recommendation to present: Scale Campaign B, increase ROI by 12.7x**
