import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# API 키 불러오기
UPBIT_ACCESS_KEY = os.getenv("UPBIT_ACCESS_KEY")
UPBIT_SECRET_KEY = os.getenv("UPBIT_SECRET_KEY")

print(f"Access Key: {UPBIT_ACCESS_KEY}")
print(f"Secret Key: {UPBIT_SECRET_KEY}")