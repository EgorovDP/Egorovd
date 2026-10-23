import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/1.png", width=600)

with col2:
    st.title("Егоров Дмитрий Михайлович")
    content = """
    Учащийся 10 класса, я активно участвую в общественной жизни школы и «Движения Первых»: занимаю должность заместителя председателя Совета Первых Первичного отделения и возглавляю направление «Волонтёрство и добровольчество». Кроме того, выступаю в роли ведущего и организатора различных мероприятий - мне важно не просто быть в гуще событий, а создавать их и вовлекать в них других ребят.
    """
    st.info(content)

content2 = """
Моя история по годам:
"""
st.title(content2)

col3, col4 = st.columns(2)

with col3:
    st.image("images/5.png", width=500)

with col4:
    st.title("2024")
    content3 = """
    Начало моего пути в активистической жизни.
    Первые мероприятия в роли волонтера,
    первые встречи в администрации
    """
    st.write(content3)

col5, col6 = st.columns(2)

with col5:
    st.title("2025")
    content4 = """
    Первая поездка на всероссийское мероприятие
    """
    st.write(content4)

with col6:
    st.image("images/2.png", width=500)

col7, col8 = st.columns(2)

with col7:
    st.image("images/3.png", width=500)

with col8:
    st.title("2026")
    content5 = """
    Получение грамоты от Совета Федерации Федерального Собрания РФ
    """
    st.write(content5)

st.title("Работа вожатым:")

col9, col10, col11 = st.columns(3)

with col9:
    st.image("images/10.png", width=400)

with col10:
    content6 = """
    Было круто
    """
    st.write(content6)

with col11:
    st.image("images/7.png", width=400)

st.title("Волонтерство и добровольчество")

col12, col13 = st.columns(2)

with col12:
    st.write('Волонтерство это круто')

with col13:
    st.image("images/13.png", width=400)
    st.image("images/11.png", width=400)
    st.image("images/12.png", width=400)