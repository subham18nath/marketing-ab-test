#!/bin/bash
set -e

echo "=========================================="
echo "Marketing A/B Test Analysis Pipeline"
echo "=========================================="
echo ""

# Wait for database
echo "⏳ Waiting for PostgreSQL..."
for i in {1..30}; do
    PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "SELECT 1" 2>/dev/null && break
    echo "  Attempt $i/30..."
    sleep 1
done
echo "✅ Database ready"
echo ""

# Run data generation
echo "📊 Step 1: Generating synthetic data..."
python python/01_generate_data.py
echo "✅ Data generation complete"
echo ""

# Import data to database
echo "📤 Step 2: Loading data into PostgreSQL..."
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -U $DB_USER -d $DB_NAME -f sql/03_analytics_queries.sql > /dev/null 2>&1 || true
echo "✅ Analytics queries loaded"
echo ""

# Run A/B test analysis
echo "🔬 Step 3: Running statistical A/B tests..."
python python/02_ab_test_analysis.py
echo "✅ A/B test analysis complete"
echo ""

# Generate visualizations
echo "📈 Step 4: Creating visualizations..."
python python/03_visualizations.py
echo "✅ Visualizations created"
echo ""

echo "=========================================="
echo "✨ Pipeline Complete!"
echo "=========================================="
echo "Output files:"
echo "  - output/ab_test_results.png"
echo "  - data/daily_metrics.csv"
echo "  - data/user_events.csv"
echo ""
echo "View database with Adminer:"
echo "  http://localhost:8080"
echo "  Server: postgres"
echo "  User: marketing_user"
echo "  Password: marketing_pass"
echo "=========================================="

# Keep container running for inspection
tail -f /dev/null
