import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="THON Donation Email Generator")

# === Load and inject custom font ===
def load_custom_font():
    font_path = Path("Gill Sans MT.ttf")  # Font file must be in project directory
    with open(font_path, "rb") as f:
        font_data = f.read()
    encoded_font = base64.b64encode(font_data).decode("utf-8")
    st.markdown(f"""
        <style>
        @font-face {{
            font-family: 'GillSansMT';
            src: url(data:font/ttf;base64,{encoded_font}) format('truetype');
        }}
        .custom-font {{
            font-family: 'GillSansMT', sans-serif;
            font-size: 16px;
            line-height: 1.6;
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #ddd;
            white-space: pre-wrap;
        }}
        </style>
    """, unsafe_allow_html=True)

# Load the font
load_custom_font()

st.title("THON Donation Script Generator")

# Input fields
name = st.text_input("Your Full Name")
email = st.text_input("Your Email Address")
phone = st.text_input("Your Phone Number")
company = st.text_input("Company Name")
item = st.text_input("Item Name")
item_use = st.text_input("How the Item Will Be Used (e.g., raffle prize)")
option = st.selectbox("Message Type", ["online", "email"])

# Generate script
if st.button("Generate Script"):

    # Basic validation
    if not name or not email or not phone or not company or not item or not item_use:
        st.error("❗ Please fill in all fields before generating the script.")
    else:
        # Compose the message
        if option == "online":
            message = f"""Dear {company},

My name is {name} and I am a captain for Penn State Dance Marathon, more commonly known as THON™. THON is the world’s largest student-run philanthropy, committed to enhancing the lives of children and families impacted by childhood cancer. Our mission is to provide emotional and financial support, spread awareness, and ensure funding for critical research, all For The Kids®.  

With the help of our donors, THON has raised over $236 million since 1977 to benefit our sole beneficiary, Four Diamonds at Penn State Health Children’s Hospital. As a result, over 4,800 families battling childhood cancer have never seen a bill. The year-long efforts of 16,500 student volunteers culminate each February with a 46-hour no-sitting, no-sleeping dance marathon. Our hope is that one day we will be dancing in celebration of a cure.   

We would not be able to impact the lives of so many families without the generous support of our donors. With their help, we are proudly able to donate 96 cents of every dollar raised to the fight against childhood cancer. If interested, I can send a copy of our Corporate Sponsorship Packet, outlining the extensive list of benefits and exposure opportunities available to our incredible donors, as well as a document of frequently asked questions to help you further understand our mission.   

I am reaching out because I was wondering if {company} would be interested in making an in-kind donation of a {item} to support our year-long efforts. Your donation would be used for {item_use}.

If you are interested in supporting THON or have any other questions, please contact me via email at {email} or by phone at {phone}. Thank you for your time and consideration. 

FTK®, 
"""
        else:
            message = f"""Dear {company},

My name is {name} and I am a captain for Penn State Dance Marathon, more commonly known as THON™. THON is the world’s largest student-run philanthropy, committed to enhancing the lives of children and families impacted by childhood cancer. Our mission is to provide emotional and financial support, spread awareness, and ensure funding for critical research, all For The Kids®.  

With the help of our donors, THON has raised over $236 million since 1977 to benefit our sole beneficiary, Four Diamonds at Penn State Health Children’s Hospital. As a result, over 4,800 families battling childhood cancer have never seen a bill. The year-long efforts of 16,500 student volunteers culminate each February with a 46-hour no-sitting, no-sleeping dance marathon. Our hope is that one day we will be dancing in celebration of a cure.   

We would not be able to impact the lives of so many families without the generous support of our donors. With their help, we are proudly able to donate 96 cents of every dollar raised to the fight against childhood cancer. I’ve attached a copy of the THON 2025 Corporate Sponsorship Packet, outlining the extensive list of benefits and exposure opportunities available to our incredible donors, as well as a document of frequently asked questions to help you further understand our mission.   

I am reaching out because I was wondering if {company} would be interested in making an in-kind donation of a {item} to support our year-long efforts. Your donation would be used for {item_use}.

If you are interested in supporting THON or have any other questions, please contact me via email at {email} or by phone at {phone}. Thank you for your time and consideration. 

FTK®, 
"""

        # Show formatted message
        st.markdown(f'<div class="custom-font">{message.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)

        # Copy to clipboard button
        safe_message = message.replace("`", "'")  # prevent JS breaking
        st.markdown(f"""
            <button onclick="navigator.clipboard.writeText(`{safe_message}`)"
            style="
                margin-top:10px;
                background-color:#4CAF50;
                color:white;
                padding:10px 15px;
                border:none;
                border-radius:4px;
                cursor:pointer;">
            📋 Copy to Clipboard
            </button>
        """, unsafe_allow_html=True)

        st.success("✅ Email script generated! You can now copy it.")

