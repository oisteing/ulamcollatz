import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ulam-Collatz-løkke")

st.title("🔁 Ulam-Collatz-løkke – steg for steg")

# Brukarinput
starttall = st.number_input("Vel starttalet ditt", min_value=1, value=7, step=1)

# Start på nytt automatisk viss starttallet endrast
if "forrige_start" not in st.session_state or st.session_state.forrige_start != starttall:
    st.session_state.forrige_start = starttall
    st.session_state.sekvens = [starttall]
    st.session_state.ferdig = False

# Neste steg-knappen
if st.button("Neste steg"):
    if not st.session_state.ferdig:
        n = st.session_state.sekvens[-1]
        if n == 1:
            st.session_state.ferdig = True
        else:
            neste = n // 2 if n % 2 == 0 else 3 * n + 1
            st.session_state.sekvens.append(neste)
            if neste == 1:
                st.session_state.ferdig = True

# Vis status
gjeldande = st.session_state.sekvens[-1]
st.write(f"**Gjeldande verdi:** {gjeldande}")
st.write(f"**Antal steg:** {len(st.session_state.sekvens) - 1}")

# Teikn graf
fig, ax = plt.subplots()
ax.plot(range(len(st.session_state.sekvens)), st.session_state.sekvens, marker='o', linestyle='-')
ax.set_xlabel("Iterasjon")
ax.set_ylabel("Verdi")
ax.set_title("Ulam-Collatz-sekvens")
st.pyplot(fig)

# Ferdig?
if st.session_state.ferdig:
    st.success("🎉 Du er ferdig – sekvensen enda med 1!")

