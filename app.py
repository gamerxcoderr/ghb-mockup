import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Grocery HeartBeat",
    page_icon="🛒",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .metric-card {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15);
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🛒 GHB")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Chat Interface"]
)

if page == "Dashboard":
    st.title("Grocery HeartBeat Dashboard")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Customers", "124,532", "↑ 12%")
    with col2:
        st.metric("Cross-Banner Shopping", "23%", "↑ 5%")
    with col3:
        st.metric("Avg Order Value", "$84.23", "↑ 8%")
    with col4:
        st.metric("Customer Satisfaction", "4.8/5.0", "↑ 0.2")
    
    # Charts
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Purchase Trends
        st.subheader("Purchase Trends")
        dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
        df = pd.DataFrame({
            'Date': dates,
            'WFM Orders': np.random.normal(100, 10, len(dates)),
            'Fresh Orders': np.random.normal(80, 15, len(dates))
        })
        
        fig = px.line(df, x='Date', y=['WFM Orders', 'Fresh Orders'],
                     title="Monthly Purchase Trends")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Customer Segments
        st.subheader("Customer Segments")
        segments = pd.DataFrame({
            'Segment': ['Prime Enthusiasts', 'Fresh Regulars', 'Organic Seekers', 'Occasional'],
            'Percentage': [45, 30, 15, 10]
        })
        
        fig = px.pie(segments, values='Percentage', names='Segment',
                    title="Customer Segment Distribution")
        st.plotly_chart(fig, use_container_width=True)

else:  # Chat Interface
    st.title("Interactive Chat Interface")
    
    # Query input
    user_input = st.text_input(
        "Ask about your grocery data",
        placeholder="e.g., Show my purchases from last week"
    )
    
    # Example queries
    with st.expander("📝 Example Queries"):
        st.markdown("""
        - What are my most frequent purchases?
        - Show my cross-banner shopping patterns
        - Compare my organic vs non-organic spending
        """)
    
    # Sample chat
    st.markdown("""
    **You:** Show my purchases from last week
    
    **GHB:** Here are your recent purchases:
    
    🛒 Whole Foods Market (Oct 3):
    - Organic Bananas ($2.99)
    - Almond Milk ($3.99)
    - Greek Yogurt ($4.99)
    
    🛒 Amazon Fresh (Oct 5):
    - Bread ($3.49)
    - Eggs ($4.99)
    - Milk ($3.99)
    
    Total Spent: $24.44
    """)
    
    # Sample visualization
    if st.button("Show Purchase Pattern"):
        items = ['Milk', 'Bread', 'Eggs', 'Bananas', 'Yogurt']
        purchases = [12, 10, 8, 7, 6]
        
        fig = px.bar(x=items, y=purchases,
                    title="Most Frequently Purchased Items",
                    labels={'x': 'Items', 'y': 'Number of Purchases'})
        st.plotly_chart(fig, use_container_width=True)
