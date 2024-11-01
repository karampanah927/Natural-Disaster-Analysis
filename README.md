Natural Disaster Analysis

Project Overview
This project provides a comprehensive analysis of natural disaster data collected from various APIs. Our goal is to gather, process, and visualize real-time disaster data, enabling effective monitoring and decision-making based on this information.

Data Collection

We collected disaster-related data from multiple APIs, bringing together diverse datasets to provide a comprehensive view of current and past events. The data retrieval is handled by a Python script, which gathers and structures data from these sources.

Data Processing (ETL) on GCP
The ETL (Extract, Transform, Load) process is implemented using Google Cloud Platform (GCP). After retrieving data, we process and clean it within GCP to prepare it for analysis and visualization. The processed data is stored in BigQuery, where it is ready for further querying and visualization.

Flask Application Deployment
A Flask application is deployed on GCP to automate and streamline our ETL process. This application:

Retrieves and processes new data.
Applies data preparation steps such as cleaning and transformation.
Implements a staging schema for organized storage.
We have configured a GCP job to automatically run this Flask app once daily, ensuring we always have up-to-date data.

Data Visualization
Once the data is in BigQuery, we connect it to Power BI to create interactive dashboards. These dashboards visualize the data, highlighting trends and insights that help monitor natural disasters effectively. This setup allows users to gain real-time insights into natural disasters, supporting management and preparedness.

