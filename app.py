
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Synergy IT Analytics Dashboard",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL COLOR PALETTES
# =========================================================

BLUE = "#2563EB"
PURPLE = "#7C3AED"
CYAN = "#0891B2"
GREEN = "#059669"
LIME = "#65A30D"
ORANGE = "#EA580C"
RED = "#DC2626"
PINK = "#DB2777"
INDIGO = "#4F46E5"

SERVICE_COLORS = [
    BLUE, PURPLE, CYAN, GREEN, LIME,
    "#CA8A04", ORANGE, RED, PINK, INDIGO
]

TECHNOLOGY_COLORS = [
    BLUE, INDIGO, PURPLE, "#9333EA",
    PINK, RED, ORANGE, "#CA8A04",
    GREEN, CYAN, "#0284C7", "#0EA5E9"
]

INDUSTRY_COLORS = [
    BLUE, CYAN, GREEN, LIME,
    "#CA8A04", ORANGE, RED
]

# =========================================================
# MODERN LIGHT THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef4ff 50%,
            #f8fafc 100%
        );
    color: #172033;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #ffffff 0%,
        #f4f7ff 100%
    );

    border-right: 1px solid #dbe4f0;
}

section[data-testid="stSidebar"] * {
    color: #172033 !important;
}

/* HEADER */

.main-title {
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #12355b;
    margin-bottom: 4px;
}

.subtitle {
    font-size: 16px;
    color: #64748b;
    margin-bottom: 20px;
}

.header-accent {
    width: 75px;
    height: 5px;

    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );

    border-radius: 10px;
    margin-bottom: 20px;
}

/* INFO */

.info-box {
    background: linear-gradient(
        135deg,
        #eff6ff,
        #f5f3ff
    );

    border: 1px solid #dbeafe;
    border-left: 5px solid #2563eb;

    padding: 18px 20px;
    border-radius: 14px;

    color: #334155;

    margin-bottom: 30px;

    box-shadow:
        0 5px 20px rgba(37, 99, 235, 0.08);
}

/* SECTION */

.section-title {
    font-size: 25px;
    font-weight: 750;
    color: #12355b;

    margin-top: 35px;
    margin-bottom: 18px;

    padding-bottom: 8px;

    border-bottom: 2px solid #e2e8f0;
}

/* KPI */

.kpi-card {
    position: relative;

    background: rgba(255,255,255,0.96);

    border: 1px solid #e2e8f0;
    border-radius: 16px;

    padding: 22px;

    min-height: 135px;

    overflow: hidden;

    box-shadow:
        0 8px 25px rgba(15,23,42,0.07);
}

.kpi-card::before {
    content: "";

    position: absolute;

    top: 0;
    left: 0;
    right: 0;

    height: 4px;

    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
}

.kpi-title {
    font-size: 13px;
    font-weight: 700;

    text-transform: uppercase;

    letter-spacing: 0.5px;

    color: #64748b;

    margin-bottom: 10px;
}

