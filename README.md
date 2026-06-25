# InsightStream - دليل التشغيل الكامل

## قبل ما تبدأ
- لازم يكون عندك CSV files بتاعة Olist Dataset
- ضعهم في فولدر: `data/raw/` (داخل الفولدر ده بالظبط)

## الخطوة 1: عدّل بيانات Snowflake
عدّل القيم دي في **ملفين**:
1. `data/load_to_snowflake.py` (السطور اللي فيها SNOWFLAKE_ACCOUNT, USER, PASSWORD)
2. `dbt_project/profiles_template.yml`

بعدين خد نسخة من `profiles_template.yml` وضعها في:
- ماك/لينكس: `~/.dbt/profiles.yml`
- ويندوز: `C:\Users\YOUR_NAME\.dbt\profiles.yml`

## الخطوة 2: شغّل Docker
من جوه فولدر المشروع:
```
docker-compose up --build
```
استنى لحد ما يقولك إن كل الـ containers شغالة (هياخد 5-10 دقايق أول مرة).

## الخطوة 3: افتح Airflow
- روح على المتصفح: http://localhost:8080
- Username: `admin` / Password: `admin`
- هتلاقي DAG اسمه `insightstream_elt_pipeline`
- فعّله (الزرار بجنب اسمه) وبعدين دوس Trigger (زرار ▶️)

## الخطوة 4: تابع التنفيذ
- دوس على اسم الـ DAG، هتشوف 3 خطوات: load_raw_data_to_snowflake → dbt_run → dbt_test
- كل خطوة هتتلون أخضر لو نجحت. لو حمرا، دوس عليها وشوف الـ Logs

## الخطوة 5: تأكد في Snowflake
```sql
SELECT * FROM insightstream_db.analytics.fct_orders LIMIT 10;
SELECT * FROM insightstream_db.analytics.mart_sales_summary;
```

## الخطوة 6: Power BI
- افتح Power BI Desktop
- Get Data → Snowflake
- حط الـ Account identifier
- اختار database: insightstream_db، schema: analytics
- اعمل Dashboard على fct_orders و mart_sales_summary
