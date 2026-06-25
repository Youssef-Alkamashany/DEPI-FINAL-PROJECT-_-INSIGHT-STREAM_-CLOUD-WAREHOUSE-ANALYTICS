select
    f.customer_state,
    dp.product_category,
    date_trunc('month', f.order_purchase_timestamp) as order_month,
    count(distinct f.order_id) as total_orders,
    sum(f.price) as total_sales,
    avg(f.delivery_days) as avg_delivery_days
from {{ ref('fct_orders') }} f
left join {{ ref('dim_products') }} dp on f.product_id = dp.product_id
group by 1, 2, 3
