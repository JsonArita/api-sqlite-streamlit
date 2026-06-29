import streamlit as st
from api_client import obtener_usuarios_api
from database import (
    crear_tabla,
    guardar_usuarios,
    obtener_usuarios,
    eliminar_datos
)

st.set_page_config(
    page_title="API + SQLite + Streamlit",
    layout="wide"
)

crear_tabla()

st.title("Proyecto Cloud: API + SQLite + Streamlit")

st.write(
    """
Aplicación que consume una API pública, guarda la información en SQLite y permite consultarla mediante una interfaz desarrollada con Streamlit.
"""
)

menu = st.sidebar.selectbox(
    "Seleccione una opción",
    [
        "Inicio",
        "Consumir API",
        "Ver base de datos",
        "Buscar usuario",
        "Eliminar datos"
    ]
)

# -------------------------------------------------
# Inicio
# -------------------------------------------------

if menu == "Inicio":

    st.header("Panel principal")

    st.write("""
Esta aplicación simula una arquitectura básica de Computación en la Nube.

Componentes utilizados:

- API pública (JSONPlaceholder)
- SQLite
- Streamlit
- GitHub
- Streamlit Cloud
""")

    st.info("Seleccione una opción desde el menú lateral.")

# -------------------------------------------------
# Consumir API
# -------------------------------------------------

elif menu == "Consumir API":

    st.header("Consumir API Pública")

    st.code("https://jsonplaceholder.typicode.com/users")

    if st.button("Obtener datos desde API"):

        usuarios = obtener_usuarios_api()

        if usuarios:

            guardar_usuarios(usuarios)

            st.success("Los usuarios fueron almacenados correctamente.")

            st.subheader("Primer usuario obtenido")

            st.json(usuarios[0])

        else:

            st.error("No fue posible consumir la API.")

# -------------------------------------------------
# Ver Base de Datos
# -------------------------------------------------

elif menu == "Ver base de datos":

    st.header("Usuarios almacenados")

    df = obtener_usuarios()

    if df.empty:

        st.warning("No existen registros.")

    else:

        st.dataframe(df, use_container_width=True)

        col1, col2, col3 = st.columns(3)

        col1.metric("Usuarios", len(df))
        col2.metric("Ciudades", df["ciudad"].nunique())
        col3.metric("Correos", df["email"].nunique())

# -------------------------------------------------
# Buscar Usuario
# -------------------------------------------------

elif menu == "Buscar usuario":

    st.header("Buscar usuario")

    df = obtener_usuarios()

    if df.empty:

        st.warning("No existen datos.")

    else:

        texto = st.text_input("Ingrese nombre o usuario")

        if texto:

            resultado = df[
                df["nombre"].str.contains(texto, case=False, na=False)
                |
                df["usuario"].str.contains(texto, case=False, na=False)
            ]

            if resultado.empty:

                st.error("No se encontraron resultados.")

            else:

                st.success(f"Se encontraron {len(resultado)} usuario(s).")

                st.dataframe(resultado, use_container_width=True)

# -------------------------------------------------
# Eliminar Datos
# -------------------------------------------------

elif menu == "Eliminar datos":

    st.header("Eliminar registros")

    st.warning("Esta acción eliminará todos los usuarios almacenados.")

    if st.button("Eliminar todos"):

        eliminar_datos()

        st.success("Todos los registros fueron eliminados correctamente.")