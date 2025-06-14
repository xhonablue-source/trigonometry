import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import math

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="MathCraft: Complete Trigonometry Journey", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("# 📚 Lesson Navigation")
lesson_choice = st.sidebar.selectbox(
    "Choose your lesson:",
    ["🏠 Home & History", "📐 Angles: Degrees vs Radians", "📏 What ARE Sine & Cosine?", 
     "🌀 Unit Circle Explorer", "📊 Sine & Cosine as Functions", "🔢 The Famous Limit", 
     "🎯 Practice Problems", "🌍 Real-World Applications", "🧮 Quick Reference Guide"]
)

# --- HEADER ---
st.markdown("""
<div style='text-align: center;'>
    <h1 style='color:#4B0082; font-size: 2.5rem;'>🧠 MathCraft: Complete Trigonometry Journey</h1>
    <h3 style='color:#8B4B8B;'>From Ancient Wisdom to Modern Mathematics</h3>
    <p style='font-size: 1rem; color: #555;'>Built by <strong>Xavier Honablue, M.Ed</strong> • Grade 9 Mathematics</p>
    <hr style='border-top: 3px solid #4B0082; width: 50%; margin: auto;'>
</div>
""", unsafe_allow_html=True)

# --- LESSON 1: HOME & HISTORY ---
if lesson_choice == "🏠 Home & History":
    st.header("🏺 The Ancient Roots of Trigonometry")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🌍 Before the Greeks: African and Arab Mathematical Legacy
        
        **Did you know?** Trigonometry didn't start with the Greeks! Long before European scholars, brilliant minds in Africa and the Arab world were masters of angles, astronomy, and mathematical relationships.
        
        #### 🏛️ Physical Evidence:
        - **Great Pyramid of Giza** (Egypt, ~2580 BCE): Built with precise angles using sine and cosine relationships
        - **Nubian Pyramids** (Sudan, ~700 BCE): Complex astronomical alignments requiring trigonometric calculations
        - **Temple of Abu Simbel** (Egypt, ~1264 BCE): Designed so sunlight hits specific statues only on certain days
        
        #### 📜 Written Records:
        - **Babylonian tablets** (1800-1600 BCE): Contained trigonometric tables and astronomical calculations
        - **Islamic Golden Age** (8th-13th centuries): Al-Battani, Al-Biruni, and others refined sine, cosine, and tangent
        - **African scholars in Timbuktu**: Advanced mathematical texts predating European "discoveries"
        
        The Greeks learned from these civilizations—they didn't invent trigonometry, they inherited and built upon it!
        """)
    
    with col2:
        st.info("""
        **Fun Fact! 🤯**
        
        The word "sine" comes from the Arabic word "jayb" (meaning pocket or bay), which was mistranslated into Latin as "sinus"!
        
        **Today's Mission:**
        Master the tools that ancient African and Arab mathematicians used to:
        - Build monuments
        - Predict eclipses  
        - Navigate by stars
