page_bg = """
<style>

/* FUNDO MANTIDO (NÃO MEXE) */
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

    filter: brightness(0.50) contrast(0.95);
    z-index: -1;
}

.stApp{
    background: rgba(0,0,0,0.60);
}

/* =====================
   🔥 TEXTO DA PÁGINA (LABELS + TEXTOS)
   ===================== */

/* títulos */
h1, h2, h3 {
    color: #ffffff !important;
}

/* textos gerais da página */
p, span, div {
    color: #ffffff !important;
}

/* labels dos campos (PN, T.O etc) */
label {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* =====================
   🔥 TEXTO DIGITADO NOS CAMPOS (PN / T.O.)
   ===================== */
input, textarea {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* Streamlit inputs reais */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* =====================
   PLACEHOLDER (opcional)
   ===================== */
input::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

/* BOTÃO MANTIDO VISÍVEL */
.stButton > button {
    color: #000000 !important;
    font-weight: 700 !important;
}

</style>
"""
