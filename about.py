import streamlit as st

def aboutpage():
    # Set the title for the contact section
    st.title("Contact Information")

    # Display contact details
    st.subheader("📞 Phone Number")
    st.write("+91 8108301759")  # Replace with your mobile number

    st.subheader("📧 Email Address")
    st.write("[jinesh.bommali004@gmail.com](mailto:jinesh.bommali004@gmail.com)")  # Replace with your email address


    st.subheader("💻 GitHub")
    st.write("[https://github.com/jinesh-Bommali07/DeepLearning](https://github.com/jinesh-Bommali07/DeepLearning)")  # Replace with your GitHub URL

    # Add optional styling or spacing
    st.markdown("---")
    st.write("Feel free to reach out via any of the platforms above!")
