st.header("📊 Sine & Cosine: From Definitions to Functions")
    
    st.markdown("""
    ### 🌊 From Points to Waves: The Function Story
    Now that you know sine and cosine are **ratios** and **coordinates**, let's see what happens when we **connect all the dots**!
    
    **The big idea**: As the angle changes continuously, sine and cosine create beautiful wave patterns!
    """)
    
    # Show the connection from circle to function
    st.subheader("🎬 Watch the Magic Happen: Circle → Wave")
    
    demo_choice = st.radio("Choose your demo:", 
                          ["🎭 Interactive: Move the angle yourself", "🎬 Animation: Watch it unfold", "📊 Both views side-by-side"])
    
    if demo_choice == "🎭 Interactive: Move the angle yourself":
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            angle_demo = st.slider("Move the angle:", 0, 720, 0, 15, key="demo_angle")
            angle_rad_demo = math.radians(angle_demo)
            
            st.markdown(f"""
            #### 📊 Current State:
            - **Angle**: {angle_demo}°
            - **x-coordinate**: {math.cos(angle_rad_demo):.3f}
            - **y-coordinate**: {math.sin(angle_rad_demo):.3f}
            - **cos({angle_demo}°)** = {math.cos(angle_rad_demo):.3f}
            - **sin({angle_demo}°)** = {math.sin(angle_rad_demo):.3f}
            """)
        
        with col2:
            # Unit circle view
            fig_circle_demo = go.Figure()
            
            # Circle
            theta_vals = np.linspace(0, 2*math.pi, 100)
            circle_x_vals = np.cos(theta_vals)
            circle_y_vals = np.sin(theta_vals)
            fig_circle_demo.add_trace(go.Scatter(x=circle_x_vals, y=circle_y_vals, mode='lines',
                                               line=dict(color='lightblue', width=3), name='Unit Circle'))
            
            # Current point
            current_x = math.cos(angle_rad_demo)
            current_y = math.sin(angle_rad_demo)
            fig_circle_demo.add_trace(go.Scatter(x=[current_x], y=[current_y], mode='markers',
                                               marker=dict(size=15, color='red'), name='Current Point'))
            
            # Line from center
            fig_circle_demo.add_trace(go.Scatter(x=[0, current_x], y=[0, current_y], mode='lines',
                                               line=dict(color='red', width=3)))
            
            # Coordinate lines
            fig_circle_demo.add_trace(go.Scatter(x=[current_x, current_x], y=[0, current_y], mode='lines',
                                               line=dict(color='green', width=2, dash='dash')))
            fig_circle_demo.add_trace(go.Scatter(x=[0, current_x], y=[current_y, current_y], mode='lines',
                                               line=dict(color='blue', width=2, dash='dash')))
            
            fig_circle_demo.update_layout(title="Unit Circle", xaxis=dict(scaleanchor="y", scaleratio=1, range=[-1.2, 1.2]),
                                        yaxis=dict(range=[-1.2, 1.2]), height=300, showlegend=False)
            
            st.plotly_chart(fig_circle_demo, use_container_width=True)
        
        with col3:
            # Function values up to current angle
            angles_so_far = np.linspace(0, math.radians(angle_demo), max(angle_demo//5, 1))
            angles_degrees = np.degrees(angles_so_far)
            cos_values = np.cos(angles_so_far)
            sin_values = np.sin(angles_so_far)
            
            fig_function_demo = go.Figure()
            fig_function_demo.add_trace(go.Scatter(x=angles_degrees, y=cos_values, mode='lines+markers',
                                                 line=dict(color='blue', width=3), name='cosine'))
            fig_function_demo.add_trace(go.Scatter(x=angles_degrees, y=sin_values, mode='lines+markers',
                                                 line=dict(color='red', width=3), name='sine'))
            
            # Current point on functions
            fig_function_demo.add_trace(go.Scatter(x=[angle_demo], y=[math.cos(angle_rad_demo)], mode='markers',
                                                 marker=dict(size=12, color='blue'), showlegend=False))
            fig_function_demo.add_trace(go.Scatter(x=[angle_demo], y=[math.sin(angle_rad_demo)], mode='markers',
                                                 marker=dict(size=12, color='red'), showlegend=False))
            
            fig_function_demo.update_layout(title="Building the Functions", xaxis_title="Angle (degrees)",
                                          yaxis_title="Function Value", height=300, yaxis=dict(range=[-1.2, 1.2]))
            
            st.plotly_chart(fig_function_demo, use_container_width=True)
    
    elif demo_choice == "🎬 Animation: Watch it unfold":
        if st.button("▶️ Start Animation"):
            placeholder_circle = st.empty()
            placeholder_function = st.empty()
            
            angles_animated = []
            cos_animated = []
            sin_animated = []
            
            for angle_deg in range(0, 361, 10):
                angle_rad = math.radians(angle_deg)
                angles_animated.append(angle_deg)
                cos_animated.append(math.cos(angle_rad))
                sin_animated.append(math.sin(angle_rad))
                
                # Circle plot
                fig_anim_circle = go.Figure()
                theta_circle = np.linspace(0, 2*math.pi, 100)
                fig_anim_circle.add_trace(go.Scatter(x=np.cos(theta_circle), y=np.sin(theta_circle),
                                                   mode='lines', line=dict(color='lightblue', width=3)))
                fig_anim_circle.add_trace(go.Scatter(x=[math.cos(angle_rad)], y=[math.sin(angle_rad)],
                                                   mode='markers', marker=dict(size=15, color='red')))
                fig_anim_circle.add_trace(go.Scatter(x=[0, math.cos(angle_rad)], y=[0, math.sin(angle_rad)],
                                                   mode='lines', line=dict(color='red', width=3)))
                fig_anim_circle.update_layout(title=f"Angle: {angle_deg}°", xaxis=dict(scaleanchor="y", range=[-1.2, 1.2]),
                                            yaxis=dict(range=[-1.2, 1.2]), height=250, showlegend=False)
                
                # Function plot  
                fig_anim_func = go.Figure()
                fig_anim_func.add_trace(go.Scatter(x=angles_animated, y=cos_animated, mode='lines',
                                                 line=dict(color='blue', width=3), name='cosine'))
                fig_anim_func.add_trace(go.Scatter(x=angles_animated, y=sin_animated, mode='lines',
                                                 line=dict(color='red', width=3), name='sine'))
                fig_anim_func.update_layout(title="Functions Being Created", xaxis_title="Angle (degrees)",
                                          yaxis_title="Value", height=250, yaxis=dict(range=[-1.2, 1.2]))
                
                placeholder_circle.plotly_chart(fig_anim_circle, use_container_width=True)
                placeholder_function.plotly_chart(fig_anim_func, use_container_width=True)
    
    else:  # Both views side-by-side
        st.markdown("#### 📊 Complete Picture: Circle and Functions Together")
        
        range_choice = st.selectbox("Choose angle range to display:", 
                                   ["One full rotation (0° to 360°)", "Two rotations (0° to 720°)", "Custom range"])
        
        if range_choice == "Custom range":
            max_angle = st.slider("Maximum angle to show:", 180, 1440, 360, 90)
        elif range_choice == "Two rotations (0° to 720°)":
            max_angle = 720
        else:
            max_angle = 360
        
        # Generate complete function data
        angles_complete = np.linspace(0, max_angle, max_angle//2)
        angles_rad_complete = np.radians(angles_complete)
        cos_complete = np.cos(angles_rad_complete)
        sin_complete = np.sin(angles_rad_complete)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            # Unit circle (showing current position)
            current_angle = st.slider("Current angle:", 0, max_angle, 0, 15, key="current_pos")
            current_rad = math.radians(current_angle)
            
            fig_both_circle = go.Figure()
            
            # Circle
            theta_both = np.linspace(0, 2*math.pi, 100)
            fig_both_circle.add_trace(go.Scatter(x=np.cos(theta_both), y=np.sin(theta_both), mode='lines',
                                               line=dict(color='lightblue', width=3), name='Unit Circle'))
            
            # Current position
            curr_x = math.cos(current_rad)
            curr_y = math.sin(current_rad)
            fig_both_circle.add_trace(go.Scatter(x=[curr_x], y=[curr_y], mode='markers',
                                               marker=dict(size=15, color='red'), name='Current'))
            fig_both_circle.add_trace(go.Scatter(x=[0, curr_x], y=[0, curr_y], mode='lines',
                                               line=dict(color='red', width=3)))
            
            # Trail showing path
            if current_angle > 0:
                trail_angles = np.linspace(0, current_rad, max(current_angle//10, 1))
                trail_x = np.import streamlit as st
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
    
    if definition_approach == "🔄 Both Together":
        st.markdown("---")
        st.subheader("🔄 Connecting Both Definitions")
        
        st.markdown("""
        ### 🎯 The Big Picture: They're the SAME Thing!
        
        The right triangle and circle definitions are **identical**:
        
        - **Right triangle**: sine = opposite ÷ hypotenuse
        - **Circle**: sine = y-coordinate ÷ radius
        
        **Why?** Because the "opposite side" IS the y-coordinate, and the "hypotenuse" IS the radius!
        
        The "adjacent side" IS the x-coordinate!
        """)
        
        # Side-by-side comparison
        compare_angle = st.slider("Compare at angle:", 10, 80, 30, 5, key="compare_angle")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📐 Triangle View")
            triangle_hyp = 8
            triangle_opp = triangle_hyp * math.sin(math.radians(compare_angle))
            triangle_adj = triangle_hyp * math.cos(math.radians(compare_angle))
            
            st.write(f"**Opposite**: {triangle_opp:.2f}")
            st.write(f"**Adjacent**: {triangle_adj:.2f}")
            st.write(f"**Hypotenuse**: {triangle_hyp:.2f}")
            st.write(f"**sin({compare_angle}°)**: {triangle_opp/triangle_hyp:.3f}")
            st.write(f"**cos({compare_angle}°)**: {triangle_adj/triangle_hyp:.3f}")
        
        with col2:
            st.markdown("#### 🌀 Circle View")
            circle_r = 8
            circle_x = circle_r * math.cos(math.radians(compare_angle))
            circle_y = circle_r * math.sin(math.radians(compare_angle))
            
            st.write(f"**x-coordinate**: {circle_x:.2f}")
            st.write(f"**y-coordinate**: {circle_y:.2f}")
            st.write(f"**Radius**: {circle_r:.2f}")
            st.write(f"**sin({compare_angle}°)**: {circle_y/circle_r:.3f}")
            st.write(f"**cos({compare_angle}°)**: {circle_x/circle_r:.3f}")
        
        if abs(triangle_opp - circle_y) < 0.01 and abs(triangle_adj - circle_x) < 0.01:
            st.success("🎉 See? The opposite = y-coordinate, and adjacent = x-coordinate!")
    
    st.markdown("---")
    st.subheader("💡 Key Insights")
    
    insight_cols = st.columns(3)
    
    with insight_cols[0]:
        st.markdown("""
        #### 🔢 **Sine & Cosine are RATIOS**
        - They're always between -1 and 1
        - They don't depend on the size of the triangle/circle
        - Only the angle matters!
        """)
    
    with insight_cols[1]:
        st.markdown("""
        #### 📍 **Sine & Cosine are COORDINATES**
        - On the unit circle, they ARE the coordinates
        - cos = how far right/left
        - sin = how far up/down
        """)
    
    with insight_cols[2]:
        st.markdown("""
        #### 🎯 **They're the SAME concept**
        - Triangle ratios = coordinate ratios
        - Ancient builders used both views
        - Modern math connects them beautifully
        """)
    
    # Quick check understanding
    st.markdown("---")
    st.subheader("🧠 Quick Understanding Check")
    
    check_questions = [
        {
            "question": "If you're at angle 60° on a circle with radius 5, and the point is at (2.5, 4.33), what is cos(60°)?",
            "options": ["A) 4.33/5 = 0.866", "B) 2.5/5 = 0.5", "C) 4.33/2.5 = 1.732", "D) 5/2.5 = 2"],
            "correct": "B",
            "explanation": "cos(60°) = x-coordinate ÷ radius = 2.5 ÷ 5 = 0.5"
        },
        {
            "question": "In a right triangle, if the opposite side is 3 and hypotenuse is 5, what is sin(θ)?",
            "options": ["A) 3/5 = 0.6", "B) 4/5 = 0.8", "C) 3/4 = 0.75", "D) 5/3 = 1.67"],
            "correct": "A", 
            "explanation": "sin(θ) = opposite ÷ hypotenuse = 3 ÷ 5 = 0.6"
        }
    ]
    
    for i, q in enumerate(check_questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        user_choice = st.radio(f"Choose your answer:", q["options"], key=f"check_{i}")
        
        if st.button(f"Check Answer {i+1}", key=f"check_btn_{i}"):
            if user_choice.startswith(q["correct"]):
                st.success(f"✅ Correct! {q['explanation']}")
            else:
                st.error(f"❌ Not quite. {q['explanation']}")

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
    st.header("📊 Sine & Cosine: The Wave Functions")
    
    st.markdown("""
    ### 🌊 From Circle to Wave
    When we "unwrap" the unit circle, we get the beautiful wave patterns of sine and cosine!
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

# --- LESSON 5: THE FAMOUS LIMIT ---
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
        
        # For degrees comparison
        x_vals_deg = np.linspace(-zoom*180/math.pi, zoom*180/math.pi, 1000)
        x_vals_deg = x_vals_deg[x_vals_deg != 0]
        sinx_over_x_deg = np.sin(np.radians(x_vals_deg)) / x_vals_deg
        
        fig = go.Figure()
        
        # sin(x)/x in radians
        fig.add_trace(go.Scatter(x=x_vals, y=sinx_over_x_rad, name='sin(x)/x (x in radians)', 
                               line=dict(color='red', width=3)))
        
        # Reference line y=1
        fig.add_hline(y=1, line_dash="dash", line_color="green", 
                     annotation_text="y = 1 (the limit!)")
        
        # sin(x)/x in degrees (for comparison)
        if zoom >= 0.1:  # Only show for larger zooms
            fig.add_trace(go.Scatter(x=x_vals_deg, y=sinx_over_x_deg, name='sin(x)/x (x in degrees)', 
                                   line=dict(color='blue', width=2, dash='dot')))
        
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
                               ["Degree ↔ Radian Conversion", "Unit Circle Values", "Function Properties", "Word Problems"])
    
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
    
    else:  # Word Problems
        st.subheader("🌍 Real-World Applications")
        
        problems = [
            {
                "question": "A Ferris wheel has a radius of 50 feet and rotates once every 2 minutes. If you start at the bottom, write a function for your height above the center.",
                "hint": "Think about amplitude, period, and vertical shift",
                "answer": "h(t) = 50cos(πt) + 50"
            },
            {
                "question": "The ancient Egyptians built the Great Pyramid with sides at a 51.8° angle. Convert this to radians.",
                "hint": "Use the conversion formula: radians = degrees × π/180",
                "answer": "51.8 × π/180 ≈ 0.904 radians"
            },
            {
                "question": "A pendulum swings according to θ(t) = 0.2sin(2t). What is the maximum angle and the period?",
                "hint": "Look at the coefficient and the inside of the sine function",
                "answer": "Max angle: 0.2 radians, Period: π seconds"
            }
        ]
        
        problem_choice = st.selectbox("Choose a word problem:", range(len(problems)), format_func=lambda x: f"Problem {x+1}")
        
        problem = problems[problem_choice]
        st.write(f"**Problem:** {problem['question']}")
        
        if st.button("Show Hint"):
            st.info(f"💡 Hint: {problem['hint']}")
        
        user_solution = st.text_area("Your solution:")
        
        if st.button("Show Answer"):
            st.success(f"✅ Answer: {problem['answer']}")

# --- LESSON 8: REAL-WORLD APPLICATIONS ---
elif lesson_choice == "🌍 Real-World Applications":
    st.header("🌍 Trigonometry in the Real World")
    
    st.markdown("""
    ### 🏗️ Where Ancient Mathematics Meets Modern Life
    
    From the pyramids of ancient Egypt to modern skyscrapers, trigonometry shapes our world!
    """)
    
    app_choice = st.selectbox("Explore an application:", 
                             ["🏛️ Ancient Architecture", "🌊 Ocean Waves", "🎵 Sound & Music", 
                              "🚁 Flight Paths", "⚡ Electrical Circuits", "🌙 Astronomy"])
    
    if app_choice == "🏛️ Ancient Architecture":
        st.subheader("🏛️ Building Like the Ancients")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            #### The Great Pyramid of Giza
            - **Base**: 230.4 meters per side
            - **Height**: 146.5 meters (originally)
            - **Slope angle**: 51.84°
            
            **How did they do it without calculators?**
            
            Ancient Egyptian mathematicians used:
            - **Seked**: Their version of slope (rise over run)
            - **Sacred geometry**: Ratios based on π and φ (golden ratio)
            - **Rope and shadow methods**: Practical trigonometry
            """)
            
            # Interactive pyramid calculator
            st.markdown("#### 🧮 Build Your Own Pyramid")
            base_length = st.slider("Base length (meters):", 50, 300, 230)
            slope_angle = st.slider("Slope angle (degrees):", 45, 65, 52)
            
            # Calculate height
            height = (base_length / 2) * math.tan(math.radians(slope_angle))
            volume = (base_length ** 2 * height) / 3
            
            st.metric("Height", f"{height:.1f} meters")
            st.metric("Volume", f"{volume:,.0f} cubic meters")
        
        with col2:
            # 3D pyramid visualization
            fig = go.Figure()
            
            # Pyramid base
            base_x = [-base_length/2, base_length/2, base_length/2, -base_length/2, -base_length/2]
            base_y = [-base_length/2, -base_length/2, base_length/2, base_length/2, -base_length/2]
            base_z = [0, 0, 0, 0, 0]
            
            # Pyramid apex
            apex_x, apex_y, apex_z = 0, 0, height
            
            # Draw edges
            for i in range(4):
                fig.add_trace(go.Scatter3d(
                    x=[base_x[i], apex_x], y=[base_y[i], apex_y], z=[base_z[i], apex_z],
                    mode='lines', line=dict(color='brown', width=3), showlegend=False
                ))
            
            # Draw base
            fig.add_trace(go.Scatter3d(
                x=base_x, y=base_y, z=base_z,
                mode='lines', line=dict(color='brown', width=3), showlegend=False
            ))
            
            fig.update_layout(
                scene=dict(
                    xaxis_title="X (meters)",
                    yaxis_title="Y (meters)", 
                    zaxis_title="Height (meters)",
                    aspectmode='cube'
                ),
                title="Your Pyramid Design",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
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
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("#### 🎛️ Wave Controls")
            wave_amplitude = st.slider("Wave height (A):", 0.5, 5.0, 2.0, 0.1)
            wavelength = st.slider("Wavelength (λ):", 5, 50, 20, 1)
            period = st.slider("Period (T) seconds:", 2, 20, 8, 1)
            time_control = st.slider("Time:", 0.0, 20.0, 0.0, 0.5)
            
            # Calculate derived values
            k = 2 * math.pi / wavelength  # wave number
            omega = 2 * math.pi / period  # angular frequency
            
            st.markdown(f"""
            #### 📊 Wave Properties:
            - **Wave number (k)**: {k:.3f}
            - **Angular frequency (ω)**: {omega:.3f}
            - **Wave speed**: {wavelength/period:.1f} units/second
            """)
        
        with col2:
            # Generate wave data
            x = np.linspace(0, 100, 1000)
            y = wave_amplitude * np.sin(k * x - omega * time_control)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Ocean Wave',
                                   line=dict(color='blue', width=3)))
            fig.add_hline(y=0, line_dash="dot", line_color="gray")
            
            fig.update_layout(
                title=f"Ocean Wave at t = {time_control} seconds",
                xaxis_title="Distance",
                yaxis_title="Wave Height",
                height=300
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Add animation
        if st.button("🎬 Animate Wave"):
            placeholder = st.empty()
            for t in np.linspace(0, period, 50):
                y_animated = wave_amplitude * np.sin(k * x - omega * t)
                fig_animated = go.Figure()
                fig_animated.add_trace(go.Scatter(x=x, y=y_animated, mode='lines', 
                                                name='Wave', line=dict(color='blue', width=3)))
                fig_animated.update_layout(
                    title=f"Animated Wave (t = {t:.1f}s)",
                    xaxis_title="Distance", yaxis_title="Height",
                    yaxis=dict(range=[-wave_amplitude*1.2, wave_amplitude*1.2]),
                    height=300
                )
                placeholder.plotly_chart(fig_animated, use_container_width=True)
    
    elif app_choice == "🎵 Sound & Music":
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
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            selected_note = st.selectbox("Choose a musical note:", list(notes.keys()))
            frequency = notes[selected_note]
            duration = st.slider("Duration (seconds):", 0.1, 2.0, 0.5, 0.1)
            
            st.metric("Frequency", f"{frequency} Hz")
            st.metric("Period", f"{1/frequency:.4f} seconds")
            
            st.markdown("""
            #### 🎼 Fun Facts:
            - **A4 = 440 Hz**: International tuning standard
            - **Octave**: Doubling frequency (C5 = 2 × C4)
            - **Perfect Fifth**: 3:2 frequency ratio
            """)
        
        with col2:
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
            
            # Chord visualization
            if st.checkbox("Add harmony (play chord)"):
                # Add a perfect fifth (frequency × 3/2)
                fifth_freq = frequency * 3/2
                y_chord = y + 0.7 * np.sin(2 * math.pi * fifth_freq * t)
                
                fig_chord = go.Figure()
                fig_chord.add_trace(go.Scatter(x=t, y=y, mode='lines', name=f'Root: {selected_note}',
                                             line=dict(color='purple', width=2)))
                fig_chord.add_trace(go.Scatter(x=t, y=0.7 * np.sin(2 * math.pi * fifth_freq * t), 
                                             mode='lines', name=f'Fifth: {fifth_freq:.1f} Hz',
                                             line=dict(color='orange', width=2)))
                fig_chord.add_trace(go.Scatter(x=t, y=y_chord, mode='lines', name='Chord (combined)',
                                             line=dict(color='red', width=3)))
                
                fig_chord.update_layout(
                    title="Musical Harmony = Adding Sine Waves!",
                    xaxis_title="Time (seconds)", yaxis_title="Amplitude",
                    height=400
                )
                
                st.plotly_chart(fig_chord, use_container_width=True)
    
    elif app_choice == "🚁 Flight Paths":
        st.subheader("🚁 Navigation and Flight Paths")
        
        st.markdown("""
        #### Pilots use trigonometry for:
        - **Heading calculations**: Direction angles
        - **Ground speed**: Dealing with wind vectors
        - **Landing approaches**: Glide path angles
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### ✈️ Flight Planning Problem")
            
            # Wind triangle problem
            airspeed = st.slider("Aircraft airspeed (mph):", 100, 300, 150)
            wind_speed = st.slider("Wind speed (mph):", 0, 50, 20)
            wind_direction = st.slider("Wind direction (degrees):", 0, 360, 45)
            desired_heading = st.slider("Desired ground track (degrees):", 0, 360, 90)
            
            # Convert to radians for calculations
            wind_dir_rad = math.radians(wind_direction)
            desired_rad = math.radians(desired_heading)
            
            # Vector calculations (simplified)
            # This is a simplified calculation - real navigation is more complex
            wind_x = wind_speed * math.sin(wind_dir_rad)
            wind_y = wind_speed * math.cos(wind_dir_rad)
            
            desired_x = math.sin(desired_rad)
            desired_y = math.cos(desired_rad)
            
            # Calculate required heading (simplified)
            drift_angle = math.degrees(math.atan2(wind_x, airspeed))
            actual_heading = desired_heading - drift_angle
            ground_speed = math.sqrt((airspeed + wind_y)**2 + wind_x**2)
            
            st.metric("Wind drift angle", f"{drift_angle:.1f}°")
            st.metric("Required heading", f"{actual_heading:.1f}°")
            st.metric("Ground speed", f"{ground_speed:.1f} mph")
        
        with col2:
            # Vector diagram
            fig = go.Figure()
            
            # Aircraft vector
            aircraft_x = airspeed * math.sin(math.radians(actual_heading))
            aircraft_y = airspeed * math.cos(math.radians(actual_heading))
            fig.add_trace(go.Scatter(x=[0, aircraft_x], y=[0, aircraft_y], 
                                   mode='lines+markers', name='Aircraft velocity',
                                   line=dict(color='blue', width=3)))
            
            # Wind vector
            fig.add_trace(go.Scatter(x=[0, wind_x], y=[0, wind_y], 
                                   mode='lines+markers', name='Wind velocity',
                                   line=dict(color='red', width=3)))
            
            # Ground track vector
            ground_x = aircraft_x + wind_x
            ground_y = aircraft_y + wind_y
            fig.add_trace(go.Scatter(x=[0, ground_x], y=[0, ground_y], 
                                   mode='lines+markers', name='Ground track',
                                   line=dict(color='green', width=3)))
            
            fig.update_layout(
                title="Wind Triangle Navigation",
                xaxis_title="East-West (mph)",
                yaxis_title="North-South (mph)",
                height=400,
                xaxis=dict(scaleanchor="y", scaleratio=1)
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    elif app_choice == "⚡ Electrical Circuits":
        st.subheader("⚡ AC Electricity and Power")
        
        st.markdown("""
        #### Alternating Current (AC) = Sine Waves!
        The electricity in your home follows: **V(t) = V₀ sin(ωt)**
        """)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("#### 🔌 AC Circuit Parameters")
            voltage_amplitude = st.slider("Peak voltage (V₀):", 100, 400, 170)  # ~120V RMS
            frequency_hz = st.slider("Frequency (Hz):", 50, 60, 60)  # US standard
            phase_shift = st.slider("Phase shift (degrees):", -180, 180, 0)
            
            # Calculate RMS values
            rms_voltage = voltage_amplitude / math.sqrt(2)
            omega = 2 * math.pi * frequency_hz
            
            st.metric("RMS Voltage", f"{rms_voltage:.1f} V")
            st.metric("Angular frequency (ω)", f"{omega:.1f} rad/s")
            
            st.info("""
            **Why RMS?**
            
            Root Mean Square voltage is what we measure on household outlets (~120V in US).
            
            RMS = Peak / √2
            """)
        
        with col2:
            # Generate AC waveform
            t = np.linspace(0, 3/frequency_hz, 1000)  # Show 3 cycles
            v = voltage_amplitude * np.sin(omega * t + math.radians(phase_shift))
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=t*1000, y=v, mode='lines', name='AC Voltage',
                                   line=dict(color='orange', width=3)))
            
            # Add RMS lines
            fig.add_hline(y=rms_voltage, line_dash="dash", line_color="green", 
                         annotation_text=f"RMS = {rms_voltage:.1f}V")
            fig.add_hline(y=-rms_voltage, line_dash="dash", line_color="green")
            fig.add_hline(y=0, line_dash="dot", line_color="gray")
            
            fig.update_layout(
                title=f"AC Voltage: {frequency_hz} Hz",
                xaxis_title="Time (milliseconds)",
                yaxis_title="Voltage (V)",
                height=300
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Power calculation
            if st.checkbox("Show power consumption"):
                # Power = V² / R, using arbitrary resistance
                resistance = 10  # ohms
                power = v**2 / resistance
                
                fig_power = go.Figure()
                fig_power.add_trace(go.Scatter(x=t*1000, y=power, mode='lines', name='Instantaneous Power',
                                             line=dict(color='red', width=2)))
                
                avg_power = (voltage_amplitude**2) / (2 * resistance)
                fig_power.add_hline(y=avg_power, line_dash="dash", line_color="blue",
                                   annotation_text=f"Average Power = {avg_power:.1f}W")
                
                fig_power.update_layout(
                    title="Power Consumption (P = V²/R)",
                    xaxis_title="Time (milliseconds)",
                    yaxis_title="Power (W)",
                    height=300
                )
                
                st.plotly_chart(fig_power, use_container_width=True)
    
    else:  # Astronomy
        st.subheader("🌙 Ancient Astronomy & Modern Space")
        
        st.markdown("""
        #### From African Star Charts to Modern Satellites
        Ancient astronomers used trigonometry to:
        - Track planetary motion
        - Predict eclipses
        - Create accurate calendars
        - Navigate by stars
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### 🌍 Earth's Orbit Around the Sun")
            
            day_of_year = st.slider("Day of year:", 1, 365, 80)  # Start around spring equinox
            
            # Earth's position (simplified circular orbit)
            angle = 2 * math.pi * day_of_year / 365
            earth_x = math.cos(angle)
            earth_y = math.sin(angle)
            
            # Calculate season info
            seasons = {
                80: "Spring Equinox", 171: "Summer Solstice", 
                266: "Fall Equinox", 355: "Winter Solstice"
            }
            
            closest_season = min(seasons.keys(), key=lambda x: abs(x - day_of_year))
            current_season = seasons[closest_season]
            
            # Daylight hours (simplified)
            latitude = 40  # degrees (approximate US latitude)
            declination = 23.45 * math.sin(math.radians((day_of_year - 81) * 360 / 365))
            hour_angle = math.degrees(math.acos(-math.tan(math.radians(latitude)) * math.tan(math.radians(declination))))
            daylight_hours = 2 * hour_angle / 15  # Convert to hours
            
            st.metric("Current season", current_season)
            st.metric("Daylight hours", f"{daylight_hours:.1f} hours")
            st.metric("Sun's declination", f"{declination:.1f}°")
        
        with col2:
            # Solar system diagram
            fig = go.Figure()
            
            # Sun
            fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', name='Sun',
                                   marker=dict(size=20, color='yellow')))
            
            # Earth's orbit
            orbit_theta = np.linspace(0, 2*math.pi, 100)
            orbit_x = np.cos(orbit_theta)
            orbit_y = np.sin(orbit_theta)
            fig.add_trace(go.Scatter(x=orbit_x, y=orbit_y, mode='lines', name="Earth's Orbit",
                                   line=dict(color='lightblue', dash='dash')))
            
            # Earth's current position
            fig.add_trace(go.Scatter(x=[earth_x], y=[earth_y], mode='markers+text', name='Earth',
                                   marker=dict(size=15, color='blue'),
                                   text=[f'Day {day_of_year}'], textposition="top center"))
            
            # Earth-Sun line
            fig.add_trace(go.Scatter(x=[0, earth_x], y=[0, earth_y], mode='lines', name='Distance',
                                   line=dict(color='orange', width=2)))
            
            fig.update_layout(
                title="Earth's Position in Orbit",
                xaxis_title="Distance (AU)",
                yaxis_title="Distance (AU)",
                xaxis=dict(scaleanchor="y", scaleratio=1, range=[-1.5, 1.5]),
                yaxis=dict(range=[-1.5, 1.5]),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Ancient vs Modern
        st.markdown("---")
        st.markdown("### 🏺 Ancient Wisdom Meets Modern Science")
        
        comparison_cols = st.columns(2)
        
        with comparison_cols[0]:
            st.markdown("""
            #### 🏺 Ancient Methods
            - **Shadow sticks**: Measuring angles with shadows
            - **Astrolabe**: Islamic navigation instrument
            - **Rope geometry**: Egyptian surveying
            - **Star maps**: Tracking celestial motion
            """)
        
        with comparison_cols[1]:
            st.markdown("""
            #### 🚀 Modern Applications  
            - **GPS satellites**: Trigonometric positioning
            - **Space missions**: Orbital mechanics
            - **Telescopes**: Coordinate systems
            - **Planetary exploration**: Navigation
            """)

# --- LESSON 9: QUICK REFERENCE ---
elif lesson_choice == "🧮 Quick Reference Guide":
    st.header("🧮 Quick Reference Guide")
    
    st.markdown("""
    ### 📋 Your Trigonometry Cheat Sheet
    Everything you need to remember in one place!
    """)
    
    # Create tabs for different reference sections
    ref_tabs = st.tabs(["🔄 Conversions", "🌀 Unit Circle", "📊 Functions", "🧮 Formulas", "📝 Vocabulary"])
    
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
            | 120° | 2.094 | 2π/3 |
            | 135° | 2.356 | 3π/4 |
            | 150° | 2.618 | 5π/6 |
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
        
        # Interactive unit circle reference
        quadrant = st.selectbox("Choose quadrant:", ["All", "Quadrant I (0° to 90°)", 
                                                   "Quadrant II (90° to 180°)", 
                                                   "Quadrant III (180° to 270°)", 
                                                   "Quadrant IV (270° to 360°)"])
        
        # Unit circle values
        circle_values = {
            "0°/0": (1, 0), "30°/π/6": (math.sqrt(3)/2, 1/2), "45°/π/4": (math.sqrt(2)/2, math.sqrt(2)/2),
            "60°/π/3": (1/2, math.sqrt(3)/2), "90°/π/2": (0, 1), "120°/2π/3": (-1/2, math.sqrt(3)/2),
            "135°/3π/4": (-math.sqrt(2)/2, math.sqrt(2)/2), "150°/5π/6": (-math.sqrt(3)/2, 1/2),
            "180°/π": (-1, 0), "210°/7π/6": (-math.sqrt(3)/2, -1/2), "225°/5π/4": (-math.sqrt(2)/2, -math.sqrt(2)/2),
            "240°/4π/3": (-1/2, -math.sqrt(3)/2), "270°/3π/2": (0, -1), "300°/5π/3": (1/2, -math.sqrt(3)/2),
            "315°/7π/4": (math.sqrt(2)/2, -math.sqrt(2)/2), "330°/11π/6": (math.sqrt(3)/2, -1/2)
        }
        
        st.markdown("#### 📊 Special Angle Values")
        for angle, (cos_val, sin_val) in circle_values.items():
            degrees_part = angle.split('/')[0]
            if quadrant == "All" or \
               (quadrant == "Quadrant I (0° to 90°)" and 0 <= int(degrees_part[:-1]) <= 90) or \
               (quadrant == "Quadrant II (90° to 180°)" and 90 < int(degrees_part[:-1]) <= 180) or \
               (quadrant == "Quadrant III (180° to 270°)" and 180 < int(degrees_part[:-1]) <= 270) or \
               (quadrant == "Quadrant IV (270° to 360°)" and 270 < int(degrees_part[:-1]) <= 360):
                st.write(f"**{angle}**: cos = {cos_val:.3f}, sin = {sin_val:.3f}")
    
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
        
        st.markdown("#### 🔗 Key Relationships")
        st.latex(r"\sin^2(x) + \cos^2(x) = 1")
        st.latex(r"\tan(x) = \frac{\sin(x)}{\cos(x)}")
        st.latex(r"\sin(x + 2\pi) = \sin(x)")
        st.latex(r"\cos(x + 2\pi) = \cos(x)")
    
    with ref_tabs[3]:  # Formulas
        st.subheader("🧮 Essential Formulas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### 🔢 Basic Identities
            """)
            st.latex(r"\sin^2(x) + \cos^2(x) = 1")
            st.latex(r"1 + \tan^2(x) = \sec^2(x)")
            st.latex(r"1 + \cot^2(x) = \csc^2(x)")
            
            st.markdown("#### ➕ Sum/Difference Formulas")
            st.latex(r"\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B")
            st.latex(r"\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B")
        
        with col2:
            st.markdown("""
            #### 📐 Law of Sines/Cosines
            """)
            st.latex(r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}")
            st.latex(r"c^2 = a^2 + b^2 - 2ab\cos C")
            
            st.markdown("#### 🎯 The Famous Limit")
            st.latex(r"\lim_{x \to 0} \frac{\sin x}{x} = 1")
            st.markdown("**(Only when x is in radians!)**")
    
    with ref_tabs[4]:  # Vocabulary
        st.subheader("📝 Mathematical Vocabulary")
        
        vocab_terms = {
            "Amplitude": "The maximum displacement from the center line of a wave or function",
            "Period": "The distance (or time) it takes for a function to complete one full cycle",
            "Frequency": "How many cycles occur in a unit of time or distance (inverse of period)",
            "Phase shift": "Horizontal displacement of a function left or right",
            "Radian": "An angle measure where the arc length equals the radius (≈ 57.3°)",
            "Unit circle": "A circle with radius 1, centered at the origin",
            "Sine": "The y-coordinate (vertical position) of a point on the unit circle",
            "Cosine": "The x-coordinate (horizontal position) of a point on the unit circle",
            "Tangent": "The slope of the line from origin to a point on the unit circle (sin/cos)",
            "Limit": "The value a function approaches as the input approaches a specific value",
            "Asymptote": "A line that a function approaches but never touches",
            "Domain": "All possible input values (x-values) for a function",
            "Range": "All possible output values (y-values) for a function"
        }
        
        for term, definition in vocab_terms.items():
            with st.expander(f"📖 {term}"):
                st.write(definition)
                
        st.markdown("---")
        st.markdown("### 🎯 Study Tips")
        
        tips_col1, tips_col2 = st.columns(2)
        
        with tips_col1:
            st.markdown("""
            #### 💡 Memory Strategies
            - **SOH-CAH-TOA**: Sin = Opposite/Hypotenuse, etc.
            - **Unit circle dance**: Move around physically
            - **CAST rule**: Which functions are positive in each quadrant
            - **π landmarks**: 0, π/2, π, 3π/2, 2π
            """)
        
        with tips_col2:
            st.markdown("""
            #### 🎮 Practice Methods
            - **Flashcards**: Unit circle values
            - **Real-world connections**: Waves, music, astronomy
            - **Graphing**: Sketch functions by hand
            - **Error analysis**: Learn from mistakes
            """)

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

st.sidebar.markdown("### 🔗 Next Steps")
st.sidebar.markdown("""
- **Precalculus**: Advanced function transformations
- **Calculus**: Derivatives of trig functions  
- **Physics**: Wave mechanics & oscillations
- **Engineering**: Signal processing & circuits
""")

# Add some session state management for interactive elements
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
