import streamlit as st
from home import homepage
from Account import loginpage
from about import aboutpage
from image_to_text import image_to_textpage
from text_to_image import text_to_imgpage
from object import objectpage

# Function to apply custom CSS
def add_custom_css():
    st.markdown(
        """
        <style>
        .big-font {
            font-size: 3rem;
            color: #f0a500;
            font-weight: 800;
            cursor: pointer;
            transition: 0.3s ease;
        }
        .big-font:hover {
            color: red;
        }
        body {
            font-family: "Arial", sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    add_custom_css()

    # Define pages
    pages = {
        "Main": [
            st.Page(homepage, title="Home", icon="🏠"),            
        ],
        "AI Tools": [
            st.Page(image_to_textpage, title="Image Recognition", icon="🖼️"),          
            st.Page(text_to_imgpage, title="Image Genaeration", icon="🖼️"),          
        ],
        
        "Info": [
            st.Page(loginpage, title="Login", icon="ℹ️"),
            st.Page(aboutpage, title="About", icon="📞"),
        ],
    }

    # Set up navigation
    page = st.navigation(pages)

    # Display page title
    st.markdown(f'<h1 class="big-font">{page.title}</h1>', unsafe_allow_html=True)

    # Run the selected page
    page.run()

if __name__ == "__main__":
    main()
               
