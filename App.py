import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Gestão de Projetos",
    page_icon="🧊",
    layout="wide",
)
st.title('Gestão de projetos')
st.sidebar.title('Menu')

df_status = pd.read_excel('Data.xlsx')
print(df_status.info())

options_eng = st.sidebar.multiselect(
    "Filtro por Engenheiro",
    ["João Ribeiro", "Marcos Santos", "Everton Rodrigues", "Rodrigo Santos"],
    ["João Ribeiro", "Marcos Santos", "Everton Rodrigues", "Rodrigo Santos"]
)

df_final_status = pd.DataFrame()
for eng in options_eng:
    condicao = (df_status['Engineer'] == eng)
    df_filter = df_status[condicao]
    df_final_status = pd.concat([df_final_status, df_filter])

st.write("---")
"""Timing Projetos"""
st.dataframe(
    df_final_status,
    column_config={
        "Project_name": st.column_config.TextColumn(
            "Projetos",
            width="medium",
            help="Projetos",
            max_chars=50,
        ),
        "Engineer": st.column_config.TextColumn(
            "Engenheiro",
            help="Engenheiro",
            max_chars=50,
        ),
        "01-Project Development": st.column_config.ProgressColumn(
            "Project Development",
            help="Project Development",
            format="%.0f%%",
            min_value=0,
            max_value=100,
        ),
        "02-Purchasing": st.column_config.ProgressColumn(
            "Purchasing",
            help="Purchasing",
            format="%.0f%%",
            min_value=0,
            max_value=100,
        ),
        "03-Manufacturing": st.column_config.ProgressColumn(
            "Manufacturing",
            help="Manufacturing",
            format="%.0f%%",
            min_value=0,
            max_value=100,
        ),
        "04-Assembly": st.column_config.ProgressColumn(
            "Assembly",
            help="Assembly",
            format="%.0f%%",
            min_value=0,
            max_value=100,
        ),
        "05-Machine Start-up": st.column_config.ProgressColumn(
            "Machine Start-up",
            help="Machine Start-up",
            format="%.0f%%",
            min_value=0,
            max_value=100,
        ),
        "06-Team Buy-off": st.column_config.ProgressColumn(
            "Team Buy-Off",
            help="Team Buy-Off",
            format="%.0f%%",
            min_value=0,
            max_value=100,
        ),
        "df_timing": st.column_config.TextColumn(
            "Status",
            help="Status",
            max_chars=50,
        ),
    },
    hide_index=True,
)
st.write("---")

"""Etapas dos projetos em andamento"""
df_ongoing = pd.read_excel('Data_OnGoing.xlsx')

df_final_ongoing = pd.DataFrame()
for eng in options_eng:
    condicao = (df_ongoing['Engineer'] == eng)
    df_filter = df_ongoing[condicao]
    df_final_ongoing = pd.concat([df_final_ongoing, df_filter])


cols_to_sum = ["01-Project Development",
               "02-Purchasing",
               "03-Manufacturing",
               "04-Assembly",
               "05-Machine Start-up",
               "06-Team Buy-off"]
df_sum = df_final_ongoing[cols_to_sum].sum()

with st.container():
    st.bar_chart(df_sum, width=400, height=300, use_container_width=False)

st.write("---")
