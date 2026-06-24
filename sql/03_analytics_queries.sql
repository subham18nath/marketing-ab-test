-- ============================================================
-- ANALYTICAL QUERIES
-- ============================================================

-- Query 1: Overall Campaign Performance Summary
SELECT 
    c.campaign_name,
    SUM(d.impressions)::BIGINT AS total_impressions,
    SUM(d.clicks)::BIGINT AS total_clicks,
    SUM(d.conversions)::BIGINT AS total_conversions,
    ROUND(SUM(d.clicks)::FLOAT / NULLIF(SUM(d.impressions), 0) * 100, 3) AS ctr_pct,
    ROUND(SUM(d.conversions)::FLOAT / NULLIF(SUM(d.clicks), 0) * 100, 3) AS conversion_rate_pct,
    ROUND(SUM(d.spend), 2) AS total_spend,
    ROUND(SUM(d.revenue), 2) AS total_revenue,
    ROUND(SUM(d.spend) / NULLIF(SUM(d.conversions), 0), 2) AS cost_per_acquisition,
    ROUND(SUM(d.spend) / NULLIF(SUM(d.clicks), 0), 2) AS cost_per_click,
    ROUND(SUM(d.revenue) / NULLIF(SUM(d.spend), 0), 3) AS roas,
    ROUND((SUM(d.revenue) - SUM(d.spend)) / NULLIF(SUM(d.spend), 0) * 100, 2) AS roi_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
GROUP BY c.campaign_name
ORDER BY roi_pct DESC;

-- Query 2: Daily ROI Trend
SELECT 
    d.date,
    c.campaign_name,
    d.impressions,
    d.clicks,
    d.conversions,
    ROUND(d.spend, 2) AS spend,
    ROUND(d.revenue, 2) AS revenue,
    ROUND((d.revenue - d.spend) / NULLIF(d.spend, 0) * 100, 2) AS daily_roi_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
ORDER BY d.date, c.campaign_id;

-- Query 3: Funnel Analysis
SELECT 
    c.campaign_name,
    SUM(d.impressions)::BIGINT AS impressions,
    SUM(d.clicks)::BIGINT AS clicks,
    SUM(d.conversions)::BIGINT AS conversions,
    ROUND(SUM(d.clicks)::FLOAT / NULLIF(SUM(d.impressions), 0) * 100, 2) AS impression_to_click_pct,
    ROUND(SUM(d.conversions)::FLOAT / NULLIF(SUM(d.clicks), 0) * 100, 2) AS click_to_conversion_pct,
    ROUND(SUM(d.conversions)::FLOAT / NULLIF(SUM(d.impressions), 0) * 100, 4) AS overall_conversion_pct
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
GROUP BY c.campaign_name;

-- Query 4: Cost Efficiency Comparison
SELECT 
    c.campaign_name,
    ROUND(SUM(d.spend), 2) AS total_spend,
    ROUND(SUM(d.spend) / NULLIF(SUM(d.impressions), 0) * 1000, 2) AS cpm,
    ROUND(SUM(d.spend) / NULLIF(SUM(d.clicks), 0), 2) AS cpc,
    ROUND(SUM(d.spend) / NULLIF(SUM(d.conversions), 0), 2) AS cpa,
    ROUND(AVG(d.revenue / NULLIF(d.conversions, 0)), 2) AS avg_order_value,
    ROUND(SUM(d.revenue) / NULLIF(SUM(d.spend), 0), 3) AS roas
FROM daily_metrics d
JOIN campaigns c ON d.campaign_id = c.campaign_id
GROUP BY c.campaign_name;
