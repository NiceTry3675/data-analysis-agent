# 💡 Gemini 기반 고급 데이터 분석 및 시각화

CSV 파일을 업로드하고 자연어로 질문하면, Google Gemini AI가 데이터를 분석하고 인사이트를 제공하는 Streamlit 웹 애플리케이션입니다.

## 🚀 주요 기능

- **자연어 데이터 분석**: 복잡한 코드 없이 일상 언어로 데이터에 대해 질문
- **자동 시각화**: Plotly를 활용한 인터랙티브 차트 자동 생성
- **깊이 있는 인사이트**: Gemini AI가 제공하는 전문가 수준의 분석 결과
- **다양한 차트 지원**: 막대그래프, 선그래프, 산점도, 파이차트, 히스토그램 등

## 📋 사전 요구사항

- Python 3.8 이상
- Google AI Studio API 키 ([발급 방법](#api-키-발급-방법))

## 🛠️ 설치 및 실행 방법

### 1. 프로젝트 클론 또는 다운로드

```bash
git clone https://github.com/NiceTry3675/data-analysis-agent
cd data-analysis-agent
```

### 2. 가상환경 생성 및 활성화

#### Windows:
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
venv\Scripts\activate.bat
```

#### macOS/Linux:
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
source venv/bin/activate
```

### 3. 필요한 라이브러리 설치

```bash
pip install -r requirements.txt
```

또는 개별 설치:
```bash
pip install streamlit pandas google-generativeai plotly
```

### 4. 애플리케이션 실행

```bash
streamlit run app.py
```

### 5. 브라우저에서 접속

자동으로 브라우저가 열리거나, 수동으로 `http://localhost:8501`에 접속하세요.

## 🔑 API 키 발급 방법

1. [Google AI Studio](https://aistudio.google.com/)에 접속
2. Google 계정으로 로그인
3. "Get API Key" 클릭
4. "Create API Key" 선택
5. 생성된 API 키를 복사
6. 애플리케이션 사이드바에서 API 키 입력

## 📊 사용 방법

### 1. 데이터 업로드
- 사이드바에서 CSV 파일을 업로드하세요
- 업로드된 데이터의 미리보기가 표시됩니다

### 2. 분석 설정
- **주요 컬럼 선택**: 분석에 사용할 컬럼들을 선택
- **차트 유형 제안**: 원하는 시각화 유형을 선택 (선택사항)

### 3. 질문 작성
구체적이고 명확한 질문을 작성하세요. 예시:

```
도시별, 제품 카테고리별 총 판매액을 비교하고 싶어. 
가장 실적이 좋은 조합은 어디야? 막대그래프로 보여줘.
```

```
월별 매출 트렌드를 분석해줘. 
계절성이 있는지 확인하고 선그래프로 시각화해줘.
```

```
고객 연령대별 구매 패턴을 분석하고, 
가장 많이 구매하는 연령대는 어디인지 파이차트로 보여줘.
```

### 4. 결과 확인
- **분석 및 시각화**: AI가 생성한 인사이트와 차트
- **데이터 요약**: 선택된 컬럼의 통계 정보
- **생성된 코드**: AI가 작성한 Python 분석 코드

## 📁 프로젝트 구조

```
data-analysis-agent/
├── app.py              # 메인 Streamlit 애플리케이션
├── requirements.txt    # 필요한 Python 패키지 목록
├── README.md          # 프로젝트 설명서
└── venv/              # 가상환경 폴더 (생성 후)
```

## 🔧 문제 해결

### 가상환경 활성화가 안 될 때
**Windows PowerShell에서 실행 정책 오류가 발생하는 경우:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 패키지 설치 오류
```bash
# pip 업그레이드
python -m pip install --upgrade pip

# 캐시 클리어 후 재설치
pip cache purge
pip install -r requirements.txt
```

### 포트 충돌 시
```bash
# 다른 포트로 실행
streamlit run app.py --server.port 8502
```

## 💡 사용 팁

1. **구체적인 질문**: "매출을 분석해줘" 보다는 "월별 매출 트렌드와 전년 대비 증감률을 분석해줘"가 더 좋은 결과를 제공합니다.

2. **컬럼 선택**: 분석에 필요한 핵심 컬럼만 선택하면 더 정확한 분석이 가능합니다.

3. **데이터 품질**: 결측값이나 이상값이 많은 데이터는 전처리 후 사용하는 것을 권장합니다.

4. **API 사용량**: Gemini API는 사용량에 따라 과금될 수 있으니 주의하세요.

## 🤝 기여하기

버그 리포트나 기능 제안은 이슈로 등록해주세요.

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

---

**문제가 발생하거나 질문이 있으시면 이슈를 등록해주세요!** 🙋‍♂️
