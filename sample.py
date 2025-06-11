import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 재현성을 위한 랜덤 시드 설정
np.random.seed(42)
random.seed(42)

# 데이터 생성
data_size = 300
cities = ['서울', '부산', '인천', '대구', '광주']
genders = ['남성', '여성']
categories = ['전자제품', '의류', '식품', '도서']

price_range = {
    '전자제품': (100000, 2000000),
    '의류': (20000, 300000),
    '식품': (5000, 50000),
    '도서': (10000, 40000)
}

data = []
start_date = datetime(2023, 1, 1)

for i in range(data_size):
    category = random.choice(categories)
    unit_price = random.randint(price_range[category][0] // 1000, price_range[category][1] // 1000) * 1000
    quantity = random.randint(1, 5)

    data.append({
        '주문ID': 1001 + i,
        '고객ID': random.randint(1, 50),
        '나이': random.randint(20, 65),
        '성별': random.choice(genders),
        '도시': random.choice(cities),
        '제품카테고리': category,
        '수량': quantity,
        '단가': unit_price,
        '총액': unit_price * quantity,
        '구매일자': (start_date + timedelta(days=random.randint(0, 364))).strftime('%Y-%m-%d'),
        '만족도': random.randint(1, 5)
    })

# 데이터프레임 생성
df = pd.DataFrame(data)

# CSV 파일로 저장 (Excel에서 한글 깨짐 방지를 위해 encoding='utf-8-sig')
file_path = 'sample_sales_data.csv'
df.to_csv(file_path, index=False, encoding='utf-8-sig')

print(f"'{file_path}' 파일이 성공적으로 생성되었습니다.")
print("\n생성된 데이터 미리보기 (상위 5개):")
print(df.head())
