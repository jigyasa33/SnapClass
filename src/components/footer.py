import streamlit as st

def footer_home():


    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; text-align:center;">
            <p style="font-weight:bold; color:white;">Created with ❤️ by </p>
            <span style="font-size:22px; font-weight:bold; color:white;">
                <p style="max-height:25px; color:black; font-weight:bold;">Jigyasa Rajpoot</p>
            </span>
        </div>

                """, unsafe_allow_html=True)

def footer_dashboard():


    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; text-align:center;">
            <p style="font-weight:bold; color:black;">Created with ❤️ by </p>
            <span style="font-size:20px; font-weight:bold; color:white;">
                <p style="max-height:22px; color:#5865F2; font-weight:bold;">Jigyasa Rajpoot</p>
            </span>
        </div>

                """, unsafe_allow_html=True)