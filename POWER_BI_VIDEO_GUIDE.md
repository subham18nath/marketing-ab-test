# Power BI Dashboard - Step-by-Step Video Guide

## VIDEO TUTORIAL OUTLINE (11 Minutes Total)

---

## SECTION 1: DATA CONNECTION (2 minutes)

### 00:00-00:30 | Opening Power BI
**What to show:**
- Open Power BI Desktop
- Blank report canvas
- File menu location

**Action:**
```
Click: File → Open
Navigate to your project folder
OR Start with Blank Report
```

### 00:30-01:30 | Connecting to PostgreSQL
**What to show:**
1. Home menu
2. Get Data dropdown
3. PostgreSQL Database option

**Step-by-step clicks:**
```
1. Home → Get Data (dropdown arrow)
2. Search for "PostgreSQL"
3. Click PostgreSQL Database
4. Enter Connection Details:
   - Server: localhost
   - Database: marketing_ab_test
5. Click OK
6. Choose Import mode
7. Enter Credentials:
   - Username: marketing_user
   - Password: marketing_pass
8. Select tables: campaigns, daily_metrics, user_events
9. Click Load (wait 1-2 minutes)
```

### 01:30-02:00 | Data Preview
**What to show:**
- Data loaded in Power BI
- Table preview
- Fields panel on right

---

## SECTION 2: DATA MODELING (2 minutes)

### 02:00-02:30 | Accessing Model View
**What to show:**
```
Left sidebar → Click "Model" (icon looks like connected nodes)
You'll see 3 tables: campaigns, daily_metrics, user_events
```

### 02:30-03:00 | Creating Relationships
**Visual representation:**
```
TABLE: campaigns
├─ campaign_id (Primary Key)
├─ campaign_name
├─ channel
└─ budget

TABLE: daily_metrics
├─ date
├─ campaign_id (Foreign Key) ← CONNECT TO campaigns
├─ impressions
├─ clicks
├─ conversions
├─ spend
└─ revenue

TABLE: user_events
├─ user_id
├─ campaign_id (Foreign Key) ← CONNECT TO campaigns
├─ event_date
├─ clicked
├─ converted
└─ order_value
```

**Action:**
```
1. Drag campaign_id from daily_metrics 
   → Drop on campaign_id in campaigns
2. Repeat for user_events.campaign_id → campaigns.campaign_id
3. Verify: See connecting lines between tables
4. Click Back to Report
```

---

## SECTION 3: CREATING MEASURES (3 minutes)

### 03:00-03:30 | First Measure
**Screen recording:**
```
1. Select daily_metrics table in Fields panel
2. Right-click or use Home → New Measure
3. Name: "Total Revenue"
4. Formula: = SUM(daily_metrics[revenue])
5. Press Enter
6. Repeat for all measures below
```

### 03:30-04:00 | Essential Measures (list with formulas)
**Create each measure:**

```
Total Spend = SUM(daily_metrics[spend])

Total Conversions = SUM(daily_metrics[conversions])

Total Clicks = SUM(daily_metrics[clicks])

Total Impressions = SUM(daily_metrics[impressions])

CTR % = DIVIDE([Total Clicks], [Total Impressions], 0) * 100

Conversion Rate % = DIVIDE([Total Conversions], [Total Clicks], 0) * 100

CPC = DIVIDE([Total Spend], [Total Clicks], 0)

CPA = DIVIDE([Total Spend], [Total Conversions], 0)

ROAS = DIVIDE([Total Revenue], [Total Spend], 0)

ROI % = DIVIDE(([Total Revenue] - [Total Spend]), [Total Spend], 0) * 100

Net Profit = [Total Revenue] - [Total Spend]

AOV = DIVIDE([Total Revenue], [Total Conversions], 0)

CPM = DIVIDE([Total Spend], [Total Impressions], 0) * 1000
```

### 04:00-04:30 | Verify Measures
**Show:**
- All measures appear in Fields panel under daily_metrics
- Each one can be dragged to visualizations

---

## SECTION 4: BUILDING VISUALIZATIONS (3.5 minutes)

### 04:30-05:00 | Page 1 Setup - Executive Summary

**Screen layout:**
```
┌─────────────────────────────────────────┐
│ Marketing A/B Test Dashboard            │
├─────────────────┬───────────────────────┤
│ Campaign A Card │ Campaign B Card       │
├─────────────────┼───────────────────────┤
│ Revenue Card A  │ Revenue Card B        │
├─────────────────┼───────────────────────┤
│ ROI Card A      │ ROI Card B            │
├─────────────────┼───────────────────────┤
│ Conv Rate Card  │ Conv Rate Card        │
├─────────────────────────────────────────┤
│                                         │
│  Revenue vs Spend Chart (Clustered Bar) │
│                                         │
├─────────────────────────────────────────┤
│       Daily Revenue Trend (Line)         │
└─────────────────────────────────────────┘
```

