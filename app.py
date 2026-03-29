import streamlit as st
from sklearn.linear_model import LogisticRegression
import numpy as np

st.title("🎓 Smart Student Predictor")

# ✅ Improved Dataset (final)
X = np.array([
    [0,16,0],
    [0,10,0],
    [1,12,0],
    [2,10,1],
    [3,5,1],
    [4,6,2],
    [5,6,1],
    [6,3,3],   # borderline
    [6,7,2],
    [6,8,3],
    [7,6,5],
])

y = np.array([0,0,0,0,0,1,1,1,1,1,1])

model = LogisticRegression()
model.fit(X, y)

# 🎯 Inputs
hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0)
sleep = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0)
practice = st.number_input("Practice Tests", min_value=0)

# 🚀 Predict Button
if st.button("Predict"):

    # ❌ Validation Rules
    if hours + sleep > 24:
        st.error("❌ Total hours (study + sleep) cannot exceed 24")
    
    else:
        prediction = model.predict([[hours, sleep, practice]])[0]
        prob = model.predict_proba([[hours, sleep, practice]])[0]

        fail_prob = prob[0]
        pass_prob = prob[1]

        st.subheader("Result")

        # ✅ PASS Case
        if prediction == 1:
            st.success(f"PASS ✅ (Confidence: {pass_prob*100:.2f}%)")

            if pass_prob < 0.75:
                st.warning("⚠️ Improve performance:")
                if practice < 2:
                    st.write("- Do more practice tests")
                if sleep < 5:
                    st.write("- Improve sleep")

        # ❌ FAIL Case
        else:
            st.error(f"FAIL ❌ (Confidence: {fail_prob*100:.2f}%)")

            st.warning("⚠️ Suggestions:")
            if hours < 4:
                st.write("- Increase study hours")
            if practice < 2:
                st.write("- Do more practice tests")
            if sleep < 5:
                st.write("- Improve sleep")
            if sleep > 10:
                st.write("- Avoid oversleeping")