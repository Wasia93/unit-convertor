import streamlit as st

# Function to set background image and apply custom CSS styling
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
        }}

        /* Apply white text with black outline */
        h1, h2, h3, h4, h5, h6, p, label, div {{
            color: white !important;
            text-shadow: 2px 2px 4px black; /* Enhanced black outline */
        }}

        /* Title Styling */
        h1 {{
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            background: rgba(0, 0, 0, 0.6);
            padding: 10px;
            border-radius: 10px;
        }}

        /* Dropdown Styling */
        div[data-baseweb="select"] {{
            background-color: black !important;
            border-radius: 5px !important;
            border: 1px solid white !important;
            transition: 0.3s;
        }}
        div[data-baseweb="select"]:hover {{
            box-shadow: 0px 0px 10px white;
        }}
        div[data-baseweb="select"] * {{
            color: white !important;
            text-shadow: 1px 1px 2px black;
        }}
        div[data-baseweb="select"] svg {{
            fill: white !important;
        }}

        /* Convert Button Styling */
        .stButton>button {{
            background: linear-gradient(45deg, #111, #444) !important;
            color: white !important;
            text-shadow: 1px 1px 2px black;
            border-radius: 10px !important;
            font-size: 18px !important;
            padding: 12px 25px !important;
            border: none !important;
            transition: 0.4s ease-in-out;
        }}
        .stButton>button:hover {{
            background: linear-gradient(45deg, #444, #777) !important;
            box-shadow: 0px 0px 15px white;
            transform: scale(1.05);
        }}

        /* Footer Styling */
        .footer {{
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background: rgba(0, 0, 0, 0.7);
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-top: 2px solid white;
            backdrop-filter: blur(5px);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to add footer
def add_footer():
    st.markdown(
        """
        <div class="footer">
            Powered by Wasia Haris 🚀
        </div>
        """,
        unsafe_allow_html=True
    )

# Set background image
set_background("https://s7d1.scene7.com/is/image/dmqualcommprod/getting-personal-with-on-device-ai")

# Title
st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)

# Dropdown for unit selection
conversion_type = st.selectbox("Choose conversion type:", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    units = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084}
elif conversion_type == "Weight":
    units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
elif conversion_type == "Temperature":
    units = {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}

# Input fields
input_value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From:", list(units.keys()))
to_unit = st.selectbox("To:", list(units.keys()))

# Conversion logic
def convert(value, from_unit, to_unit, units):
    if conversion_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # Same unit

    else:
        return value * (units[to_unit] / units[from_unit])

# Convert and display result
if st.button("Convert"):
    result = convert(input_value, from_unit, to_unit, units)
    st.success(f"Converted Value: {result:.2f} {to_unit}")

# Add footer
add_footer()
