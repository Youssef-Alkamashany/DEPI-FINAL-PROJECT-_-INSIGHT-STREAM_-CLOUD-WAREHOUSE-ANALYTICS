select
    "product_category_name"::varchar as product_category_name,
    "product_category_name_english"::varchar as product_category_name_english
from {{ source('raw', 'raw_category_translation') }}
