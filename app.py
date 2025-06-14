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
        - Create calendars
        """)
    
    st.markdown("---")
    st.subheader("🎯 What You'll Learn Today")
    
    progress_cols = st.columns(4)
    with progress_cols[0]:
        st.markdown("✅ **Angles**\nDegrees vs Radians")
    with progress_cols[1]:
        st.markdown("📐 **Unit Circle**\nThe Foundation")
    with progress_cols[2]:
        st.markdown("📈 **Functions**\nSine & Cosine")
    with progress_cols[3]:
        st.markdown("🔬 **Advanced**\nLimits & Calculus Prep")

# --- LESSON 2: ANGLES ---
elif lesson_choice == "📐 Angles: Degrees vs Radians":
    st.header("📐 Understanding Angles: Two Ways to Measure")
    
    st.markdown("""
    ### 🤔 Why Do We Need Two Systems?
    Think of it like measuring distance in **miles** vs **kilometers**—both work, but each has its best uses!
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🌟 **Degrees** (Familiar Friend)
        - **Full circle**: 360°
        - **Half circle**: 180°  
        - **Right angle**: 90°
        - **Best for**: Everyday measurements, construction, navigation
        
        **Why 360?** Ancient Babylonians loved the number 60 (it divides evenly many ways), and 360 = 6 × 60!
        """)
    
    with col2:
        st.markdown("""
        #### 🎯 **Radians** (Mathematical Natural)
        - **Full circle**: 2π ≈ 6.28
        - **Half circle**: π ≈ 3.14
        - **Right angle**: π/2 ≈ 1.57  
        - **Best for**: Calculus, physics, advanced math
        
        **What's a radian?** The angle when the arc length equals the radius!
        """)
    
    st.markdown("### 🔄 Interactive Converter")
    converter_mode = st.radio("Convert:", ["Degrees → Radians", "Radians → Degrees"])
    
    if converter_mode == "Degrees → Radians":
        degrees_input = st.number_input("Enter degrees:", value=90.0, step=1.0)
        radians_result = degrees_input * math.pi / 180
        st.success(f"{degrees_input}° = {radians_result:.4f} radians = {radians_result/math.pi:.2f}π radians")
    else:
        radians_input = st.number_input("Enter radians:", value=1.57, step=0.1)
        degrees_result = radians_input * 180 / math.pi
        st.success(f"{radians_input} radians = {degrees_result:.2f}°")
    
    # Visual comparison
    st.markdown("### 📊 Common Angles Comparison")
    angle_df = {
        "Angle Description": ["Right angle", "Straight angle", "Full rotation", "30°", "45°", "60°"],
        "Degrees": ["90°", "180°", "360°", "30°", "45°", "60°"],
        "Radians (Decimal)": ["1.57", "3.14", "6.28", "0.52", "0.79", "1.05"],
        "Radians (π form)": ["π/2", "π", "2π", "π/6", "π/4", "π/3"]
    }
    st.table(angle_df)

# --- LESSON 3: WHAT ARE SINE & COSINE? ---
elif lesson_choice == "📏 What ARE Sine & Cosine?":
    st.header("📏 What ARE Sine and Cosine? (The Definitions)")
    
    st.markdown("""
    ### 🤔 Before we get to fancy functions...
    **Let's answer the most important question: WHAT exactly are sine and cosine?**
    
    Sine and cosine are NOT mysterious magic—they're just **ratios** and **coordinates**!
    """)
    
    # Definition approach selector
    definition_approach = st.radio(
        "Choose how you want to learn the definitions:",
        ["📐 Right Triangle Approach (SOH-CAH-TOA)", "🌀 Circle Coordinate Approach", "🔄 Both Together"]
    )
    
    if definition_approach in ["📐 Right Triangle Approach (SOH-CAH-TOA)", "🔄 Both Together"]:
        st.markdown("---")
        st.subheader("📐 Method 1: Right Triangle Definitions")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            #### 📏 In a Right Triangle:
            
            **SINE** = **Opposite** ÷ **Hypotenuse**
            
            **COSINE** = **Adjacent** ÷ **Hypotenuse**
            
            **TANGENT** = **Opposite** ÷ **Adjacent**
            
            #### 🎯 Memory Device: SOH-CAH-TOA
            - **S**ine = **O**pposite / **H**ypotenuse
            - **C**osine = **A**djacent / **H**ypotenuse  
            - **T**angent = **O**pposite / **A**djacent
            """)
            
            # Interactive triangle
            angle_deg = st.slider("Choose angle θ (degrees):", 10, 80, 30, 5, key="triangle_angle")
            
            # Calculate triangle sides (using hypotenuse = 10 for simplicity)
            hypotenuse = 10
            opposite = hypotenuse * math.sin(math.radians(angle_deg))
            adjacent = hypotenuse * math.cos(math.radians(angle_deg))
            
            # Calculate ratios
            sine_ratio = opposite / hypotenuse
            cosine_ratio = adjacent / hypotenuse
            tangent_ratio = opposite / adjacent
            
            st.markdown(f"""
            #### 📊 For θ = {angle_deg}°:
            - **Opposite side**: {opposite:.2f}
            - **Adjacent side**: {adjacent:.2f}  
            - **Hypotenuse**: {hypotenuse:.2f}
            
            #### 🧮 The Ratios:
            - **sin({angle_deg}°)** = {opposite:.2f} ÷ {hypotenuse:.2f} = **{sine_ratio:.3f}**
            - **cos({angle_deg}°)** = {adjacent:.2f} ÷ {hypotenuse:.2f} = **{cosine_ratio:.3f}**
            - **tan({angle_deg}°)** = {opposite:.2f} ÷ {adjacent:.2f} = **{tangent_ratio:.3f}**
            """)
        
        with col2:
            # Draw the right triangle
            fig_triangle = go.Figure()
            
            # Triangle vertices
            vertices_x = [0, adjacent, adjacent, 0]
            vertices_y = [0, 0, opposite, 0]
            
            # Draw triangle
            fig_triangle.add_trace(go.Scatter(
                x=vertices_x, y=vertices_y, mode='lines+markers',
                line=dict(color='blue', width=3), marker=dict(size=8),
                name='Triangle', showlegend=False
            ))
            
            # Label sides
            fig_triangle.add_annotation(x=adjacent/2, y=-0.5, text=f"Adjacent = {adjacent:.1f}",
                                      showarrow=False, font=dict(size=12, color='green'))
            fig_triangle.add_annotation(x=adjacent+0.5, y=opposite/2, text=f"Opposite = {opposite:.1f}",
                                      showarrow=False, font=dict(size=12, color='red'), textangle=90)
            fig_triangle.add_annotation(x=adjacent/2-1, y=opposite/2+0.5, text=f"Hypotenuse = {hypotenuse:.1f}",
                                      showarrow=False, font=dict(size=12, color='blue'), textangle=angle_deg)
            
            # Mark the angle
            angle_arc_x = [1 * math.cos(math.radians(t)) for t in range(0, angle_deg)]
            angle_arc_y = [1 * math.sin(math.radians(t)) for t in range(0, angle_deg)]
            fig_triangle.add_trace(go.Scatter(
                x=angle_arc_x, y=angle_arc_y, mode='lines',
                line=dict(color='purple', width=2), name='θ', showlegend=False
            ))
            fig_triangle.add_annotation(x=1.5, y=0.3, text=f"θ = {angle_deg}°",
                                      showarrow=False, font=dict(size=14, color='purple'))
            
            # Right angle marker
            fig_triangle.add_trace(go.Scatter(
                x=[adjacent-1, adjacent-1, adjacent], y=[0, 1, 1], mode='lines',
                line=dict(color='gray', width=2), showlegend=False
            ))
            
            fig_triangle.update_layout(
                title=f"Right Triangle: θ = {angle_deg}°",
                xaxis=dict(range=[-1, max(adjacent+2, 12)], scaleanchor="y", scaleratio=1),
                yaxis=dict(range=[-2, max(opposite+2, 8)]),
                height=400, showlegend=False
            )
            
            st.plotly_chart(fig_triangle, use_container_width=True)
    
    if definition_approach in ["🌀 Circle Coordinate Approach", "🔄 Both Together"]:
        st.markdown("---")
        st.subheader("🌀 Method 2: Circle Coordinate Definitions")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            #### 🎯 On ANY Circle (not just unit circle):
            
            When you have a circle and draw a line from the center at angle θ:
            
            **COSINE** = **x-coordinate** ÷ **radius**
            
            **SINE** = **y-coordinate** ÷ **radius**
            
            #### 🌟 Special Case: Unit Circle (radius = 1)
            
            **COSINE** = **x-coordinate** (exactly!)
            
            **SINE** = **y-coordinate** (exactly!)
            
            This is why the unit circle is so powerful—no division needed!
            """)
            
            # Interactive circle
            circle_radius = st.slider("Circle radius:", 1, 10, 5, 1, key="circle_radius")
            circle_angle = st.slider("Angle θ (degrees):", 0, 360, 45, 15, key="circle_angle")
            
            # Calculate coordinates
            angle_rad = math.radians(circle_angle)
            x_coord = circle_radius * math.cos(angle_rad)
            y_coord = circle_radius * math.sin(angle_rad)
            
            # Calculate the ratios
            cosine_from_circle = x_coord / circle_radius
            sine_from_circle = y_coord / circle_radius
            
            st.markdown(f"""
            #### 📊 For radius = {circle_radius}, θ = {circle_angle}°:
            - **Point coordinates**: ({x_coord:.2f}, {y_coord:.2f})
            - **Radius**: {circle_radius}
            
            #### 🧮 The Definitions:
            - **cos({circle_angle}°)** = {x_coord:.2f} ÷ {circle_radius} = **{cosine_from_circle:.3f}**
            - **sin({circle_angle}°)** = {y_coord:.2f} ÷ {circle_radius} = **{sine_from_circle:.3f}**
            """)
            
            if circle_radius == 1:
                st.success("🌟 With radius = 1, cos and sin ARE the coordinates!")
        
        with col2:
            # Draw the circle
            fig_circle = go.Figure()
            
            # Circle
            theta_circle = np.linspace(0, 2*math.pi, 100)
            circle_x = circle_radius * np.cos(theta_circle)
            circle_y = circle_radius * np.sin(theta_circle)
            fig_circle.add_trace(go.Scatter(
                x=circle_x, y=circle_y, mode='lines',
                line=dict(color='lightblue', width=3), name='Circle', showlegend=False
            ))
            
            # Axes
            axis_range = circle_radius + 1
            fig_circle.add_trace(go.Scatter(
                x=[-axis_range, axis_range], y=[0, 0], mode='lines',
                line=dict(color='gray', width=1), showlegend=False
            ))
            fig_circle.add_trace(go.Scatter(
                x=[0, 0], y=[-axis_range, axis_range], mode='lines',
                line=dict(color='gray', width=1), showlegend=False
            ))
            
            # Radius line to point
            fig_circle.add_trace(go.Scatter(
                x=[0, x_coord], y=[0, y_coord], mode='lines+markers',
                line=dict(color='red', width=3), marker=dict(size=10),
                name='Radius', showlegend=False
            ))
            
            # Point on circle
            fig_circle.add_trace(go.Scatter(
                x=[x_coord], y=[y_coord], mode='markers+text',
                marker=dict(size=12, color='red'),
                text=[f'({x_coord:.1f}, {y_coord:.1f})'], textposition="top center",
                showlegend=False
            ))
            
            # Coordinate lines
            fig_circle.add_trace(go.Scatter(
                x=[x_coord, x_coord], y=[0, y_coord], mode='lines',
                line=dict(color='green', width=2, dash='dash'), 
                name='y-coordinate', showlegend=False
            ))
            fig_circle.add_trace(go.Scatter(
                x=[0, x_coord], y=[y_coord, y_coord], mode='lines',
                line=dict(color='blue', width=2, dash='dash'),
                name='x-coordinate', showlegend=False
            ))
            
            # Labels
            fig_circle.add_annotation(x=x_coord/2, y=-0.3, text=f"x = {x_coord:.1f}",
                                    showarrow=False, font=dict(size=12, color='blue'))
            fig_circle.add_annotation(x=-0.3, y=y_coord/2, text=f"y = {y_coord:.1f}",
                                    showarrow=False, font=dict(size=12, color='green'))
            fig_circle.add_annotation(x=1, y=0.5, text=f"θ = {circle_angle}°",
                                    showarrow=False, font=dict(size=12, color='purple'))
            
            fig_circle.update_layout(
                title=f"Circle Definition: r = {circle_radius}, θ = {circle_angle}°",
                xaxis=dict(scaleanchor="y", scaleratio=1, range=[-axis_range, axis_range]),
                yaxis=dict(range=[-axis_range, axis_range]),
                height=400
            )
            
            st.plotly_chart(fig_circle, use_container_width=True)

# --- LESSON 4: UNIT CIRCLE EXPLORER ---  
elif lesson_choice == "🌀 Unit Circle Explorer":
    st.header("🌀 The Unit Circle: Your Trig Command Center")
    
    st.markdown("""
    ### 🎯 What's the Unit Circle?
    A circle with **radius = 1** centered at the origin. It's the **key** to understanding all trigonometry!
    
    **Magic fact**: Any point on this circle has coordinates **(cos θ, sin θ)** where θ is the angle!
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Interactive unit circle
        angle_mode = st.radio("Angle measurement:", ["Degrees", "Radians"], horizontal=True)
        
        if angle_mode == "Degrees":
            angle = st.slider("Angle (degrees):", 0, 360, 45, step=15)
            angle_rad = math.radians(angle)
            angle_display = f"{angle}°"
        else:
            angle_options = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, 2*math.pi/3, 3*math.pi/4, 5*math.pi/6, math.pi, 7*math.pi/6, 5*math.pi/4, 4*math.pi/3, 3*math.pi/2, 5*math.pi/3, 7*math.pi/4, 11*math.pi/6, 2*math.pi]
            angle_labels = ["0", "π/6", "π/4", "π/3", "π/2", "2π/3", "3π/4", "5π/6", "π", "7π/6", "5π/4", "4π/3", "3π/2", "5π/3", "7π/4", "11π/6", "2π"]
            selected_index = st.select_slider("Angle (radians):", options=range(len(angle_options)), format_func=lambda x: angle_labels[x], value=2)
            angle_rad = angle_options[selected_index]
            angle = math.degrees(angle_rad)
            angle_display = angle_labels[selected_index]
        
        # Calculate coordinates
        x = math.cos(angle_rad)
        y = math.sin(angle_rad)
        
        # Create unit circle plot
        theta = np.linspace(0, 2*math.pi, 100)
        circle_x = np.cos(theta)
        circle_y = np.sin(theta)
        
        fig = go.Figure()
        
        # Circle
        fig.add_trace(go.Scatter(x=circle_x, y=circle_y, mode='lines', name='Unit Circle', line=dict(color='lightblue', width=3)))
        
        # Axes
        fig.add_trace(go.Scatter(x=[-1.2, 1.2], y=[0, 0], mode='lines', name='X-axis', line=dict(color='gray', width=1)))
        fig.add_trace(go.Scatter(x=[0, 0], y=[-1.2, 1.2], mode='lines', name='Y-axis', line=dict(color='gray', width=1)))
        
        # Angle line
        fig.add_trace(go.Scatter(x=[0, x], y=[0, y], mode='lines+markers', name='Angle Ray', 
                                line=dict(color='red', width=3), marker=dict(size=8)))
        
        # Point on circle
        fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers+text', name='Point', 
                                marker=dict(size=12, color='red'),
                                text=[f'({x:.3f}, {y:.3f})'], textposition="top center"))
        
        # Coordinate lines
        fig.add_trace(go.Scatter(x=[x, x], y=[0, y], mode='lines', name='sin θ', 
                                line=dict(color='green', width=2, dash='dash')))
        fig.add_trace(go.Scatter(x=[0, x], y=[y, y], mode='lines', name='cos θ', 
                                line=dict(color='blue', width=2, dash='dash')))
        
        fig.update_layout(
            title=f"Unit Circle: θ = {angle_display}",
            xaxis=dict(scaleanchor="y", scaleratio=1, range=[-1.3, 1.3], zeroline=True),
            yaxis=dict(range=[-1.3, 1.3], zeroline=True),
            width=500, height=500,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Current Values")
        st.metric("**Angle**", angle_display)
        st.metric("**cos θ** (x-coordinate)", f"{x:.4f}")
        st.metric("**sin θ** (y-coordinate)", f"{y:.4f}")
        st.metric("**tan θ** (slope)", f"{y/x:.4f}" if abs(x) > 0.001 else "undefined")
        
        st.markdown("---")
        st.markdown("### 🧠 Key Insights")
        st.markdown(f"""
        - **cos θ = {x:.3f}** (horizontal distance)
        - **sin θ = {y:.3f}** (vertical distance)  
        - **Point coordinates**: ({x:.3f}, {y:.3f})
        - **Distance from origin**: {math.sqrt(x**2 + y**2):.3f} (always = 1!)
        """)

# --- LESSON 5: SINE & COSINE AS FUNCTIONS ---
elif lesson_choice == "📊 Sine & Cosine as Functions":
    st.header("📊 Sine & Cosine: From Definitions to Functions")
    
    st.markdown("""
    ### 🌊 From Points to Waves: The Function Story
    Now that you know sine and cosine are **ratios** and **coordinates**, let's see what happens when we **connect all the dots**!
    
    **The big idea**: As the angle changes continuously, sine and cosine create beautiful wave patterns!
    """)
    
    # Interactive function explorer
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🎛️ Function Controls")
        amplitude = st.slider("Amplitude (A):", 0.5, 3.0, 1.0, 0.1)
        frequency = st.slider("Frequency (B):", 0.5, 3.0, 1.0, 0.1)
        phase = st.slider("Phase shift (C):", -math.pi, math.pi, 0.0, 0.1)
        vertical = st.slider("Vertical shift (D):", -2.0, 2.0, 0.0, 0.1)
        
        show_cos = st.checkbox("Show cosine", True)
        show_sin = st.checkbox("Show sine", True)
        
        st.markdown(f"""
        ### 📝 Current Function:
        **f(x) = {amplitude} sin({frequency}x + {phase:.2f}) + {vertical}**
        
        - **A = {amplitude}**: Amplitude (height)
        - **B = {frequency}**: Frequency (how fast it oscillates)  
        - **C = {phase:.2f}**: Phase shift (left/right)
        - **D = {vertical}**: Vertical shift (up/down)
        """)
    
    with col2:
        # Generate function data
        x = np.linspace(-2*math.pi, 2*math.pi, 1000)
        
        fig = go.Figure()
        
        if show_sin:
            y_sin = amplitude * np.sin(frequency * x + phase) + vertical
            fig.add_trace(go.Scatter(x=x, y=y_sin, name=f'y = {amplitude}sin({frequency}x + {phase:.2f}) + {vertical}', 
                                   line=dict(color='red', width=3)))
        
        if show_cos:
            y_cos = amplitude * np.cos(frequency * x + phase) + vertical
            fig.add_trace(go.Scatter(x=x, y=y_cos, name=f'y = {amplitude}cos({frequency}x + {phase:.2f}) + {vertical}', 
                                   line=dict(color='blue', width=3)))
        
        # Add reference lines
        fig.add_hline(y=0, line_dash="dot", line_color="gray")
        fig.add_vline(x=0, line_dash="dot", line_color="gray")
        
        fig.update_layout(
            title="Sine and Cosine Functions",
            xaxis_title="x (radians)",
            yaxis_title="y",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Key properties
    st.markdown("### 🔑 Key Properties to Remember")
    
    prop_col1, prop_col2 = st.columns(2)
    
    with prop_col1:
        st.markdown("""
        #### 📈 **Sine Function**
        - **Domain**: All real numbers
        - **Range**: [-1, 1] (for basic function)
        - **Period**: 2π
        - **Starts at**: (0, 0)
        - **Maximum**: π/2, 5π/2, ...
        - **Minimum**: 3π/2, 7π/2, ...
        """)
    
    with prop_col2:
        st.markdown("""
        #### 📉 **Cosine Function**
        - **Domain**: All real numbers  
        - **Range**: [-1, 1] (for basic function)
        - **Period**: 2π
        - **Starts at**: (0, 1)
        - **Maximum**: 0, 2π, 4π, ...
        - **Minimum**: π, 3π, 5π, ...
        """)

# --- LESSON 6: THE FAMOUS LIMIT ---
elif lesson_choice == "🔢 The Famous Limit":
    st.header("🔢 The Most Important Limit in Trigonometry")
    
    st.markdown("""
    ### 🎯 The Fundamental Limit
    This limit is the foundation of calculus and explains why radians are "natural":
    """)
    
    st.latex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📚 Mathematical Vocabulary Breakdown
        
        Let's decode this expression symbol by symbol:
        
        - **lim** = "limit" (the value we approach)
        - **x → 0** = "as x approaches 0" (getting closer and closer to 0)
        - **sin x** = sine of x (the trigonometric function)
        - **x** = the angle (in radians!)
        - **= 1** = equals exactly 1
        
        ### 🤔 What Does This Mean?
        
        As angles get smaller and smaller (approaching 0), the ratio of **sin(angle)** to the **angle itself** approaches exactly 1.
        
        **BUT**: This only works when the angle is measured in **radians**!
        """)
        
        # Interactive limit explorer
        st.markdown("### 🔍 Explore the Limit")
        
        zoom_level = st.selectbox("Choose how close to 0:", 
                                ["±1 radian", "±0.5 radians", "±0.1 radians", "±0.01 radians"])
        
        zoom_dict = {"±1 radian": 1, "±0.5 radians": 0.5, "±0.1 radians": 0.1, "±0.01 radians": 0.01}
        zoom = zoom_dict[zoom_level]
        
        x_vals = np.linspace(-zoom, zoom, 1000)
        x_vals = x_vals[x_vals != 0]  # Remove x=0 to avoid division by zero
        
        # Calculate sin(x)/x for radians and degrees
        sinx_over_x_rad = np.sin(x_vals) / x_vals
        
        fig = go.Figure()
        
        # sin(x)/x in radians
        fig.add_trace(go.Scatter(x=x_vals, y=sinx_over_x_rad, name='sin(x)/x (x in radians)', 
                               line=dict(color='red', width=3)))
        
        # Reference line y=1
        fig.add_hline(y=1, line_dash="dash", line_color="green", 
                     annotation_text="y = 1 (the limit!)")
        
        fig.update_layout(
            title=f"The Limit sin(x)/x as x approaches 0 (zoom: {zoom_level})",
            xaxis_title="x",
            yaxis_title="sin(x)/x",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Show numerical values
        if zoom <= 0.1:
            test_values = [0.1, 0.01, 0.001, 0.0001]
            st.markdown("### 📊 Getting Closer to 1:")
            for val in test_values:
                if val <= zoom:
                    result = math.sin(val) / val
                    st.write(f"When x = {val}: sin({val})/{val} = {result:.6f}")
    
    with col2:
        st.markdown("""
        ### 💡 Why This Matters
        
        **For Calculus:**
        - This limit helps us find the derivative of sin(x)
        - It's why d/dx[sin(x)] = cos(x)
        
        **For Physics:**
        - Small angle approximations
        - Harmonic motion
        - Wave mechanics
        
        **For Engineering:**
        - Signal processing
        - Control systems
        - Oscillations
        """)
        
        st.info("""
        **🎯 Key Insight:**
        
        Radians make trigonometric functions "natural" because:
        
        sin(x) ≈ x when x is small (in radians)
        
        This is NOT true for degrees!
        """)
        
        st.markdown("### 🧮 Quick Check")
        test_angle = st.number_input("Test a small angle (radians):", value=0.1, min_value=0.001, max_value=1.0, step=0.01)
        sin_val = math.sin(test_angle)
        ratio = sin_val / test_angle
        st.write(f"sin({test_angle}) = {sin_val:.4f}")
        st.write(f"sin({test_angle})/{test_angle} = {ratio:.4f}")
        
        if abs(ratio - 1) < 0.1:
            st.success("See how close to 1 it is! 🎉")
        else:
            st.info("Try a smaller angle to see it approach 1!")

# --- LESSON 7: PRACTICE PROBLEMS ---
elif lesson_choice == "🎯 Practice Problems":
    st.header("🎯 Practice Problems & Quizzes")
    
    # Problem selector
    problem_type = st.selectbox("Choose problem type:", 
                               ["Degree ↔ Radian Conversion", "Unit Circle Values", "Function Properties", "Definition Practice"])
    
    if problem_type == "Degree ↔ Radian Conversion":
        st.subheader("🔄 Conversion Practice")
        
        # Generate random problem
        if st.button("Generate New Problem"):
            st.session_state.problem_angles = np.random.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360], 3)
        
        if 'problem_angles' not in st.session_state:
            st.session_state.problem_angles = [45, 90, 180]
        
        for i, angle in enumerate(st.session_state.problem_angles):
            st.write(f"**Problem {i+1}:** Convert {angle}° to radians")
            user_answer = st.text_input(f"Answer {i+1} (in terms of π):", key=f"conv_{i}")
            
            if user_answer:
                correct_rad = angle * math.pi / 180
                correct_pi = f"{angle/180}π" if angle % 180 == 0 else f"{angle}π/180"
                st.write(f"Correct answer: {correct_pi} = {correct_rad:.4f} radians")
    
    elif problem_type == "Unit Circle Values":
        st.subheader("🌀 Unit Circle Memory Challenge")
        
        special_angles = {
            "0°": (1, 0), "30°": (math.sqrt(3)/2, 1/2), "45°": (math.sqrt(2)/2, math.sqrt(2)/2),
            "60°": (1/2, math.sqrt(3)/2), "90°": (0, 1), "120°": (-1/2, math.sqrt(3)/2),
            "135°": (-math.sqrt(2)/2, math.sqrt(2)/2), "150°": (-math.sqrt(3)/2, 1/2),
            "180°": (-1, 0), "210°": (-math.sqrt(3)/2, -1/2), "225°": (-math.sqrt(2)/2, -math.sqrt(2)/2),
            "240°": (-1/2, -math.sqrt(3)/2), "270°": (0, -1), "300°": (1/2, -math.sqrt(3)/2),
            "315°": (math.sqrt(2)/2, -math.sqrt(2)/2), "330°": (math.sqrt(3)/2, -1/2)
        }
        
        if st.button("New Challenge"):
            st.session_state.challenge_angle = np.random.choice(list(special_angles.keys()))
        
        if 'challenge_angle' not in st.session_state:
            st.session_state.challenge_angle = "45°"
        
        challenge_angle = st.session_state.challenge_angle
        correct_cos, correct_sin = special_angles[challenge_angle]
        
        st.write(f"**What are the coordinates of {challenge_angle} on the unit circle?**")
        
        col1, col2 = st.columns(2)
        with col1:
            cos_answer = st.number_input("cos value:", step=0.1, format="%.3f")
        with col2:
            sin_answer = st.number_input("sin value:", step=0.1, format="%.3f")
        
        if st.button("Check Answer"):
            if abs(cos_answer - correct_cos) < 0.01 and abs(sin_answer - correct_sin) < 0.01:
                st.success("🎉 Correct! Great job!")
            else:
                st.error(f"Not quite. The correct answer is cos({challenge_angle}) = {correct_cos:.3f}, sin({challenge_angle}) = {correct_sin:.3f}")
    
    elif problem_type == "Function Properties":
        st.subheader("📊 Function Analysis")
        
        st.markdown("""
        **Analyze this function:** f(x) = 2sin(3x + π/4) - 1
        
        Fill in the properties:
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            amplitude_answer = st.number_input("Amplitude:", step=0.1)
            period_answer = st.number_input("Period:", step=0.1)
        with col2:
            phase_answer = st.number_input("Phase shift:", step=0.1)
            vertical_answer = st.number_input("Vertical shift:", step=0.1)
        
        if st.button("Check Function Analysis"):
            correct_amp = 2
            correct_period = 2*math.pi/3
            correct_phase = -math.pi/12  # -π/4 ÷ 3
            correct_vertical = -1
            
            results = []
            if abs(amplitude_answer - correct_amp) < 0.01:
                results.append("✅ Amplitude correct!")
            else:
                results.append(f"❌ Amplitude: {correct_amp}")
            
            if abs(period_answer - correct_period) < 0.01:
                results.append("✅ Period correct!")
            else:
                results.append(f"❌ Period: {correct_period:.3f}")
            
            if abs(phase_answer - correct_phase) < 0.01:
                results.append("✅ Phase shift correct!")
            else:
                results.append(f"❌ Phase shift: {correct_phase:.3f}")
            
            if abs(vertical_answer - correct_vertical) < 0.01:
                results.append("✅ Vertical shift correct!")
            else:
                results.append(f"❌ Vertical shift: {correct_vertical}")
            
            for result in results:
                st.write(result)
    
    else:  # Definition Practice
        st.subheader("📏 Definition Practice")
        
        definition_problems = [
            {
                "question": "In a right triangle, if the opposite side is 6 and the hypotenuse is 10, what is sin(θ)?",
                "options": ["A) 6/10 = 0.6", "B) 8/10 = 0.8", "C) 6/8 = 0.75", "D) 10/6 = 1.67"],
                "correct": "A",
                "explanation": "sin(θ) = opposite ÷ hypotenuse = 6 ÷ 10 = 0.6"
            },
            {
                "question": "On a circle with radius 5, if a point is at (3, 4), what is cos(θ)?",
                "options": ["A) 4/5 = 0.8", "B) 3/5 = 0.6", "C) 3/4 = 0.75", "D) 4/3 = 1.33"],
                "correct": "B",
                "explanation": "cos(θ) = x-coordinate ÷ radius = 3 ÷ 5 = 0.6"
            }
        ]
        
        for i, problem in enumerate(definition_problems):
            st.write(f"**Problem {i+1}:** {problem['question']}")
            user_choice = st.radio(f"Choose your answer:", problem["options"], key=f"def_prob_{i}")
            
            if st.button(f"Check Answer {i+1}", key=f"def_check_{i}"):
                if user_choice.startswith(problem["correct"]):
                    st.success(f"✅ Correct! {problem['explanation']}")
                else:
                    st.error(f"❌ Not quite. {problem['explanation']}")

# --- LESSON 8: REAL-WORLD APPLICATIONS ---
elif lesson_choice == "🌍 Real-World Applications":
    st.header("🌍 Trigonometry in the Real World")
    
    st.markdown("""
    ### 🏗️ Where Ancient Mathematics Meets Modern Life
    
    From the pyramids of ancient Egypt to modern skyscrapers, trigonometry shapes our world!
    """)
    
    app_choice = st.selectbox("Explore an application:", 
                             ["🏛️ Ancient Architecture", "🌊 Ocean Waves", "🎵 Sound & Music"])
    
    if app_choice == "🏛️ Ancient Architecture":
        st.subheader("🏛️ Building Like the Ancients")
        
        # Interactive pyramid calculator
        st.markdown("#### 🧮 Build Your Own Pyramid")
        base_length = st.slider("Base length (meters):", 50, 300, 230)
        slope_angle = st.slider("Slope angle (degrees):", 45, 65, 52)
        
        # Calculate height
        height = (base_length / 2) * math.tan(math.radians(slope_angle))
        volume = (base_length ** 2 * height) / 3
        
        st.metric("Height", f"{height:.1f} meters")
        st.metric("Volume", f"{volume:,.0f} cubic meters")
    
    elif app_choice == "🌊 Ocean Waves":
        st.subheader("🌊 The Mathematics of Ocean Waves")
        
        st.markdown("""
        #### Wave Equation: h(x,t) = A sin(kx - ωt + φ)
        
        Where:
        - **A**: Amplitude (wave height)
        - **k**: Wave number (2π/wavelength)
        - **ω**: Angular frequency (2π/period)
        - **φ**: Phase shift
        """)
        
        # Wave controls
        wave_amplitude = st.slider("Wave height (A):", 0.5, 5.0, 2.0, 0.1)
        wavelength = st.slider("Wavelength (λ):", 5, 50, 20, 1)
        period = st.slider("Period (T) seconds:", 2, 20, 8, 1)
        
        # Calculate derived values
        k = 2 * math.pi / wavelength  # wave number
        omega = 2 * math.pi / period  # angular frequency
        
        # Generate wave data
        x = np.linspace(0, 100, 1000)
        y = wave_amplitude * np.sin(k * x)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Ocean Wave',
                               line=dict(color='blue', width=3)))
        fig.add_hline(y=0, line_dash="dot", line_color="gray")
        
        fig.update_layout(
            title="Ocean Wave Pattern",
            xaxis_title="Distance",
            yaxis_title="Wave Height",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    else:  # Sound & Music
        st.subheader("🎵 The Trigonometry of Sound")
        
        st.markdown("""
        #### Musical Notes as Sine Waves
        Every musical note is a sine wave with a specific frequency!
        """)
        
        # Musical note frequencies (in Hz)
        notes = {
            "C4": 261.63, "D4": 293.66, "E4": 329.63, "F4": 349.23,
            "G4": 392.00, "A4": 440.00, "B4": 493.88, "C5": 523.25
        }
        
        selected_note = st.selectbox("Choose a musical note:", list(notes.keys()))
        frequency = notes[selected_note]
        duration = st.slider("Duration (seconds):", 0.1, 2.0, 0.5, 0.1)
        
        st.metric("Frequency", f"{frequency} Hz")
        st.metric("Period", f"{1/frequency:.4f} seconds")
        
        # Generate sound wave
        sample_rate = 1000  # samples per second
        t = np.linspace(0, duration, int(sample_rate * duration))
        y = np.sin(2 * math.pi * frequency * t)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name=f'{selected_note} ({frequency} Hz)',
                               line=dict(color='purple', width=2)))
        
        fig.update_layout(
            title=f"Sound Wave: {selected_note}",
            xaxis_title="Time (seconds)",
            yaxis_title="Amplitude",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)

