import streamlit as st

st.set_page_config(page_title="WinGo Analyzer", layout="centered")

st.title("🎯 WinGo Analyzer")

# Session state initialize karna
if 'numbers' not in st.session_state:
    st.session_state.numbers = []

# Function: Number add karne ke liye
def add_number(num):
    if len(st.session_state.numbers) >= 20:  # Sirf pichle 20 results
        st.session_state.numbers.pop(0)
    st.session_state.numbers.append(num)

# Function: Clear karne ke liye
def clear_numbers():
    st.session_state.numbers = []

st.write("Game ka result aate hi niche wale button dabaiye:")

# 0-9 ke buttons ka layout
cols = st.columns(5)

for i in range(10):
    if i < 5:
        with cols[i]:
            if st.button(str(i), use_container_width=True):
                add_number(i)
                st.rerun()
    else:
        with cols[i - 5]:
            if st.button(str(i), use_container_width=True):
                add_number(i)
                st.rerun()

# Delete aur Clear buttons
st.write("")
col_del, col_clear = st.columns(2)
with col_del:
    if st.button("⬅️ Last Delete", use_container_width=True):
        if st.session_state.numbers:
            st.session_state.numbers.pop()
        st.rerun()
with col_clear:
    if st.button("🗑️ Clear All", use_container_width=True):
        clear_numbers()
        st.rerun()

st.write("---")
st.subheader("Aapke Daale Hue Numbers:")
if st.session_state.numbers:
    st.write(" ".join([str(n) for n in st.session_state.numbers]))
else:
    st.write("Abhi koi number nahi daala.")

# Analysis aur Prediction Logic
if len(st.session_state.numbers) >= 5:
    numbers = st.session_state.numbers
    big_count = len([n for n in numbers if n >= 5])
    small_count = len(numbers) - big_count
    
    green_count = len([n for n in numbers if n in [1, 3, 7, 9]])
    red_count = len([n for n in numbers if n in [2, 4, 6, 8]])
    violet_count = len([n for n in numbers if n in [0, 5]])
    
    st.subheader("📊 Analysis Report")
    col1, col2, col3 = st.columns(3)
    col1.metric("Big", big_count)
    col2.metric("Small", small_count)
    col3.metric("Green", green_count)
    
    col4, col5 = st.columns(2)
    col4.metric("Red", red_count)
    col5.metric("Violet", violet_count)
    
    st.subheader("🤖 Prediction Suggestion")
    if big_count > small_count:
        st.warning("Agla result 'Small' aa sakta hai (Big zyada hai).")
    elif small_count > big_count:
        st.info("Agla result 'Big' aa sakta hai (Small zyada hai).")
    else:
        st.write("Big aur Small barabar hain.")
        
    last_three = numbers[-3:]
    if all(n >= 5 for n in last_three):
        st.error("⚠️ Alert: Lagatar 3 baar 'Big' aa chuka hai!")
    elif all(n < 5 for n in last_three):
        st.error("⚠️ Alert: Lagatar 3 baar 'Small' aa chuka hai!")
