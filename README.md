# Global E-Commerce Review Analysis Pipeline

## About  
An end-to-end AWS data pipeline that processes millions of e-commerce reviews using NLP sentiment analysis. Designed as a showcase project for modern ETL workflows with serverless components.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)

---

## Purpose  
Automates sentiment analysis on **Amazon/eBay product reviews** to:
- Extract raw customer feedback from multiple sources  
- Transform text data using NLP (DistilBERT model)  
- Load analyzed sentiments into query-optimized storage  
- Visualize trends in customer satisfaction  

---

## Technologies Used  
### Core Stack
| Component | Technology |
|-----------|------------|
| **Extract** | AWS S3 (Raw Data) |
| **Transform** | AWS Glue (PySpark + HuggingFace Transformers) |
| **Load** | Parquet via AWS Glue |
| **Query** | AWS Athena |
| **Visualize** | Amazon QuickSight |

### Key Libraries
```python
transformers==4.30.0  # DistilBERT sentiment analysis
pyspark==3.3.1        # Data processing
boto3==1.28.0         # AWS operations
```

---

## How to Run

1. **Infrastructure Setup**
```
cd infra/terraform
terraform init && terraform apply
```

2. **Run ETL Pipeline**
```
# Deploy Glue Job
aws glue create-job --name etl-reviews \
    --script-location s3://your-bucket/scripts/glue_job.py \
    --role AWSGlueServiceRoleDefault
```

3. **Analyze Results**
```
-- Athena Sample Query
SELECT product_category, 
       AVG(sentiment_score) as avg_rating
FROM processed_reviews
GROUP BY 1 ORDER BY 2 DESC;
```

## Why This Project?

**Real-world applicable**: Mirrors production-grade e-commerce analytics

**Serverless-first**: Uses AWS managed services for scalability

**ML Integration**: Combines ETL with NLP (DistilBERT)

**Infra-as-Code**: Reproducible via Terraform