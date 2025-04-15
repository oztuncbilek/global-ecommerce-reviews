
import os
import boto3
from dotenv import load_dotenv

load_dotenv()  

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = "etl-project-global-reviews" 


def get_file_path(filename):
    """Güvenli dosya yolu oluşturur."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    return os.path.join(project_root, "data", "processed", filename)


def upload_to_s3(file_path, s3_key):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")
        
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name="eu-central-1"
        )
        
        s3.upload_file(file_path, BUCKET_NAME, s3_key)
        print(f"{os.path.basename(file_path)} başarıyla yüklendi -> s3://{BUCKET_NAME}/{s3_key}")
    except Exception as e:
        print(f"Hata: {str(e)}")


files_to_upload = [
    ("train_clean.csv", "processed/train_clean.csv"),
    ("test_clean.csv", "processed/test_clean.csv")
]

for local_file, s3_key in files_to_upload:
    file_path = get_file_path(local_file)
    upload_to_s3(file_path, s3_key)

print("\nLoading phase completed! Check AWS S3.")