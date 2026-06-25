select
    order_id,
    customer_id,
    customer_state,
    product_id,
    order_status,
    order_purchase_timestamp,
    order_delivered_customer_date,
    datediff('day', order_purchase_timestamp, order_delivered_customer_date) as delivery_days,
    price,
    freight_value,
    total_payment_value
from {{ ref('int_orders_enriched') }}
