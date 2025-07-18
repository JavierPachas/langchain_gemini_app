import streamlit as st
import langchain_menu 
st.title("Generate Restaurant Name")

cuisine = st.sidebar.selectbox("Select a Cuisine", ("Peruvian", "Mexican","Italian","American","Chinese","Korean"))


if cuisine:
    response = langchain_menu.generator_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu items**")
    for item in menu_items:
        st.write("-", item)

