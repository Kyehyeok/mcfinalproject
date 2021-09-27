import csv
import os
import django
import sys

from django.db.models import Model

os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcfinal.settings")  # 1. 여기서 프로젝트명.settings입력
django.setup()

# 위의 과정까지가 python manage.py shell을 키는 것과 비슷한 효과

from articleapp.models import *  # 2. App이름.models

CSV_PATH = './컬리_식자재_수량+키워드(수정전) - 컬리_식자재_수량+키워드(수정전).csv'  # 3. csv 파일 경로

with open(CSV_PATH, newline=',') as csvfile:  # 4. newline =''
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        print(row)
        Model.objects.create(  # 5. class명.objects.create
            name=row['model']
            # 6
        )