# --- LESSON 9: QUICK REFERENCE ---
elif lesson_choice == "🧮 Quick Reference Guide":
    st.header("🧮 Quick Reference Guide")
    
    st.markdown("""
    ### 📋 Your Trigonometry Cheat Sheet
    Everything you need to remember in one place!
    """)
    
    # Create tabs for different reference sections
    ref_tabs = st.tabs(["🔄 Conversions", "🌀 Unit Circle", "📊 Functions", "🧮 Formulas"])
    
    with ref_tabs[0]:  # Conversions
        st.subheader("🔄 Degree ↔ Radian Conversions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 📐 Common Angles
            | Degrees | Radians | π Form |
            |---------|---------|---------|
            | 0° | 0 | 0 |
            | 30° | 0.524 | π/6 |
            | 45° | 0.785 | π/4 |
            | 60° | 1.047 | π/3 |
            | 90° | 1.571 | π/2 |
            | 180° | 3.142 | π |
            | 270° | 4.712 | 3π/2 |
            | 360° | 6.283 | 2π |
            """)
        
        with col2:
            st.markdown("""
            #### 🧮 Conversion Formulas
            
            **Degrees to Radians:**
            ```
            radians = degrees × π/180
            ```
            
            **Radians to Degrees:**
            ```
            degrees = radians × 180/π
            ```
            
            #### 💡 Memory Tricks
            - **π radians = 180°** (half circle)
            - **2π radians = 360°** (full circle)
            - **1 radian ≈ 57.3°**
            """)
    
    with ref_tabs[1]:  # Unit Circle
        st.subheader("🌀 Unit Circle Values")
        
        st.markdown("""
        #### 📊 Special Angle Values
        - **0°/0**: cos = 1, sin = 0
        - **30°/π/6**: cos = √3/2, sin = 1/2
        - **45°/π/4**: cos = √2/2, sin = √2/2
        - **60°/π/3**: cos = 1/2, sin = √3/2
        - **90°/π/2**: cos = 0, sin = 1
        - **180°/π**: cos = -1, sin = 0
        - **270°/3π/2**: cos = 0, sin = -1
        """)
    
    with ref_tabs[2]:  # Functions
        st.subheader("📊 Trigonometric Functions")
        
        st.markdown("""
        #### 📈 Basic Function Properties
        
        | Function | Domain | Range | Period | Starts at (0,?) |
        |----------|--------|-------|--------|-----------------|
        | sin(x) | All reals | [-1, 1] | 2π | 0 |
        | cos(x) | All reals | [-1, 1] | 2π | 1 |
        | tan(x) | x ≠ π/2 + nπ | All reals | π | 0 |
        
        #### 🔄 Function Transformations
        **General form**: f(x) = A sin(Bx + C) + D
        
        - **A**: Amplitude (vertical stretch)
        - **B**: Frequency (horizontal compression if B > 1)
        - **C**: Phase shift (horizontal shift = -C/B)
        - **D**: Vertical shift
        - **Period**: 2π/|B|
        """)
    
    with ref_tabs[3]:  # Formulas
        st.subheader("🧮 Essential Formulas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 🔢 Basic Identities
            """)
            st.latex(r"\sin^2(x) + \cos^2(x) = 1")
            st.latex(r"\tan(x) = \frac{\sin(x)}{\cos(x)}")
            
        with col2:
            st.markdown("""
            #### 🎯 The Famous Limit
            """)
            st.latex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1")
            st.markdown("**(Only when x is in radians!)**")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; background-color: #f0f0f0; padding: 20px; border-radius: 10px;'>
    <h3 style='color: #4B0082;'>🎓 Congratulations!</h3>
    <p style='font-size: 1.1rem;'>You've completed the trigonometry journey from ancient wisdom to modern applications!</p>
    <p style='font-size: 0.9rem; color: #555;'>
        Remember: Every mathematical concept you've learned today has roots in the brilliant minds of 
        ancient African, Arab, and other civilizations who built monuments, predicted eclipses, 
        and navigated by the stars long before these ideas reached Greece.
    </p>
    <hr style='border-top: 1px solid #ccc; width: 50%; margin: 20px auto;'>
    <p style='font-size: 0.85rem;'>
        Built with ❤️ for 9th grade learners | <strong>Xavier Honablue, M.Ed</strong><br>
        <em>MathCraft: Where Ancient Wisdom Meets Modern Learning</em>
    </p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR ADDITIONAL INFO ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Quick Access")

