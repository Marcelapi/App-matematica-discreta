import random
import streamlit as st

# Configuración de la página web
st.title("Generador y Analizador de Relaciones en A")
st.write("Estudiante: Profesorado de Informática - INET")

# 1. Definir el conjunto A y su producto cartesiano A x A
A = {2, 4, 8}
A_x_A = [(x, y) for x in A for y in A]

st.subheader("Conjunto A y Producto Cartesiano")
st.write(f"**Conjunto A:** `{A}`")
st.write(f"**Producto Cartesiano (A x A):** `{A_x_A}`")


# 2. Función para generar relación aleatoria
def generar_relacion_aleatoria():
  k = random.randint(0, len(A_x_A))
  relacion = random.sample(A_x_A, k)
  return set(relacion)


# Botón interactivo en la app
if st.button("Generar nueva relación aleatoria"):
  relacion_actual = generar_relacion_aleatoria()

  st.subheader("Relación Seleccionada (R)")
  st.write(f"`{relacion_actual}`")

  # 3. Determinar si es reflexiva
  # Una relación es reflexiva si contiene todos los elementos de la forma (x, x) para todo x en A
  pares_reflexivos = {(x, x) for x in A}
  es_reflexiva = pares_reflexivos.issubset(relacion_actual)

  # 4. Determinar si es simétrica
  # Una relación es simétrica si para cada (x, y) en R, su inverso (y, x) también está en R
  es_simetrica = True
  for x, y in relacion_actual:
    if (y, x) not in relacion_actual:
      es_simetrica = False
      break

  # 5. Informar claramente los resultados en la interfaz
  st.subheader("Resultados del Análisis de Propiedades")

  if es_reflexiva:
    st.success("✅ La relación **ES REFLEXIVA** (contiene todos los pares de identidad).")
  else:
    st.error("❌ La relación **NO ES REFLEXIVA** (faltan pares de identidad).")

  if es_simetrica:
    st.success("✅ La relación **ES SIMÉTRICA** (todos sus pares tienen su inverso).")
  else:
    st.error(
        "❌ La relación **NO ES SIMÉTRICA** (hay pares que no tienen su"
        " inverso)."
    )