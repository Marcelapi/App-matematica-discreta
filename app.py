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
    .card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #003366;
        margin-bottom: 15px;
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
A = {2, 4, 8}
A_x_A = [(x, y) for x in A for y in A]

col1, col2 = st.columns(2)
with col1:
  st.info(f"**Conjunto A:**\n`{A}`")
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
  relacion_actual = sorted(list(set(random.sample(A_x_A, k))))

  # Contenedor visual para la relación
  st.markdown("### Relación Seleccionada ($R$)")
  if relacion_actual:
    st.success(f"**$R$ =** `{set(relacion_actual)}`")
  else:
    st.warning("**$R$ =** `∅` (Relación vacía)")

  # --- 3. EVALUACIÓN DE PROPIEDADES ---
  pares_reflexivos = {(x, x) for x in A}
  es_reflexiva = pares_reflexivos.issubset(set(relacion_actual))

  es_simetrica = True
  for x, y in relacion_actual:
    if (y, x) not in relacion_actual:
      es_simetrica = False
      break

  # --- 4. RESULTADOS VISUALES ---
  st.markdown("### 📊 Análisis de Propiedades")

  col_ref, col_sim = st.columns(2)

  with col_ref:
    st.markdown("#### Reflexividad")
    if es_reflexiva:
      st.success("✅ **Es Reflexiva**\n\nContiene todos los pares $(x, x)$.")
    else:
      st.error(
          "❌ **No es Reflexiva**\n\nFaltan pares de identidad de la forma"
          " $(x, x)$."
      )

  with col_sim:
    st.markdown("#### Simetría")
    if es_simetrica:
      st.success(
          "✅ **Es Simétrica**\n\nPara todo $(x, y) \\in R$, su inverso"
          " $(y, x)$ también está."
      )
    else:
      st.error(
          "❌ **No es Simétrica**\n\nExisten pares que no tienen su simétrico"
          " invertido."
      )
