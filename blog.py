import streamlit as st
import time
import sqlite3 as sql
conn = sql.connect("db.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS myblog(id INTEGER PRIMARY KEY AUTOINCREMENT, author TEXT, title TEXT, blog TEXT, postdate DATE)")

def add_data(authorD,titleD,blogD,postdateD):
    c.execute("INSERT INTO myblog(author,title,blog,postdate) VALUES(?,?,?,?)",(authorD,titleD,blogD,postdateD))
    conn.commit()

def view_title():
    c.execute("SELECT DISTINCT title FROM myblog order by rowid DESC")
    data = c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute("SELECT * FROM myblog where title =  '{}'".format(title))
    data = c.fetchall()
    return data

def get_all_data():
    c.execute("SELECT * FROM myblog")
    data = c.fetchall()
    return data

def delete_blog(title):
    c.execute("DELETE FROM myblog where title = '{}'".format(title))
    conn.commit()

with st.sidebar:
    choise = st.selectbox("Menu",["Home","View Blog"])
if (choise == "Home"):
    st.write("Home")
    author = st.text_input("Enter Author Name:")
    title = st.text_input("Enter Blog Title:")
    blog = st.text_area("Enter Blog Text(with markdown symbol):")
    blogdt = time.strftime("%d/%m/%y",time.gmtime())
    btn = st.button("Add Blog")
    if btn:
        create_table()
        add_data(author, title, blog, blogdt)

elif (choise == "View Blog"):
    all_titles = [i[0] for i in view_title()]
    selblog = st.sidebar.selectbox("Select Blog",all_titles)
    if selblog:
        all_data = get_blog_by_title(selblog)
        for i in all_data:
            st.write(i[0])
            st.write(i[1])
            st.write(i[2])
            st.write(i[3])