#number guessing game
import streamlit as st
import random

st.title("Number Guessing Game😁")
st.write("Guess a number between 0-100")
if "number" not in st.session_state:
     st.session_state.number=random.randint(0,100)   
if "store" not in st.session_state:
     st.session_state.store=0


    
num=st.number_input("Enter a number",min_value=0, max_value=100, step=1)
if st.button("Guess"):
    st.session_state.store+=1
    if num==st.session_state.number:
        st.success(f"Congratulations! You Gussed It!{st.session_state.store} attempts!")
    elif num>st.session_state.number:
        st.warning("Too High")
    else:
        st.warning("Too Low")
if st.button("Restart Game"):
    st.session_state.number=random.randint(0,100)
    st.session_state.store=0
    st.rerun()               