if st.sidebar.button("🎯 Random Practice Problem"):
    problems = [
        "Convert 135° to radians",
        "Find sin(π/3) without a calculator",
        "What's the period of y = 3sin(2x)?",
        "Sketch one cycle of y = cos(x) + 1"
    ]
    random_problem = np.random.choice(problems)
    st.sidebar.success(f"Try this: {random_problem}")

st.sidebar.markdown("### 🌟 Did You Know?")
facts = [
    "The Great Pyramid's angle (51.8°) creates a perfect mathematical relationship with π!",
    "Ancient Islamic scholars invented many trigonometric functions we use today.",
    "The word 'algebra' comes from Arabic 'al-jabr' meaning 'reunion of broken parts'.",
    "African mathematicians in Timbuktu had advanced trigonometry texts in the 1200s.",
    "Sine waves describe everything from sound to light to ocean waves!"
]

if 'current_fact' not in st.session_state:
    st.session_state.current_fact = np.random.choice(facts)

if st.sidebar.button("🔄 New Fact"):
    st.session_state.current_fact = np.random.choice(facts)

st.sidebar.info(st.session_state.current_fact)

# Add session state management for interactive elements
if 'student_progress' not in st.session_state:
    st.session_state.student_progress = {
        'lessons_completed': [],
        'problems_attempted': 0,
        'correct_answers': 0
    }

# Track lesson completion
current_lesson = lesson_choice
if current_lesson not in st.session_state.student_progress['lessons_completed']:
    st.session_state.student_progress['lessons_completed'].append(current_lesson)

# Progress indicator in sidebar
progress_percentage = len(st.session_state.student_progress['lessons_completed']) / 9 * 100
st.sidebar.markdown(f"### 📊 Your Progress: {progress_percentage:.0f}%")
st.sidebar.progress(progress_percentage / 100)
