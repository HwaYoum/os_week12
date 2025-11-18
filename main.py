import streamlit as st
import pandas as pd


# Task 3: 차트 그리기
st.header("Task3: 차트 그리기")

df = pd.read_csv("penguins.csv")
st.subheader("선 그래프")
st.line_chart(df,y="bill_length_mm")  # 선 그래프
st.subheader("막대 그래프")
st.bar_chart(df,y="body_mass_g")   # 막대 그래프
st.subheader("영역 차트")
st.area_chart(df,y="flipper_length_mm")  # 영역 차트