.kpi-value {
    font-size: 32px;
    font-weight: 800;

    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.kpi-note {
    font-size: 12px;
    color: #94a3b8;
    margin-top: 6px;
}

/* CARDS */

.support-card,
.location-card {
    background: #ffffff;

    border: 1px solid #e2e8f0;

    border-radius: 12px;

    padding: 16px;

    margin-bottom: 11px;

    box-shadow:
        0 4px 14px rgba(15,23,42,0.05);
}

.support-card {
    border-left: 5px solid #2563eb;
}

.location-card {
    border-left: 5px solid #7c3aed;
}

.support-title,
.location-title {
    font-size: 15px;
    font-weight: 700;
    color: #172033;
}

.support-category,
.location-type {
    font-size: 12px;
    color: #64748b;
    margin-top: 4px;
}

/* FILTERS */

div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 9px !important;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;

    margin-top: 40px;
    padding-top: 20px;

    border-top: 1px solid #e2e8f0;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
# =========================================================

company_metrics = pd.DataFrame([
    ["Years in Business", "25+", "Company-stated"],
    ["Endpoints Managed", "20K+", "Company-stated"],
    ["Certified Technicians", "350+", "Company-stated"],
    ["Awards", "8", "Company-stated"],
    ["Service Areas", "10", "Calculated"],
    ["Industries", "7", "Documented"],
], columns=["Metric", "Value", "Source Type"])


services = pd.DataFrame([
    ["Managed IT Services", "Managed Services"],
    ["Cloud Services", "Cloud"],
    ["Cybersecurity", "Security"],
    ["Network & Infrastructure", "Infrastructure"],
    ["IT Consulting", "Consulting"],
    ["Microsoft & Azure", "Microsoft"],
    ["IT Procurement", "Procurement"],
    ["Digital Transformation", "Digital Transformation"],
    ["IT Support", "Support"],
    ["Business Applications", "Development"],
], columns=["Service", "Category"])


technologies = pd.DataFrame([
    ["Microsoft Azure", "Cloud"],
    ["Microsoft 365", "Microsoft"],
    ["SharePoint", "Microsoft"],
    ["Cisco", "Networking"],
    ["VMware", "Infrastructure"],
    ["Citrix", "Infrastructure"],
    ["AWS", "Cloud"],
    ["Google Cloud", "Cloud"],
    ["Fortinet", "Security"],
    ["Palo Alto", "Security"],
    ["Sophos", "Security"],
    ["SonicWall", "Security"],
    ["Salesforce", "Development"],
    ["Odoo", "Development"],
], columns=["Technology", "Category"])


industries = pd.DataFrame([
    ["Healthcare"],
    ["Manufacturing"],
    ["Legal"],
    ["Retail"],
    ["Distribution & Logistics"],
    ["Non-Profit"],
    ["Services"],
], columns=["Industry"])


locations = pd.DataFrame([
    ["Mississauga, Ontario", "Office", "Canada"],
    ["Toronto, Ontario", "Office", "Canada"],
    ["New York, USA", "Office", "USA"],
], columns=["Location", "Type", "Country"])


support = pd.DataFrame([
    ["24/7/365 Service Desk", "Support"],
    ["Managed IT Support", "Managed Services"],
    ["Network Support", "Infrastructure"],
    ["Cybersecurity Support", "Security"],
    ["Cloud Support", "Cloud"],
    ["Disaster Recovery", "Business Continuity"],
    ["IT Consulting", "Consulting"],
    ["Technical Staffing", "Staffing"],
], columns=["Service", "Category"])


success_stories = pd.DataFrame([
    ["Cloud", "Cloud Migration", "Healthcare", "Azure", "Cloud"],
    ["Cybersecurity", "Security Enhancement", "Manufacturing", "Fortinet", "Security"],
    ["Microsoft", "Microsoft 365", "Legal", "Microsoft 365", "Microsoft"],
    ["Infrastructure", "Network Modernization", "Retail", "Cisco", "Infrastructure"],
    ["Development", "Business Application", "Services", "Odoo", "Development"],
], columns=[
    "Solution Area",
    "Project",
    "Industry",
    "Technology",
    "Category"
])

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <h2>🔎 Dashboard Filters</h2>
    <p style="color:#64748b;">
    Explore Synergy IT services and solutions
    </p>
    """,
    unsafe_allow_html=True
)

service_categories = sorted(services["Category"].unique())

selected_services = st.sidebar.multiselect(
    "Service Category",
    service_categories
)

industry_options = sorted(industries["Industry"].unique())

selected_industries = st.sidebar.multiselect(
    "Industry",
    industry_options
)

technology_categories = sorted(
    technologies["Category"].unique()
)

selected_technology = st.sidebar.multiselect(
    "Technology Category",
    technology_categories
)

location_options = sorted(locations["Location"].unique())

selected_locations = st.sidebar.multiselect(
    "Location",
    location_options
)

solution_options = sorted(
    success_stories["Solution Area"].unique()
)

selected_solution = st.sidebar.multiselect(
    "Solution Area",
    solution_options
)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="header-accent"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">💻 Synergy IT Analytics Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Executive analytics view of publicly available services, '
    'technologies, industries and business solutions.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-box">
    📊 <b>Company profile:</b> Dashboard figures combine
    company-stated information, documented public information,
    and calculated values from the structured dataset.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# FILTER DATA
# =========================================================

filtered_services = services.copy()

if selected_services:
    filtered_services = filtered_services[
        filtered_services["Category"].isin(selected_services)
    ]

filtered_industries = industries.copy()

if selected_industries:
    filtered_industries = filtered_industries[
        filtered_industries["Industry"].isin(selected_industries)
    ]

filtered_technologies = technologies.copy()

if selected_technology:
    filtered_technologies = filtered_technologies[
        filtered_technologies["Category"].isin(selected_technology)
    ]

filtered_locations = locations.copy()

if selected_locations:
    filtered_locations = filtered_locations[
        filtered_locations["Location"].isin(selected_locations)
    ]

filtered_success = success_stories.copy()

if selected_solution:
    filtered_success = filtered_success[
        filtered_success["Solution Area"].isin(selected_solution)
    ]

if selected_industries:
    filtered_success = filtered_success[
        filtered_success["Industry"].isin(selected_industries)
    ]

# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================

st.markdown("""
<style>
.kpi-card {
    background: white;
    border-radius: 14px;
    padding: 22px 18px;
    min-height: 145px;
    border-top: 5px solid #2563EB;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    text-align: center;
}

.kpi-title {
    font-size: 15px;
    font-weight: 600;
    color: #475569;
    margin-bottom: 12px;
}

.kpi-value {
    font-size: 30px;
    font-weight: 800;
    color: #0F3D66;
    margin-bottom: 10px;
}

.kpi-note {
    font-size: 12px;
    color: #64748B;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">📊 Executive Overview</div>',
    unsafe_allow_html=True
)

kpis = [
    ("Years in Business", "25+", "Company-stated"),
    ("Endpoints Managed", "20K+", "Company-stated"),
    ("Certified Technicians", "350+", "Company-stated"),
    ("Awards", "8", "Company-stated"),
    ("Service Areas", "10", "Calculated"),
    ("Industries", "7", "Documented"),
]

cols = st.columns(6)

for col, (title, value, note) in zip(cols, kpis):
    with col:
        html = f"""<div class="kpi-card">
<div class="kpi-title">{title}</div>
<div class="kpi-value">{value}</div>
<div class="kpi-note">{note}</div>
</div>"""

        st.markdown(html, unsafe_allow_html=True)
# =========================================================
# SERVICE PORTFOLIO
# =========================================================

st.markdown(
    '<div class="section-title">🛠️ Service Portfolio</div>',
    unsafe_allow_html=True
)

service_counts = (
    filtered_services
    .groupby("Category")
    .size()
    .reset_index(name="Count")
)

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        service_counts,
        x="Category",
        y="Count",
        color="Category",
        color_discrete_sequence=SERVICE_COLORS,
        title="Service Offering Coverage by Category"
    )

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        margin=dict(l=30, r=20, t=60, b=100)
    )

    fig.update_traces(
        marker_line_width=0,
        opacity=0.9
    )

    st.plotly_chart(fig, width="stretch")

