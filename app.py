import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Grocery HeartBeat",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# AWS-style CSS
st.markdown("""
<style>
    /* AWS Theme Colors */
    :root {
        --aws-squid-ink: #232F3E;
        --aws-anchor: #FF9900;
        --aws-steel: #6C757D;
        --aws-grey: #F8F9FA;
    }
    
    /* Main Layout */
    .main {
        background-color: var(--aws-grey);
        padding: 1rem;
    }
    
    /* Navigation */
    .sidebar .sidebar-content {
        background-color: var(--aws-squid-ink);
        color: white;
    }
    
    /* Cards */
    .aws-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        margin-bottom: 1rem;
    }
    
    /* Metrics */
    .metric-container {
        padding: 1rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
    }
    
    /* Buttons */
    .stButton > button {
        background-color: var(--aws-anchor);
        color: var(--aws-squid-ink);
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: var(--aws-squid-ink);
    }
    
    /* Chat Interface */
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 4px;
    }
    .user-message {
        background-color: var(--aws-grey);
    }
    .bot-message {
        background-color: #E6F3FF;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://place-hold.it/300x100?text=GHB&fontsize=32", use_column_width=True)
    st.markdown("---")
    
    # Navigation Menu
    selected = st.radio(
        "Navigation",
        ["Home", "Chat Interface", "Analytics", "Settings"],
        format_func=lambda x: {
            "Home": "🏠 Home",
            "Chat Interface": "💬 Chat Interface",
            "Analytics": "📊 Analytics",
            "Settings": "⚙️ Settings"
        }[x]
    )

# Main Content
if selected == "Home":
    # Header
    st.title("Grocery HeartBeat Dashboard")
    
    # Top Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    metrics = [
        {"label": "Total Customers", "value": "124,532", "delta": "↑ 12%"},
        {"label": "Cross-Banner Shopping", "value": "23%", "delta": "↑ 5%"},
        {"label": "Avg Order Value", "value": "$84.23", "delta": "↑ 8%"},
        {"label": "Customer Satisfaction", "value": "4.8/5.0", "delta": "↑ 0.2"}
    ]
    
    for col, metric in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(f"""
            <div class="metric-container">
                <h4>{metric['label']}</h4>
                <h2>{metric['value']}</h2>
                <p style="color: green;">{metric['delta']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Main Content Area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="aws-card">', unsafe_allow_html=True)
        st.subheader("Cross-Banner Purchase Trends")
        
        # Sample data for trends
        dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
        df = pd.DataFrame({
            'Date': dates,
            'Whole Foods': np.random.normal(100, 10, len(dates)),
            'Amazon Fresh': np.random.normal(80, 15, len(dates))
        })
        
        fig = px.line(df, x='Date', y=['Whole Foods', 'Amazon Fresh'],
                     title="Monthly Purchase Trends")
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            xaxis_title="Date",
            yaxis_title="Purchase Volume"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Customer Segments
        st.markdown('<div class="aws-card">', unsafe_allow_html=True)
        st.subheader("Customer Segments")
        segments = {
            "Prime Enthusiasts": 45,
            "Fresh Regulars": 30,
            "Organic Seekers": 15,
            "Occasional Shoppers": 10
        }
        fig = px.pie(values=list(segments.values()),
                    names=list(segments.keys()),
                    hole=0.4)
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quick Insights
        st.markdown('<div class="aws-card">', unsafe_allow_html=True)
        st.subheader("Quick Insights")
        insights = [
            "80% of Prime customers shop at WFM",
            "26% use Amazon Fresh",
            "10% shop across both banners",
            "15% increase in organic purchases"
        ]
        for insight in insights:
            st.markdown(f"• {insight}")
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Chat Interface":
    st.title("Interactive Chat Interface")
    
    # Chat Interface
    st.markdown('<div class="aws-card">', unsafe_allow_html=True)
    
    # Query Input
    user_input = st.text_input(
        "Ask about your grocery data",
        placeholder="e.g., Show my purchases from last week"
    )
    
    # Example Queries
    with st.expander("📝 Example Queries"):
        st.markdown("""
        - What are my most frequent purchases?
        - Show my cross-banner shopping patterns
        - Compare my organic vs non-organic spending
        - What's my average weekly spend?
        """)
    
    # Chat History
    st.markdown("""
    <div class="chat-message user-message">
        <b>You:</b> Show my purchases from last week
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chat-message bot-message">
        <b>GHB:</b> Here are your recent purchases:
        
        🛒 Whole Foods Market (Oct 3):
        - Organic Bananas ($2.99)
        - Almond Milk ($3.99)
        - Greek Yogurt ($4.99)
        
        🛒 Amazon Fresh (Oct 5):
        - Bread ($3.49)
        - Eggs ($4.99)
        - Milk ($3.99)
        
        Total Spent: $24.44
        
        Would you like to see any patterns or trends in your purchases?
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Analytics":
    st.title("Advanced Analytics")
    
    # Tabs for different analytics views
    tab1, tab2, tab3 = st.tabs(["Customer Segments", "Purchase Patterns", "Trends"])
    
    with tab1:
        st.markdown('<div class="aws-card">', unsafe_allow_html=True)
        st.subheader("Customer Segmentation Analysis")
        
        # Sample segmentation data
        segments_df = pd.DataFrame({
            'Segment': ['Prime Enthusiasts', 'Fresh Regulars', 'Organic Seekers', 'Occasional'],
            'Size': [45, 30, 15, 10],
            'Avg Order': [120, 85, 95, 45],
            'Frequency': ['Weekly', 'Bi-weekly', 'Weekly', 'Monthly']
        })
        
        st.dataframe(segments_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="aws-card">', unsafe_allow_html=True)
        st.subheader("Purchase Pattern Analysis")
        
        # Sample pattern data
        pattern_data = pd.DataFrame({
            'Hour': range(24),
            'Orders': np.random.normal(50, 15, 24)
        })
        
        fig = px.bar(pattern_data, x='Hour', y='Orders',
                    title="Order Distribution by Hour")
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="aws-card">', unsafe_allow_html=True)
        st.subheader("Trend Analysis")
        
        # Sample trend data
        trend_data = pd.DataFrame({
            'Week': range(1, 53),
            'WFM': np.cumsum(np.random.normal(0, 1, 52)),
            'Fresh': np.cumsum(np.random.normal(0, 1, 52))
        })
        
        fig = px.line(trend_data, x='Week', y=['WFM', 'Fresh'],
                     title="Year-over-Year Growth")
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Settings":
    st.title("Settings")
    
    st.markdown('<div class="aws-card">', unsafe_allow_html=True)
    # Preferences
    st.subheader("Preferences")
    st.checkbox("Enable real-time notifications")
    st.checkbox("Auto-refresh dashboard")
    st.number_input("Refresh interval (minutes)", min_value=1, max_value=60, value=5)
    
    # Data Sources
    st.subheader("Data Sources")
    st.multiselect(
        "Active Data Sources",
        ["Whole Foods Market", "Amazon Fresh", "Prime Now"],
        ["Whole Foods Market", "Amazon Fresh"]
    )
    
    # Display Settings
    st.subheader("Display Settings")
    st.select_slider(
        "Chart Animation Speed",
        options=["Slow", "Medium", "Fast"],
        value="Medium"
    )
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    # This will be executed when the script is run directly
    pass
