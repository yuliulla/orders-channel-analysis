import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    orders = pd.read_csv("data/orders.csv")
    orders["order_date"] = pd.to_datetime(orders["order_date"])
    orders["month"] = orders["order_date"].dt.to_period("M")
    orders["gross_revenue"] = orders["units"] * orders["unit_price"]
    orders["discount_amount"] = orders["gross_revenue"] * orders["discount_pct"] / 100
    orders["revenue"] = (orders["gross_revenue"] - orders["discount_amount"]).where(~orders["refund_flag"], 0)
    orders["non_refund_order_value"] = (orders["gross_revenue"] - orders["discount_amount"]).where(~orders["refund_flag"])
    orders.head()
    return (orders,)


@app.cell
def _(orders):
    print(orders.shape)
    orders.info()
    return


@app.cell
def _(orders):
    channel_metrics = (
            orders
            .groupby("channel", as_index=False)
            .agg(
            orders_count=("order_id", "count"),
            revenue=("revenue", "sum"),
            average_order_value=("non_refund_order_value", "mean"),
            refund_count=("refund_flag", "sum")
            )
        )
    channel_metrics["refund_share_pct"] = channel_metrics["refund_count"] / channel_metrics ["orders_count"] * 100
    channel_metrics = channel_metrics.round(
            {"revenue": 2, "average_order_value": 2, "refund_share_pct": 2}
        )
    channel_metrics
    return


@app.cell
def _(orders):
    monthly_metrics = (
            orders
            .groupby("month", as_index=False)
            .agg(
                orders_count=("order_id", "count"),
                revenue=("revenue", "sum"),
                average_order_value=("non_refund_order_value", "mean"),
            )
        )
    monthly_metrics = monthly_metrics.round(
            {"revenue": 2, "average_order_value": 2}
        )

    monthly_metrics
    return


@app.cell
def _(pd):
    costs = pd.read_csv("data/channel_costs.csv")
    costs["month"] = pd.to_datetime(costs["month"]).dt.to_period("M")
    return (costs,)


@app.cell
def _(costs, orders, pd):
    channel_month_metrics = (orders.groupby(["month", "channel"], as_index=False)
                                .agg(
                                orders_count=("order_id", "count"),
                                revenue=("revenue", "sum"),
                                refund_count=("refund_flag", "sum")                                
                                )
                            )
    channel_month = pd.merge(channel_month_metrics, costs, on=["month", "channel"], how="left")
    channel_month["revenue_to_cost"] = channel_month["revenue"] / channel_month["marketing_cost"]
    channel_month = channel_month.round(
                    {"revenue": 2, "average_order_value": 2, "revenue_to_cost": 2}
    )
    channel_month["marketing_cost"].isna().sum()
    channel_month
    return (channel_month,)


@app.cell
def _(channel_month):
    channel = (channel_month.groupby(["channel"], as_index=False)
               .agg(
                orders_count=("orders_count", "sum"),
                revenue=("revenue", "sum"),
                refund_count=("refund_count", "sum"),
                marketing_cost=("marketing_cost", "sum"),
                avg_revenue_to_cost = ("revenue_to_cost", "mean")
                    )
               )
    channel["channel_total"] = channel["revenue"] / channel["marketing_cost"]
    channel = channel.round(
                    {"revenue": 2, "channel_total": 2, "avg_revenue_to_cost": 2}
    )

    channel
    return


@app.cell
def _(avg):
    avg
    return


if __name__ == "__main__":
    app.run()
