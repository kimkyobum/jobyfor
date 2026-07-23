import base64
import os
import time
import streamlit as st

# 1. 페이지 설정 (넓은 레이아웃 고정)
st.set_page_config(
    page_title="MyStair - 세상으로 나아가는 너의 첫 번째 계단",
    page_icon="📈",
    layout="wide",
)

# 2. 토스 스타일 디자인, 카드 높이 일치 및 여유로운 여백 CSS 주입
st.markdown(
    """
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

body, [class*="css"] {
    font-family: 'Pretendard', -apple-system, sans-serif !important;
}

@keyframes smoothFadeIn {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floatAnimation {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

.stApp {
    background: #ffffff;
    color: #1e293b;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 10rem;
    max-width: 1050px !important;
    margin: 0 auto;
    animation: smoothFadeIn 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

/* 히어로 섹션 여백 확장 */
.hero-section {
    text-align: center;
    padding: 80px 0 50px 0;
    animation: smoothFadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 18px;
    background: #f8fafc;
    color: #475569;
    border-radius: 50px;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 28px;
    border: 1px solid #e2e8f0;
}

.hero-title {
    font-size: 60px;
    font-weight: 800;
    margin: 0 0 24px 0;
    line-height: 1.18;
    letter-spacing: -2.5px;
    color: #0f172a;
}

.hero-title span {
    background: linear-gradient(90deg, #3bb2b8, #7e57c2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 20px;
    color: #64748b;
    margin: 0 0 50px 0;
    font-weight: 400;
    letter-spacing: -0.5px;
}

.studio-podium {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    padding: 40px 60px;
    background: radial-gradient(circle at 50% 20%, rgba(59, 178, 184, 0.08) 0%, rgba(255, 255, 255, 1) 70%);
    border-radius: 40px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.03);
    border: 1px solid #f1f5f9;
    margin: 10px 0 60px 0;
    animation: floatAnimation 4s ease-in-out infinite;
}

.hero-graphic {
    width: 320px;
    height: auto;
    object-fit: contain;
}

/* 롱 스크롤 섹션 틈새를 아주 넓게(160px) 설정 */
.scroll-section {
    padding: 160px 0 60px 0;
    border-top: 1px solid #f8fafc;
    animation: smoothFadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.section-tag {
    font-size: 14px;
    font-weight: 700;
    color: #3bb2b8;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.section-heading {
    font-size: 42px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 16px;
    letter-spacing: -1.2px;
    line-height: 1.25;
}

.section-desc {
    font-size: 18px;
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 60px;
}

/* 설명 블록(카드)들의 크기와 높이를 완벽하게 일치시키는 설정 */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #f8fafc !important;
    border-radius: 24px !important;
    padding: 35px 30px !important;
    border: 1px solid #f1f5f9 !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.02) !important;
    transition: all 0.3s ease !important;
    height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-6px) !important;
    background-color: #ffffff !important;
    box-shadow: 0 20px 40px rgba(0,0,0,0.06) !important;
    border-color: #e2e8f0 !important;
}

.app-container {
    width: 100%;
    margin: 0 auto;
    padding: 20px 0;
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.bento-box {
    background: #ffffff;
    border-radius: 24px;
    padding: 35px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    border: 1px solid #e2e8f0;
}
</style>
""",
    unsafe_allow_html=True,
)

# 3. 세션 상태 관리
if "page" not in st.session_state:
  st.session_state.page = "landing"


def navigate_to(page_name):
  st.session_state.page = page_name
  st.rerun()


# =========================================================
# 상단 네비게이션 바 (버튼 테두리 없이 세련된 텍스트 로고 적용)
# =========================================================
nav_col1, nav_col2 = st.columns([8, 2])
with nav_col1:
  st.markdown(
      """
<style>
div[data-testid="column"] button[key="logo_btn"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
    font-size: 24px !important;
    font-weight: 800 !important;
    background: linear-gradient(90deg, #0f172a, #334155);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -1px;
    text-align: left !important;
}
</style>
""",
      unsafe_allow_html=True,
  )
  if st.button("MyStair", key="logo_btn"):
    navigate_to("landing")

