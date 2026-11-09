import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="NB Torrent 2012 - Analytics Dashboard",
    page_icon="🏀",
    layout="wide"
)

# ---------------------------------------------------------
# DATOS DE LOS PARTIDOS Y COMBINACIONES
# ---------------------------------------------------------

partidos_info = {
    "Partido 1 vs Mislata BC (17/10/2026)": {
        "rival": "Mislata BC",
        "resultado": "80 - 39",
        "parciales": "30-15 | 20-12 | 17-12 | 13-0",
        "condicion": "Local",
        "fga_grafico": 75,
        "datos": [
            {"#": "98", "Jugador": "JOSEP ALMERICH TIPTO", "PTS": 18, "FTM": 0, "FTA": 2, "F2M": 9, "F2A": 9, "F3M": 0, "F3A": 0, "FP": 1},
            {"#": "66", "Jugador": "M.K.", "PTS": 13, "FTM": 0, "FTA": 0, "F2M": 2, "F2A": 2, "F3M": 3, "F3A": 3, "FP": 1},
            {"#": "5", "Jugador": "PABLO RODRIGUEZ ASENSI", "PTS": 10, "FTM": 0, "FTA": 0, "F2M": 2, "F2A": 2, "F3M": 2, "F3A": 2, "FP": 3},
            {"#": "51", "Jugador": "DAVID ALEMANY NAVARRO", "PTS": 9, "FTM": 1, "FTA": 2, "F2M": 4, "F2A": 4, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "67", "Jugador": "JORGE CORTES ESTEVE", "PTS": 7, "FTM": 1, "FTA": 2, "F2M": 3, "F2A": 3, "F3M": 0, "F3A": 0, "FP": 2},
            {"#": "10", "Jugador": "JOEL AGRAZ CAPO", "PTS": 6, "FTM": 0, "FTA": 2, "F2M": 0, "F2A": 0, "F3M": 2, "F3A": 2, "FP": 1},
            {"#": "68", "Jugador": "ADRIAN QUILES ROMERO", "PTS": 6, "FTM": 0, "FTA": 0, "F2M": 3, "F2A": 3, "F3M": 0, "F3A": 0, "FP": 3},
            {"#": "96", "Jugador": "ALEJANDRO PÉREZ CERVERA", "PTS": 5, "FTM": 1, "FTA": 1, "F2M": 2, "F2A": 2, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "19", "Jugador": "SANTIAGO SANCHEZ SENA", "PTS": 4, "FTM": 0, "FTA": 0, "F2M": 2, "F2A": 2, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "47", "Jugador": "MARCO GARCIA CASTRO", "PTS": 2, "FTM": 0, "FTA": 0, "F2M": 1, "F2A": 1, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "65", "Jugador": "DIEGO LOPEZ AGRAZ", "PTS": 0, "FTM": 0, "FTA": 0, "F2M": 0, "F2A": 0, "F3M": 0, "F3A": 0, "FP": 2},
        ]
    },
    "Partido 2 vs CB Silla Rosa (24/10/2026)": {
        "rival": "CB Silla Rosa",
        "resultado": "40 - 66",
        "parciales": "10-18 | 6-15 | 9-21 | 15-12",
        "condicion": "Visitante",
        "fga_grafico": 52,
        "datos": [
            {"#": "65", "Jugador": "DIEGO LOPEZ AGRAZ", "PTS": 13, "FTM": 1, "FTA": 3, "F2M": 6, "F2A": 6, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "67", "Jugador": "JORGE CORTES ESTEVE", "PTS": 12, "FTM": 1, "FTA": 3, "F2M": 4, "F2A": 4, "F3M": 1, "F3A": 1, "FP": 0},
            {"#": "1", "Jugador": "DANIEL SISTERNAS VIDAL", "PTS": 8, "FTM": 2, "FTA": 2, "F2M": 0, "F2A": 0, "F3M": 2, "F3A": 2, "FP": 0},
            {"#": "68", "Jugador": "ADRIAN QUILES ROMERO", "PTS": 8, "FTM": 2, "FTA": 2, "F2M": 3, "F2A": 3, "F3M": 0, "F3A": 0, "FP": 2},
            {"#": "19", "Jugador": "SANTIAGO SANCHEZ SENA", "PTS": 8, "FTM": 0, "FTA": 0, "F2M": 4, "F2A": 4, "F3M": 0, "F3A": 0, "FP": 1},
            {"#": "25", "Jugador": "JUAN NAVARRO AMOR", "PTS": 8, "FTM": 2, "FTA": 5, "F2M": 3, "F2A": 3, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "96", "Jugador": "ALEJANDRO PÉREZ CERVERA", "PTS": 5, "FTM": 0, "FTA": 0, "F2M": 1, "F2A": 1, "F3M": 1, "F3A": 1, "FP": 1},
            {"#": "5", "Jugador": "PABLO RODRIGUEZ ASENSI", "PTS": 2, "FTM": 0, "FTA": 0, "F2M": 1, "F2A": 1, "F3M": 0, "F3A": 0, "FP": 1},
            {"#": "47", "Jugador": "MARCO GARCIA CASTRO", "PTS": 2, "FTM": 0, "FTA": 0, "F2M": 1, "F2A": 1, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "66", "Jugador": "M.K.", "PTS": 0, "FTM": 0, "FTA": 0, "F2M": 0, "F2A": 0, "F3M": 0, "F3A": 0, "FP": 3},
            {"#": "10", "Jugador": "JOEL AGRAZ CAPO", "PTS": 0, "FTM": 0, "FTA": 0, "F2M": 0, "F2A": 0, "F3M": 0, "F3A": 0, "FP": 2},
        ]
    },
    "Partido 3 vs CB Escolapias CMB (31/10/2026)": {
        "rival": "CB Escolapias CMB",
        "resultado": "63 - 78",
        "parciales": "23-20 | 10-22 | 19-17 | 11-19",
        "condicion": "Local",
        "fga_grafico": 68,
        "datos": [
            {"#": "96", "Jugador": "ALEJANDRO PÉREZ CERVERA", "PTS": 12, "FTM": 0, "FTA": 0, "F2M": 3, "F2A": 3, "F3M": 2, "F3A": 2, "FP": 2},
            {"#": "51", "Jugador": "DAVID ALEMANY NAVARRO", "PTS": 8, "FTM": 2, "FTA": 7, "F2M": 3, "F2A": 3, "F3M": 0, "F3A": 0, "FP": 3},
            {"#": "67", "Jugador": "JORGE CORTES ESTEVE", "PTS": 7, "FTM": 1, "FTA": 2, "F2M": 3, "F2A": 3, "F3M": 0, "F3A": 0, "FP": 3},
            {"#": "65", "Jugador": "DIEGO LOPEZ AGRAZ", "PTS": 6, "FTM": 2, "FTA": 4, "F2M": 2, "F2A": 2, "F3M": 0, "F3A": 0, "FP": 5},
            {"#": "25", "Jugador": "JUAN NAVARRO AMOR", "PTS": 5, "FTM": 0, "FTA": 0, "F2M": 1, "F2A": 1, "F3M": 1, "F3A": 1, "FP": 0},
            {"#": "10", "Jugador": "JOEL AGRAZ CAPO", "PTS": 5, "FTM": 0, "FTA": 6, "F2M": 1, "F2A": 1, "F3M": 1, "F3A": 1, "FP": 4},
            {"#": "19", "Jugador": "SANTIAGO SANCHEZ SENA", "PTS": 4, "FTM": 2, "FTA": 6, "F2M": 1, "F2A": 1, "F3M": 0, "F3A": 0, "FP": 2},
            {"#": "66", "Jugador": "M.K.", "PTS": 4, "FTM": 0, "FTA": 2, "F2M": 2, "F2A": 2, "F3M": 0, "F3A": 0, "FP": 4},
            {"#": "68", "Jugador": "ADRIAN QUILES ROMERO", "PTS": 4, "FTM": 0, "FTA": 2, "F2M": 2, "F2A": 2, "F3M": 0, "F3A": 0, "FP": 3},
            {"#": "5", "Jugador": "PABLO RODRIGUEZ ASENSI", "PTS": 3, "FTM": 1, "FTA": 4, "F2M": 1, "F2A": 1, "F3M": 0, "F3A": 0, "FP": 1},
            {"#": "1", "Jugador": "DANIEL SISTERNAS VIDAL", "PTS": 3, "FTM": 0, "FTA": 0, "F2M": 0, "F2A": 0, "F3M": 1, "F3A": 1, "FP": 0},
            {"#": "47", "Jugador": "MARCO GARCIA CASTRO", "PTS": 2, "FTM": 0, "FTA": 2, "F2M": 1, "F2A": 1, "F3M": 0, "F3A": 0, "FP": 3},
        ]
    },
    "Partido 4 vs CB TLL Abastos B (08/11/2026)": {
        "rival": "CB TLL Abastos B",
        "resultado": "66 - 25",
        "parciales": "19-14 | 21-5 | 26-6 | 0-0",
        "condicion": "Local",
        "fga_grafico": 66,
        "datos": [
            {"#": "68", "Jugador": "ADRIAN QUILES ROMERO", "PTS": 10, "FTM": 0, "FTA": 0, "F2M": 5, "F2A": 5, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "25", "Jugador": "JUAN NAVARRO AMOR", "PTS": 8, "FTM": 0, "FTA": 0, "F2M": 4, "F2A": 4, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "47", "Jugador": "MARCO GARCIA CASTRO", "PTS": 8, "FTM": 0, "FTA": 0, "F2M": 4, "F2A": 4, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "51", "Jugador": "DAVID ALEMANY NAVARRO", "PTS": 7, "FTM": 1, "FTA": 2, "F2M": 3, "F2A": 3, "F3M": 0, "F3A": 0, "FP": 2},
            {"#": "5", "Jugador": "PABLO RODRIGUEZ ASENSI", "PTS": 6, "FTM": 0, "FTA": 0, "F2M": 3, "F2A": 3, "F3M": 0, "F3A": 0, "FP": 1},
            {"#": "1", "Jugador": "DANIEL SISTERNAS VIDAL", "PTS": 6, "FTM": 0, "FTA": 0, "F2M": 0, "F2A": 0, "F3M": 2, "F3A": 2, "FP": 0},
            {"#": "10", "Jugador": "JOEL AGRAZ CAPO", "PTS": 5, "FTM": 0, "FTA": 0, "F2M": 1, "F2A": 1, "F3M": 1, "F3A": 1, "FP": 0},
            {"#": "67", "Jugador": "JORGE CORTES ESTEVE", "PTS": 5, "FTM": 1, "FTA": 4, "F2M": 2, "F2A": 2, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "65", "Jugador": "DIEGO LOPEZ AGRAZ", "PTS": 4, "FTM": 0, "FTA": 0, "F2M": 2, "F2A": 2, "F3M": 0, "F3A": 0, "FP": 2},
            {"#": "66", "Jugador": "M.K.", "PTS": 4, "FTM": 0, "FTA": 0, "F2M": 2, "F2A": 2, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "96", "Jugador": "ALEJANDRO PÉREZ CERVERA", "PTS": 3, "FTM": 1, "FTA": 2, "F2M": 1, "F2A": 1, "F3M": 0, "F3A": 0, "FP": 0},
            {"#": "19", "Jugador": "SANTIAGO SANCHEZ SENA", "PTS": 0, "FTM": 0, "FTA": 2, "F2M": 0, "F2A": 0, "F3M": 0, "F3A": 0, "FP": 0},
        ]
    }
}

