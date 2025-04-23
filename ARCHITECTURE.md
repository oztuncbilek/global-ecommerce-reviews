# Pipeline Architecture

## Overview
End-to-end flow for processing e-commerce reviews with sentiment analysis:

![Architecture Diagram](./assets/architecture_diagram.png)

## Components

### 1. Data Ingestion Layer
- **Source**: Amazon/eBay review datasets (CSV/JSON)
- **Storage**: 
  - Raw Zone: `s3://<bucket>/raw/` (Immutable original data)
  - Processed Zone: `s3://<bucket>/processed/` (Parquet formatted)

### 2. Processing Layer
| Service | Role |
|---------|------|
| AWS Glue | PySpark ETL jobs with: <br>- Text cleaning <br>- Sentiment analysis (DistilBERT) |
| AWS Lambda | (Optional) Trigger Glue jobs on new file uploads |

### 3. Analytics Layer
- **AWS Athena**: SQL queries on processed Parquet files
- **QuickSight**: Dashboards for:<br>
  - Sentiment distribution<br>
  - Model vs manual labeling comparison

### 4. Machine Learning


## Data Flow
```mermaid
graph LR
    A[Raw CSV] --> B(S3 Raw Zone)
    B --> C{Glue Job}
    C --> D[Text Cleaning]
    D --> E[Sentiment Analysis]
    E --> F(S3 Processed Zone)
    F --> G{Athena}
    G --> H[(QuickSight)]