**Actions:**
```
1. Insert → Card
2. Drag [Total Revenue] to card
3. Drag campaigns[campaign_name] to Filters
4. Filter to Campaign A only
5. Format → Data label size: 28pt
6. Repeat for Campaign B, ROI %, Conversion Rate %
```

### 05:00-05:30 | Visualization 1: Revenue vs Spend Chart

**Steps:**
```
1. Insert → Clustered Column Chart
2. X-axis: Drag campaigns[campaign_name]
3. Y-axis: Drag [Total Revenue]
4. Y-axis: Add [Total Spend] (click + icon)
5. Y-axis: Add [Net Profit] (click + icon)
6. Format:
   - Title: "Revenue vs Spend vs Profit"
   - Data labels: ON
   - Legend position: Top
```

### 05:30-06:00 | Visualization 2: Daily Revenue Trend

**Steps:**
```
1. Insert → Line Chart
2. X-axis: daily_metrics[date]
3. Y-axis: [Total Revenue]
4. Legend: campaigns[campaign_name]
5. Format:
   - Line style: Smooth
   - Title: "Daily Revenue Trend"
   - Highlight Campaign B line (thicker, green)
```

### 06:00-06:30 | Visualization 3: Conversion Rate Comparison

**Steps:**
```
1. Insert → Clustered Column Chart
2. X-axis: campaigns[campaign_name]
3. Y-axis: [Conversion Rate %]
4. Format:
   - Data labels: ON (show percentages)
   - Colors: Blue (Campaign A), Green (Campaign B)
   - Title: "Conversion Rate Comparison (%)"
```

### 06:30-07:00 | Visualization 4: Key Metrics Table

**Steps:**
```
1. Insert → Matrix
2. Rows: campaigns[campaign_name]
3. Values (add each):
   - [Total Clicks]
   - [Total Conversions]
   - [Conversion Rate %]
   - [Total Spend]
   - [Total Revenue]
   - [CPA]
   - [ROAS]
   - [ROI %]
4. Format:
   - Font size: 12pt
   - Currency format: USD
   - Percentage: 2 decimals
   - Title: "Complete Performance Metrics"
```

---

## SECTION 5: PAGE 2 - DEEP DIVE (2 minutes)

### 07:00-07:30 | Create New Page

**Steps:**
```
1. Right-click on page tab at bottom
2. Insert → New Page
3. Name it: "Detailed Analysis"
4. Add visuals (same process as Page 1):
```

**Visualization 6: Funnel Chart**
```
1. Insert → Funnel Chart
2. Category: campaigns[campaign_name]
3. Values (in order):
   - [Total Impressions]
   - [Total Clicks]
   - [Total Conversions]
4. Format: Show percentages
```

**Visualization 7: Cost Metrics**
```
1. Insert → Clustered Bar
2. Y-axis: campaigns[campaign_name]
3. X-axis (add multiple):
   - [CPC]
   - [CPA]
   - [CPM]
4. Format: Data labels ON
```

**Visualization 8: Spend Efficiency Scatter**
```
1. Insert → Scatter Plot
2. X-axis: [Total Spend]
3. Y-axis: [Total Revenue]
4. Legend: campaigns[campaign_name]
5. Size: [Net Profit]
6. Format: Title "Spend Efficiency Analysis"
```

### 07:30-08:00 | Page 3 - Statistical Summary

**Steps:**
```
1. Create new page: "Statistical Insights"
2. Insert Text Box
3. Paste summary statistics:

A/B TEST RESULTS
━━━━━━━━━━━━━━━━━━━
Campaign A (Banner Ads)
Clicks: 53,550 | Conversions: 1,345 | Conv Rate: 2.51%
Spend: $50,057 | Revenue: $86,414 | ROI: 72.6%

Campaign B (Influencer Video)
Clicks: 149,302 | Conversions: 6,350 | Conv Rate: 4.25%
Spend: $50,349 | Revenue: $514,139 | ROI: 921.2%

STATISTICAL SIGNIFICANCE
Z-statistic: 18.72 (p-value < 0.0001)
Relative Lift: 74% improvement
Power: 100%

RECOMMENDATION: Scale Campaign B
```

---

## SECTION 6: INTERACTIVITY & FORMATTING (1.5 minutes)

### 08:00-08:30 | Add Slicers

**Steps:**
```
1. Insert → Slicer
2. Field: campaigns[campaign_name]
3. Position: Top of page
4. Title: "Select Campaign"
5. Click each slicer visual
6. Ctrl + Click all charts
7. Right-click → Filter card
8. Select slicers to apply filters

Create Slicers:
- Campaign filter (dropdown or buttons)
- Date range filter
- Channel filter (optional)
```

