import streamlit as st
import google.generativeai as genai

# Configure the API key for Google Generative AI
genai.configure(api_key="AIzaSyCuWxxiBiv7tIlqiB9iPdOzcFU8BFEdZLg")

# Ensure correct model usage
# Replace with the correct way of calling the model for your use case
def get_gemini_response(input_text, image_data, prompt):
    # Assuming `generate_text` is the correct method for generating text
    response = genai.generate_text(model="gemini-1.5-flash", prompt=f"{input_text} {prompt}")
    return response['candidates'][0]['output']  # Adjust based on actual response structure

# Function to process the uploaded image and convert it into the necessary format
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded.")

# Streamlit interface
st.title("Generative AI + Image Input Example")
st.sidebar.header("Made by HYPERx")
st.sidebar.write("Associated with ApexHypero")

# Input fields
input_text = st.text_input("Enter some text for the AI")
input=st.text_input("What do you want me to do?",key="input")
prompt = st.text_input("Enter a prompt for the model")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
st.sidebar.header("RoboBill🦾")

st.sidebar.write("Assistant used is Gemini Pro Vision.")

# If inputs are provided, run the model
if st.button("Generate AI Response"):
    try:
        if uploaded_file is not None and input_text and prompt:
            image_data = input_image_details(uploaded_file)
            result = get_gemini_response(input_text, image_data, prompt)
            st.write("Response from AI:")
            st.write(result)
        else:
            st.warning("Please provide text, prompt, and upload an image.")
    except Exception as e:
        st.error(f"Error: {e}")





