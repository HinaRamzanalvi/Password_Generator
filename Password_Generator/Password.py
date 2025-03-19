import streamlit as st
import random
import string

# Page config
st.set_page_config(
    page_title="Ultimate Password Tool 🔐",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
def set_custom_style():
    st.markdown("""
    <style>
    /* Main container */
    .stApp {
        background-color:lightgray;
        
    }

    [data-testid="stSidebar"] {
        background: #2c3e50 !important;
        padding: 20px;
    }

    /* Sidebar Text Color */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: white !important;
    }

    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    
    /* Buttons */
    .stButton>button {
        background: #e74c3c;
        color: white;
        border-radius: 25px;
        padding: 10px 25px;
        transition: all 0.3s ease;
        border: none;
    }
    
    .stButton>button:hover {
        background: #c0392b;
        transform: scale(1.05);
    }
    
    /* Slider */
    .stSlider {
        color: #e74c3c !important;
    }
    
    /* Cards */
    .custom-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 15px 0;
    }
    
    /* Footer */
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background: #2c3e50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

set_custom_style()

set_custom_style()

# Password functions
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits: characters += string.digits
    if use_special: characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    checks = [
        (len(password) >= 8, "Minimum 8 characters"),
        (any(c.isupper() for c in password), "Uppercase letter"),
        (any(c.islower() for c in password), "Lowercase letter"),
        (any(c.isdigit() for c in password), "Digit"),
        (any(c in string.punctuation for c in password), "Special character")
    ]
    missing = [req for met, req in checks if not met]
    return "Strong 💪" if not missing else f"Weak 😔 ({', '.join(missing)} required)"

# Sidebar content
with st.sidebar:
    st.header("⚙️ Settings")
    length = st.slider("Password Length", 8, 32, 12)
    use_digits = st.checkbox("Include Digits", True)
    use_special = st.checkbox("Include Special Characters", True)
    st.markdown("---")
    st.markdown("**Made with ❤️ by [Hina Alvi]")
    st.markdown("[![GitHub](https://img.icons8.com/material-outlined/30/ffffff/github.png)](https://github.com)")

# Main content
st.title("🔐 Ultimate Password Tool")
st.markdown("Generate secure passwords and check your password strength instantly!")

# Password Generator Card
with st.container():
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🛠️ Password Generator")
    if st.button("Generate New Password "):
        password = generate_password(length, use_digits, use_special)
        st.session_state.generated_password = password
    if 'generated_password' in st.session_state:
        st.code(f"Your Password: {st.session_state.generated_password}", language="text")
        strength = check_password_strength(st.session_state.generated_password)
        st.success(f"Strength: {strength}")
    st.markdown('</div>', unsafe_allow_html=True)

# Password Checker Card
with st.container():
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("🔍 Password Strength Checker")
    user_password = st.text_input("Enter password to check:", type="password")
    if st.button("Analyze Password"):
        result = check_password_strength(user_password)
        if "Strong" in result:
            st.success(result)
        else:
            st.error(result)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Password Manager - All rights reserved</div>', unsafe_allow_html=True)