import streamlit as st
import pandas as pd
from app.core.sorteio import sortear_ordem_unidades, alocar_vagas
from app.core.exportacao import exportar_excel

def run_app():
    st.set_page_config(page_title="Sorteio de Vagas", page_icon=':car:', layout="wide")
    st.title("🎯 Aplicativo de Sorteio de Vagas por Preferência")

    st.sidebar.header("📂 Upload dos Arquivos")
    unidades_file = 'app/data/CadastroUnidades.csv' # st.sidebar.file_uploader("Cadastro de Unidades", type=["csv", "xlsx"])
    vagas_file = 'app/data/CadastroVagas.csv' # st.sidebar.file_uploader("Cadastro de Vagas", type=["csv", "xlsx"])

    tipo_sorteio = st.sidebar.selectbox("🔀 Tipo de Vaga", ["PNE", "TRIPLO", "DUPLO"])

    if "df_sorteio" not in st.session_state:
        st.session_state["df_sorteio"] = None
    if "df_resultado" not in st.session_state:
        st.session_state["df_resultado"] = None
    if "sorteio_realizado" not in st.session_state:
        st.session_state["sorteio_realizado"] = False
    if "alocacao_realizada" not in st.session_state:
        st.session_state["alocacao_realizada"] = False

    if unidades_file and vagas_file:
        #df_unidades = pd.read_excel(unidades_file) if unidades_file.name.endswith("xlsx") else pd.read_csv(unidades_file)
        #df_vagas = pd.read_excel(vagas_file) if vagas_file.name.endswith("xlsx") else pd.read_csv(vagas_file)
        df_unidades = pd.read_csv(unidades_file)
        df_vagas = pd.read_csv(vagas_file)
        
        df_vagas["ocupada"] = False

        df_unidades_tipo = df_unidades[df_unidades['tipo'] == tipo_sorteio].copy()
        df_vagas_tipo = df_vagas[df_vagas['tipo'] == tipo_sorteio].copy()

        st.subheader(f"📋 Dados - Tipo {tipo_sorteio}")
        tab1, tab2 = st.tabs(["Unidades", "Vagas"])
        with tab1:
            st.dataframe(df_unidades_tipo, use_container_width=True)
        with tab2:
            st.dataframe(df_vagas_tipo, use_container_width=True)

        if st.button("🎲 Sortear Ordem"):
            df_sorteio = sortear_ordem_unidades(df_unidades_tipo)
            st.session_state["df_sorteio"] = df_sorteio
            st.session_state["sorteio_realizado"] = True
            st.session_state["alocacao_realizada"] = False

        if st.session_state["sorteio_realizado"] and st.session_state["df_sorteio"] is not None:
            st.subheader("📑 Ordem das Unidades Sorteadas")
            st.dataframe(st.session_state["df_sorteio"], use_container_width=True)

        if st.session_state["df_sorteio"] is not None:
            if st.button("✅ Alocar Vagas"):
                df_resultado = alocar_vagas(st.session_state["df_sorteio"], df_vagas_tipo)
                st.session_state["df_resultado"] = df_resultado
                st.session_state["alocacao_realizada"] = True

        if st.session_state["alocacao_realizada"] and st.session_state["df_resultado"] is not None:
            df_resultado = st.session_state["df_resultado"]
            st.success("Alocação finalizada!")

            aloc_pref = df_resultado[df_resultado["alocacao"] == "preferência"]
            aloc_rand = df_resultado[df_resultado["alocacao"] == "aleatória"]

            tab3, tab4 = st.tabs(["🎯 Alocações por Preferência", "🎲 Alocações Aleatórias"])
            with tab3:
                st.write(f"Total: {len(aloc_pref)} unidades alocadas por preferência")
                st.dataframe(aloc_pref, use_container_width=True)
            with tab4:
                st.write(f"Total: {len(aloc_rand)} unidades alocadas aleatoriamente")
                st.dataframe(aloc_rand, use_container_width=True)

            st.markdown("---")
            st.subheader("🔎 Buscar Alocação por Unidade")

            unidades_sorteadas = sorted(df_resultado['unidade'].dropna().unique().tolist())

            if unidades_sorteadas:
                unidade_selecionada = st.selectbox("Selecione uma unidade para consultar:", unidades_sorteadas)
                resultado_unidade = df_resultado[df_resultado['unidade'] == unidade_selecionada]

                if not resultado_unidade.empty:
                    st.success(f"Unidade **{unidade_selecionada}** foi alocada:")
                    st.dataframe(resultado_unidade, use_container_width=True)
                else:
                    st.warning("Essa unidade não foi alocada.")
            else:
                st.info("Nenhuma unidade foi alocada ainda.")

            excel_bytes = exportar_excel(df_resultado)
            st.download_button("⬇️ Baixar Resultado Completo (.xlsx)", data=excel_bytes, file_name=f"resultado_{tipo_sorteio}.xlsx")