### 08:30-09:00 | Apply Color Theme

**Steps:**
```
1. View → Themes → Select preset
2. Recommended: "Blue Teal" or "Executive"
3. Custom colors:
   - Campaign A (Blue): #2196F3
   - Campaign B (Green): #4CAF50
   - Revenue (Gold): #FFD700
   - Loss (Red): #FF6B6B
```

---

## SECTION 7: PUBLISHING & SHARING (1 minute)

### 09:00-09:30 | Save & Publish

**Steps:**
```
1. File → Save As
2. Name: "Marketing_AB_Test_Dashboard"
3. Save location: OneDrive (for auto-refresh)
4. File → Publish
5. Select workspace
6. Dashboard published!
```

### 09:30-10:00 | Share Dashboard

**Steps:**
```
1. Power BI Service (web): app.powerbi.com
2. Find your report
3. Share button (top right)
4. Enter email addresses
5. Choose permission: View/Edit
6. Send invitation
```

---

## SECTION 8: REFRESH DATA & MAINTAIN (1 minute)

### 10:00-10:30 | Setup Automatic Refresh

**In Power BI Service:**
```
1. Settings (gear icon) → Admin Portal
2. Capacity settings → Datasets
3. Find your dataset
4. Refresh schedule:
   - Frequency: Daily
   - Time: 2:00 AM
   - Notifications: Enable
```

### 10:30-11:00 | Updating Dashboard

**When new data arrives:**
```
1. New data automatically loads via refresh schedule
2. All visuals update automatically
3. Historical trend visible in Date slicer
4. Export reports: File → Export → PDF/PowerPoint
```

---

## DASHBOARD INTERACTION DEMO

### User Interaction Scenario:

```
1. User opens dashboard
2. Sees Campaign A selected (default)
3. Clicks Campaign B in slicer
   → All cards update
   → All charts update
   → Revenue jumps to $514k
   → ROI changes to 921%
   → Conversion rate shows 4.25%
4. User clicks date range slider
   → Charts show Week 1, Week 2, Week 3
   → Line chart shows trend over time
5. User hovers over bar chart
   → Tooltip shows exact values
6. User clicks drill-through on chart
   → Navigates to detailed page
   → Shows daily breakdown for selected campaign
```

---

## EXPECTED RESULTS WHEN COMPLETE

### Page 1: Executive Summary
```
┌────────────────────────────────────────────┐
│  CAMPAIGN A: BANNER ADS                    │
│  Revenue: $86,414  |  ROI: 72.6%           │
│  Conv Rate: 2.51%                          │
├────────────────────────────────────────────┤
│  CAMPAIGN B: INFLUENCER VIDEO              │
│  Revenue: $514,139  |  ROI: 921.2%         │
│  Conv Rate: 4.25%                          │
├────────────────────────────────────────────┤
│  [Revenue vs Spend Chart shows B dominates]│
├────────────────────────────────────────────┤
│  [Daily Revenue Trend Chart - Green line   │
│   clearly above blue line]                 │
├────────────────────────────────────────────┤
│  [Complete Metrics Table with all KPIs]    │
└────────────────────────────────────────────┘
```

### Key Visual Insights:
- **Campaign B clearly outperforms Campaign A**
- **ROI difference is dramatic: 921% vs 73%**
- **Daily trend shows consistent advantage**
- **Conversion rate is 69% higher for Campaign B**
- **CPA is 79% lower for Campaign B**

---

## TROUBLESHOOTING CHECKLIST

✅ Data not loading?
- Verify PostgreSQL container is running: `docker ps`
- Check firewall on port 5432
- Switch to CSV import method

✅ Slicers not working?
- Ensure relationships are created in Model view
- Check filters are applied to all visuals

✅ Slow performance?
- Use Import mode instead of DirectQuery
- Reduce date range in slicers
- Refresh data manually

✅ Cannot publish to Power BI Service?
- Sign in with Power BI account (FREE or PRO)
- Check workspace permissions
- Save file first

---

## TIPS & BEST PRACTICES

1. **Update Frequency:** Set auto-refresh daily (off-peak hours)
2. **Sharing:** Use Power BI Service for web sharing (not .pbix files)
3. **Drill-down:** Create drill-through pages for deeper analysis
4. **Mobile:** Power BI mobile optimizes automatically
5. **Export:** Users can export to PowerPoint/PDF on-demand
6. **Performance:** Limit date range to 90 days if slow
7. **Comments:** Enable annotations for team collaboration

---

**Download this guide and follow along step-by-step for best results!**
