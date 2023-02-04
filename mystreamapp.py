import streamlit as st
from gsheetsdb import connect
#read data from .streamlit\secrets.toml file
#newvalue = st.secrets["oldvalue"]
#st.write(newvalue)

# Remove the sandwich menu in the upper right corner
hide_streamlit_style = """
            <style>
            # MainMenu {visibility: hidden;}
            header, footer {visibility: hidden;}
            div.block-container {padding-top:1rem;padding-left:2rem;padding-right:2rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#normal html tag
heading = """<h1>Welcome My google Sheet Application</h1>"""
st.markdown(heading, unsafe_allow_html=True)

conn = connect()

@st.cache(ttl=60)
def run_query(sql):
    rows = conn.execute(sql, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_google_sheet"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
for row in rows:
    st.write(f"Name: {row.Name} Title: {row.Title} Number: {row.Number} Email: {row.Email} ")
    img = f'<img src="{row.Photo}"  width="300" height="300">'
    st.markdown(img, unsafe_allow_html=True)
    #st.image(row.Photo)
