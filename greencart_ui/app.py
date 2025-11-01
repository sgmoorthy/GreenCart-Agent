import streamlit as st
import requests

st.title("GreenCart Agent Marketplace")
q = st.text_input("What organic product are you looking for?")
if st.button("Search") and q:
    response = requests.post("http://localhost:8000/search_catalog", params={"query": q, "top_k": 5})
    products = response.json()
    st.write("Top results:")
    for prod in products:
        st.write(f"{prod['snippet']} (Ref: {prod['doc_id']}, score={prod['score']})")
        st.button(f"Add {prod['snippet']} to cart", key=prod['doc_id'])
else:
    st.write("Try searching for something above.")

if st.button("Checkout"):
    st.success("Proceeding to secure checkout. (Payment token flow starts here)")
