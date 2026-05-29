st.markdown("""
<style>

/* =====================
   INPUTS BRANCOS + TEXTO PRETO
   ===================== */
.stTextInput input,
.stTextArea textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 600 !important;
    border: 1px solid #d0d0d0 !important;
    border-radius: 6px !important;
}

/* Streamlit base inputs */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* placeholder */
input::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

</style>
""", unsafe_allow_html=True)
