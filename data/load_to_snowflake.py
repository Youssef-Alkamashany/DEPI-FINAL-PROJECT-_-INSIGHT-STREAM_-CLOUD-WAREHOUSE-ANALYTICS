"""
InsightStream - Phase 1: Data Ingestion to Snowflake Internal Stage
يرفع ملفات CSV من فولدر raw ويحملها داخل Snowflake (Bronze / raw layer)
"""

import os
import pandas as pd
import snowflake.connector

# ============== CONFIG - غيّر القيم دي بمعلوماتك ==============
SNOWFLAKE_ACCOUNT = "wimlmns-yg71923"
SNOWFLAKE_USER = "youssefalkamashany"
SNOWFLAKE_PASSWORD = "Youssefalkamashany2072006y"
SNOWFLAKE_WAREHOUSE = "insightstream_wh"
SNOWFLAKE_DATABASE = "insightstream_db"
SNOWFLAKE_SCHEMA = "raw"

DATA_FOLDER = "./raw"   # داخل الـ Docker، الملفات هتكون هنا

FILES = {
    "olist_customers_dataset.csv": "raw_customers",
    "olist_orders_dataset.csv": "raw_orders",
    "olist_order_items_dataset.csv": "raw_order_items",
    "olist_products_dataset.csv": "raw_products",
    "olist_sellers_dataset.csv": "raw_sellers",
    "olist_order_payments_dataset.csv": "raw_payments",
    "olist_order_reviews_dataset.csv": "raw_reviews",
    "product_category_name_translation.csv": "raw_category_translation",
}
# ================================================================


def get_connection():
    return snowflake.connector.connect(
        account=SNOWFLAKE_ACCOUNT,
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
    )


def create_table_from_csv(cur, filepath, table_name):
    df = pd.read_csv(filepath, nrows=5)
    columns = ", ".join([f'"{col}" STRING' for col in df.columns])
    cur.execute(f'CREATE OR REPLACE TABLE {table_name} ({columns})')
    print(f"  -> تم إنشاء الجدول {table_name}")


def upload_and_load(cur, filepath, table_name):
    filename = os.path.basename(filepath)
    cur.execute(
        f"PUT file://{os.path.abspath(filepath)} @raw_stage "
        f"AUTO_COMPRESS=TRUE OVERWRITE=TRUE"
    )
    print(f"  -> تم رفع {filename} إلى الـ Stage")

    cur.execute(f"""
        COPY INTO {table_name}
        FROM @raw_stage/{filename}.gz
        FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY='"' SKIP_HEADER=1)
        ON_ERROR = 'CONTINUE'
    """)
    print(f"  -> تم تحميل البيانات داخل {table_name}")


def main():
    conn = get_connection()
    cur = conn.cursor()

    for filename, table_name in FILES.items():
        filepath = os.path.join(DATA_FOLDER, filename)
        print(f"\nبيتعالج: {filename}")
        if not os.path.exists(filepath):
            print(f"  !! الملف غير موجود: {filepath} - تم تخطيه")
            continue
        create_table_from_csv(cur, filepath, table_name)
        upload_and_load(cur, filepath, table_name)

    cur.close()
    conn.close()
    print("\nتم تحميل كل الملفات في Snowflake (raw schema) بنجاح.")


if __name__ == "__main__":
    main()
