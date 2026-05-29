page_bg = """
<style>

/* =====================
   FUNDO (SEGURO)
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

    filter: brightness(0.45);
    z-index: -1;
}

/* camada escura segura */
.stApp {
    background: rgba(0,0,0,0.50);
}

/* =====================
   INPUTS (SEMPRE LEGÍVEIS)
   ===================== */
input, textarea {
    background: #ffffff !important;
    color: #000000 !important;
}

/* Streamlit inputs */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background: #ffffff !important;
    color: #000000 !important;
}

/* =====================
   LABELS (SEM QUEBRAR NADA)
   ===================== */
label {
    color: #ffffff !important;
    font-weight: 600;
}

/* =====================
   BOTÃO
   ===================== */
.stButton > button {
    background: #ffffff !important;
    color: #000000 !important;
    font-weight: 700;
    border-radius: 8px;
}

</style>
"""
