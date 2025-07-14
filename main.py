import streamlit as st
from openai_promptlivre import enviar_prompt_livre

st.set_page_config(layout="wide", page_title="Prompt Livre - Agente Jurídico", initial_sidebar_state="expanded")
with st.sidebar:
    st.image("logo_eug.png", width=220)
    st.markdown(
        """
        <div style='background-color:#111124;padding:20px;border-radius:10px; text-align:center; margin-top: 10px;'>
            <a href='https://poc-goiania-v1.streamlit.app/' style='color:#fff;text-decoration:none;'><b>Análise Jurídica</b></a>
        </div>
        <div style='background-color:#111124;padding:20px;border-radius:10px; text-align:center; margin-top: 20px;'>
            <a href='/' style='color:#fff;text-decoration:none;'><b>Gerar Documentação</b></a>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.title("Gerar Documentos")

st.markdown("Use o campo abaixo para digitar um prompt ou clique em um dos quebra-gelos abaixo:")

# Inicia histórico
if "historico" not in st.session_state:
    st.session_state["historico"] = []

# Campo para prompt livre
prompt_text = st.text_area("Digite seu prompt", height=120)

col1, col2, col3, col4, col5 = st.columns([1.2, 1.5, 1.5, 1.5, 1.5])
enviar = col1.button("Enviar")
limpar = col2.button("Limpar histórico")
quebra_termo = col3.button("Gerar Termo de referência")
quebra_minuta = col4.button("Gerar Minuta de Contrato")
quebra_edital = col5.button("Gerar Edital de Licitação")

resposta = None
prompt_enviado = None

if enviar and prompt_text.strip():
    with st.spinner("Consultando Eugenia..."):
        resposta = enviar_prompt_livre(prompt_text.strip())
        prompt_enviado = prompt_text.strip()
elif quebra_termo:
    prompt_padrao = (
        "Gerar termo de referencia para aquisição de equipamentos de informática pela Prefeitura de Goiânia, "
        "com prazo de 12 meses, valor global de R$ 300.000,00, pagamento em até 30 dias, garantias legais, "
        "aplicação das penalidades previstas na Lei nº 14.133/2021, e fiscalização pelo Departamento de TI."
    )
    with st.spinner("Consultando Eugenia..."):
        resposta = enviar_prompt_livre(prompt_padrao)
        prompt_enviado = prompt_padrao
elif quebra_minuta:
    prompt_padrao = (
        "Gerar minuta de contrato detalhada para aquisição de equipamentos pela Prefeitura de Goiânia, "
        "com prazo de 12 meses, valor global de R$ 300.000,00, pagamento em até 30 dias, garantias legais, "
        "aplicação das penalidades previstas na Lei nº 14.133/2021, e fiscalização pelo Departamentos competentes."
    )
    with st.spinner("Consultando Eugenia..."):
        resposta = enviar_prompt_livre(prompt_padrao)
        prompt_enviado = prompt_padrao
elif quebra_edital:
    prompt_padrao = (
        "Gerar edital de licitação para aquisição de equipamentos de informática pela Prefeitura de Goiânia, "
        "com prazo de 12 meses, valor global de R$ 300.000,00, pagamento em até 30 dias, garantias legais, "
        "aplicação das penalidades previstas na Lei nº 14.133/2021, e fiscalização pelo Departamento de TI."
    )
    with st.spinner("Consultando OpenAI..."):
        resposta = enviar_prompt_livre(prompt_padrao)
        prompt_enviado = prompt_padrao

# Adiciona ao histórico
if resposta:
    st.session_state["historico"].append({
        "prompt": prompt_enviado,
        "resposta": resposta,
    })

# Limpa histórico
if limpar:
    st.session_state["historico"] = []
    st.experimental_rerun()

# Exibe histórico
if st.session_state["historico"]:
    st.markdown("---")
    st.markdown("### Histórico de respostas")
    for item in reversed(st.session_state["historico"]):
        if item.get("prompt"):
            st.markdown(f"**Prompt:** `{item['prompt']}`")
        st.markdown("**Resposta:**")
        st.markdown(item["resposta"], unsafe_allow_html=True)
        st.markdown("---")
