st.markdown("""
<style>

/* =====================
   FUNDO GARANTIDO (STREAMLIT SAFE)
   ===================== */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    
    background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/f_auto,dpr_auto,q_auto,fl_progressive/w_2048,h_1152,c_scale/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    /* escurecimento leve pra não sumir UI */
    filter: brightness(0.45);
    
    z-index: -1;
}

/* garante que conteúdo fica acima */
.stApp {
    background: transparent;
}

/* =====================
   TEXTO BRANCO (FIXO)
   ===================== */
h1, h2, h3, p, span, label {
    color: white !important;
}

/* botão texto branco */
.stButton > button {
    color: white !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)
