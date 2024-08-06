from transformers import AutoTokenizer, AutoModelForCausalLM
Import streamlit as st
import torch


# Load the model and tokenizer
model_path = 'path_to_your_trained_model'  # Update this path to your model's directory
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)


def get_model_response(query):
    inputs = tokenizer.encode(query, return_tensors='pt')
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=512)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


# Streamlit page configuration
st.set_page_config(page_title="Doc-GPT Medical Inquiry", page_icon=":hospital:", layout="wide")


# Streamlit application
def main():
    st.title("Doc-GPT Medical Inquiry Interface")
   
    # Sidebar for query parameters
    st.sidebar.header("Query Parameters")
    max_length = st.sidebar.slider("Max Length of Response", 50, 512, 150, 10)


    # Text box for user input
    user_input = st.text_area("Enter your medical question here:", height=150)


    # Button to generate response
    if st.button("Generate Response"):
        if user_input:
            response = get_model_response(user_input)
            st.text_area("Model Response:", value=response, height=200, max_chars=None)
        else:
            st.warning("Please enter a question to get a response.")


if __name__ == '__main__':
    main()