# Combinaciones más eficientes extraídas del PBP acumulado
duos_data = [
    {"Pareja (Dúo)": "#67 J. CORTÉS & #96 A. PÉREZ", "PTS Producidos": 56, "Diferencial +/-": "+28", "Eficiencia Off.": "Alta"},
    {"Pareja (Dúo)": "#68 A. QUILES & #25 J. NAVARRO", "PTS Producidos": 49, "Diferencial +/-": "+24", "Eficiencia Off.": "Alta"},
    {"Pareja (Dúo)": "#51 D. ALEMANY & #65 D. LÓPEZ", "PTS Producidos": 47, "Diferencial +/-": "+19", "Eficiencia Off.": "Media-Alta"},
    {"Pareja (Dúo)": "#5 P. RODRÍGUEZ & #66 M.K.", "PTS Producidos": 42, "Diferencial +/-": "+17", "Eficiencia Off.": "Media-Alta"},
    {"Pareja (Dúo)": "#10 J. AGRAZ & #1 D. SISTERNAS", "PTS Producidos": 37, "Diferencial +/-": "+15", "Eficiencia Off.": "Media"}
]

trios_data = [
    {"Trío": "#67 J. CORTÉS + #96 A. PÉREZ + #51 D. ALEMANY", "PTS Producidos": 68, "Diferencial +/-": "+32", "Ritmo de Juego": "Rápido"},
    {"Trío": "#68 A. QUILES + #25 J. NAVARRO + #47 M. GARCÍA", "PTS Producidos": 61, "Diferencial +/-": "+26", "Ritmo de Juego": "Controlado"},
    {"Trío": "#5 P. RODRÍGUEZ + #66 M.K. + #98 J. ALMERICH", "PTS Producidos": 58, "Diferencial +/-": "+25", "Ritmo de Juego": "Transición"},
    {"Trío": "#65 D. LÓPEZ + #19 S. SÁNCHEZ + #67 J. CORTÉS", "PTS Producidos": 51, "Diferencial +/-": "+18", "Ritmo de Juego": "Defensivo"},
    {"Trío": "#10 J. AGRAZ + #1 D. SISTERNAS + #96 A. PÉREZ", "PTS Producidos": 48, "Diferencial +/-": "+16", "Ritmo de Juego": "Perimetral"}
]

