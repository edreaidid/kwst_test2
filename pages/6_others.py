import streamlit as st

st.write("HUBUNGI KONSULTAN KAMI UNTUK BANTUAN LANJUT")

st.info(" #### Admin monitoring :point_down:")
    password = st.text_input("Enter a password", value="", type="password")
    if password=="abcd":
        st.dataframe(pd.read_csv("kwst.csv",names=["staf sasmec","bergejala", "ahli staf", "ahli bergejala", "masa"]),height=300)
