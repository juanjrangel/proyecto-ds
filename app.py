import streamlit as st

# Configuración de la página (agregamos que la barra inicie expandida)
st.set_page_config(
    page_title="DataSci Exchange - Q&A", 
    page_icon="📊", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado corregido
st.markdown("""
<style>
    /* Ocultamos el menú superior derecho y el pie de página, pero conservamos el botón de la barra lateral */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Estilos del foro falso */
    .forum-title { font-size: 26px; font-weight: 500; color: #1e2b3c; margin-bottom: 10px; }
    .forum-stats { color: #6c7a89; font-size: 13px; margin-bottom: 15px; border-bottom: 1px solid #d2d7d3; padding-bottom: 10px;}
    .forum-q-text { font-size: 15px; color: #34495e; margin-bottom: 15px; font-family: -apple-system, sans-serif; }
    .forum-tags { display: inline-block; background-color: #e8f8f5; color: #16a085; padding: 4px 8px; border-radius: 4px; font-size: 12px; margin-right: 5px; margin-bottom: 20px;}
    .forum-answer-header { font-size: 18px; font-weight: 500; color: #2c3e50; padding-top: 15px; border-top: 1px solid #d2d7d3; margin-bottom: 15px;}
    .forum-answer-box { display: flex; align-items: flex-start; margin-bottom: 15px;}
    .forum-votes { display: flex; flex-direction: column; align-items: center; margin-right: 20px; color: #bdc3c7; font-size: 18px;}
    .forum-votes span { color: #7f8c8d; font-size: 20px; font-weight: bold; margin: 5px 0; }
    .forum-accepted { color: #27ae60; font-size: 24px; margin-top: 5px;}
    
    /* Cajas de alerta para lo que debes cambiar */
    .alert-cambio { background-color: #fcf3cf; border-left: 4px solid #f1c40f; padding: 10px; margin-bottom: 10px; font-size: 14px; color: #7d6608;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# BARRA LATERAL (ÍNDICE)
# ==========================================
st.sidebar.markdown("### 🔍 Search Results")
menu = st.sidebar.radio(
    "Selecciona el hilo de discusión:",
    [
        "1. Exploración y Limpieza (Pandas)", 
        "2. Gráficos Nativos Pandas", 
        "3. Gráfico Marimekko", 
        "4. Matplotlib y Subplots",
        "5. Ejemplo 1"
    ]
)

# ==========================================
# CONTENIDO DINÁMICO SEGÚN LA SELECCIÓN
# ==========================================

if menu == "1. Exploración y Limpieza (Pandas)":
    st.markdown('<div class="forum-title">Standard procedure for data exploration and cleaning in Pandas?</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-stats">Asked 2 years ago | Active today | Viewed 14k times</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-q-text">What is the most robust template for loading, exploring, cleaning nulls/duplicates, and filtering outliers using the IQR method in a dataset?</div>', unsafe_allow_html=True)
    st.markdown('<span class="forum-tags">python</span><span class="forum-tags">pandas</span><span class="forum-tags">data-cleaning</span><span class="forum-tags">outliers</span>', unsafe_allow_html=True)

    st.markdown('<div class="forum-answer-header">1 Answer</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="forum-answer-box">
        <div class="forum-votes">▲<br><span>842</span><br>▼<br><div class="forum-accepted">✔️</div></div>
        <div style="width: 100%;">
            <div class="forum-q-text">Here is a complete template. Pay attention to the variables you need to adapt to your specific dataset:</div>
            <div class="alert-cambio">⚠️ <b>ATENCIÓN:</b> Cambiar el nombre del CSV, valores de llenado de nulos, condiciones lógicas del query y la columna para evaluar outliers.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    codigo_limpieza = '''import pandas as pd

# CAMBIAR: 'tu_archivo.csv' por el nombre del archivo del parcial
df = pd.read_csv('tu_archivo.csv') 

# === 1. VISTAS RÁPIDAS (No necesitan cambios) ===
df.info()
resumen_estadistico = df.describe()
nulos_por_columna = df.isnull().sum()
valores_unicos = df.nunique()

# === 2. LIMPIEZA Y FILTRADO ===
df_sin_nulos = df.dropna()
# CAMBIAR: 0 por el valor que te pidan (ej. df['col'].mean())
df_nulos_cero = df.fillna(0) 
df_sin_duplicados = df.drop_duplicates()

# Filtrado con Query -> CAMBIAR: La condición lógica
datos_filtrados = df.query('Age >= 18 and Survived == 1')

# Agrupación -> CAMBIAR: 'Sex' y 'Pclass'
conteo_categorias = df['Sex'].value_counts()
promedio_grupos = df.groupby('Pclass').mean(numeric_only=True)

# === 3. DETECCIÓN DE OUTLIERS (Método IQR) ===
# CAMBIAR: 'Fare' por la columna numérica a evaluar
col_outliers = 'Fare' 
columna_a_evaluar = df[col_outliers]

Q1 = columna_a_evaluar.quantile(0.25)
Q3 = columna_a_evaluar.quantile(0.75)
IQR = Q3 - Q1

limite_inf = Q1 - (1.5 * IQR)
limite_sup = Q3 + (1.5 * IQR)

mascara_outliers = (columna_a_evaluar < limite_inf) | (columna_a_evaluar > limite_sup)
dataframe_solo_outliers = df[mascara_outliers]
dataframe_sin_outliers = df[~mascara_outliers]'''
    st.code(codigo_limpieza, language='python')

elif menu == "2. Gráficos Nativos Pandas":
    st.markdown('<div class="forum-title">How to plot basic charts directly from a Pandas DataFrame?</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-stats">Asked 5 months ago | Viewed 3.2k times</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-q-text">I need to generate histograms, bar charts, scatter plots, and boxplots without writing too much matplotlib boilerplate.</div>', unsafe_allow_html=True)
    st.markdown('<span class="forum-tags">pandas</span><span class="forum-tags">data-visualization</span>', unsafe_allow_html=True)

    st.markdown('<div class="forum-answer-header">1 Answer</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="forum-answer-box">
        <div class="forum-votes">▲<br><span>315</span><br>▼<br><div class="forum-accepted">✔️</div></div>
        <div style="width: 100%;">
            <div class="alert-cambio">⚠️ <b>ATENCIÓN:</b> Cambiar nombres de columnas ('Age', 'Sex', 'Fare', 'Pclass') y configurar los títulos/bins según pida el ejercicio.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    codigo_pandas_plots = '''import matplotlib.pyplot as plt

# Histograma -> CAMBIAR: 'Age', cantidad de bins y title
df['Age'].plot.hist(bins=15, title='Histograma de Distribución')
plt.show()

# Gráfico de Barras (Frecuencias) -> CAMBIAR: 'Sex'
df['Sex'].value_counts().plot(kind='bar', title='Frecuencia por Categoría')
plt.show()

# Dispersión (Scatter) -> CAMBIAR: 'Age' (X) y 'Fare' (Y)
df.plot.scatter(x='Age', y='Fare', title='Dispersión')
plt.show()

# Boxplot -> CAMBIAR: column='Fare' (numérica), by='Pclass' (categórica)
df.plot.box(column='Fare', by='Pclass', title='Cajas por Grupo')
plt.show()'''
    st.code(codigo_pandas_plots, language='python')

elif menu == "3. Gráfico Marimekko":
    st.markdown('<div class="forum-title">Implementing a Marimekko (Mosaic) chart in Python</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-stats">Asked 1 year ago | Viewed 8k times</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-q-text">What is the most efficient mathematical approach to plot a Marimekko chart using matplotlib?</div>', unsafe_allow_html=True)
    st.markdown('<span class="forum-tags">matplotlib</span><span class="forum-tags">marimekko</span><span class="forum-tags">advanced-dataviz</span>', unsafe_allow_html=True)

    st.markdown('<div class="forum-answer-header">1 Answer</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="forum-answer-box">
        <div class="forum-votes">▲<br><span>590</span><br>▼<br><div class="forum-accepted">✔️</div></div>
        <div style="width: 100%;">
            <div class="alert-cambio">⚠️ <b>ATENCIÓN:</b> NO TOCAR los cálculos matemáticos. Solo cambia las variables de las columnas, la paleta de colores (HEX) y los textos de los ejes.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    codigo_marimekko = '''import numpy as np
import matplotlib.ticker as mtick

# CAMBIAR: Nombres de las columnas para el cruce de datos
col_x = 'Nombre_Columna_Horizontal' 
col_y = 'Nombre_Columna_Apilada'    

cross_tab = pd.crosstab(df[col_x], df[col_y])

# --- CÁLCULOS MATEMÁTICOS DE PROPORCIONES (NO TOCAR) ---
bar_widths = cross_tab.sum(axis=1)
widths_normalized = bar_widths / bar_widths.sum()
heights_normalized = cross_tab.div(bar_widths, axis=0)
x_positions = np.append(0, widths_normalized.cumsum()[:-1])
# -------------------------------------------------------

fig, ax = plt.subplots(figsize=(12, 8))
bottoms = np.zeros(len(cross_tab))

# CAMBIAR: Agregar o quitar colores HEX según categorías en col_y
colores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

for i, col in enumerate(heights_normalized.columns):
    ax.bar(
        x_positions, heights_normalized[col], width=widths_normalized,
        bottom=bottoms, align='edge', edgecolor='white',
        color=colores[i], label=col
    )
    bottoms += heights_normalized[col]

# Estética y Etiquetas (Automático)
centro_barras = x_positions + (widths_normalized / 2)
ax.set_xticks(centro_barras)
ax.set_xticklabels(cross_tab.index, rotation=45, ha='right')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

# CAMBIAR: Textos de los títulos y etiquetas
plt.title('Título Principal del Gráfico', fontsize=16, pad=20)
plt.ylabel('Proporción (100%)', fontsize=12)
plt.legend(title='Categorías', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()'''
    st.code(codigo_marimekko, language='python')

elif menu == "4. Matplotlib y Subplots":
    st.markdown('<div class="forum-title">Creating a 2x2 grid with mixed plot types (Matplotlib)</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-stats">Asked 3 months ago | Viewed 5.1k times</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-q-text">Need a reference template for subplots, pie charts, violin plots, and custom scatter bubbles.</div>', unsafe_allow_html=True)
    st.markdown('<span class="forum-tags">matplotlib</span><span class="forum-tags">subplots</span>', unsafe_allow_html=True)

    st.markdown('<div class="forum-answer-header">1 Answer</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="forum-answer-box">
        <div class="forum-votes">▲<br><span>422</span><br>▼<br><div class="forum-accepted">✔️</div></div>
        <div style="width: 100%;">
            <div class="alert-cambio">⚠️ <b>ATENCIÓN:</b> Reemplazar los datos sintéticos (np.random / x_val) por las variables reales de tu DataFrame. Presta atención a los parámetros de diseño (alpha, c, s, explode).</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    codigo_subplots = '''# === PARTE 1: GRILLA 2x2 ===
# Variables de prueba (Reemplazar con datos reales)
x_val = np.linspace(0, 20, 50)
y_val = np.sin(x_val)

fig = plt.figure(figsize=(10, 8)) # CAMBIAR: Tamaño de ventana

# Cuadrante 1: Línea simple
plt.subplot(2, 2, 1)
plt.plot(x_val, y_val, 'g--', label="Línea 1") # CAMBIAR: 'g--' por formato requerido
plt.legend(); plt.title("Cuadrante 1")

# Cuadrante 2: Líneas y ruido
plt.subplot(2, 2, 2)
y_ruido = y_val + (np.random.random(y_val.shape) - 0.5) * 0.5
plt.plot(x_val, y_val, color="black", linewidth=1)
plt.scatter(x_val, y_ruido, c="red", alpha=0.4, label="Ruido") # CAMBIAR: color y alpha
plt.legend()

# Cuadrante 3: Barras Básicas
plt.subplot(2, 2, 3)
categorias = np.array(["A", "B", "C", "D"]) # CAMBIAR: Etiquetas
valores = np.array([3, 8, 1, 10])           # CAMBIAR: Datos numéricos
plt.bar(categorias, valores, color="purple")
plt.xlabel("Eje X"); plt.ylabel("Eje Y")

# Cuadrante 4: Burbujas
plt.subplot(2, 2, 4)
N = 50 
x_burb, y_burb, colores = np.random.rand(N), np.random.rand(N), np.random.rand(N)
area = (30 * np.random.rand(N))**2 # CAMBIAR: Multiplicador 30 para radio
plt.scatter(x_burb, y_burb, s=area, c=colores, alpha=0.5)

plt.tight_layout()
plt.show()

# === PARTE 2: GRÁFICOS INDIVIDUALES ===

# 1. Pastel (Pie Chart)
sizes = [15, 30, 45, 10] # CAMBIAR: Tamaños
labels = ['Cat A', 'Cat B', 'Cat C', 'Cat D']
myexp = [0.1, 0, 0, 0] # CAMBIAR: Qué porción resaltar (0.1 separa)

plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=90, explode=myexp)
plt.axis('equal'); plt.title("Gráfico de Proporciones")
plt.show()

# 2. Boxplot Avanzado
data_box = np.random.normal(100, 15, 200) # Reemplazar con datos reales
# CAMBIAR: notch (True/False para muescas), vert (Vertical/Horizontal)
plt.boxplot(data_box, notch=True, vert=False) 
plt.grid(True); plt.title("Boxplot con Matplotlib")
plt.show()

# 3. Violin Plot (Densidad)
data_vio = [np.random.normal(0, std, 100) for std in range(1, 5)] 
plt.violinplot(data_vio, showmedians=True)
# CAMBIAR: Ticks y labels según la cantidad de grupos
plt.xticks([1, 2, 3, 4], ['G1', 'G2', 'G3', 'G4']) 
plt.title('Diagramas de Violín')
plt.show()'''
    st.code(codigo_subplots, language='python')

elif menu == "5. EJEMPLO PRÁCTICO: Taller 01 (Titanic)":
    st.markdown('<div class="forum-title">Full EDA Example solving Workshop 1 (Titanic Dataset)?</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-stats">Asked yesterday | Active today | Viewed 1.5k times</div>', unsafe_allow_html=True)
    st.markdown('<div class="forum-q-text">Can someone provide the exact code sequence to perform the EDA on the Titanic dataset, including info extraction, null dropping, basic plotting, and outlier detection?</div>', unsafe_allow_html=True)
    st.markdown('<span class="forum-tags">python</span><span class="forum-tags">eda</span><span class="forum-tags">titanic</span><span class="forum-tags">workshop-solution</span>', unsafe_allow_html=True)

    st.markdown('<div class="forum-answer-header">1 Answer</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="forum-answer-box">
        <div class="forum-votes">▲<br><span>99</span><br>▼<br><div class="forum-accepted">✔️</div></div>
        <div style="width: 100%;">
            <div class="forum-q-text">Here is the consolidated code based on the expected workflow for that specific dataset. This brings together all the templates into a real-world scenario:</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    codigo_taller = '''import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset (URL original del Taller)
df = pd.read_csv("https://drive.google.com/uc?id=1ecyq7xyieIlGkz-hx1qroq19P31ojA50")

# 2. Exploración básica: Vistas y Dimensiones
print("Primeras 5 filas:\\n", df.head())
print("\\nDimensiones (filas, columnas):", df.shape)
print("\\nÚltimas 5 filas:\\n", df.tail())

# 3. Información general y resumen estadístico
print("\\nInformación del Dataset:")
df.info()
print("\\nEstadísticas Principales:\\n", df.describe())

# 4. Limpieza: Eliminar valores faltantes (Drop missing values)
df.dropna(inplace=True)

# 5. Visualización: Histograma de Edad (15 bins)
df['Age'].plot.hist(bins=15, title='Distribution of Value')
plt.show()

# 6. Visualización: Cantidad de pasajeros que sobrevivieron por género
dff = df.query('Survived == 1')
dff['Sex'].value_counts().plot(kind='bar')
plt.ylabel("Cantidad")
plt.show()

# 7. Detección de Outliers en "Fare" (Método IQR) y guardado en DataFrame
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

outlier_mask = (df['Fare'] < lower_bound) | (df['Fare'] > upper_bound)
outliers_df = df[outlier_mask]

print("\\nDataFrame de Outliers:\\n", outliers_df)

# 8. Mostrar dimensiones del dataframe de outliers
print("\\nDimensiones del DataFrame de Outliers:", outliers_df.shape)
'''
    st.code(codigo_taller, language='python')