import streamlit as st

st.set_page_config(
    page_title="st.balloons() st.snow()",
    page_icon=":balloon:",
)

st.title(":streamlit:")
col1_1, col1_2 = st.columns(2)

with col1_1:
    st.header("balloons")
    if st.button("風船を飛ばす"):
        st.balloons()

with col1_2:
    st.header("snow")
    if st.button("雪を降らす"):
        st.snow()
