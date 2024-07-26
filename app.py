import streamlit as st
import urllib.parse

def main():
    col1, col2 = st.columns(2)
    with col1:
        st.image('mhc_logo.png')
    with col2:
        st.image('happy_people.jpeg')
        
    st.title("Bienvenido a la Sala de Quirófanos")
    st.write("¡Creamos experiencias únicas!")
    st.write("Aquí puedes encontrar información y solicitar servicios adicionales.")

    menu = ["Inicio", "Servicios", "Información de Contacto", "Encuesta"]
    choice = st.selectbox("Selecciona una opción", menu)
    
    if choice == "Inicio":
        st.subheader("Inicio")
        st.write("Bienvenido a la Sala de Quirófanos. Navega por las diferentes secciones para más información.")
    
    elif choice == "Servicios":
        st.subheader("Servicios Disponibles")
        st.write("1. **Clave de WIFI:** Tu clave de WIFI es **ABC123**.")
        st.write("2. **Café:** Puedes solicitar 1 café gratuito haciendo clic en el botón a continuación.")
        if st.button("Solicitar Café"):
            mensaje = urllib.parse.quote("Quiero el café de cortesía")
            st.markdown(f"[Enviar solicitud de café](https://wa.me/5930993513082?text={mensaje})")
        st.write("3. **Servicios de Catering:** Completa el formulario a continuación para solicitar catering.")
        with st.form(key='catering_form'):
            nombre = st.text_input("Nombre")
            servicio = st.selectbox("Tipo de Servicio", ["Bocadillos", "Bebidas", "Comida Completa"])
            cantidad = st.number_input("Cantidad", min_value=1)
            submit_button = st.form_submit_button(label='Enviar Solicitud')
            if submit_button:
                mensaje = urllib.parse.quote(f"Quiero {servicio} para {cantidad} personas")
                st.markdown(f"[Enviar solicitud de catering](https://wa.me/5930993513082?text={mensaje})")
                st.write(f"Solicitud de catering recibida para {nombre}. Tipo de servicio: {servicio}. Cantidad: {cantidad}.")
    
    elif choice == "Información de Contacto":
        st.subheader("Información de Contacto")
        st.write("Para asistencia adicional, por favor contacta a:")
        st.write("Teléfono: 123-456-789")
        st.write("Correo Electrónico: soporte@hospital.com")
    
    elif choice == "Encuesta":
        st.subheader("Encuesta de Satisfacción")
        st.write("Por favor, califica tu experiencia con los servicios:")
        rating = st.slider("Calificación", 1, 5)
        feedback = st.text_area("Comentarios")
        if st.button("Enviar"):
            st.write(f"Gracias por tu calificación de {rating} estrellas y tus comentarios: {feedback}")

if __name__ == "__main__":
    main()
