import streamlit as st
import math

# --- FUNGSI HELPER (LOGIKA MATEMATIKA) ---
def get_factorial_series(n, limit=12):
    if n == 0 or n == 1:
        return "1"
    if n <= limit:
        return r" \times ".join([str(i) for i in range(n, 0, -1)])
    else:
        return rf"{n} \times {n-1} \times \dots \times 1"

def generate_steps_permutation(n, r):
    numerator = math.factorial(n)
    denominator = math.factorial(n - r)
    result = numerator // denominator
    
    series_n = get_factorial_series(n)
    series_nr = get_factorial_series(n - r)
    
    step1 = r"P(n, r) = \frac{n!}{(n-r)!}"
    
    # Memastikan pemisah antar faktorial jelas
    step2 = rf"P({n}, {r}) = \frac{{{n}!}}{{({n}-{r})!}} = \frac{{{n}!}}{{{n-r}!}}"
    
    step3 = rf"= \frac{{{series_n}}}{{{series_nr}}}"
    step4 = rf"= \frac{{{numerator:,}}}{{{denominator:,}}}"
    step5 = rf"= {result:,}"
    
    return result, [step1, step2, step3, step4, step5]

def generate_steps_combination(n, r):
    numerator = math.factorial(n)
    denom_r = math.factorial(r)
    denom_nr = math.factorial(n - r)
    denominator = denom_r * denom_nr
    result = numerator // denominator
    
    series_n = get_factorial_series(n)
    series_r = get_factorial_series(r)
    series_nr = get_factorial_series(n - r)
    
    step1 = r"C(n, r) = \frac{n!}{r!(n-r)!}"
    
    step2 = rf"C({n}, {r}) = \frac{{{n}!}}{{{r}!({n}-{r})!}} = \frac{{{n}!}}{{{r}! \times {n-r}!}}"
    
    step3 = rf"= \frac{{{series_n}}}{{({series_r}) \times ({series_nr})}}"
    
    step4 = rf"= \frac{{{numerator:,}}}{{{denom_r:,} \times {denom_nr:,}}}"
    
    step5 = rf"= {result:,}"
    
    return result, [step1, step2, step3, step4, step5]

# --- UI STREAMLIT ---
st.set_page_config(page_title="Kalkulator PK", page_icon="📊")

hide_streamlit_style = """
            <style>
            div[data-testid="InputInstructions"] > span:nth-child(1) {
                visibility: hidden;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Judul Utama
st.title("Kalkulator Permutasi & Kombinasi")

# --- FORM INPUT ---
with st.form("kalkulator_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Metode Perhitungan")
        mode = st.radio("Label Hidden", ["Permutasi (P)", "Kombinasi (C)"], label_visibility="collapsed")

    with col2:
        st.markdown("### Nilai n")
        n = st.number_input("n", min_value=0, value=10, step=1, label_visibility="collapsed")

    with col3:
        st.markdown("### Nilai r")
        r = st.number_input("r", min_value=0, value=5, step=1, label_visibility="collapsed")

    st.write("") 
    
    # Tombol Submit
    submitted = st.form_submit_button("Hitung Hasil", use_container_width=True, type="primary")

# --- HASIL PERHITUNGAN ---
if submitted:
    st.divider()
    
    if r > n:
        st.error(f"⚠️ **Error:** Nilai **r** ({r}) tidak boleh lebih besar dari nilai **n** ({n}).")
    else:
        if "Permutasi" in mode:
            st.subheader(f"Hasil Permutasi P({n}, {r})")
            nilai, langkah = generate_steps_permutation(n, r)
            st.info("Info: Permutasi digunakan ketika urutan objek diperhatikan.")
        else:
            st.subheader(f"Hasil Kombinasi C({n}, {r})")
            nilai, langkah = generate_steps_combination(n, r)
            st.info("Info: Kombinasi digunakan ketika urutan objek TIDAK diperhatikan.")

        st.markdown("### Langkah Pengerjaan:")
        
        st.write("1. Rumus:")
        st.latex(langkah[0])
        
        st.write("2. Substitusi:")
        st.latex(langkah[1])
        
        st.write("3. Penjabaran:")
        st.latex(langkah[2])
        
        st.write("4. Hitung:")
        st.latex(langkah[3])
        
        st.write("5. Hasil:")
        st.success(f"**{nilai:,}**")
        st.latex(langkah[4])