select
    "review_id"::varchar as review_id,
    "order_id"::varchar as order_id,
    "review_score"::number as review_score,
    "review_creation_date"::timestamp as review_creation_date
from {{ source('raw', 'raw_reviews') }}
