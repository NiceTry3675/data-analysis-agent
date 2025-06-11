import streamlit as st
import pandas as pd
import google.generativeai as genai
import plotly.express as px
from io import StringIO

# --- 페이지 설정 ---
st.set_page_config(
    page_title="고급 데이터 분석 자동화 📊",
    page_icon="💡",
    layout="wide",
)

# --- Gemini API 설정 ---
with st.sidebar:
    st.header("1. 설정")
    api_key = st.text_input("Gemini API 키를 입력하세요.", type="password", key="api_key_input")
    if api_key:
        try:
            genai.configure(api_key=api_key)
            st.success("API 키가 성공적으로 설정되었습니다.")
        except Exception as e:
            st.error(f"API 키 설정 중 오류: {e}")

# --- 메인 화면 ---
st.title("💡 Gemini 기반 고급 데이터 분석 및 시각화")
st.write("CSV 파일을 올리고, 원하는 분석을 구체적으로 요청하여 깊이 있는 인사이트를 얻어보세요.")

# --- 파일 업로드 및 데이터 준비 ---
st.sidebar.header("2. 데이터 업로드")
uploaded_file = st.sidebar.file_uploader("CSV 파일을 선택하세요.", type="csv")

if uploaded_file is not None:
    try:
        # 데이터 로딩
        df = pd.read_csv(uploaded_file)

        st.header("📂 업로드된 데이터")
        with st.expander("데이터 미리보기 (상위 10개 행)"):
            st.dataframe(df.head(10))

        # --- 분석 입력 UI ---
        st.header("📝 분석 요청하기")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # 관심 컬럼 선택
            selected_columns = st.multiselect(
                "분석에 사용할 주요 컬럼을 선택하세요.",
                options=df.columns.tolist(),
                default=df.columns.tolist() if len(df.columns) < 10 else None,
                help="AI가 분석 대상을 더 잘 이해하도록 돕습니다."
            )
        
        with col2:
            # 차트 유형 제안
            chart_suggestion = st.selectbox(
                "원하는 차트 유형을 제안해보세요.",
                options=["AI가 자동 선택", "막대 그래프 (Bar Chart)", "선 그래프 (Line Chart)", "산점도 (Scatter Plot)", "파이 차트 (Pie Chart)", "히스토그램 (Histogram)"],
                help="결과의 형태를 제안할 수 있습니다."
            )

        # 사용자 질문 입력
        user_question = st.text_area(
            "데이터에 대해 무엇이 궁금하신가요? (최대한 구체적으로 작성해주세요!)",
            height=150,
            placeholder="예시: 도시별, 제품 카테고리별 총 판매액을 비교하고 싶어. 가장 실적이 좋은 조합은 어디야? 막대그래프로 보여줘."
        )

        if st.button("🚀 분석 실행하기", type="primary"):
            if not api_key:
                st.warning("사이드바에서 Gemini API 키를 먼저 입력해주세요.")
            elif not selected_columns or not user_question:
                st.warning("분석할 컬럼과 질문을 모두 입력해주세요.")
            else:
                with st.spinner("Gemini가 데이터를 심층 분석하고 있습니다... 잠시만 기다려주세요."):
                    try:
                        # --- 고도화된 프롬프트 엔지니어링 ---
                        
                        # 데이터의 구조적 정보를 문자열로 변환
                        sio = StringIO()
                        df[selected_columns].info(buf=sio)
                        df_info = sio.getvalue()
                        
                        df_desc = df[selected_columns].describe(include='all').to_string()

                        prompt = f"""
                        당신은 Plotly를 사용하는 파이썬 시각화 전문가이자 시니어 데이터 분석가입니다.
                        주어진 데이터와 사용자의 질문을 바탕으로, 실용적이고 깊이 있는 데이터 분석과 시각화 코드를 생성해야 합니다.

                        # 제공된 데이터 정보:
                        - 사용자가 선택한 컬럼: {', '.join(selected_columns)}
                        - 데이터 구조 (info):
                        {df_info}
                        - 기술 통계 (describe):
                        {df_desc}
                        - 데이터 샘플 (head):
                        {df[selected_columns].head().to_string()}

                        # 사용자의 요청:
                        - 질문: "{user_question}"
                        - 제안된 차트 유형: {chart_suggestion}

                        # 최종 목표:
                        사용자의 질문에 답할 수 있는 명확하고, 통찰력 있으며, 시각적으로 미려한 Plotly 차트와 전문적인 분석 요약을 생성하세요.

                        # 필수 지시사항:
                        1.  분석 결과(인사이트, 트렌드, 결론)를 전문가 수준의 상세한 설명으로 작성하여 `analysis_text` 변수(Markdown 형식 문자열)에 할당하세요.
                        2.  데이터 시각화를 위한 `plotly` 차트를 생성하여 `fig` 변수에 할당하세요.
                            - 차트에는 반드시 **의미있는 제목과 축 레이블**을 포함해야 합니다.
                            - 차원의 깊이를 더하기 위해 Plotly Express의 `color`, `symbol`, `facet_row`, `facet_col` 등의 파라미터를 적극적으로 활용하세요.
                            - 사용자가 날짜/시간 관련 분석을 원하면, 해당 컬럼을 `pd.to_datetime`으로 변환하여 사용하세요.
                        3.  답변은 반드시 아래 Python 코드 형식으로만 제공해야 합니다. 코드 외에 다른 설명은 절대 추가하지 마세요.

                        ```python
                        # 분석 결과 텍스트 (Markdown 형식)
                        analysis_text = \"\"\"
                        ### [여기에 분석 제목 작성]
                        - **핵심 발견 1**: ...
                        - **핵심 발견 2**: ...
                        - **세부 분석**: ...
                        - **결론 및 제언**: ...
                        \"\"\"

                        # Plotly 시각화 코드
                        import plotly.express as px
                        import pandas as pd

                        # df 변수는 이미 로드되어 있다고 가정합니다.
                        # 필요 시, 데이터 전처리를 여기에 포함하세요 (예: 날짜 변환).
                        fig = ... # 이 부분에 plotly 차트 객체를 할당
                        ```
                        """
                        
                        # Gemini API 호출
                        model = genai.GenerativeModel('gemini-2.5-pro-preview-06-05')
                        response = model.generate_content(prompt)
                        generated_code = response.text.strip().replace("```python", "").replace("```", "")

                        # 결과 실행 및 표시를 위한 네임스페이스
                        local_vars = {"df": df.copy()} # 원본 데이터 보호를 위해 복사본 전달

                        # Gemini가 생성한 코드 실행
                        exec(generated_code, globals(), local_vars)

                        # 결과 가져오기
                        analysis_text = local_vars.get("analysis_text", "분석 텍스트를 생성하지 못했습니다.")
                        fig = local_vars.get("fig")

                        # --- 결과 출력 (탭 활용) ---
                        st.header("💡 분석 결과")
                        tab1, tab2, tab3 = st.tabs(["📊 분석 및 시각화", "📄 데이터 요약", "🤖 생성된 코드"])

                        with tab1:
                            st.markdown(analysis_text)
                            if fig:
                                st.plotly_chart(fig, use_container_width=True)
                            else:
                                st.warning("시각화 차트를 생성하지 못했습니다. 질문을 더 구체적으로 작성해보세요.")
                        
                        with tab2:
                            st.subheader("선택된 컬럼 통계 요약")
                            st.dataframe(df[selected_columns].describe(include='all'))

                        with tab3:
                            st.subheader("Gemini가 생성한 Python 코드")
                            st.code(generated_code, language='python')

                    except Exception as e:
                        st.error(f"분석 중 오류가 발생했습니다: {e}")
                        st.text("Gemini가 생성한 코드에 오류가 있을 수 있습니다. 아래 코드를 확인하세요.")
                        st.code(response.text if 'response' in locals() else "응답을 받지 못했습니다.", language='text')

    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    st.info("데이터 분석을 시작하려면 사이드바에서 CSV 파일을 업로드해주세요.")