with nav_col2:
  st.markdown(
      """
<style>
div[data-testid="column"] button[key="login_btn"] {
    background: #f8fafc !important;
    color: #0f172a !important;
    border: 1px solid #e2e8f0 !important;
    padding: 8px 18px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    border-radius: 20px !important;
    transition: all 0.2s ease !important;
}
div[data-testid="column"] button[key="login_btn"]:hover {
    background: #0f172a !important;
    color: #ffffff !important;
    border-color: #0f172a !important;
}
</style>
""",
      unsafe_allow_html=True,
  )
  if st.button("로그인", key="login_btn", use_container_width=True):
    st.toast("로그인 창이 열립니다.")

st.markdown(
    "<hr style='margin: 15px 0 40px 0; border: none; border-top: 1px solid"
    " #f1f5f9;'>",
    unsafe_allow_html=True,
)

# =========================================================
# [PAGE 1] 메인 랜딩 페이지 (롱 스크롤 방식)
# =========================================================
if st.session_state.page == "landing":

  # --- [섹션 1] 첫 화면 (히어로) ---
  st.markdown(
      """
<div class="hero-section">
    <div class="hero-badge">✨ 마이스터고 학생을 위한 단 하나의 진로 파트너</div>
    <h1 class="hero-title">세상으로 나아가는<br><span>너의 첫 번째 계단</span></h1>
    <p class="hero-subtitle">실습 기록부터 AI 자소서까지, 꿈을 현실로 만드는 혁신적인 커리어 플랫폼</p>
</div>
""",
      unsafe_allow_html=True,
  )

  # 3D 스튜디오 포디움 이미지
  img_col1, img_col2, img_col3 = st.columns([1, 1.4, 1])
  with img_col2:
    if os.path.exists("main_image.png"):
      with open("main_image.png", "rb") as f:
        encoded_img = base64.b64encode(f.read()).decode("utf-8")
      st.markdown(
          f"""
<div style="text-align: center; width: 100%;">
    <div class="studio-podium">
        <img src="data:image/png;base64,{encoded_img}" class="hero-graphic" alt="3D 계단 이미지">
    </div>
</div>
""",
          unsafe_allow_html=True,
      )
    else:
      st.warning("⚠️ 'main_image.png' 파일이 없습니다.")

  # CTA 버튼 여백 포함 배치
  st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
  col_c1, col_c2, col_c3 = st.columns([2, 1.6, 2])
  with col_c2:
    st.markdown(
        """
<style>
div.stButton > button[kind="primary"] {
    background: #0f172a !important;
    color: #ffffff !important;
    border: none !important;
    padding: 18px 36px !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    border-radius: 50px !important;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.15) !important;
    width: 100%;
    transition: all 0.3s ease !important;
}
div.stButton > button[kind="primary"]:hover {
    background: #334155 !important;
    transform: translateY(-2px);
}
</style>
""",
        unsafe_allow_html=True,
    )
    if st.button(
        "나의 진로 탐색 시작하기", type="primary", use_container_width=True
    ):
      navigate_to("dashboard")

  # --- [섹션 2] 핵심 기능 소개 (높이 일치형 카드 블록) ---
  st.markdown(
      """
<div class="scroll-section">
    <div class="section-tag">Core Features</div>
    <div class="section-heading">성장을 기록하고,<br>커리어를 완성하세요</div>
    <div class="section-desc">마이스터고 생활에 꼭 필요한 기능들만 엄선해 담았습니다.</div>
</div>
""",
      unsafe_allow_html=True,
  )

  f_col1, f_col2, f_col3 = st.columns(3, gap="large")
  with f_col1:
    with st.container(border=True):
      st.markdown("### 🎯 맞춤형 진로 로드맵")
      st.markdown(
          "전공과 역량에 딱 맞춘 단계별 성장 경로를 지능적으로 설계하고"
          " 관리합니다."
      )
  with f_col2:
    with st.container(border=True):
      st.markdown("### 📅 실습 및 경험 기록")
      st.markdown(
          "학교 생활과 현장 실습 활동을 스마트하게 기록하여 나만의 커리어 자산을"
          " 구축합니다."
      )
  with f_col3:
    with st.container(border=True):
      st.markdown("### ✨ AI STAR 자소서 변환")
      st.markdown(
          "축적된 활동 데이터를 바탕으로 기업 맞춤형 STAR 자기소개서를 1초 만에"
          " 완성합니다."
      )

  # --- [섹션 3] 만든 사람들 (높이 일치형 팀 소개 블록) ---
  st.markdown(
      """
<div class="scroll-section">
    <div class="section-tag">About Us</div>
    <div class="section-heading">만든 사람들</div>
    <div class="section-desc">학생들의 빛나는 도전과 가능성을 믿는 팀원들이 함께 만들었습니다.</div>
</div>
""",
      unsafe_allow_html=True,
  )

  t_col1, t_col2 = st.columns(2, gap="large")
  with t_col1:
    with st.container(border=True):
      st.markdown("### 💡 왜 MyStair를 만들었나요?")
      st.markdown(
          "일반 인문계 고등학교와는 다른 마이스터고만의 특수한 실습 경험과 기술"
          " 역량이 입사 지원서나 포트폴리오에 온전히 녹아들지 못하는 안타까움에서"
          " 출발했습니다. 학생들이 흘린 땀방울이 가장 가치 있는 취업 무기가"
          " 되도록 돕고 싶었습니다."
      )
  with t_col2:
    with st.container(border=True):
      st.markdown("### 🚀 우리의 목표와 비전")
      st.markdown(
          "단순한 자소서 작성 툴을 넘어, 마이스터고 학생들이 자신만의 확신을"
          " 가지고 세상이라는 더 큰 무대로 나아갈 수 있는 가장 믿음직하고"
          " 혁신적인 첫 번째 계단이 되는 것입니다."
      )

  # 하단 여백 추가
  st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)

