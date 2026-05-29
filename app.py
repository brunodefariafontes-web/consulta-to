page_bg = """
<style>

/* =====================
   FUNDO (INALTERADO)
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

    filter: brightness(0.50) contrast(0.95);
    z-index: -1;
}

.stApp{
    background: rgba(0,0,0,0.60);
}

/* =====================
   🔥 APENAS TEXTOS SEGURAMENTE CONTROLADOS
   ===================== */

/* título */
h1, h2, h3 {
    color: #ffffff !important;
}

/* labels (PN / T.O.) */
label {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* textos da interface (SEM quebrar componentes internos) */
p {
    color: rgba(255,255,255,0.85) !important;
}

/* =====================
   🔥 INPUTS (CORRETO E ESTÁVEL)
   ===================== */
input, textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 600 !important;
}

/* Streamlit base inputs */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 600 !important;
}

/* placeholder */
input::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

/* =====================
   BOTÃO
   ===================== */
.stButton > button {
    color: #000000 !important;
    font-weight: 700 !important;
}

</style>
"""
