# Sales Channels and Refunds

An exploratory analysis of a small educational orders dataset for January–March 2026.

## Business question

How does channel revenue compare with monthly marketing costs?

## Data

- `data/orders.csv`: one row per order; includes date, customer, channel, product, price, discount and refund flag.
- `data/channel_costs.csv`: monthly marketing cost by channel.

The dataset is small and educational. Observed differences between channels are descriptive; they do not establish that a channel caused refunds or higher sales.

## Metric definitions

- **Gross revenue:** `units × unit_price`.
- **Discounted order value:** gross revenue after `discount_pct`.
- **Recognized revenue:** discounted order value for non-refunded orders; zero for refunded orders.
- **Refund rate:** refunded orders divided by all orders in the same group.
- **Average non-refunded order value:** recognized revenue divided by the number of non-refunded orders.

The denominator of each rate and average must be checked after filtering and grouping.

## Initial data checks

- 48 rows and 48 unique `order_id` values: one row per order in this extract.
- 46 unique `customer_id` values: some customers appear in more than one order.
- No missing values in the loaded table (`orders.isna().sum()`).

These checks do not yet establish that prices, quantities, discounts, or dates are valid.

## Analysis plan

1. Check row count, unique order IDs, missing values, date range and valid numeric fields.
2. Calculate order-level revenue and verify a few rows manually.
3. Summarize orders, refunds, refund rate and recognized revenue by channel.
4. Compare months and add marketing costs at the matching `(month, channel)` level.
5. Write a short conclusion with limitations and follow-up questions.

## Status

Completed. The analysis is reproducible in analysis.py (marimo notebook). 
## Findings

Revenue-to-cost ratio for the quarter (total recognized revenue / total marketing cost):

| Channel | Revenue | Marketing cost | Ratio |
|---|---:|---:|---:|
| Organic | 154,500 | 25,500 | 6.06 |
| Referral | 111,150 | 39,000 | 2.85 |
| Partner | 82,700 | 56,000 | 1.48 |
| Ads | 78,650 | 137,000 | 0.57 |

- Ads is the only channel with a ratio below 1: its revenue did not cover its marketing cost.
- Ads also had the highest refund rate (33.33%, 5 of 15 orders).
- Ads marketing cost increased from month to month (42,000 → 45,000 → 50,000), while Ads revenue decreased (28,250 → 27,900 → 22,500). The monthly ratio fell from 0.67 to 0.45.
- Hypothesis: this may indicate diminishing returns on Ads spending. The data do not establish this.

## Limitations

- Revenue, not profit: there are no data on the cost of goods, so channel profitability cannot be assessed.
- Short period and small sample: 3 months and 48 orders (7 of them from Partner).
- Attribution: some orders attributed to Organic or Referral may come from customers who had earlier seen ads, so the contribution of Ads may be underestimated.

## Next step

- Reduce the Ads budget for a limited period and track orders and revenue across all channels, not only Ads. This would show whether part of the orders attributed to other channels depends on Ads.
