import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="MathCraft: Radians vs Degrees", layout="centered")

# --- HEADER ---
st.markdown("""
<div style='text-align: center;'>
    <h1 style='color:#4B0082;'>🧠 MathCraft: Radians, Degrees & Trig</h1>
    <h3>Understanding angle measures & functions</h3>
    <p style='font-size: 0.9rem; color: #555;'>Built by <strong>Xavier Honablue, M.Ed</strong></p>
    <hr style='border-top: 2px solid #ccc;'>
</div>
""", unsafe_allow_html=True)

# --- SECTION 1: INTRODUCTION ---
st.subheader("🎯 Why Do Radians Matter?")
st.markdown("""
Radians are essential for deeper mathematical understanding—especially when dealing with limits, calculus, and continuous trigonometric functions. 
This interactive module shows why degrees are useful for practical applications, but radians are **necessary** for math that goes beyond measurement.

📜 **Historical Note:** Long before the Greeks, early African and Arab scholars had extensive knowledge of astronomy and trigonometry. Evidence from the architectural alignments of ancient Nubian and Egyptian monuments, as well as Babylonian and Islamic astrological charts, shows that they understood sine, cosine, and celestial angles centuries earlier. Trigonometric relationships helped predict solstices, build massive stone structures, and track planetary motion—proving math was a legacy **inherited by the Greeks**, not invented by them.
""")

# --- SECTION 2: UNIT CIRCLE ---
st.subheader("🌀 Visualizing the Unit Circle")
angle_mode = st.radio("Choose angle mode:", ["Degrees", "Radians"])
angle = st.slider("Select an angle:", min_value=0.0, max_value=360.0 if angle_mode=="Degrees" else 2*np.pi, value=90.0 if angle_mode=="Degrees" else np.pi/2, step=1.0 if angle_mode=="Degrees" else 0.1)

# Convert to radians if needed
angle_rad = np.deg2rad(angle) if angle_mode == "Degrees" else angle

x = np.cos(angle_rad)
y = np.sin(angle_rad)

fig = go.Figure()
fig.add_shape(type="circle", xref="x", yref="y", x0=-1, y0=-1, x1=1, y1=1, line_color="LightBlue")
fig.add_trace(go.Scatter(x=[0, x], y=[0, y], mode="lines+markers", name="Angle Arm", line=dict(color="blue")))
fig.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", name="(cos, sin)", text=[f"({x:.2f}, {y:.2f})"], textposition="top center"))
fig.update_layout(width=500, height=500, title="Unit Circle", xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]), yaxis=dict(range=[-1.2, 1.2]))
st.plotly_chart(fig)

# --- SECTION 3: SIN(X)/X LIMIT ---
st.subheader("📉 Explore: Why sin(x)/x only works with Radians")
st.latex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1")

x_vals = np.linspace(-1, 1, 400)
sin_x_over_x_rad = np.sinc(x_vals / np.pi)
sin_x_over_x_deg = np.sin(np.deg2rad(x_vals)) / x_vals

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=x_vals, y=sin_x_over_x_rad, name="sin(x)/x in Radians"))
fig2.add_trace(go.Scatter(x=x_vals, y=sin_x_over_x_deg, name="sin(x)/x in Degrees", line=dict(dash="dash")))
fig2.update_layout(title="Behavior of sin(x)/x near 0", xaxis_title="x", yaxis_title="sin(x)/x", legend_title="Angle Type")
st.plotly_chart(fig2)

# --- SECTION 4: CLASSROOM TAKEAWAYS ---
st.subheader("📝 Teaching Implications")
st.markdown("""
- **Degrees** are more familiar and used in everyday applications.
- **Radians** are mathematically coherent with functions, limits, and derivatives.
- Students should **start with degrees** for measurement, but be **introduced to radians** in Algebra II to prepare for Precalculus and Calculus.

✔ Radians are not harder—they're **just more natural** when we connect circular motion and algebra.
""")

# --- FOOTER ---
st.markdown("""
---
<div style='text-align: center;'>
    <p style='font-size: 0.85rem;'>Built with ❤️ for 9th grade math learners | MathCraft | <strong>Xavier Honablue, M.Ed</strong></p>
</div>
""", unsafe_allow_html=True)
