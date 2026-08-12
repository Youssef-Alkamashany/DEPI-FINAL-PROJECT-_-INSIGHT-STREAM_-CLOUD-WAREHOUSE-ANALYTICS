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

## 📁 Source Dataset
The pipeline is fed by the **Brazilian E-Commerce Public Dataset by Olist (Kaggle)**, containing ~100k real commercial orders.

<p align="center">
  <img src="https://raw.githubusercontent.com/Youssef-Alkamashany/DEPI-FINAL-PROJECT-_-INSIGHT-STREAM_-CLOUD-WAREHOUSE-ANALYTICS/main/presentation_and_docs/DEPI%205.jpeg" width="85%" alt="Kaggle Source Dataset" />
</p>

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

## 📊 Data Lineage (Bronze → Silver → Gold)

<p align="center">
  <img src="https://raw.githubusercontent.com/Youssef-Alkamashany/DEPI-FINAL-PROJECT-_-INSIGHT-STREAM_-CLOUD-WAREHOUSE-ANALYTICS/main/presentation_and_docs/DEPI%207.jpeg" width="90%" alt="dbt Lineage Graph" />
</p>

---

## ⚙️ Airflow Orchestration & Pipeline Proof

The pipeline is orchestrated via the `insightstream_elt_pipeline` DAG running on a daily schedule (`@daily`).

### 🔹 DAG Graph & Tasks Execution
<p align="center">
  <img src="https://raw.githubusercontent.com/Youssef-Alkamashany/DEPI-FINAL-PROJECT-_-INSIGHT-STREAM_-CLOUD-WAREHOUSE-ANALYTICS/main/presentation_and_docs/DEPI%201.jpeg" width="85%" alt="Airflow DAG Graph" />
</p>

### 🔹 Successful Pipeline Execution History
<p align="center">
  <img src="https://raw.githubusercontent.com/Youssef-Alkamashany/DEPI-FINAL-PROJECT-_-INSIGHT-STREAM_-CLOUD-WAREHOUSE-ANALYTICS/main/presentation_and_docs/DEPI%206.jpeg" width="85%" alt="Airflow Pipeline Run History" />
</p>

### 🔹 Ingestion Task Duration & Code Structure
<p align="center">
  <img src="https://raw.githubusercontent.com/Youssef-Alkamashany/DEPI-FINAL-PROJECT-_-INSIGHT-STREAM_-CLOUD-WAREHOUSE-ANALYTICS/main/presentation_and_docs/DEPI%202.jpeg" width="48%" alt="Task Duration" />
  <img src="https://raw.githubusercontent.com/Youssef-Alkamashany/DEPI-FINAL-PROJECT-_-INSIGHT-STREAM_-CLOUD-WAREHOUSE-ANALYTICS/main/presentation_and_docs/DEPI%203.jpeg" width="48%" alt="DAG Python Code" />
</p>

### 🔹 Active DAG Dashboard Status
<p align="center">
  <img src="https://raw.githubusercontent.com/Youssef-Alkamashany/DEPI-FINAL-PROJECT-_-INSIGHT-STREAM_-CLOUD-WAREHOUSE-ANALYTICS/main/presentation_and_docs/DEPI%204.jpeg" width="85%" alt="Airflow DAGs List" />
</p>

---

## 📈 Business Intelligence Dashboard
The final, governed Gold-layer tables feed directly into Power BI Desktop via live connection, providing deep commercial insights on order volumes, revenue trends, and geographical distribution.

<p align="center">
  <img src="https://raw.githubusercontent.com/Youssef-Alkamashany/DEPI-FINAL-PROJECT-_-INSIGHT-STREAM_-CLOUD-WAREHOUSE-ANALYTICS/main/presentation_and_docs/DEPI%208.jpeg" width="90%" alt="InsightStream Power BI Sales Dashboard" />
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
* 🚀 **Advancing toward MLOps/LLMOps & AI Data Engineer**.
* 💼 Team Leader — Microsoft Data Engineering | Digital Egypt Pioneers Initiative (DEPI).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-alkamashany-18261132b)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Youssef-Alkamashany)

---

<p align="center">"Building the foundation so solidly that the dashboard becomes the easy part." ☁️📊</p>