# =========================================================
# [PAGE 2] 앱 대시보드 페이지
# =========================================================
elif st.session_state.page == "dashboard":
  if st.button("⬅️ 홈 화면으로 돌아가기", key="back_to_home_dash"):
    navigate_to("landing")

  st.markdown(
      """
<div class="app-container">
    <h2 style="font-size: 30px; font-weight: 800; margin: 0; color: #0f172a;">나의 진로 대시보드</h2>
</div>
""",
      unsafe_allow_html=True,
  )

  col_d1, col_d2 = st.columns([1, 1.5], gap="large")

  with col_d1:
    st.markdown(
        """
<div class="bento-box">
    <h3>📝 오늘의 과제</h3>
</div>
""",
        unsafe_allow_html=True,
    )
    st.checkbox("오늘 PLC 제어 도면 1개 해석하기 (15분)", value=True)
    st.checkbox("오답노트 3개 정리 (20분)")
    st.checkbox("설비보전기사 기출문제 1회 풀이 (30분)")

  with col_d2:
    st.markdown(
        """
<div class="bento-box">
    <h3>📅 경험 캘린더 & AI 자소서</h3>
    <div style="background:#f8fafc; padding:20px; border-radius:16px; margin-bottom: 20px; border: 1px solid #e2e8f0; color: #334155;">
        <b>[2026년 7월]</b> 실습 캘린더 데이터 적재 완료
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button(
        "✨ AI STAR 자소서 자동 추출하기",
        type="primary",
        use_container_width=True,
    ):
      with st.spinner("AI가 캘린더 데이터를 심층 분석 중입니다..."):
        time.sleep(1)
      st.success("자소서 추출 완료!")
      st.info("""
* **[Situation]** 7월 설비 실습 중 예기치 않은 회로 단락 오류 발생
* **[Task]** 팀 내 트러블슈팅 담당으로서 2시간 내 원인 분석 및 복구 임무 수행
* **[Action]** 테스터기를 이용해 단락 구간을 정밀 진단하고 도면을 재검토하여 배선 재배치
* **[Result]** 제한 시간 내 완전 복구 성공 및 현장 실무 역량 인증 획득
""")
