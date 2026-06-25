select
    "order_id"::varchar as order_id,
    "payment_type"::varchar as payment_type,
    "payment_installments"::number as payment_installments,
    "payment_value"::float as payment_value
from {{ source('raw', 'raw_payments') }}
