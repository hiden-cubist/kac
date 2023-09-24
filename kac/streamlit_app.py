import numpy as np
import pandas as pd
import streamlit as st

date = "20230924"
rounds = ["a", "b"]
titles = ["2dx", "sdvx", "popn", "ddr"]

st.set_page_config(
    page_title="KAC 2023 ランキング",
    layout="wide",
)

for i, t in enumerate(st.tabs(titles)):
    with t:
        for j, r in enumerate(st.tabs(rounds)):
            if not (i == 2 and j == 0):  # popn a
                with r:
                    st.write(f"KAC 2023 {titles[i]} 予選ラウンド{rounds[j].upper()}")
                    st.write(f"最終更新 {date}")
                    df = pd.read_csv(f"csv/{titles[i]}_{rounds[j]}_{date}.csv")
                    df.index = np.arange(1, len(df) + 1)
                    st.dataframe(df)

                    st.bar_chart(
                        df.iloc[1:, 2:],
                    )