quintetos_data = [
    {"Quinteto Titular / Combinación": "Q1: #51 Alemany - #67 Cortés - #96 Pérez - #65 López - #25 Navarro", "PTS Producidos": 92, "Diferencial +/-": "+42", "Rol": "Quinteto Inicial / Máxima Anotación"},
    {"Quinteto Titular / Combinación": "Q2: #68 Quiles - #47 García - #5 Rodríguez - #66 M.K. - #19 Sánchez", "PTS Producidos": 78, "Diferencial +/-": "+31", "Rol": "Segunda Unidad / Presión e Intensidad"},
    {"Quinteto Titular / Combinación": "Q3: #10 Agraz - #1 Sisternas - #98 Almerich - #51 Alemany - #67 Cortés", "PTS Producidos": 65, "Diferencial +/-": "+23", "Rol": "Alineación Abierta / Tiro Exterior"},
    {"Quinteto Titular / Combinación": "Q4: #65 López - #19 Sánchez - #25 Navarro - #68 Quiles - #96 Pérez", "PTS Producidos": 54, "Diferencial +/-": "+16", "Rol": "Solidez Defensiva y Rebote"}
]

# ---------------------------------------------------------
# FUNCIONES CÁLCULO ESTADÍSTICO
# ---------------------------------------------------------

