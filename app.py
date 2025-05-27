import streamlit as st
from src.autenticacion import verificar_login, registrar_usuario

st.title("Sistema de Ropa Inteligente")

menu = ["Iniciar sesión", "Registrar nuevo usuario"]
eleccion = st.sidebar.selectbox("Menú", menu)

if eleccion == "Iniciar sesión":
    st.subheader("Inicia sesión")
    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        if verificar_login(usuario, contraseña):
            st.success(f"Bienvenido, {usuario}!")
            st.session_state["usuario"] = usuario
            # Aquí irá el sistema principal
        else:
            st.error("Credenciales incorrectas")

elif eleccion == "Registrar nuevo usuario":
    st.subheader("Registro")
    nuevo_usuario = st.text_input("Nuevo usuario")
    nueva_clave = st.text_input("Nueva contraseña", type="password")
    if st.button("Registrar"):
        if registrar_usuario(nuevo_usuario, nueva_clave):
            st.success("Usuario registrado exitosamente")
        else:
            st.warning("Ese usuario ya existe")
