# Sales Channels and Refunds

An exploratory analysis of a small educational orders dataset for January–March 2026.

## Business question

Which acquisition channels generated revenue after discounts and refunds, and which channels need closer investigation because of refunds? A later step will compare channel results with monthly marketing costs.

## Data

- `data/orders.csv`: one row per order; includes date, customer, channel, product, price, discount and refund flag.
- `data/channel_costs.csv`: monthly marketing cost by channel. This table will be added after the order-level analysis.

The dataset is small and educational. Observed differences between channels are descriptive; they do not establish that a channel caused refunds or higher sales.

## Metric definitions

- **Gross revenue:** `units × unit_price`.
- **Discounted order value:** gross revenue after `discount_pct`.
- **Recognized revenue:** discounted order value for non-refunded orders; zero for refunded orders.
- **Refund rate:** refunded orders divided by all orders in the same group.
- **Average non-refunded order value:** recognized revenue divided by the number of non-refunded orders.

The denominator of each rate and average must be checked after filtering and grouping.

## Preliminary findings

Ads had the lowest recognized revenue (78,650) and the highest refund rate (33.33%, 5 of 15 orders) in this dataset. These 48 orders do not establish that Ads caused the refunds, and channel profitability cannot be assessed without marketing costs.

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

In progress. Results and reproducible analysis will be added after the calculations are checked.
