import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# AWS Bilgileri
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = "etl-project-global-reviews"  

def upload_raw_data():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name="eu-central-1"
    )
    
    # Raw verileri yükle
    raw_files = [
        ("data/raw/train.csv", "raw/train.csv"),
        ("data/raw/test.csv", "raw/test.csv")
    ]
    
    for local_path, s3_key in raw_files:
        try:
            s3.upload_file(local_path, BUCKET_NAME, s3_key)
            print(f"{local_path} → s3://{BUCKET_NAME}/{s3_key}")
        except Exception as e:
            print(f" Error ({local_path}): {str(e)}")

if __name__ == "__main__":
    upload_raw_data()