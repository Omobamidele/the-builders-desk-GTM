-- Multi-Touch Attribution Template — Module 3 (Very Technical track)
-- Week 6, Builder's Desk
--
-- Credits every touchpoint in a deal's path, not just the last click.
-- This uses linear attribution (equal credit to every touch) as the
-- starting model — it's the simplest one that's still honest about the
-- fact that more than one channel usually contributed to a closed deal.
--
-- Expects two tables:
--   touchpoints (contact_id, channel, touch_date)
--   deals       (contact_id, deal_id, deal_value, close_date)
--
-- Swap the table/column names for your own schema. Tested against
-- standard ANSI SQL — should run on BigQuery, Snowflake, and Postgres
-- with minimal changes.

WITH deal_touchpoints AS (
    -- Every touch that happened before the deal closed
    SELECT
        d.deal_id,
        d.deal_value,
        t.channel,
        t.touch_date
    FROM deals d
    JOIN touchpoints t
        ON t.contact_id = d.contact_id
        AND t.touch_date <= d.close_date
),

touch_counts AS (
    -- How many touches each deal had, so we can split credit evenly
    SELECT
        deal_id,
        COUNT(*) AS total_touches
    FROM deal_touchpoints
    GROUP BY deal_id
),

credited AS (
    -- Linear attribution: each touch gets (deal_value / total_touches)
    SELECT
        dt.deal_id,
        dt.channel,
        dt.deal_value / tc.total_touches AS credited_value
    FROM deal_touchpoints dt
    JOIN touch_counts tc
        ON tc.deal_id = dt.deal_id
)

SELECT
    channel,
    ROUND(SUM(credited_value), 2) AS attributed_revenue,
    COUNT(DISTINCT deal_id) AS deals_touched
FROM credited
GROUP BY channel
ORDER BY attributed_revenue DESC;

-- What to do with this:
-- Compare this ranking against a last-click-only version (just filter
-- deal_touchpoints to each deal's single latest touch before close).
-- The channels that rank higher here than in last-click are usually
-- the ones getting underfunded because nobody sees their real credit.
