import streamlit as st

# Google AdSense Ad Code with your AdMob Ad Unit ID
adsense_code = """
<!-- Google AdSense ad -->
<iframe src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-5333465889348969&output=html&h=250&slotname=9775276681&width=300&height=250"
        width="300" height="250" frameborder="0" style="border:none; overflow:hidden; width:300px; height:250px;" scrolling="no"></iframe>
"""

# Streamlit code
st.title("My Streamlit App with Google AdSense")

st.markdown(adsense_code, unsafe_allow_html=True)

st.write("This is the content of your app.")