with col2:

    fig = px.pie(
        service_counts,
        names="Category",
        values="Count",
        hole=0.58,
        color_discrete_sequence=SERVICE_COLORS,
        title="Service Portfolio Categories"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent"
    )

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(fig, width="stretch")

# =========================================================
# TECHNOLOGY
# =========================================================

st.markdown(
    '<div class="section-title">☁️ Technology & Solutions</div>',
    unsafe_allow_html=True
)

technology_counts = (
    filtered_technologies
    .groupby("Category")
    .size()
    .reset_index(name="Count")
)

fig = px.bar(
    technology_counts,
    x="Category",
    y="Count",
    color="Category",
    color_discrete_sequence=TECHNOLOGY_COLORS,
    title="Technology Coverage by Category"
)

fig.update_layout(
    template="plotly_white",
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=False,
    margin=dict(l=30, r=20, t=60, b=80)
)

fig.update_traces(
    marker_line_width=0,
    opacity=0.9
)

st.plotly_chart(fig, width="stretch")

# =========================================================
# INDUSTRY COVERAGE
# =========================================================

st.markdown(
    '<div class="section-title">🏢 Industry Coverage</div>',
    unsafe_allow_html=True
)

industry_counts = (
    filtered_industries
    .groupby("Industry")
    .size()
    .reset_index(name="Count")
)

