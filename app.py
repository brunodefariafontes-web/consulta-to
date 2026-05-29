page_bg = """
<style>

/* =====================
   FUNDO SEGURO (SEM OVERLAY QUEBRADO)
   ===================== */
.stApp {
    background-image: url("https://res.cloudinary.com/dkkd45ayz/image/upload/c_scale,w_2048/episerver/071584a2-31d6-4c72-bae3-343a753229e6/gripen-e_jer_4875.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    /* escurecimento seguro */
    background-color: rgba(0,0,0,0.55);
    background-blend-mode: darken;
}

/* =====================
   INPUTS (VISÍVEIS SEM SUMIR)
   ===================== */
input, textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* Streamlit inputs reais */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* =====================
   LABELS
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
