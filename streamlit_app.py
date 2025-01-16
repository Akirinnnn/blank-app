import streamlit as st

left, right = st.columns(2)

left.image("profile.PNG", width=250)

right.header("Kira Akimov", anchor=False)

st.header("IT-kompetenz", anchor=False, divider="blue")

st.write("""
            -  Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
            - Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            - Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            - Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            - Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen 
         """)

st.header("Schulbildung", anchor=False, divider="blue")

st.subheader("Fachmittelschule Schaumburgergasse, Wien", anchor=False)

st.write("""
           - ► Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
           - ► Zeitraum: September 2024 - Juli 2025
           - ► Derzeitiger Notenschnitt: 1,5
         """)

st.subheader("FMS4 Schaumburgergasse 4, Wien", anchor=False)

st.write("""
            - ► 🌃 Zeitraum: September 2024 – Juli 2025
            - ► 🌃 Abschluss-Notendurchschnitt
         """)
         
st.header("Arbeitserfahrung", anchor=False, divider="blue")

st.write("""
            - 🚀 Berufspraktische Tage 1: Bei Mcdonald's von 18. bis 22. feb. 2024
            - 🚀 Berufspraktische Tage 2: Bei Kfc von 24. bis 28. Feb. 2023 
         """)

st.header("Zusätzliche Qualifikationen", anchor=False,divider="blue")

st.write("""
            - 🌟 Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien
            - 🌟 Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich
            - 🌟 Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten
         """)

st.header("Interessen und Hobbys", anchor=False, divider="blue")



st.write("""
            - 🌌 Fashion Design: Skizzen von kleidungen
            - 🌌 Sprachen: Fluent in 4 sprachen (De, Eng, Ru, ukr) und lernt noch zwei sprachen 
            - 🌌 Schach: Engagiert im Schachklub
         """)