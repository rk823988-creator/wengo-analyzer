import streamlit as st

st.title("🎯 WinGo Analyzer App")
st.write("Apne pichle results daaliye aur analysis dekhiye.")

user_input = st.text_input("Numbers daaliye (comma lagakar):", "9,7,3,7,8,8,5,3,1,6")

if st.button("Analyze Karein"):
    try:
        numbers = [int(num) for num in user_input.split(",")]
        green_count = red_count = violet_count = big_count = small_count = 0
        
        for num in numbers:
            if num >= 5:
                big_count += 1
            else:
                small_count += 1
            if num in [1, 3, 7, 9]:
                green_count += 1
            elif num in [2, 4, 6, 8]:
                red_count += 1
            elif num in [0, 5]:
                violet_count += 1
        
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
            
    except:
        st.error("Kripya sahi numbers daaliye (comma lagakar).")
