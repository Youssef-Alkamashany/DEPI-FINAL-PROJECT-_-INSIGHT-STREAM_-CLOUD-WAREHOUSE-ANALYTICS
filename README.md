# 🌊 InsightStream: Cloud Data Warehouse & Analytics
> **A Modern ELT Pipeline engineered with Airflow, Snowflake, dbt, and Power BI for Scalable Data Analytics.**

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Airflow-017CE2?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)

</div>

---

## 🌟 Project Overview
**InsightStream** is a high-performance, cloud-native ELT (Extract, Load, Transform) solution designed to handle massive dataset ingestion (~100K real e-commerce orders) and complex data modeling. The project eliminates external dependencies and reduces data latency by leveraging **Snowflake’s Internal Stages** and orchestrating the entire lifecycle using **Apache Airflow**.

---

## 🚀 Key Technical Objectives
* **Scalable Data Ingestion:** Automating the ingestion of large-scale CSV datasets directly into Snowflake Internal Storage.
* **Modular Transformation (dbt):** Building a multi-layered Medallion architecture (Bronze/Staging, Silver/Intermediate, and Gold/Marts) using dbt to ensure data quality and automated documentation.
* **Workflow Orchestration:** Implementing robust Airflow DAGs to manage end-to-end schedules and monitor pipeline health.
* **Advanced BI & Analytics:** Creating interactive, enterprise-grade dashboards in Power BI to provide real-time business insights.

---

## 🏗️ End-to-End Pipeline Architecture (The ELT Flow)


```

+------------------+      +--------------------------+      +---------------------------+      +--------------------+
|  Olist CSV Data  | ---> | Snowflake Internal Stage | ---> | dbt Transformations       | ---> |  Power BI          |
|  (Source Files)  |      | (Bronze / Raw Layer)     |      | (Silver & Gold Layers)    |      |  Dashboards        |
+------------------+      +--------------------------+      +---------------------------+      +--------------------+
^                                    ^
|                                    |
+----- Scheduled & Executed via -----+
Apache Airflow (Docker Engine)

```
---

## 📌 Medallion Data Modeling Layers:
1. **Bronze (Raw):** Untransformed source data stored exactly as ingested into Snowflake.
2. **Silver (Staging & Intermediate):** 
   * *Staging:* Type casting, column renaming, and initial cleaning (No business logic).
   * *Intermediate:* Joins orders, items, products, customers, and payments into enriched views (`int_orders_enriched`).
3. **Gold (Marts):** Governed Star-Schema tables optimized for BI consumption (`fct_orders`, `dim_customers`, `dim_products`, `mart_sales_summary`).

---

## 📊 Data Lineage & Schema Relationships

#### 🔹 dbt Lineage Graph (Bronze → Silver → Gold)
<p align="center">
  <img src="presentation_and_docs/images/dbt_lineage.png" width="90%" alt="dbt Lineage Graph" />
</p>

#### 🔹 Power BI Data Model (Gold Layer Relationships)
<p align="center">
  <img src="presentation_and_docs/images/powerbi_model.png" width="85%" alt="Power BI Data Model View" />
</p>

---

## 🛠️ Tech Stack & Role Breakdown
| Technology | Role & Implementation |
| :--- | :--- |
| **Python** | Core language for dataset ingestion scripts and Airflow DAG development. |
| **Snowflake** | Cloud Data Warehouse utilizing internal storage for high-speed raw data staging. |
| **dbt (Data Build Tool)** | Handles SQL-based transformations, version control, lineage, and testing. |
| **Apache Airflow** | The orchestration engine for scheduling, monitoring, and error handling (Dockerized). |
| **Power BI** | Enterprise BI tool for building interactive visualizations directly connected to Snowflake Gold Marts. |

---

## ⚙️ Airflow Orchestration & Reproducibility
The pipeline is orchestrated via the `insightstream_elt_pipeline` DAG running on a daily schedule (`@daily`). Execution is strictly linear (`load_raw_data_to_snowflake` ➔ `dbt_run` ➔ `dbt_test`) to ensure downstream data integrity.

<p align="center">
  <img src="presentation_and_docs/images/airflow_dag_tree.png" width="85%" alt="Airflow DAG Execution Tree" />
</p>

---

## 📈 Business Intelligence Dashboard
The final, governed Gold-layer tables feed directly into Power BI Desktop via live connection, providing deep commercial insights on order volumes, revenue trends, and geographical distribution.

<p align="center">
  <img src="presentation_and_docs/images/sales_dashboard.png" width="90%" alt="InsightStream Power BI Sales Dashboard" />
</p>

---

## 🧪 Quality Assurance & Testing Pyramid
* **Data Quality (dbt test):** Uniqueness, `not_null`, and referential integrity assertions (`schema.yml`).
* **Integration Testing:** Verified end-to-end DAG execution from raw Kaggle CSVs to queryable Gold marts.
* **Defect Handling:** Caught and resolved 3 real-world infrastructure issues (Flask secret key duplication, Snowflake session context loss, and uninitialized warehouse objects).

---

## 👥 Project Team
* **Team Lead:** Youssef Ahmed Mohamed Alkamashany
* **Team Members:** Abdelrahman Adel Abdelmola Abu Taleb, Abdullah Mohamed Ahmed, Omar Abdelgawad Mahmoud

---

## 👤 Author & Contact
**Youssef Alkamashany**
* 🚀 **Aspiring MLOps/LLMOps & AI Data Engineer**.
* 💼 Team Leader — Microsoft Data Engineering | Digital Egypt Pioneers Initiative (DEPI).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-alkamashany-18261132b)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Youssef-Alkamashany)

---
<p align="center">"Building the foundation so solidly that the dashboard becomes the easy part." ☁️📊</p>

---
