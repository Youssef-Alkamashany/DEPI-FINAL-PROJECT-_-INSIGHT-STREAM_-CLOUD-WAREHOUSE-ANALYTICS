select
    "order_id"::varchar as order_id,
    "order_item_id"::number as order_item_id,
    "product_id"::varchar as product_id,
    "seller_id"::varchar as seller_id,
    "price"::float as price,
    "freight_value"::float as freight_value
from {{ source('raw', 'raw_order_items') }}
