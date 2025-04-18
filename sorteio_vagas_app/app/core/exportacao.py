import io
import pandas as pd

def exportar_excel(df_resultado):
    """Exporta o DataFrame resultado para um arquivo Excel em memória"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_resultado.to_excel(writer, index=False, sheet_name='Resultado')
    output.seek(0)
    return output.read()
