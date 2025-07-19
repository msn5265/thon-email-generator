import streamlit as st

st.set_page_config(page_title="THON Donation Email Generator")

st.title("THON Donation Script Generator")

# Input fields
name = st.text_input("Your Full Name")
email = st.text_input("Your Email Address")
phone = st.text_input("Your Phone Number")
company = st.text_input("Company Name")
item = st.text_input("Item Name")
item_use = st.text_input("How the Item Will Be Used (e.g., raffle prize)")
option = st.selectbox("Message Type", ["online", "email"])

# Generate on button click
if st.button("Generate Script"):

    if option == "online":
        message = f"""Dear {company},

My name is {name} and I am a captain for Penn State Dance Marathon, more commonly known as THON™. THON is the world’s largest student-run philanthropy, committed to enhancing the lives of children and families impacted by childhood cancer. Our mission is to provide emotional and financial support, spread awareness, and ensure funding for critical research, all For The Kids®.  

With the help of our donors, THON has raised over $236 million since 1977 to benefit our sole beneficiary, Four Diamonds at Penn State Health Children’s Hospital. As a result, over 4,800 families battling childhood cancer have never seen a bill. The year-long efforts of 16,500 student volunteers culminate each February with a 46-hour no-sitting, no-sleeping dance marathon. Our hope is that one day we will be dancing in celebration of a cure.   

We would not be able to impact the lives of so many families without the generous support of our donors. With their help, we are proudly able to donate 96 cents of every dollar raised to the fight against childhood cancer. If interested, I can send a copy of our Corporate Sponsorship Packet, outlining the extensive list of benefits and exposure opportunities available to our incredible donors, as well as a document of frequently asked questions to help you further understand our mission.   

I am reaching out because I was wondering if {company} would be interested in making an in-kind donation of a {item} to support our year-long efforts. Your donation would be used for {item_use}.

If you are interested in supporting THON or have any other questions, please contact me via email at {email} or by phone at {phone}. Thank you for your time and consideration. 

FTK®, 
"""
    else:  # option == "email"
        message = f"""Dear {company},

My name is {name} and I am a captain for Penn State Dance Marathon, more commonly known as THON™. THON is the world’s largest student-run philanthropy, committed to enhancing the lives of children and families impacted by childhood cancer. Our mission is to provide emotional and financial support, spread awareness, and ensure funding for critical research, all For The Kids®.  

With the help of our donors, THON has raised over $236 million since 1977 to benefit our sole beneficiary, Four Diamonds at Penn State Health Children’s Hospital. As a result, over 4,800 families battling childhood cancer have never seen a bill. The year-long efforts of 16,500 student volunteers culminate each February with a 46-hour no-sitting, no-sleeping dance marathon. Our hope is that one day we will be dancing in celebration of a cure.   

We would not be able to impact the lives of so many families without the generous support of our donors. With their help, we are proudly able to donate 96 cents of every dollar raised to the fight against childhood cancer. I’ve attached a copy of the THON 2025 Corporate Sponsorship Packet, outlining the extensive list of benefits and exposure opportunities available to our incredible donors, as well as a document of frequently asked questions to help you further understand our mission.   

I am reaching out because I was wondering if {company} would be interested in making an in-kind donation of a {item} to support our year-long efforts. Your donation would be used for {item_use}.

If you are interested in supporting THON or have any other questions, please contact me via email at {email} or by phone at {phone}. Thank you for your time and consideration. 

FTK®, 
"""

    st.text_area("📧 Generated Email Script", value=message, height=400)
    st.code(message, language="text")
    st.success("✅ Email script generated! You can now copy it.")

