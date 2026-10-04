import streamlit as st 
import pickle

st.title("Iris Flower Classification")
st.set_page_config(page_title="Iris Feature Sliders", layout="wide")

st.subheader("Selected Feature Values")
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 5.0, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

if st.button("Classify"):
    data = [[sepal_length, sepal_width, petal_length, petal_width]]

    with open("iris.model.pkl", "rb") as file:
        model = pickle.load(file)

    result = model.predict(data)[0]

    flower_names = [
        "Iris Setosa",
        "Iris Versicolor",
        "Iris Virginica"
    ]

    if result==0:
        st.image(
                "setosa.jfif",
                caption=flower_names[result]
            )
    elif result==1:
        st.image(
                        "versicolor.jfif",
                        caption=flower_names[result]
                    )
    else:
        st.image(
                "virginica.jfif",
                caption=flower_names[result]
            )

    st.write(flower_names[result])