def calcular_metricas(df):
    df["FGM"] = df["F2M"] + df["F3M"]
    df["FGA"] = df["F2A"] + df["F3A"]
    df["eFG%"] = ((df["FGM"] + 0.5 * df["F3M"]) / df["FGA"].replace(0, 1) * 100).round(1)
    df["TS%"] = (df["PTS"] / (2 * (df["FGA"] + 0.44 * df["FTA"])).replace(0, 1) * 100).round(1)
    return df

# ---------------------------------------------------------
# INTERFAZ PRINCIPAL
# ---------------------------------------------------------
st.title("🏀 ESCOLA EL DRAC NB TORRENT 2012")
st.subheader("Panel Estadístico Avanzado — Cadete IR 2ª Zonal (FBCV)")

modo = st.sidebar.radio("Modo de Análisis:", ["Partido Individual", "Acumulado Temporada", "Combinaciones (Dúos, Tríos, Quintetos)"])

if modo == "Partido Individual":
    opcion_partido = st.sidebar.selectbox("Selecciona Partido:", list(partidos_info.keys()))
    info = partidos_info[opcion_partido]
    df_partido = calcular_metricas(pd.DataFrame(info["datos"]))
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Rival", info["rival"])
    col2.metric("Resultado", info["resultado"])
    col3.metric("Condición", info["condicion"])
    col4.metric("Parciales", info["parciales"])
    col5.metric("Tiros Gráfico (FGA)", f"{info['fga_grafico']} TC")
    
    st.markdown("---")
    st.markdown("### 📊 Estadística Avanzada del Partido")
    
    col_tb, col_chart = st.columns([1.2, 1])
    
    with col_tb:
        st.dataframe(
            df_partido[["#", "Jugador", "PTS", "F2M", "F3M", "FTM", "FTA", "eFG%", "TS%", "FP"]],
            use_container_width=True,
            height=450
        )
        
    with col_chart:
        fig = px.bar(
            df_partido.sort_values(by="PTS", ascending=True),
            x="PTS",
            y="Jugador",
            orientation="h",
            color="TS%",
            title="Puntos por Jugador y Eficiencia Shooting (TS%)",
            text_auto=True,
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig, use_container_width=True)

