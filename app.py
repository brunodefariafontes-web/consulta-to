page_bg = """
<style>

/* =====================
   FUNDO (IMAGEM)
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

    /* 🔥 ESSENCIAL: ESCURECER PRA LEGIBILIDADE */
    filter: brightness(0.35) contrast(1.05);
    z-index: -1;
}

/* camada escura extra (melhora MUITO leitura) */
.stApp {
    background: rgba(0,0,0,0.55);
}

/* =====================
   TÍTULOS E TEXTO
   ===================== */
h1, h2, h3 {
    color: #ffffff !important;
}

p, span, label {
    color: #ffffff !important;
    font-weight: 600;
}

/* =====================
   INPUTS (CAIXA BRANCA LEGÍVEL)
   ===================== */
input, textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 600 !important;
    border-radius: 6px;
}

/* Streamlit inputs reais */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
}

/* placeholder */
input::placeholder {
    color: rgba(0,0,0,0.45) !important;
}

/* =====================
   TABELA RESULTADOS (IMPORTANTE)
   ===================== */
[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.95) !important;
    border-radius: 8px;
}

/* =====================
   BOTÃO
   ===================== */
.stButton > button {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-weight: 700 !important;
    border-radius: 8px;
    border: 1px solid rgba(0,0,0,0.2);
}

</style>
"""
