import streamlit as st
st.title("网易请加强守夜人")
st.header("You need to learn some basic operations")
st.subheader("eg, Visual Studio Code")
st.text("It's not that hard")

st.markdown("this is an image: \n \
            ![](https://nie.res.netease.com/r/pic/20220609/1d3e9889-945d-423a-98dd-dfb2ec4d3ad7.jpg)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

hobbies = st.multiselect("Hobbies:",
               ['Reading',
                'Writing',
                'Coding',
                'Traveling'])
st.write("You selected: ", hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    
