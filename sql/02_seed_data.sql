-- ============================================================
-- Seed Campaign Metadata
-- ============================================================

INSERT INTO campaigns VALUES
(1, 'Summer Sale Banner Ads', 'Display Banner', 'Google Display', '2024-06-01', '2024-06-30', 50000.00),
(2, 'Influencer Video Campaign', 'Video Ad', 'Instagram/TikTok', '2024-06-01', '2024-06-30', 50000.00)
ON CONFLICT (campaign_id) DO NOTHING;
