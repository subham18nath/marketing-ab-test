-- ============================================================
-- Schema Creation (Database created by Docker)
-- ============================================================


-- Campaigns table
CREATE TABLE campaigns (
    campaign_id INT PRIMARY KEY,
    campaign_name VARCHAR(100),
    campaign_type VARCHAR(50),
    channel VARCHAR(50),
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12,2)
);

-- Daily aggregated metrics per campaign
CREATE TABLE daily_metrics (
    date DATE,
    campaign_id INT,
    impressions INT,
    clicks INT,
    conversions INT,
    spend DECIMAL(12,2),
    revenue DECIMAL(12,2),
    PRIMARY KEY (date, campaign_id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id)
);

-- User-level data for granular A/B testing
CREATE TABLE user_events (
    user_id INT,
    campaign_id INT,
    event_date DATE,
    clicked BOOLEAN,
    converted BOOLEAN,
    order_value DECIMAL(10,2),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id)
);

CREATE INDEX idx_user_events_campaign ON user_events(campaign_id);
CREATE INDEX idx_daily_metrics_campaign ON daily_metrics(campaign_id);
