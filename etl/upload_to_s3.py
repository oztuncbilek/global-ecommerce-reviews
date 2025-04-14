import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Değerlere erişim
aws_access = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY")
bucket_name = os.getenv("BUCKET_NAME")

print(bucket_name)  # Kontrol amaçlı