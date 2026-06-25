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

### 🌟 Project Overview
**InsightStream** is a high-performance, cloud-native ELT (Extract, Load, Transform) solution designed to handle massive dataset ingestion and complex data modeling. The project eliminates external dependencies and reduces data latency by leveraging **Snowflake’s Internal Stages** and orchestrating the entire lifecycle using **Apache Airflow**.

---

### 🚀 Key Technical Objectives
* **Scalable Data Ingestion:** Automating the ingestion of large-scale CSV, Parquet, and JSON datasets directly into Snowflake Internal Storage.
* **Modular Transformation (dbt):** Building a multi-layered data model (Staging, Intermediate, and Marts) using dbt to ensure data quality and automated documentation.
* **Workflow Orchestration:** Implementing robust Airflow DAGs to manage end-to-end schedules and monitor pipeline health.
* **Advanced BI & Analytics:** Creating interactive, enterprise-grade dashboards in Power BI to provide real-time business insights.

---

### 🛠️ Tech Stack & Role Breakdown
| Technology | Role & Implementation |
| :--- | :--- |
| **Python** | Core language for dataset processing scripts and Airflow DAG development. |
| **Snowflake** | Cloud Data Warehouse utilizing internal storage for high-speed raw data staging. |
| **dbt (Data Build Tool)** | Handles SQL-based transformations, version control, and automated testing. |
| **Apache Airflow** | The orchestration engine for scheduling, monitoring, and error handling. |
| **Power BI** | Enterprise BI tool for building interactive visualizations and data stories. |

---

### 📂 Pipeline Architecture (The ELT Flow)
1. **Extraction:** Custom Python scripts fetch diverse datasets (CSV, Parquet, JSON).
2. **Loading:** Data is pushed directly into **Snowflake Internal Stages**, optimizing for cost and performance.
3. **Transformation (dbt Layers):**
    * **Staging Layer:** Initial cleaning and casting of raw data.
    * **Intermediate Layer:** Applying business logic and joining multiple sources.
    * **Marts Layer:** Final, optimized tables ready for reporting and BI.
4. **Visualization:** Connecting Snowflake Marts to Power BI for dynamic reporting.

---

### 🧪 Quality Assurance & Monitoring
* **Data Integrity:** Utilizing dbt tests (`unique`, `not_null`, `relationships`) to ensure high data standards.
* **Integration Testing:** Verifying the full data journey from source to dashboard.
* **Performance Optimization:** Monitoring Airflow DAG execution times and dbt run performance for maximum scalability.

---

### 👥 Project Team
* **Team Lead:** Youssef Ahmed Mohamed Alkamashany
* **Team Members:** Abdullah Mohamed Ahmed, Abdelrahman Adel Abu Taleb, Omar Abdelgawad Mahmoud

---

### 👤 Author & Contact
**Youssef Alkamashany**
* 🚀 **Aspiring MLOps/LLMOps & AI Data Engineer**.
* 💼 Team Leader — Microsoft Data Engineering | Digital Egypt Pioneers Initiative (DEPI).

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/youssef-alkamashany-18261132b)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Youssef-Alkamashany)

---
<p align="center">"Building the future of data-driven decision making." ☁️📊</p>