fig = px.bar(
    industry_counts,
    x="Industry",
    y="Count",
    color="Industry",
    color_discrete_sequence=INDUSTRY_COLORS,
    title="Documented Industry Coverage"
)

fig.update_layout(
    template="plotly_white",
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=False,
    margin=dict(l=30, r=20, t=60, b=100)
)

fig.update_traces(
    marker_line_width=0,
    opacity=0.9
)

st.plotly_chart(fig, width="stretch")

# =========================================================
# SUCCESS STORIES
# =========================================================

st.markdown(
    '<div class="section-title">📈 Success Stories Analytics</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# ---------------------------------------------------------
# Solutions by Area
# ---------------------------------------------------------

with col1:

    solution_counts = (
        filtered_success
        .groupby("Solution Area")
        .size()
        .reset_index(name="Count")
    )

    fig_solution = px.bar(
        solution_counts,
        x="Count",
        y="Solution Area",
        orientation="h",
        color="Solution Area",
        color_discrete_sequence=[
            BLUE, PURPLE, CYAN, GREEN, ORANGE
        ],
        text="Count",
        title="Documented Solutions by Area"
    )

    fig_solution.update_layout(
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        xaxis_title="Number of Documented Success Stories",
        yaxis_title="Solution Area",
        margin=dict(l=30, r=30, t=60, b=40)
    )

    fig_solution.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig_solution,
        use_container_width=True
    )


# ---------------------------------------------------------
# Technology Used
# ---------------------------------------------------------

with col2:

    technology_story_counts = (
        filtered_success
        .groupby("Technology")
        .size()
        .reset_index(name="Count")
    )

    fig_technology = px.bar(
        technology_story_counts,
        x="Count",
        y="Technology",
        orientation="h",
        color="Technology",
        color_discrete_sequence=TECHNOLOGY_COLORS,
        text="Count",
        title="Technologies Featured in Success Stories"
    )

    fig_technology.update_layout(
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        xaxis_title="Number of Documented Success Stories",
        yaxis_title="Technology",
        margin=dict(l=30, r=30, t=60, b=40)
    )

    fig_technology.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig_technology,
        use_container_width=True
    )
# =========================================================
# SUPPORT + LOCATIONS
# =========================================================

st.markdown(
    '<div class="section-title">🎧 Service & Support</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🎧 Support Capabilities")

    for _, row in support.iterrows():

        support_html = f"""
<div class="support-card">
    <div class="support-title">{row['Service']}</div>
    <div class="support-category">{row['Category']}</div>
</div>
"""

        st.markdown(support_html, unsafe_allow_html=True)


with col2:

    st.markdown("### 🌎 Office Locations")

    for _, row in filtered_locations.iterrows():

        location_html = f"""
<div class="location-card">
    <div class="location-title">{row['Location']}</div>
    <div class="location-type">{row['Type']} • {row['Country']}</div>
</div>
"""

        st.markdown(location_html, unsafe_allow_html=True)

# =========================================================
# DATA EXPLORER
# =========================================================

st.markdown(
    '<div class="section-title">📋 Data Explorer</div>',
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4 = st.tabs([
    "Services",
    "Technologies",
    "Industries",
    "Locations"
])

with tab1:
    st.dataframe(
        filtered_services,
        width="stretch",
        hide_index=True
    )

with tab2:
    st.dataframe(
        filtered_technologies,
        width="stretch",
        hide_index=True
    )

with tab3:
    st.dataframe(
        filtered_industries,
        width="stretch",
        hide_index=True
    )

with tab4:
    st.dataframe(
        filtered_locations,
        width="stretch",
        hide_index=True
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Synergy IT Analytics Dashboard |
        Public-information analytics project |
        Built with Python • Pandas • Streamlit • Plotly
    </div>
    """,
    unsafe_allow_html=True
)
