select
    "product_id"::varchar as product_id,
    "product_category_name"::varchar as product_category_name,
    "product_weight_g"::float as product_weight_g
from {{ source('raw', 'raw_products') }}
