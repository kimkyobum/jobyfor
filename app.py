import pandas as pd
import plotly.express as px
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="중고차 데이터 분석 대시보드", layout="wide")
st.title("🚗 중고차 시장 데이터 분석 대시보드")
st.write("이미지 기반의 데이터 셋을 분석하고 시각화하는 대시보드입니다.")

# 2. 데이터 가상 로드 (제공된 이미지 데이터 반영)
data = {
    "Make": [
        "Mercedes",
        "Hyundai",
        "Volkswagen",
        "Chevrolet",
        "Toyota",
        "Chevrolet",
        "Nissan",
        "Mercedes",
    ],
    "Model": [
        "GLE",
        "Tucson",
        "Golf",
        "Tahoe",
        "Camry",
        "Equinox",
        "Sentra",
        "C-Class",
    ],
    "Year":,
    "Fuel_Type": [
        "Petrol",
        "Petrol",
        "Hybrid",
        "Petrol",
        "Petrol",
        "Petrol",
        "Petrol",
        "Petrol",
    ],
    "Transmission": [
        "Automatic",
        "Automatic",
        "Automatic",
        "Automatic",
        "Automatic",
        "Automatic",
        "Automatic",
        "Automatic",
    ],  # 결측치 자동 채움 가정
    "Engine_Size": [2.3, 2.3, 1.9, 2.2, 1.9, 2.7, 2.2, 2.3],
    "Mileage":,
    "Horsepower":,  # 결측치 임의 채움
    "Torque":,
    "Owners":,
    "Accident":,
    "Service_History": [
        "Full Service",
        "No Service",
        "Partial Service",
        "No Service",
        "Full Service",
        "No Service",
        "Full Service",
        "Partial Service",
    ],
    "Color": [
        "Silver",
        "Blue",
        "Gray",
        "Blue",
        "Brown",
        "Blue",
        "Gray",
        "Green",
    ],
    "Body_Type": [
        "SUV",
        "SUV",
        "Hatchback",
        "SUV",
        "Sedan",
        "SUV",
        "Sedan",
        "Sedan",
    ],
    "Drivetrain": ["AWD", "FWD", "AWD", "AWD", "FWD", "AWD", "AWD", "FWD"],
    "Fuel_Efficiency":,  # 일부 채움
    "Location": ["IL", "FL", "NY", "FL", "CA", "TX", "IL", "NY"],
    "Selling_Price":,
}

df = pd.DataFrame(data)

# 3. 사이드바 필터 설정
st.sidebar.header("🔍 필터 옵션")
selected_make = st.sidebar.multiselect(
    "브랜드 선택", options=df["Make"].unique(), default=df["Make"].unique()
)
selected_body = st.sidebar.multiselect(
    "바디 타입 선택",
    options=df["Body_Type"].unique(),
    default=df["Body_Type"].unique(),
)

# 데이터 필터링 적용
filtered_df = df[
    (df["Make"].isin(selected_make)) & (df["Body_Type"].isin(selected_body))
]

# 4. 상단 핵심 지표 (KPI) 시각화
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("총 매물 수", f"{len(filtered_df)} 대")
with col2:
    st.metric(
        "평균 판매 가격",
        f"${filtered_df['Selling_Price'].mean():,.0f}"
        if not filtered_df.empty
        else "$0",
    )
with col3:
    st.metric(
        "평균 주행거리",
        f"{filtered_df['Mileage'].mean():,.0f} miles"
        if not filtered_df.empty
        else "0 miles",
    )
with col4:
    st.metric("사고 차량 수", f"{filtered_df['Accident'].sum()} 대")

st.markdown("---")

# 5. 메인 시각화 차트 영역
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("📊 브랜드별 평균 판매 가격")
    if not filtered_df.empty:
        fig_price = px.bar(
            filtered_df.groupby("Make", as_index=False)["Selling_Price"].mean(),
            x="Make",
            y="Selling_Price",
            labels={"Selling_Price": "평균 가격 ($)"},
            color="Make",
            text_auto=",.0f",
        )
        st.plotly_chart(fig_price, use_container_width=True)
    else:
        st.write("데이터가 없습니다.")

with chart_col2:
    st.subheader("📈 주행거리 vs 판매 가격 상관관계")
    if not filtered_df.empty:
        fig_scatter = px.scatter(
            filtered_df,
            x="Mileage",
            y="Selling_Price",
            hover_data=["Model", "Year"],
            color="Body_Type",
            size="Engine_Size",
            labels={"Mileage": "주행거리 (miles)", "Selling_Price": "가격 ($)"},
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.write("데이터가 없습니다.")

st.markdown("---")

# 6. 추가 심층 분석 영역
chart_col3, chart_col4 = st.columns(2)

with chart_col3:
    st.subheader("🎨 차량 외장 색상 분포")
    if not filtered_df.empty:
        fig_pie = px.pie(
            filtered_df, names="Color", hole=0.4, color="Color"
        )  # 원형 도넛 차트
        st.plotly_chart(fig_pie, use_container_width=True)

with chart_col4:
    st.subheader("📍 지역(State)별 차량 등록 수")
    if not filtered_df.empty:
        fig_loc = px.histogram(
            filtered_df,
            x="Location",
            color="Drivetrain",
            barmode="group",
            labels={"Location": "지역 코드"},
        )
        st.plotly_chart(fig_loc, use_container_width=True)

# 7. 원본 데이터프레임 확인
st.markdown("---")
st.subheader("📋 필터링된 데이터 상세 보기")
st.dataframe(filtered_df, use_container_width=True)
