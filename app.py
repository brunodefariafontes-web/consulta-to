st.markdown("""
<style>

/* =====================
   FUNDO REAL (FORÇADO NO BODY)
   ===================== */
html, body, .stApp {
    height: 100%;
}

/* camada principal do Streamlit */
.stApp {
    background: transparent !important;
}

/* fundo aplicado no HTML inteiro */
body {
    background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/f_auto,dpr_auto,q_auto,fl_progressive/w_2048,h_1152,c_scale/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    /* escurecimento pra leitura */
    background-color: rgba(0,0,0,0.70);
    background-blend-mode: darken;
}

/* =====================
   TEXTO FIXO BRANCO
   ===================== */
h1, h2, h3, p, span, label {
    color: white !important;
}

/* botão branco */
.stButton > button {
    color: white !important;
    font-weight: 700 !important;
}

/* inputs continuam normais */
</style>
""", unsafe_allow_html=True)