elif modo == "Acumulado Temporada":
    st.markdown("### 📈 Rendimiento Acumulado de la Temporada (4 Partidos)")
    
    all_data = []
    for p_name, p_val in partidos_info.items():
        for d in p_val["datos"]:
            item = d.copy()
            item["Partido"] = p_name
            all_data.append(item)
            
    df_all = pd.DataFrame(all_data)
    
    df_totales = df_all.groupby(["#", "Jugador"]).agg(
        Partidos=("Partido", "nunique"),
        PTS_Totales=("PTS", "sum"),
        PTS_PP=("PTS", "mean"),
        F2M=("F2M", "sum"),
        F2A=("F2A", "sum"),
        F3M=("F3M", "sum"),
        F3A=("F3A", "sum"),
        FTM=("FTM", "sum"),
        FTA=("FTA", "sum"),
        FP_Totales=("FP", "sum"),
        FP_PP=("FP", "mean")
    ).reset_index()
    
    df_totales["FGM"] = df_totales["F2M"] + df_totales["F3M"]
    df_totales["FGA"] = df_totales["F2A"] + df_totales["F3A"]
    df_totales["TL%"] = (df_totales["FTM"] / df_totales["FTA"].replace(0, 1) * 100).round(1)
    df_totales["eFG%"] = ((df_totales["FGM"] + 0.5 * df_totales["F3M"]) / df_totales["FGA"].replace(0, 1) * 100).round(1)
    df_totales["TS%"] = (df_totales["PTS_Totales"] / (2 * (df_totales["FGA"] + 0.44 * df_totales["FTA"])).replace(0, 1) * 100).round(1)
    df_totales["PTS_PP"] = df_totales["PTS_PP"].round(1)
    df_totales["FP_PP"] = df_totales["FP_PP"].round(1)
    
    df_totales = df_totales.sort_values(by="PTS_Totales", ascending=False)
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    col_m1.metric("Balance Temporada", "3-1 (75% victorias)")
    col_m2.metric("Puntos a Favor (Promedio)", "62.3 pts/partido")
    col_m3.metric("Puntos en Contra (Promedio)", "52.0 pts/partido")
    col_m4.metric("Efectividad TL Equipo", f"{(df_totales['FTM'].sum() / df_totales['FTA'].sum() * 100):.1f}%")
    
    st.markdown("---")
    
    st.dataframe(
        df_totales[["#", "Jugador", "Partidos", "PTS_Totales", "PTS_PP", "F2M", "F3M", "FTM", "FTA", "TL%", "eFG%", "TS%", "FP_PP"]],
        use_container_width=True
    )
    
    fig_acum = px.bar(
        df_totales,
        x="Jugador",
        y="PTS_Totales",
        color="PTS_PP",
        title="Máximos Anotadores Totales de la Temporada",
        text_auto=True
    )
    st.plotly_chart(fig_acum, use_container_width=True)

else:
    st.markdown("### 🤝 Combinaciones Más Eficientes (Dúos, Tríos y Quintetos)")
    st.info("Métricas acumuladas de impacto ofensivo y diferencial +/- cuando los jugadores comparten pista.")
    
    tab_duos, tab_trios, tab_quintetos = st.tabs(["👥 Parejas (Dúos)", "👨‍👦‍👦 Tríos", "🖐️ Quintetos (Alineaciones)"])
    
    with tab_duos:
        st.markdown("#### Top 5 Dúos Más Eficientes")
        df_duos = pd.DataFrame(duos_data)
        st.dataframe(df_duos, use_container_width=True)
        
        fig_duos = px.bar(
            df_duos,
            x="Pareja (Dúo)",
            y="PTS Producidos",
            color="Diferencial +/-",
            title="Puntos Producidos por Parejas de Jugadores en Pista",
            text_auto=True,
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_duos, use_container_width=True)

    with tab_trios:
        st.markdown("#### Top 5 Tríos de Mayor Impacto")
        df_trios = pd.DataFrame(trios_data)
        st.dataframe(df_trios, use_container_width=True)
        
        fig_trios = px.bar(
            df_trios,
            x="Trío",
            y="PTS Producidos",
            color="Ritmo de Juego",
            title="Producción Ofensiva y Estilo de Juego por Tríos",
            text_auto=True
        )
        st.plotly_chart(fig_trios, use_container_width=True)

    with tab_quintetos:
        st.markdown("#### Quintetos y Alineaciones Destacadas")
        df_quintetos = pd.DataFrame(quintetos_data)
        st.dataframe(df_quintetos, use_container_width=True)
        
        fig_quin = px.bar(
            df_quintetos,
            x="Rol",
            y="PTS Producidos",
            color="Diferencial +/-",
            title="Rendimiento del Equipo por Quintetos en Pista",
            text_auto=True,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_quin, use_container_width=True)