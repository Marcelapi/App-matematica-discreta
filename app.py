import random
import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Matemática Discreta - INET", page_icon="🔢", layout="centered"
)

# --- ESTILOS VISUALES CON CSS ---
st.markdown("""
    <style>
    .main-title {
        font-size: 28px;
        color: #003366;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 16px;
        color: #5A6B7C;
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown(
    '<div class="main-title">Analizador de Relaciones en A</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">Estudiante: Laura Marcela Pirez Levin | INET -'
    " Profesorado de Informática</div>",
    unsafe_allow_html=True,
)

st.divider()

# --- 1. DEFINICIÓN DEL CONJUNTO A ---
# Usamos una lista o set ordenado para mostrar siempre {2, 4, 8}
A = {2, 4, 8}
A_ordenado = sorted(list(A))
A_x_A = [(x, y) for x in A_ordenado for y in A_ordenado]

col1, col2 = st.columns(2)
with col1:
  st.info(f"**Conjunto A:**\n`{A_ordenado}`")
with col2:
  st.info(f"**Producto Cartesiano (A x A):**\nTotal de pares: {len(A_x_A)}")

# --- 2. GENERACIÓN DE RELACIÓN ---
st.write("")
if st.button(
    "🎲 Generar nueva relación aleatoria",
    use_container_width=True,
    type="primary",
):
  k = random.randint(0, len(A_x_A))
  # Ordenamos la relación generada para que los pares aparezcan prolijos
  relacion_actual = sorted(list(set(random.sample(A_x_A, k))))
  relacion_set = set(relacion_actual)

  # Contenedor visual para la relación ordenando los pares por orden alfanumérico
  st.markdown("### Relación Seleccionada ($R$)")
  if relacion_set:
    # Mostramos la relación ordenada como lista para que respete el orden
    st.success(f"**$R$ =** `{sorted(list(relacion_set))}`")
  else:
    st.warning("**$R$ =** `∅` (Relación vacía)")

  # --- 3. EVALUACIÓN Y DETALLE DE REFLEXIVIDAD ---
  pares_reflexivos = {(x, x) for x in A}
  faltantes_reflexivos = sorted(list(pares_reflexivos - relacion_set))

  # --- 4. EVALUACIÓN Y DETALLE DE SIMETRÍA ---
  pares_sin_simetrico = []
  for x, y in relacion_set:
    if (y, x) not in relacion_set:
      pares_sin_simetrico.append((x, y))
  pares_sin_simetrico = sorted(list(set(pares_sin_simetrico)))

  # --- 5. RESULTADOS VISUALES CON DETALLES ESPECÍFICOS ---
  st.markdown("### 📊 Análisis de Propiedades")

  col_ref, col_sim = st.columns(2)

  with col_ref:
    st.markdown("#### Reflexividad")
    if not faltantes_reflexivos:
      st.success("✅ **Es Reflexiva**\n\nContiene todos los pares $(x, x)$.")
    else:
      st.error(
          f"❌ **No es Reflexiva**\n\nFaltan los siguientes pares de identidad:"
          f" `{faltantes_reflexivos}`"
      )

  with col_sim:
    st.markdown("#### Simetría")
    if not pares_sin_simetrico:
      st.success(
          "✅ **Es Simétrica**\n\nPara todo $(x, y) \\in R$, su inverso"
          " $(y, x)$ también está."
      )
    else:
      st.error(
          "❌ **No es Simétrica**\n\nLos siguientes pares no tienen su inverso"
          f" en $R$: `{pares_sin_simetrico}`"
      )
