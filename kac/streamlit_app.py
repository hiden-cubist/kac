import numpy as np
import pandas as pd
import streamlit as st

date = "20230923"
titles = ["2dx", "sdvx", "popn", "ddr"]

st.set_page_config(
    page_title="KAC 2023 ランキング",
    layout="wide",
)

for i, t in enumerate(st.tabs(titles)):
    with t:
        st.write(f"KAC 2023 {titles[i]} 予選ラウンドB")
        st.write(f"最終更新 {date}")
        df = pd.read_csv(f"{titles[i]}_{date}.csv")
        df.index = np.arange(1, len(df) + 1)
        st.dataframe(df)
