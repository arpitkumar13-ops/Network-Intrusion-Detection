import numpy as np
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="AI-Based Network Intrusion Detection System")

st.title("AI-Based Network Intrusion Detection System")
st.write("This project uses Machine Learning to detect malicious network activity.")

#        Data Simulation
def generate_data():
    X = np.random.rand(1000, 4)
    y = np.random.randint(0, 2, 1000)
    return X, y

#        Train Model 
if st.sidebar.button("Train Model Now"):
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    st.success(f"Model trained successfully with accuracy: {acc:.2f}")

#         Live Simulation 
st.subheader("Live Traffic Simulator")

packet_size = st.slider("Packet Size", 0.0, 1.0)
duration = st.slider("Duration", 0.0, 1.0)
protocol = st.slider("Protocol Value", 0.0, 1.0)
flag = st.slider("Flag Value", 0.0, 1.0)

if st.button("Check Traffic"):
    sample = np.array([[packet_size, duration, protocol, flag]])
    prediction = np.random.choice([0, 1])

    if prediction == 1:
        st.error("⚠️ Intrusion Detected!")
    else:
        st.success("✅ Normal Traffic")  




