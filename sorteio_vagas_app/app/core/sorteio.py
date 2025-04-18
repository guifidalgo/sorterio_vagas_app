import pandas as pd
import random

def sortear_ordem_unidades(df_unidades):
    return df_unidades.sample(frac=1).reset_index(drop=True)

def alocar_vagas(df_sorteio, df_vagas):
    alocacoes = []
    unidades_alocadas = set()

    # 1ª rodada: alocação por preferência
    for _, row in df_sorteio.iterrows():
        unidade = row['unidade']
        preferencias = row.filter(like='preferencia_').dropna().astype(int).tolist()

        for grupo in preferencias:
            idx = df_vagas[(df_vagas['grupo_vaga'] == grupo) & (~df_vagas['ocupada'])].index
            if not idx.empty:
                vaga = df_vagas.loc[idx[0]]
                df_vagas.loc[idx[0], 'ocupada'] = True
                alocacoes.append({
                    'unidade': unidade,
                    'grupo_vaga': grupo,
                    'vaga': vaga['vagas'],
                    'pavimento': vaga['pavimento'],
                    'alocacao': 'preferência'
                })
                unidades_alocadas.add(unidade)
                break

    # 2ª rodada: alocação aleatória das unidades restantes
    unidades_nao_alocadas = df_sorteio[~df_sorteio['unidade'].isin(unidades_alocadas)]
    vagas_disponiveis = df_vagas[~df_vagas['ocupada']]

    for _, row in unidades_nao_alocadas.iterrows():
        if not vagas_disponiveis.empty:
            vaga_aleatoria = vagas_disponiveis.sample(1)
            idx = vaga_aleatoria.index[0]
            df_vagas.loc[idx, 'ocupada'] = True

            alocacoes.append({
                'unidade': row['unidade'],
                'grupo_vaga': vaga_aleatoria.iloc[0]['grupo_vaga'],
                'vaga': vaga_aleatoria.iloc[0]['vagas'],
                'pavimento': vaga_aleatoria.iloc[0]['pavimento'],
                'alocacao': 'aleatória'
            })

            vagas_disponiveis = df_vagas[~df_vagas['ocupada']]

    return pd.DataFrame(alocacoes)
