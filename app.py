page_bg = """
<style>

/* =====================
   FUNDO (SEGURA E ESTÁVEL)
   ===================== */
[data-testid="stAppViewContainer"]::before{
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/c_scale,w_2048/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    filter: brightness(0.55);
    z-index: -1;
}

.stApp{
    background: rgba(0,0,0,0.55);
}

/* =====================
   🔥 ÚNICA REGRA IMPORTANTE (INPUTS)
   ===================== */
input {
    background: white !important;
    color: black !important;
}

/* Streamlit inputs reais */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background: white !important;
    color: black !important;
}

/* =====================
   LABELS (SÓ ISSO)
   ===================== */
label {
    color: white !important;
    font-weight: 700;
}

/* =====================
   BOTÃO
   ===================== */
.stButton > button {
    background: white !important;
    color: black !important;
    font-weight: 700;
}

</style>
"""
