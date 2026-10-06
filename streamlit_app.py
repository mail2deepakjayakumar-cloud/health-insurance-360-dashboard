import streamlit as st

st.set_page_config(
    page_title="Health Pulse 360",
    page_icon=":shield:",
    layout="wide",
    initial_sidebar_state="expanded",
)

session = get_active_session()

# --- Custom CSS for professional look ---
st.markdown("""
<style>
    .main .block-container { padding-top: 1.5rem; }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stMarkdown { color: #ffffff !important; }
    [data-testid="stSidebar"] .stSelectbox label { color: #93c5fd !important; }
    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] {
        background-color: rgba(37, 99, 235, 0.12) !important;
        border: 2px solid #3b82f6 !important;
        border-radius: 10px !important;
    }
    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] div[data-testid="stMarkdownContainer"],
    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] div,
    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] span,
    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] p,
    [data-testid="stSidebar"] .stSelectbox [data-baseweb="select"] input {
        color: #60a5fa !important;
        -webkit-text-fill-color: #60a5fa !important;
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] .stSelectbox svg {
        fill: #3b82f6 !important;
        color: #3b82f6 !important;
    }
    [data-testid="stSidebar"] .stRadio label {
        background: rgba(37, 99, 235, 0.06);
        border-radius: 8px;
        padding: 0.5rem 0.9rem;
        margin: 3px 0;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }
    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(37, 99, 235, 0.15);
        border-color: rgba(59, 130, 246, 0.4);
        transform: translateX(4px);
    }
    .ai-box {
        background: linear-gradient(135deg, rgba(37,99,235,0.08) 0%, rgba(59,130,246,0.06) 100%);
        border-left: 5px solid #3b82f6;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(37,99,235,0.1);
    }
    .ai-heading {
        color: #3b82f6;
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.6rem;
        letter-spacing: 0.3px;
    }
    .kpi-header {
        background: linear-gradient(135deg, #111827 0%, #1f2937 40%, #374151 100%);
        padding: 1.6rem 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(17, 24, 39, 0.6);
        border: 1px solid rgba(96, 165, 250, 0.15);
        position: relative;
        overflow: hidden;
    }
    .kpi-header::before {
        content: '';
        position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: radial-gradient(ellipse at 70% 20%, rgba(96, 165, 250, 0.08), transparent 50%);
    }
    .kpi-header h1 { color: white !important; margin: 0 !important; font-size: 1.9rem !important; position: relative; }
    .kpi-header p { color: #93c5fd !important; margin: 0.4rem 0 0 0 !important; position: relative; font-weight: 400; }
    .welcome-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 40%, #334155 100%);
        padding: 3.5rem 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(96, 165, 250, 0.15);
    }
    .welcome-banner h1 { color: #ffffff !important; font-size: 2.5rem !important; }
    .welcome-banner p { color: #93c5fd !important; font-size: 1.2rem !important; margin-top: 0.5rem !important; }
    .section-header {
        background: linear-gradient(90deg, rgba(37,99,235,0.08) 0%, rgba(59,130,246,0.03) 100%);
        border-left: 4px solid #3b82f6;
        padding: 0.7rem 1.2rem;
        border-radius: 0 10px 10px 0;
        margin: 1.2rem 0 0.8rem 0;
        font-size: 1rem;
    }
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-radius: 12px;
        padding: 0.8rem;
        border: 1px solid rgba(37, 99, 235, 0.1);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        border-radius: 14px;
        padding: 6px;
        box-shadow: 0 4px 16px rgba(17, 24, 39, 0.5);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
        color: #9ca3af !important;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(96, 165, 250, 0.1) !important;
        color: #bfdbfe !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
    }
    /* Styled dataframe tables */
    [data-testid="stDataFrame"] table {
        border-radius: 12px;
        overflow: hidden;
    }
    [data-testid="stDataFrame"] thead tr th {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
        color: #e0f2fe !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
        padding: 0.7rem 1rem !important;
        border-bottom: 2px solid #3b82f6 !important;
    }
    [data-testid="stDataFrame"] tbody tr:nth-child(odd) td {
        background: linear-gradient(90deg, #f0f9ff 0%, #f8fafc 100%) !important;
    }
    [data-testid="stDataFrame"] tbody tr:nth-child(even) td {
        background: linear-gradient(90deg, #e0f2fe 0%, #f0f9ff 100%) !important;
    }
    [data-testid="stDataFrame"] tbody tr:hover td {
        background: linear-gradient(90deg, #bfdbfe 0%, #dbeafe 100%) !important;
    }
    [data-testid="stDataFrame"] tbody tr td {
        color: #1e293b !important;
        font-size: 0.88rem !important;
        padding: 0.6rem 1rem !important;
        border-bottom: 1px solid #e2e8f0 !important;
    }
</style>
""", unsafe_allow_html=True)


# --- Data loaders ---
@st.cache_data(ttl=300)
def load_customers():
    return conn.query("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.CUSTOMERS")


@st.cache_data(ttl=300)
def load_claims():
    return conn.query("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.CLAIMS")


@st.cache_data(ttl=300)
def load_policies():
    return conn.query("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.POLICIES")


@st.cache_data(ttl=300)
def load_tickets():
    return conn.query("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.SERVICE_TICKETS")


@st.cache_data(ttl=300)
def load_agents():
    return conn.query("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.AGENTS")


@st.cache_data(ttl=300)
def load_conversations():
    return conn.query("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.CUSTOMER_CONVERSATIONS ORDER BY CONVERSATION_DATE DESC")


def ai_complete(prompt):
    escaped = prompt.replace("'", "''")
    try:
        result = conn.query(f"SELECT SNOWFLAKE.CORTEX.COMPLETE('llama3.1-70b', '{escaped}') AS RESPONSE")
        return result.iloc[0]["RESPONSE"]
    except Exception as e:
        return f"AI generation failed: {e}"


def render_ai_response(response, title="AI Recommendation"):
    formatted = response.replace("\\n", "\n").replace("\n", "  \n")
    st.markdown(f"""<div class="ai-box">
        <div class="ai-heading">🤖 {title}</div>
    </div>""", unsafe_allow_html=True)
    st.markdown(formatted)


# --- Sidebar ---
st.sidebar.markdown("### :shield: Health Pulse 360")
st.sidebar.caption("Intelligent Claims & Service Platform")
st.sidebar.divider()

agents_df = load_agents()
agent_names = ["-- Select Agent --"] + agents_df["AGENT_NAME"].tolist()
selected_agent = st.sidebar.selectbox("Login As", agent_names)

# --- Before login: show welcome screen ---
if selected_agent == "-- Select Agent --":
    st.markdown("""<div class="welcome-banner">
        <h1>🛡️ Health Pulse 360</h1>
        <p>Intelligent Claims & Service Management Platform</p>
    </div>""", unsafe_allow_html=True)

    # Show general KPIs even before login
    customers_df = load_customers()
    claims_df = load_claims()
    policies_df = load_policies()
    tickets_df = load_tickets()

    st.markdown('<div class="section-header"><strong>📊 Platform Overview</strong></div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Customers", f"{len(customers_df):,}")
    with c2:
        st.metric("Active Policies", f"{len(policies_df):,}")
    with c3:
        st.metric("Total Claims", f"{len(claims_df):,}")
    with c4:
        st.metric("Service Tickets", f"{len(tickets_df):,}")

    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown("**Claims Distribution**")
            status_counts = claims_df["TPA_APPROVAL_STATUS"].value_counts().reset_index()
            status_counts.columns = ["Status", "Count"]
            st.bar_chart(status_counts, x="Status", y="Count")
    with col2:
        with st.container():
            st.markdown("**Ticket Status**")
            ticket_status = tickets_df["STATUS"].value_counts().reset_index()
            ticket_status.columns = ["Status", "Count"]
            st.bar_chart(ticket_status, x="Status", y="Count")

    st.info("👈 Select an agent from the sidebar to access role-specific features.")
    st.stop()

# --- After login ---
agent_row = agents_df[agents_df["AGENT_NAME"] == selected_agent].iloc[0]
role_level = agent_row["ROLE_LEVEL"]

role_badges = {"MANAGER": "🟢 Manager", "SUPERVISOR": "🟠 Supervisor", "AGENT": "🔵 Agent"}
st.sidebar.markdown(f"**{role_badges.get(role_level, role_level)}**")
st.sidebar.markdown(f"📂 {agent_row['DEPARTMENT']}")
st.sidebar.divider()

# Navigation based on role — default to role-specific page
if role_level == "MANAGER":
    page = st.sidebar.radio("Navigate", ["📈 Strategic Analytics", "🏠 Home"], label_visibility="collapsed")
elif role_level == "SUPERVISOR":
    page = st.sidebar.radio("Navigate", ["📋 Claims & Tickets", "🏠 Home"], label_visibility="collapsed")
else:
    page = st.sidebar.radio("Navigate", ["🎧 Service Console", "🏠 Home"], label_visibility="collapsed")

# --- Load Data ---
customers_df = load_customers()
claims_df = load_claims()
policies_df = load_policies()
tickets_df = load_tickets()
conversations_df = load_conversations()


# --- HOME PAGE ---
def render_home():
    st.markdown(f"""<div class="kpi-header">
        <h1>Health Pulse 360</h1>
        <p>Welcome back, {selected_agent} • {role_badges.get(role_level, role_level)}</p>
    </div>""", unsafe_allow_html=True)

    total_customers = len(customers_df)
    total_claims = len(claims_df)
    total_policies = len(policies_df)
    total_tickets = len(tickets_df)
    pending_claims = len(claims_df[claims_df["TPA_APPROVAL_STATUS"] == "Pending"])
    approved_claims = len(claims_df[claims_df["TPA_APPROVAL_STATUS"] == "Approved"])
    rejected_claims = len(claims_df[claims_df["TPA_APPROVAL_STATUS"] == "Rejected"])
    total_claim_amount = claims_df["CLAIM_AMOUNT"].sum()
    open_tickets = len(tickets_df[tickets_df["STATUS"] == "OPEN"])
    avg_sla = claims_df["SLA_MINUTES_ELAPSED"].mean()

    home_css = """
    <style>
    .home-kpi-row { display: flex; gap: 0.8rem; margin-bottom: 1rem; flex-wrap: wrap; }
    .home-kpi-card {
        flex: 1; min-width: 140px; padding: 1rem 1.3rem; border-radius: 14px;
        position: relative; overflow: hidden;
    }
    .home-kpi-card::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        opacity: 0.08; background: radial-gradient(circle at 80% 20%, white, transparent 60%);
    }
    .hk-1 { background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%); }
    .hk-2 { background: linear-gradient(135deg, #1e4035 0%, #059669 100%); }
    .hk-3 { background: linear-gradient(135deg, #4a1d6b 0%, #9333ea 100%); }
    .hk-4 { background: linear-gradient(135deg, #1d4e6b 0%, #0891b2 100%); }
    .hk-5 { background: linear-gradient(135deg, #6b3a1d 0%, #ea580c 100%); }
    .hk-6 { background: linear-gradient(135deg, #065f46 0%, #10b981 100%); }
    .hk-7 { background: linear-gradient(135deg, #7f1d1d 0%, #ef4444 100%); }
    .hk-8 { background: linear-gradient(135deg, #4a1d4a 0%, #db2777 100%); }
    .home-kpi-card .hk-icon { font-size: 1.5rem; position: relative; }
    .home-kpi-card .hk-val {
        font-size: 1.6rem; font-weight: 800; color: #ffffff; margin: 0.2rem 0 0 0; position: relative;
    }
    .home-kpi-card .hk-lbl {
        font-size: 0.72rem; color: rgba(255,255,255,0.7); text-transform: uppercase;
        letter-spacing: 0.8px; font-weight: 600; position: relative;
    }
    .home-kpi-card .hk-badge {
        display: inline-block; margin-top: 0.3rem; padding: 0.1rem 0.4rem;
        border-radius: 20px; font-size: 0.65rem; font-weight: 700;
        background: rgba(255,255,255,0.15); position: relative;
    }
    .hk-badge-green { color: #86efac; }
    .hk-badge-amber { color: #fcd34d; }
    .hk-badge-red { color: #fca5a5; }
    </style>
    """
    st.markdown(home_css, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="home-kpi-row">
        <div class="home-kpi-card hk-1">
            <div class="hk-icon">👥</div>
            <div class="hk-val">{total_customers:,}</div>
            <div class="hk-lbl">Total Customers</div>
        </div>
        <div class="home-kpi-card hk-2">
            <div class="hk-icon">📋</div>
            <div class="hk-val">{total_policies:,}</div>
            <div class="hk-lbl">Active Policies</div>
        </div>
        <div class="home-kpi-card hk-3">
            <div class="hk-icon">🏥</div>
            <div class="hk-val">{total_claims:,}</div>
            <div class="hk-lbl">Total Claims</div>
        </div>
        <div class="home-kpi-card hk-4">
            <div class="hk-icon">🎫</div>
            <div class="hk-val">{total_tickets:,}</div>
            <div class="hk-lbl">Service Tickets</div>
        </div>
    </div>
    <div class="home-kpi-row">
        <div class="home-kpi-card hk-5">
            <div class="hk-icon">⏳</div>
            <div class="hk-val">{pending_claims}</div>
            <div class="hk-lbl">Pending Claims</div>
            <span class="hk-badge hk-badge-amber">Action Needed</span>
        </div>
        <div class="home-kpi-card hk-6">
            <div class="hk-icon">✅</div>
            <div class="hk-val">{approved_claims}</div>
            <div class="hk-lbl">Approved Claims</div>
            <span class="hk-badge hk-badge-green">{approved_claims/total_claims*100:.0f}% rate</span>
        </div>
        <div class="home-kpi-card hk-7">
            <div class="hk-icon">❌</div>
            <div class="hk-val">{rejected_claims}</div>
            <div class="hk-lbl">Rejected Claims</div>
            <span class="hk-badge hk-badge-red">{rejected_claims/total_claims*100:.0f}% rate</span>
        </div>
        <div class="home-kpi-card hk-8">
            <div class="hk-icon">💰</div>
            <div class="hk-val">₹{total_claim_amount/100000:.1f}L</div>
            <div class="hk-lbl">Total Claim Value</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown("**📊 Claims by Status**")
            status_counts = claims_df["TPA_APPROVAL_STATUS"].value_counts().reset_index()
            status_counts.columns = ["Status", "Count"]
            st.bar_chart(status_counts, x="Status", y="Count")
    with col2:
        with st.container():
            st.markdown("**🏆 Top Claims by Amount**")
            top_claims = claims_df.nlargest(10, "CLAIM_AMOUNT")[["CLAIM_ID", "HOSPITAL_NAME", "CLAIM_AMOUNT", "TPA_APPROVAL_STATUS"]]
            tc_html = '<div class="table-scroll-wrapper"><table class="styled-table"><thead><tr><th>Claim</th><th>Hospital</th><th>Amount</th><th>Status</th></tr></thead><tbody>'
            for _, r in top_claims.iterrows():
                s_col = "#10b981" if r["TPA_APPROVAL_STATUS"] == "Approved" else ("#f59e0b" if r["TPA_APPROVAL_STATUS"] == "Pending" else "#ef4444")
                tc_html += f'<tr><td>{r["CLAIM_ID"]}</td><td>{r["HOSPITAL_NAME"]}</td><td>₹{r["CLAIM_AMOUNT"]:,.0f}</td><td><span style="color:{s_col};font-weight:700;">{r["TPA_APPROVAL_STATUS"]}</span></td></tr>'
            tc_html += '</tbody></table></div>'
            st.markdown(tc_html, unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        with st.container():
            st.markdown("**🎫 Ticket Pipeline**")
            ticket_status = tickets_df["STATUS"].value_counts().reset_index()
            ticket_status.columns = ["Status", "Count"]
            st.bar_chart(ticket_status, x="Status", y="Count")
    with col4:
        with st.container():
            st.markdown("**🏥 Claims by Hospital (Top 8)**")
            hosp_claims = claims_df.groupby("HOSPITAL_NAME")["CLAIM_AMOUNT"].sum().sort_values(ascending=False).head(8).reset_index()
            hosp_claims.columns = ["Hospital", "Amount"]
            st.bar_chart(hosp_claims, x="Hospital", y="Amount")


# --- MANAGER VIEW ---
def render_manager_view():
    st.markdown("""<div class="kpi-header">
        <h1>📈 Strategic Analytics & AI Insights</h1>
        <p>Year-over-Year Analysis • Business Intelligence • AI Planning</p>
    </div>""", unsafe_allow_html=True)

    tab1, tab2 = st.tabs([
        "📊 YoY Metrics", "🤖 AI Strategy Hub"
    ])

    with tab1:
        yoy_css = """
        <style>
        .yoy-kpi-row { display: flex; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
        .yoy-kpi-card {
            flex: 1; min-width: 180px; padding: 1.2rem 1.5rem; border-radius: 14px;
            position: relative; overflow: hidden;
        }
        .yoy-kpi-card::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            opacity: 0.08; background: radial-gradient(circle at 80% 20%, white, transparent 60%);
        }
        .kpi-g1 { background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%); }
        .kpi-g2 { background: linear-gradient(135deg, #1e4035 0%, #059669 100%); }
        .kpi-g3 { background: linear-gradient(135deg, #4a1d6b 0%, #9333ea 100%); }
        .kpi-g4 { background: linear-gradient(135deg, #6b3a1d 0%, #ea580c 100%); }
        .kpi-g5 { background: linear-gradient(135deg, #1d4e6b 0%, #0891b2 100%); }
        .kpi-g6 { background: linear-gradient(135deg, #4a1d4a 0%, #db2777 100%); }
        .yoy-kpi-card .kpi-value {
            font-size: 1.8rem; font-weight: 800; color: #ffffff; margin: 0;
        }
        .yoy-kpi-card .kpi-label {
            font-size: 0.8rem; color: rgba(255,255,255,0.7); text-transform: uppercase;
            letter-spacing: 1px; margin-bottom: 0.3rem; font-weight: 600;
        }
        .yoy-kpi-card .kpi-delta {
            display: inline-block; margin-top: 0.4rem; padding: 0.15rem 0.5rem;
            border-radius: 20px; font-size: 0.75rem; font-weight: 700;
            background: rgba(255,255,255,0.15); color: #86efac;
        }
        </style>
        """
        st.markdown(yoy_css, unsafe_allow_html=True)

        avg_claim = claims_df["CLAIM_AMOUNT"].mean()
        approval_rate = len(claims_df[claims_df['TPA_APPROVAL_STATUS']=='Approved'])/len(claims_df)*100
        avg_sla = claims_df['SLA_MINUTES_ELAPSED'].mean()
        total_premium = customers_df['TOTAL_PREMIUM_PAID'].sum()

        st.markdown(f"""
        <div class="yoy-kpi-row">
            <div class="yoy-kpi-card kpi-g1">
                <div class="kpi-label">Total Customers</div>
                <div class="kpi-value">{len(customers_df):,}</div>
                <span class="kpi-delta">▲ 15% YoY</span>
            </div>
            <div class="yoy-kpi-card kpi-g2">
                <div class="kpi-label">Claims Processed</div>
                <div class="kpi-value">{len(claims_df):,}</div>
                <span class="kpi-delta">▲ 8% YoY</span>
            </div>
            <div class="yoy-kpi-card kpi-g3">
                <div class="kpi-label">Avg Claim Amount</div>
                <div class="kpi-value">₹{avg_claim/1000:.0f}K</div>
                <span class="kpi-delta">▲ 12% YoY</span>
            </div>
            <div class="yoy-kpi-card kpi-g4">
                <div class="kpi-label">Approval Rate</div>
                <div class="kpi-value">{approval_rate:.0f}%</div>
                <span class="kpi-delta">▲ 3% YoY</span>
            </div>
            <div class="yoy-kpi-card kpi-g5">
                <div class="kpi-label">Avg SLA (mins)</div>
                <div class="kpi-value">{avg_sla:.0f}</div>
                <span class="kpi-delta">▼ 10% faster</span>
            </div>
            <div class="yoy-kpi-card kpi-g6">
                <div class="kpi-label">Total Premium</div>
                <div class="kpi-value">₹{total_premium/10000000:.1f}Cr</div>
                <span class="kpi-delta">▲ 18% YoY</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                st.markdown("**📊 Policy Type Distribution**")
                if "POLICY_TYPE" in policies_df.columns:
                    type_dist = policies_df["POLICY_TYPE"].value_counts().reset_index()
                    type_dist.columns = ["Policy Type", "Count"]
                    st.bar_chart(type_dist, x="Policy Type", y="Count")
        with col2:
            with st.container():
                st.markdown("**🏥 Claims by Hospital**")
                hospital_claims = claims_df.groupby("HOSPITAL_NAME")["CLAIM_AMOUNT"].sum().sort_values(ascending=False).head(8).reset_index()
                hospital_claims.columns = ["Hospital", "Total Amount"]
                st.bar_chart(hospital_claims, x="Hospital", y="Total Amount")

        col3, col4 = st.columns(2)
        with col3:
            with st.container():
                st.markdown("**⚠️ Churn Risk Distribution**")
                customers_df["Risk Band"] = customers_df["CHURN_RISK_SCORE"].apply(
                    lambda x: "Low (<0.3)" if x < 0.3 else ("Medium (0.3-0.6)" if x < 0.6 else "High (>0.6)")
                )
                risk_dist = customers_df["Risk Band"].value_counts().reset_index()
                risk_dist.columns = ["Risk Band", "Count"]
                st.bar_chart(risk_dist, x="Risk Band", y="Count")
        with col4:
            with st.container():
                st.markdown("**📋 Claims Status Breakdown**")
                status_dist = claims_df["TPA_APPROVAL_STATUS"].value_counts().reset_index()
                status_dist.columns = ["Status", "Count"]
                st.bar_chart(status_dist, x="Status", y="Count")

    with tab2:
        import re

        ai_content_css = """
        <style>
        @keyframes pulse-glow {
            0%, 100% { opacity: 0.4; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.05); }
        }
        .ai-loading-container {
            display: flex; flex-direction: column; align-items: center;
            justify-content: center; padding: 3rem; margin: 2rem 0;
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
            border-radius: 16px;
        }
        .ai-loading-icon {
            font-size: 3.5rem; animation: pulse-glow 1.5s ease-in-out infinite;
        }
        .ai-loading-text {
            font-size: 1.2rem; color: #a5b4fc; margin-top: 0.75rem;
            font-weight: 600; letter-spacing: 0.5px;
        }
        .ai-loading-subtext {
            font-size: 0.85rem; color: #94a3b8; margin-top: 0.25rem;
        }
        .ai-strategy-card {
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
            border-radius: 16px; padding: 1.5rem 2rem; margin: 1rem 0;
            border: 1px solid rgba(129, 140, 248, 0.3);
            box-shadow: 0 4px 24px rgba(99, 102, 241, 0.15);
        }
        .ai-strategy-card .ai-content {
            color: #e0e7ff; font-size: 1rem; line-height: 1.8;
            font-weight: 400;
        }
        .ai-strategy-card .ai-content strong {
            color: #fbbf24; font-weight: 700;
        }
        </style>
        """
        st.markdown(ai_content_css, unsafe_allow_html=True)

        def md_to_html(text):
            text = text.replace("\\n", "\n").replace("\n", "<br>")
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            return text

        @st.cache_data(show_spinner=False)
        def load_ai_strategy(customers_count, claims_count, pending, rejected, avg_claim, avg_sla, total_premium, avg_churn, open_tickets, approval_rate, rejection_rate):
            insights_prompt = f"""You are a health insurance business analyst. Based on this data, provide exactly 5 crisp business insights as bullet points. Each point must be 1-2 sentences max. No intro, no conclusion, just the 5 points with actionable recommendations.

Data: {customers_count} customers, {claims_count} claims ({pending} pending, {rejected} rejected), avg claim INR {avg_claim:,.0f}, avg SLA {avg_sla:.0f} min, total premium INR {total_premium:,.0f}, avg churn risk {avg_churn:.2f}, {open_tickets} open tickets.

Format each as: **[Category]:** insight and recommendation."""

            target_prompt = f"""You are a health insurance strategy consultant. Given: {customers_count} customers, {approval_rate:.0f}% approval rate, {avg_churn:.2f} avg churn risk, INR {total_premium:,.0f} total premium, {rejection_rate:.0f}% rejection rate.

Provide exactly 5 strategic actions to achieve 20% growth target. Format as numbered list. Each action: **bold title** followed by 1 specific sentence with expected impact percentage. No intro or conclusion."""

            plan_prompt = f"""You are a health insurance CEO advisor. Create a next year plan based on: {customers_count} customers (15% YoY growth), INR {total_premium:,.0f} premium, {claims_count} claims, {avg_sla:.0f} min avg SLA, {avg_churn:.2f} churn risk.

Provide exactly 7 strategic priorities. Format each as: **[Priority Area]:** one specific actionable sentence with a measurable KPI target. No paragraphs, no intro, no conclusion."""

            return ai_complete(insights_prompt), ai_complete(target_prompt), ai_complete(plan_prompt)

        # Pre-compute values for cache key
        customers_count = len(customers_df)
        claims_count = len(claims_df)
        pending = len(claims_df[claims_df['TPA_APPROVAL_STATUS']=='Pending'])
        rejected = len(claims_df[claims_df['TPA_APPROVAL_STATUS']=='Rejected'])
        avg_claim = claims_df['CLAIM_AMOUNT'].mean()
        avg_sla = claims_df['SLA_MINUTES_ELAPSED'].mean()
        total_premium = customers_df['TOTAL_PREMIUM_PAID'].sum()
        avg_churn = customers_df['CHURN_RISK_SCORE'].mean()
        open_tickets = len(tickets_df[tickets_df['STATUS']=='OPEN'])
        approval_rate = len(claims_df[claims_df['TPA_APPROVAL_STATUS']=='Approved'])/len(claims_df)*100
        rejection_rate = rejected/len(claims_df)*100

        # Check if data is already cached
        cache_key_exists = "ai_strategy_loaded" in st.session_state

        content_area = st.empty()

        if not cache_key_exists:
            content_area.markdown("""
            <div class="ai-loading-container">
                <div class="ai-loading-icon">🧠</div>
                <div class="ai-loading-text">AI Strategy Engine Activating...</div>
                <div class="ai-loading-subtext">Analyzing business data & generating strategic insights</div>
            </div>
            """, unsafe_allow_html=True)

        insights_response, target_response, plan_response = load_ai_strategy(
            customers_count, claims_count, pending, rejected,
            avg_claim, avg_sla, total_premium, avg_churn,
            open_tickets, approval_rate, rejection_rate
        )
        st.session_state["ai_strategy_loaded"] = True

        content_area.empty()

        ai_section = st.radio(
            "AI Section",
            ["💡 Business Insights", "🎯 Target Plan", "🗓️ Next Year Strategy"],
            index=0,
            horizontal=True,
            label_visibility="collapsed"
        )

        if ai_section == "💡 Business Insights":
            st.markdown(f"""<div class="ai-strategy-card">
                <div class="ai-content">{md_to_html(insights_response)}</div>
            </div>""", unsafe_allow_html=True)
        elif ai_section == "🎯 Target Plan":
            st.markdown(f"""<div class="ai-strategy-card">
                <div class="ai-content">{md_to_html(target_response)}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="ai-strategy-card">
                <div class="ai-content">{md_to_html(plan_response)}</div>
            </div>""", unsafe_allow_html=True)


# --- SUPERVISOR VIEW ---
def render_supervisor_view():
    st.markdown("""<div class="kpi-header">
        <h1>📋 Claims & Ticket Management</h1>
        <p>Process Claims • Manage Tickets • AI-Assisted Decisions</p>
    </div>""", unsafe_allow_html=True)

    import re as _re

    supervisor_css = """
    <style>
    .sv-kpi-row { display: flex; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
    .sv-kpi-card {
        flex: 1; min-width: 160px; padding: 1.1rem 1.3rem; border-radius: 14px;
        position: relative; overflow: hidden;
    }
    .sv-kpi-card::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        opacity: 0.08; background: radial-gradient(circle at 80% 20%, white, transparent 60%);
    }
    .sv-g1 { background: linear-gradient(135deg, #0c4a6e 0%, #0284c7 100%); }
    .sv-g2 { background: linear-gradient(135deg, #713f12 0%, #d97706 100%); }
    .sv-g3 { background: linear-gradient(135deg, #064e3b 0%, #059669 100%); }
    .sv-g4 { background: linear-gradient(135deg, #4c0519 0%, #e11d48 100%); }
    .sv-kpi-card .sv-value {
        font-size: 1.6rem; font-weight: 800; color: #ffffff; margin: 0;
    }
    .sv-kpi-card .sv-label {
        font-size: 0.75rem; color: rgba(255,255,255,0.7); text-transform: uppercase;
        letter-spacing: 1px; margin-bottom: 0.2rem; font-weight: 600;
    }
    .sv-ai-card {
        background: linear-gradient(135deg, #111827 0%, #1f2937 50%, #374151 100%);
        border-radius: 14px; padding: 1.3rem 1.6rem; margin: 0.8rem 0;
        border: 1px solid rgba(96, 165, 250, 0.2);
        box-shadow: 0 4px 16px rgba(17, 24, 39, 0.4);
    }
    .sv-ai-card .sv-ai-content {
        color: #e2e8f0; font-size: 0.95rem; line-height: 1.7;
    }
    .sv-ai-card .sv-ai-content strong {
        color: #60a5fa; font-weight: 700;
    }
    </style>
    """
    st.markdown(supervisor_css, unsafe_allow_html=True)

    def sv_md_to_html(text):
        text = text.replace("\\n", "\n").replace("\n", "<br>")
        text = _re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        return text

    open_tickets = len(tickets_df[tickets_df["STATUS"] == "OPEN"])
    in_progress = len(tickets_df[tickets_df["STATUS"] == "IN_PROGRESS"])
    resolved = len(tickets_df[tickets_df["STATUS"] == "RESOLVED"])
    pending_claims = len(claims_df[claims_df["TPA_APPROVAL_STATUS"] == "Pending"])

    st.markdown(f"""
    <div class="sv-kpi-row">
        <div class="sv-kpi-card sv-g1">
            <div class="sv-label">Open Tickets</div>
            <div class="sv-value">{open_tickets}</div>
        </div>
        <div class="sv-kpi-card sv-g2">
            <div class="sv-label">In Progress</div>
            <div class="sv-value">{in_progress}</div>
        </div>
        <div class="sv-kpi-card sv-g3">
            <div class="sv-label">Resolved</div>
            <div class="sv-value">{resolved}</div>
        </div>
        <div class="sv-kpi-card sv-g4">
            <div class="sv-label">Pending Claims</div>
            <div class="sv-value">{pending_claims}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "⏳ Pending Claims", "🎫 Service Tickets", "📦 Queue Overview", "🤖 AI Assistant"
    ])

    with tab1:
        pending = claims_df[claims_df["TPA_APPROVAL_STATUS"] == "Pending"].copy()

        if len(pending) > 0:
            table_css = """
            <style>
            .table-scroll-wrapper { max-height:220px; overflow-y:auto; border-radius:12px; box-shadow: 0 4px 16px rgba(17,24,39,0.12); margin-bottom:1rem; }
            .styled-table { width:100%; border-collapse:separate; border-spacing:0; }
            .styled-table thead { position:sticky; top:0; z-index:1; }
            .styled-table thead tr { background: linear-gradient(135deg, #1e293b 0%, #334155 100%); }
            .styled-table th { color:#e0f2fe; font-weight:700; font-size:0.82rem; letter-spacing:0.8px; text-transform:uppercase; padding:0.75rem 1rem; text-align:left; border-bottom:2px solid #3b82f6; }
            .styled-table tbody tr:nth-child(odd) { background: linear-gradient(90deg, #eff6ff 0%, #f8fafc 100%); }
            .styled-table tbody tr:nth-child(even) { background: linear-gradient(90deg, #dbeafe 0%, #eff6ff 100%); }
            .styled-table tbody tr:hover { background: linear-gradient(90deg, #bfdbfe 0%, #dbeafe 100%); }
            .styled-table td { color:#1e293b; font-size:0.88rem; padding:0.65rem 1rem; border-bottom:1px solid #e2e8f0; }
            </style>
            """
            st.markdown(table_css, unsafe_allow_html=True)

            display_cols = ["CLAIM_ID", "CUSTOMER_ID", "HOSPITAL_NAME", "CLAIM_AMOUNT", "SLA_MINUTES_ELAPSED"]
            header_labels = ["Claim ID", "Customer", "Hospital", "Amount (₹)", "SLA (min)"]
            table_html = '<div class="table-scroll-wrapper"><table class="styled-table"><thead><tr>'
            for h in header_labels:
                table_html += f'<th>{h}</th>'
            table_html += '</tr></thead><tbody>'
            for _, row in pending[display_cols].iterrows():
                table_html += '<tr>'
                table_html += f'<td>{row["CLAIM_ID"]}</td>'
                table_html += f'<td>{row["CUSTOMER_ID"]}</td>'
                table_html += f'<td>{row["HOSPITAL_NAME"]}</td>'
                table_html += f'<td>₹{row["CLAIM_AMOUNT"]:,.0f}</td>'
                table_html += f'<td>{row["SLA_MINUTES_ELAPSED"]:.0f}</td>'
                table_html += '</tr>'
            table_html += '</tbody></table></div>'
            st.markdown(table_html, unsafe_allow_html=True)

            selected_claim = st.selectbox("Select Claim to Process", pending["CLAIM_ID"].tolist())
            claim_detail = pending[pending["CLAIM_ID"] == selected_claim].iloc[0]

            st.markdown(f"""
            <div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius:14px;
                padding:1.3rem 1.8rem; margin:0.8rem 0; border:1px solid rgba(59,130,246,0.2);
                box-shadow: 0 4px 20px rgba(15,23,42,0.3);">
                <div style="display:flex; gap:2rem; flex-wrap:wrap;">
                    <div style="flex:1; min-width:180px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Customer</div>
                        <div style="color:#ffffff; font-size:1rem; font-weight:600; margin-top:0.2rem;">{claim_detail['CUSTOMER_ID']}</div>
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.8rem; font-weight:700;">Hospital</div>
                        <div style="color:#ffffff; font-size:1rem; font-weight:600; margin-top:0.2rem;">{claim_detail['HOSPITAL_NAME']}</div>
                    </div>
                    <div style="flex:1; min-width:180px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Claim Amount</div>
                        <div style="color:#60a5fa; font-size:1.3rem; font-weight:800; margin-top:0.2rem;">₹{claim_detail['CLAIM_AMOUNT']:,.0f}</div>
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.8rem; font-weight:700;">SLA Elapsed</div>
                        <div style="color:#fbbf24; font-size:1.1rem; font-weight:700; margin-top:0.2rem;">{claim_detail['SLA_MINUTES_ELAPSED']:.0f} min</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            col_act1, col_act2 = st.columns([2, 1])
            with col_act1:
                action = st.selectbox("Action", ["Approve", "Partially Approve", "Reject"], key="claim_action")
            with col_act2:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("✅ Submit Decision", key="submit_claim", type="primary"):
                    st.success(f"Claim {selected_claim} marked as: **{action}**")

            @st.cache_data(show_spinner=False)
            def get_claim_ai(claim_id, hospital, amount, sla):
                prompt = f"""You are a claims adjudicator AI. Analyze this claim and give a crisp recommendation in exactly 5 bullet points:

Claim: {claim_id}, Hospital: {hospital}, Amount: INR {amount:,.0f}, SLA: {sla} min.

Format: 5 bullet points covering: 1) Recommend action (approve/reject/partial) with reason, 2) Risk flags, 3) Verification needed, 4) Suggested disbursement, 5) Priority level. One sentence each, no intro."""
                return ai_complete(prompt)

            ai_rec = get_claim_ai(
                claim_detail['CLAIM_ID'], claim_detail['HOSPITAL_NAME'],
                claim_detail['CLAIM_AMOUNT'], claim_detail['SLA_MINUTES_ELAPSED']
            )
            st.markdown(f"""<div class="sv-ai-card">
                <div class="sv-ai-content">{sv_md_to_html(ai_rec)}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.success("✅ No pending claims. All caught up!")

    with tab2:
        status_filter = st.multiselect(
            "Filter by Status", ["OPEN", "IN_PROGRESS", "RESOLVED"], default=["OPEN", "IN_PROGRESS"],
        )
        filtered_tickets = tickets_df[tickets_df["STATUS"].isin(status_filter)]

        if len(filtered_tickets) > 0:
            ticket_cols = ["TICKET_ID", "CUSTOMER_ID", "ISSUE_TYPE", "STATUS", "ASSIGNED_AGENT"]
            ticket_headers = ["Ticket ID", "Customer", "Issue", "Status", "Assigned To"]
            t_html = '<div class="table-scroll-wrapper"><table class="styled-table"><thead><tr>'
            for h in ticket_headers:
                t_html += f'<th>{h}</th>'
            t_html += '</tr></thead><tbody>'
            for _, row in filtered_tickets[ticket_cols].iterrows():
                status_color = "#10b981" if row["STATUS"] == "RESOLVED" else ("#f59e0b" if row["STATUS"] == "IN_PROGRESS" else "#ef4444")
                t_html += '<tr>'
                t_html += f'<td>{row["TICKET_ID"]}</td>'
                t_html += f'<td>{row["CUSTOMER_ID"]}</td>'
                t_html += f'<td>{row["ISSUE_TYPE"]}</td>'
                t_html += f'<td><span style="color:{status_color};font-weight:700;">{row["STATUS"]}</span></td>'
                t_html += f'<td>{row["ASSIGNED_AGENT"]}</td>'
                t_html += '</tr>'
            t_html += '</tbody></table></div>'
            st.markdown(t_html, unsafe_allow_html=True)

            selected_ticket = st.selectbox("Select Ticket", filtered_tickets["TICKET_ID"].tolist())
            ticket_detail = filtered_tickets[filtered_tickets["TICKET_ID"] == selected_ticket].iloc[0]

            notes_text = ticket_detail['RESOLUTION_NOTES'] if ticket_detail['RESOLUTION_NOTES'] and str(ticket_detail['RESOLUTION_NOTES']) != 'None' else '—'
            st.markdown(f"""
            <div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius:14px;
                padding:1.3rem 1.8rem; margin:0.8rem 0; border:1px solid rgba(59,130,246,0.2);
                box-shadow: 0 4px 20px rgba(15,23,42,0.3);">
                <div style="display:flex; gap:2rem; flex-wrap:wrap;">
                    <div style="flex:1; min-width:200px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Issue</div>
                        <div style="color:#ffffff; font-size:1rem; font-weight:600; margin-top:0.2rem;">{ticket_detail['ISSUE_TYPE']}</div>
                    </div>
                    <div style="flex:0 0 auto; min-width:140px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Status</div>
                        <div style="color:#fbbf24; font-size:1.1rem; font-weight:700; margin-top:0.2rem;">{ticket_detail['STATUS']}</div>
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.8rem; font-weight:700;">Assigned</div>
                        <div style="color:#60a5fa; font-size:1rem; font-weight:600; margin-top:0.2rem;">{ticket_detail['ASSIGNED_AGENT']}</div>
                    </div>
                </div>
                <div style="margin-top:0.8rem; border-top:1px solid rgba(59,130,246,0.15); padding-top:0.7rem;">
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Resolution Notes</div>
                    <div style="color:#cbd5e1; font-size:0.9rem; margin-top:0.2rem;">{notes_text}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            @st.cache_data(show_spinner=False)
            def get_ticket_ai(ticket_id, issue, status, notes):
                prompt = f"""You are a service desk AI. For this ticket, give exactly 4 crisp action points:

Ticket: {ticket_id}, Issue: {issue}, Status: {status}, Notes: {notes}.

Format: 4 numbered points covering: 1) Immediate next action, 2) Resolution approach, 3) Customer communication, 4) Estimated resolution time. One sentence each."""
                return ai_complete(prompt)

            notes_val = ticket_detail['RESOLUTION_NOTES'] if ticket_detail['RESOLUTION_NOTES'] and str(ticket_detail['RESOLUTION_NOTES']) != 'None' else 'None'
            ticket_ai = get_ticket_ai(
                ticket_detail['TICKET_ID'], ticket_detail['ISSUE_TYPE'],
                ticket_detail['STATUS'], notes_val
            )
            st.markdown(f"""<div class="sv-ai-card">
                <div class="sv-ai-content">{sv_md_to_html(ticket_ai)}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.info("No tickets matching the filter.")

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                st.markdown("**📊 Pending Claims by Hospital**")
                pending_by_hospital = claims_df[claims_df["TPA_APPROVAL_STATUS"] == "Pending"].groupby("HOSPITAL_NAME").size().reset_index()
                pending_by_hospital.columns = ["Hospital", "Pending Claims"]
                if len(pending_by_hospital) > 0:
                    st.bar_chart(pending_by_hospital, x="Hospital", y="Pending Claims")
                else:
                    st.success("No pending claims!")
        with col2:
            with st.container():
                st.markdown("**🎫 Tickets by Status**")
                ticket_status = tickets_df["STATUS"].value_counts().reset_index()
                ticket_status.columns = ["Status", "Count"]
                st.bar_chart(ticket_status, x="Status", y="Count")

        col3, col4 = st.columns(2)
        with col3:
            with st.container():
                st.markdown("**⏱️ Claims SLA Distribution**")
                claims_df["SLA Band"] = claims_df["SLA_MINUTES_ELAPSED"].apply(
                    lambda x: "< 1hr" if x < 60 else ("1-3 hrs" if x < 180 else ("3-6 hrs" if x < 360 else "> 6 hrs"))
                )
                sla_dist = claims_df["SLA Band"].value_counts().reset_index()
                sla_dist.columns = ["SLA Band", "Count"]
                st.bar_chart(sla_dist, x="SLA Band", y="Count")
        with col4:
            with st.container():
                st.markdown("**🏥 Top Hospitals by Claim Volume**")
                hosp_vol = claims_df.groupby("HOSPITAL_NAME").size().sort_values(ascending=False).head(6).reset_index()
                hosp_vol.columns = ["Hospital", "Claims"]
                st.bar_chart(hosp_vol, x="Hospital", y="Claims")

    with tab4:
        @st.cache_data(show_spinner=False)
        def get_queue_optimization(open_t, in_prog, pending_c, avg_sla):
            prompt = f"""You are an operations AI for health insurance. Current queue: {open_t} open tickets, {in_prog} in-progress, {pending_c} pending claims, avg SLA {avg_sla:.0f} min.

Give exactly 5 prioritized action items. Format each as: **[Priority X]:** one sentence with specific action. Focus on quick wins first, then escalations. No intro or conclusion."""
            return ai_complete(prompt)

        cache_exists = "sv_ai_loaded" in st.session_state
        sv_content = st.empty()

        if not cache_exists:
            sv_content.markdown("""
            <div style="display:flex;flex-direction:column;align-items:center;padding:2rem;
                background:linear-gradient(135deg,#111827,#1f2937);border-radius:14px;margin:1rem 0;">
                <div style="font-size:2.5rem;animation:pulse-glow 1.5s ease-in-out infinite;">⚡</div>
                <div style="color:#60a5fa;font-size:1.1rem;font-weight:600;margin-top:0.5rem;">Optimizing your queue...</div>
            </div>
            """, unsafe_allow_html=True)

        queue_ai = get_queue_optimization(
            open_tickets, in_progress, pending_claims, claims_df['SLA_MINUTES_ELAPSED'].mean()
        )
        st.session_state["sv_ai_loaded"] = True
        sv_content.empty()

        st.markdown(f"""<div class="sv-ai-card">
            <div class="sv-ai-content">{sv_md_to_html(queue_ai)}</div>
        </div>""", unsafe_allow_html=True)


# --- AGENT VIEW ---
def render_agent_view():
    st.markdown("""<div class="kpi-header">
        <h1>🎧 Customer Service Console</h1>
        <p>Customer Lookup • Claim Analysis • AI-Powered Support</p>
    </div>""", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["👤 Customer Lookup", "📄 Claim Analysis", "🎫 Ticket Lookup", "🎙️ Audio Transcription & AI Insights"])

    with tab1:
        st.markdown('<div class="section-header"><strong>Customer Intelligence</strong></div>', unsafe_allow_html=True)
        customer_list = customers_df["CUSTOMER_ID"].tolist()
        selected_customer = st.selectbox("Select Customer", customer_list)
        cust = customers_df[customers_df["CUSTOMER_ID"] == selected_customer].iloc[0]

        churn = cust["CHURN_RISK_SCORE"]
        churn_color = "#ef4444" if churn > 0.5 else ("#f59e0b" if churn > 0.25 else "#10b981")
        churn_label = "HIGH" if churn > 0.5 else ("MEDIUM" if churn > 0.25 else "LOW")

        st.markdown(f"""
        <div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius:14px;
            padding:1.3rem 1.8rem; margin:0.8rem 0; border:1px solid rgba(59,130,246,0.2);
            box-shadow: 0 4px 20px rgba(15,23,42,0.3);">
            <div style="display:flex; gap:2rem; flex-wrap:wrap;">
                <div style="flex:1; min-width:180px;">
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Customer</div>
                    <div style="color:#ffffff; font-size:1.1rem; font-weight:700; margin-top:0.2rem;">👤 {cust['NAME']}</div>
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.7rem; font-weight:700;">Phone</div>
                    <div style="color:#e2e8f0; font-size:0.95rem; margin-top:0.2rem;">{cust['PHONE']}</div>
                </div>
                <div style="flex:1; min-width:180px;">
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">CIBIL Score</div>
                    <div style="color:#60a5fa; font-size:1.2rem; font-weight:800; margin-top:0.2rem;">{cust['CIBIL_SCORE']}</div>
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.7rem; font-weight:700;">Tenure</div>
                    <div style="color:#e2e8f0; font-size:0.95rem; margin-top:0.2rem;">{cust['TENURE_YEARS']} years</div>
                </div>
                <div style="flex:1; min-width:180px;">
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Premium Paid</div>
                    <div style="color:#10b981; font-size:1.2rem; font-weight:800; margin-top:0.2rem;">₹{cust['TOTAL_PREMIUM_PAID']:,.0f}</div>
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.7rem; font-weight:700;">Churn Risk</div>
                    <div style="color:{churn_color}; font-size:1.1rem; font-weight:700; margin-top:0.2rem;">{churn_label} ({churn:.2f})</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        cust_claims = claims_df[claims_df["CUSTOMER_ID"] == selected_customer]
        cust_policies = policies_df[policies_df["CUSTOMER_ID"] == selected_customer]

        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                if len(cust_claims) > 0:
                    st.markdown("**Claims History**")
                    c_html = '<div class="table-scroll-wrapper"><table class="styled-table"><thead><tr><th>Claim ID</th><th>Hospital</th><th>Amount</th><th>Status</th></tr></thead><tbody>'
                    for _, r in cust_claims[["CLAIM_ID", "HOSPITAL_NAME", "CLAIM_AMOUNT", "TPA_APPROVAL_STATUS"]].iterrows():
                        s_col = "#10b981" if r["TPA_APPROVAL_STATUS"] == "Approved" else ("#f59e0b" if r["TPA_APPROVAL_STATUS"] == "Pending" else "#ef4444")
                        c_html += f'<tr><td>{r["CLAIM_ID"]}</td><td>{r["HOSPITAL_NAME"]}</td><td>₹{r["CLAIM_AMOUNT"]:,.0f}</td><td><span style="color:{s_col};font-weight:700;">{r["TPA_APPROVAL_STATUS"]}</span></td></tr>'
                    c_html += '</tbody></table></div>'
                    st.markdown(c_html, unsafe_allow_html=True)
                else:
                    st.info("No claims found.")
        with col2:
            with st.container():
                if len(cust_policies) > 0:
                    st.markdown("**Active Policies**")
                    p_html = '<div class="table-scroll-wrapper"><table class="styled-table"><thead><tr><th>Policy ID</th><th>Type</th><th>Sum Insured</th><th>Renewal</th></tr></thead><tbody>'
                    for _, r in cust_policies[["POLICY_ID", "POLICY_TYPE", "SUM_INSURED", "RENEWAL_DATE"]].iterrows():
                        p_html += f'<tr><td>{r["POLICY_ID"]}</td><td>{r["POLICY_TYPE"]}</td><td>₹{r["SUM_INSURED"]:,.0f}</td><td>{r["RENEWAL_DATE"]}</td></tr>'
                    p_html += '</tbody></table></div>'
                    st.markdown(p_html, unsafe_allow_html=True)
                else:
                    st.info("No policies found.")

        @st.cache_data(show_spinner=False)
        def get_customer_ai(cust_name, cibil, tenure, premium, churn, claims_info, policies_count):
            prompt = f"""You are a customer intelligence AI. Profile this health insurance customer in exactly 5 crisp points:

Customer: {cust_name}, CIBIL: {cibil}, Tenure: {tenure}yr, Premium: INR {premium:,.0f}, Churn Risk: {churn}, {claims_info}, Policies: {policies_count}.

Format: 5 bullet points: 1) **Persona** (happy/neutral/at-risk/unhappy + why), 2) **Value** (lifetime value assessment), 3) **Risk** (churn prevention action), 4) **Opportunity** (upsell suggestion), 5) **Approach** (how to engage). One sentence each."""
            return ai_complete(prompt)

        @st.cache_data(show_spinner=False)
        def get_conversation_ai(cust_name, conv_summary):
            prompt = f"""You are a customer relationship AI. Analyze this customer's past conversation history and provide deep insights in exactly 5 points:

Customer: {cust_name}
Conversation History: {conv_summary}

Format: 5 bullet points: 1) **Tone Pattern** (overall sentiment trend across interactions - improving/declining/stable), 2) **Pain Points** (recurring issues or frustrations), 3) **Preferences** (communication style, channel preference, what they value), 4) **Loyalty Signal** (indicators of retention or churn intent from conversations), 5) **Next Best Action** (personalized engagement recommendation based on conversation patterns). One sentence each."""
            return ai_complete(prompt)

        @st.cache_data(show_spinner=False)
        def get_last_touchpoint_ai(cust_name, last_convo_summary, last_convo_date, last_convo_channel, last_convo_topic, last_convo_sentiment):
            prompt = f"""You are a customer relationship AI. Analyze this customer's MOST RECENT conversation and provide a single concise alert for the agent who is about to call them.

Customer: {cust_name}
Last Conversation ({last_convo_date}, {last_convo_channel}, {last_convo_topic}, {last_convo_sentiment}): {last_convo_summary}

Answer in exactly 1 sentence: What is the one thing the agent MUST know before speaking to this customer right now? Focus on: any open/unresolved question, pending commitment, last emotional state, or follow-up the customer is expecting. Be specific and actionable."""
            return ai_complete(prompt)

        claims_info = f"{len(cust_claims)} claims totaling INR {cust_claims['CLAIM_AMOUNT'].sum():,.0f}" if len(cust_claims) > 0 else "No claims"
        cust_ai = get_customer_ai(
            cust['NAME'], cust['CIBIL_SCORE'], cust['TENURE_YEARS'],
            cust['TOTAL_PREMIUM_PAID'], cust['CHURN_RISK_SCORE'], claims_info, len(cust_policies)
        )

        cust_convos = conversations_df[conversations_df["CUSTOMER_ID"] == selected_customer]
        if len(cust_convos) > 0:
            conv_summary = "; ".join([
                f"{r['CONVERSATION_DATE']} ({r['CHANNEL']}, {r['TOPIC']}, {r['SENTIMENT']}): {r['SUMMARY']}"
                for _, r in cust_convos.iterrows()
            ])
        else:
            conv_summary = "No previous conversations recorded."
        conv_ai = get_conversation_ai(cust['NAME'], conv_summary)

        import re as _re_agent
        def _agent_md_to_html(text):
            text = text.replace("\\n", "\n").replace("\n", "<br>")
            text = _re_agent.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            return text

        ai_tab1, ai_tab2, ai_tab3 = st.tabs(["📋 Crisp Points", "💬 Conversation Insights", "🤖 AI Chat"])

        with ai_tab1:
            st.markdown(f"""<div style="background:linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
                border-radius:16px; padding:1.5rem 2rem; margin:0.5rem 0;
                border:1px solid rgba(129,140,248,0.3); box-shadow:0 4px 24px rgba(99,102,241,0.15);">
                <div style="color:#e0e7ff; font-size:1rem; line-height:1.8;">{_agent_md_to_html(cust_ai)}</div>
            </div>""", unsafe_allow_html=True)

        with ai_tab2:
            if len(cust_convos) > 0:
                last_convo = cust_convos.iloc[0]
                touchpoint_ai = get_last_touchpoint_ai(
                    cust['NAME'], last_convo['SUMMARY'], str(last_convo['CONVERSATION_DATE']),
                    last_convo['CHANNEL'], last_convo['TOPIC'], last_convo['SENTIMENT']
                )
                sentiment_icon = "🟢" if last_convo['SENTIMENT'] == "Positive" else ("🔴" if last_convo['SENTIMENT'] == "Negative" else "🟡")
                touchpoint_html = touchpoint_ai.replace("\\n", " ").replace("\n", " ")
                st.markdown(f"""<div style="background:linear-gradient(135deg, #7f1d1d 0%, #991b1b 50%, #b91c1c 100%);
                    border-radius:12px; padding:1rem 1.5rem; margin-bottom:0.8rem;
                    border:1px solid rgba(252,165,165,0.3); box-shadow:0 4px 16px rgba(127,29,29,0.3);">
                    <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem;">
                        <span style="font-size:1.2rem;">🚨</span>
                        <span style="color:#fca5a5; font-size:0.75rem; text-transform:uppercase; letter-spacing:1.5px; font-weight:700;">Last Touchpoint Alert</span>
                        <span style="margin-left:auto; color:#fca5a5; font-size:0.7rem;">{sentiment_icon} {last_convo['CONVERSATION_DATE']} via {last_convo['CHANNEL']}</span>
                    </div>
                    <div style="color:#ffffff; font-size:1rem; font-weight:600; line-height:1.5;">{touchpoint_html}</div>
                </div>""", unsafe_allow_html=True)

                st.markdown(f"""<div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                    border-radius:12px; padding:1rem 1.5rem; margin-bottom:0.8rem;
                    border:1px solid rgba(59,130,246,0.2);">
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700; margin-bottom:0.5rem;">Recent Interactions ({len(cust_convos)})</div>
                    <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
                        {"".join([f'<span style="background:{"#065f46" if r["SENTIMENT"]=="Positive" else ("#92400e" if r["SENTIMENT"]=="Negative" else "#1e3a5f")}; color:{"#6ee7b7" if r["SENTIMENT"]=="Positive" else ("#fbbf24" if r["SENTIMENT"]=="Negative" else "#93c5fd")}; padding:0.25rem 0.6rem; border-radius:20px; font-size:0.75rem; font-weight:600;">{r["TOPIC"]} • {r["SENTIMENT"]}</span>' for _, r in cust_convos.head(5).iterrows()])}
                    </div>
                </div>""", unsafe_allow_html=True)

            st.markdown(f"""<div style="background:linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
                border-radius:16px; padding:1.5rem 2rem; margin:0.5rem 0;
                border:1px solid rgba(129,140,248,0.3); box-shadow:0 4px 24px rgba(99,102,241,0.15);">
                <div style="color:#e0e7ff; font-size:1rem; line-height:1.8;">{_agent_md_to_html(conv_ai)}</div>
            </div>""", unsafe_allow_html=True)

        with ai_tab3:
            # Clear chat when customer changes
            if "chat_customer" not in st.session_state:
                st.session_state.chat_customer = selected_customer
            if st.session_state.chat_customer != selected_customer:
                st.session_state.chat_customer = selected_customer
                st.session_state.chat_messages = []

            if "chat_messages" not in st.session_state:
                st.session_state.chat_messages = []

            st.markdown(f"""<div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                border-radius:12px; border:1px solid rgba(59,130,246,0.2);
                padding:0.8rem 1.2rem; margin-bottom:0.5rem;">
                <span style="color:#60a5fa; font-weight:700; font-size:0.85rem;">🤖 AI Assistant</span>
                <span style="color:#64748b; font-size:0.8rem;"> — Ask anything about {cust['NAME']}</span>
            </div>""", unsafe_allow_html=True)

            chat_container = st.container()
            with chat_container:
                if len(st.session_state.chat_messages) == 0:
                    st.markdown(f"**🤖 Assistant:** Hi! I have full access to **{cust['NAME']}**'s profile, claims, policies, and conversation history. Ask me anything!")
                for msg in st.session_state.chat_messages:
                    prefix = "**🤖 Assistant:**" if msg["role"] == "assistant" else "**You:**"
                    st.markdown(f"{prefix} {msg['content']}")

            user_query = st.text_input("Ask about this customer...", key="agent_chat_input")
            if user_query and user_query != st.session_state.get("_last_chat_query", ""):
                st.session_state["_last_chat_query"] = user_query
                st.session_state.chat_messages.append({"role": "user", "content": user_query})

                cust_data = f"Name: {cust['NAME']}, Phone: {cust['PHONE']}, Email: {cust['EMAIL']}, CIBIL: {cust['CIBIL_SCORE']}, Tenure: {cust['TENURE_YEARS']}yr, Premium Paid: INR {cust['TOTAL_PREMIUM_PAID']:,.0f}, Churn Risk: {cust['CHURN_RISK_SCORE']}"

                claims_data = "No claims." if len(cust_claims) == 0 else "; ".join([
                    f"{r['CLAIM_ID']}: {r['HOSPITAL_NAME']}, INR {r['CLAIM_AMOUNT']:,.0f}, {r['TPA_APPROVAL_STATUS']}, SLA {r['SLA_MINUTES_ELAPSED']}min"
                    for _, r in cust_claims.iterrows()
                ])

                policies_data = "No policies." if len(cust_policies) == 0 else "; ".join([
                    f"{r['POLICY_ID']}: {r['POLICY_TYPE']}, Sum Insured INR {r['SUM_INSURED']:,.0f}, Renewal {r['RENEWAL_DATE']}"
                    for _, r in cust_policies.iterrows()
                ])

                convos_data = "No conversations." if len(cust_convos) == 0 else "; ".join([
                    f"{r['CONVERSATION_DATE']} ({r['CHANNEL']}, {r['TOPIC']}, {r['SENTIMENT']}): {r['SUMMARY']}"
                    for _, r in cust_convos.iterrows()
                ])

                chat_prompt = f"""You are an AI assistant for health insurance agents. Answer the agent's question about this customer concisely and helpfully.

CUSTOMER PROFILE: {cust_data}
CLAIMS: {claims_data}
POLICIES: {policies_data}
CONVERSATIONS: {convos_data}

AGENT'S QUESTION: {user_query}

Answer in 2-4 sentences max. Be specific with data points. If the answer isn't in the data, say so."""

                with st.spinner("Thinking..."):
                    response = ai_complete(chat_prompt)
                    formatted_resp = response.replace("\\n", "\n")
                st.session_state.chat_messages.append({"role": "assistant", "content": formatted_resp})
                st.rerun()

    with tab2:
        st.markdown('<div class="section-header"><strong>Claim Deep Dive</strong></div>', unsafe_allow_html=True)
        status_options = ["All"] + claims_df["TPA_APPROVAL_STATUS"].unique().tolist()
        selected_status = st.selectbox("Filter by Status", status_options, key="agent_claim_status_filter")
        filtered_claims = claims_df if selected_status == "All" else claims_df[claims_df["TPA_APPROVAL_STATUS"] == selected_status]
        claim_list = filtered_claims["CLAIM_ID"].tolist()
        if len(claim_list) == 0:
            st.info(f"No claims with status: {selected_status}")
        else:
            selected_claim = st.selectbox("Select Claim", claim_list, key="agent_claim_select")
            claim = filtered_claims[filtered_claims["CLAIM_ID"] == selected_claim].iloc[0]

            status_color = "#10b981" if claim['TPA_APPROVAL_STATUS'] == "Approved" else ("#f59e0b" if claim['TPA_APPROVAL_STATUS'] == "Pending" else "#ef4444")
            st.markdown(f"""
            <div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius:14px;
                padding:1.3rem 1.8rem; margin:0.8rem 0; border:1px solid rgba(59,130,246,0.2);
                box-shadow: 0 4px 20px rgba(15,23,42,0.3);">
                <div style="display:flex; gap:2rem; flex-wrap:wrap;">
                    <div style="flex:1; min-width:160px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Claim ID</div>
                        <div style="color:#ffffff; font-size:1rem; font-weight:600; margin-top:0.2rem;">{claim['CLAIM_ID']}</div>
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.7rem; font-weight:700;">Customer</div>
                        <div style="color:#e2e8f0; font-size:0.95rem; margin-top:0.2rem;">{claim['CUSTOMER_ID']}</div>
                    </div>
                    <div style="flex:1; min-width:160px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Hospital</div>
                        <div style="color:#ffffff; font-size:1rem; font-weight:600; margin-top:0.2rem;">{claim['HOSPITAL_NAME']}</div>
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.7rem; font-weight:700;">Amount</div>
                        <div style="color:#60a5fa; font-size:1.2rem; font-weight:800; margin-top:0.2rem;">₹{claim['CLAIM_AMOUNT']:,.0f}</div>
                    </div>
                    <div style="flex:1; min-width:160px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Status</div>
                        <div style="color:{status_color}; font-size:1.1rem; font-weight:700; margin-top:0.2rem;">{claim['TPA_APPROVAL_STATUS']}</div>
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.7rem; font-weight:700;">SLA Elapsed</div>
                        <div style="color:#fbbf24; font-size:1.1rem; font-weight:700; margin-top:0.2rem;">{claim['SLA_MINUTES_ELAPSED']:.0f} min</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            @st.cache_data(show_spinner=False)
            def get_agent_claim_ai(claim_id, policy_id, hospital, amount, status, sla, discharge):
                prompt = f"""You are a claims AI assistant for a front-line agent. Analyze this claim in exactly 5 crisp points:

Claim: {claim_id}, Policy: {policy_id}, Hospital: {hospital}, Amount: INR {amount:,.0f}, Status: {status}, SLA: {sla} min, Discharge: {discharge}.

Format: 5 bullet points: 1) **Nature** (routine/complex/urgent), 2) **Next Step** (specific action now), 3) **Verify** (documents to check), 4) **Talk Track** (what to tell customer), 5) **Risk** (any red flags). One sentence each."""
                return ai_complete(prompt)

            claim_ai = get_agent_claim_ai(
                claim['CLAIM_ID'], claim['POLICY_ID'], claim['HOSPITAL_NAME'],
                claim['CLAIM_AMOUNT'], claim['TPA_APPROVAL_STATUS'],
                claim['SLA_MINUTES_ELAPSED'], claim['DISCHARGE_STATUS']
            )

            st.markdown(f"""<div style="background:linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
                border-radius:16px; padding:1.5rem 2rem; margin:1rem 0;
                border:1px solid rgba(129,140,248,0.3); box-shadow:0 4px 24px rgba(99,102,241,0.15);">
                <div style="color:#e0e7ff; font-size:1rem; line-height:1.8;">{_agent_md_to_html(claim_ai)}</div>
            </div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="section-header"><strong>Ticket Resolution</strong></div>', unsafe_allow_html=True)
        ticket_list = tickets_df["TICKET_ID"].tolist()
        if len(ticket_list) > 0:
            selected_ticket = st.selectbox("Select Ticket", ticket_list, key="agent_ticket_select")
            ticket = tickets_df[tickets_df["TICKET_ID"] == selected_ticket].iloc[0]

            t_status_color = "#10b981" if ticket['STATUS'] == "RESOLVED" else ("#f59e0b" if ticket['STATUS'] == "IN_PROGRESS" else "#ef4444")
            t_notes = ticket['RESOLUTION_NOTES'] if ticket['RESOLUTION_NOTES'] and str(ticket['RESOLUTION_NOTES']) != 'None' else '—'
            st.markdown(f"""
            <div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius:14px;
                padding:1.3rem 1.8rem; margin:0.8rem 0; border:1px solid rgba(59,130,246,0.2);
                box-shadow: 0 4px 20px rgba(15,23,42,0.3);">
                <div style="display:flex; gap:2rem; flex-wrap:wrap;">
                    <div style="flex:1; min-width:200px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Issue</div>
                        <div style="color:#ffffff; font-size:1rem; font-weight:600; margin-top:0.2rem;">{ticket['ISSUE_TYPE']}</div>
                    </div>
                    <div style="flex:0 0 auto; min-width:140px;">
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Status</div>
                        <div style="color:{t_status_color}; font-size:1.1rem; font-weight:700; margin-top:0.2rem;">{ticket['STATUS']}</div>
                        <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; margin-top:0.7rem; font-weight:700;">Assigned</div>
                        <div style="color:#60a5fa; font-size:1rem; font-weight:600; margin-top:0.2rem;">{ticket['ASSIGNED_AGENT']}</div>
                    </div>
                </div>
                <div style="margin-top:0.8rem; border-top:1px solid rgba(59,130,246,0.15); padding-top:0.7rem;">
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Resolution Notes</div>
                    <div style="color:#cbd5e1; font-size:0.9rem; margin-top:0.2rem;">{t_notes}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            @st.cache_data(show_spinner=False)
            def get_agent_ticket_ai(ticket_id, issue, status, notes):
                prompt = f"""You are a service AI helping a front-line agent. Give resolution guidance in exactly 4 crisp points:

Ticket: {ticket_id}, Issue: {issue}, Status: {status}, Notes: {notes}.

Format: 4 numbered points: 1) **Resolution Steps** (what to do), 2) **Customer Script** (what to say), 3) **Timeline** (expected resolution), 4) **Follow-up** (next actions). One sentence each."""
                return ai_complete(prompt)

            ticket_ai = get_agent_ticket_ai(
                ticket['TICKET_ID'], ticket['ISSUE_TYPE'],
                ticket['STATUS'], t_notes
            )

            st.markdown(f"""<div style="background:linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
                border-radius:16px; padding:1.5rem 2rem; margin:1rem 0;
                border:1px solid rgba(129,140,248,0.3); box-shadow:0 4px 24px rgba(99,102,241,0.15);">
                <div style="color:#e0e7ff; font-size:1rem; line-height:1.8;">{_agent_md_to_html(ticket_ai)}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.info("No tickets available.")

    with tab4:
        import time as _time
        import json as _json
        import re as _re

        st.markdown('<div class="section-header"><strong>Audio Call Transcription & Live AI Insights</strong></div>', unsafe_allow_html=True)
        st.markdown("Upload a call recording to transcribe with speaker diarization and get progressive AI insights as the conversation unfolds.")

        # Demo transcript for testing (trimmed to ~100 seconds)
        DEMO_TRANSCRIPT = {
            "audio_duration": 98.0,
            "segments": [
                {"speaker_label": "SPEAKER_00", "text": "Good morning, thank you for calling Star Health Insurance. My name is Vishal. How may I assist you today?", "start": 0.0, "end": 6.5},
                {"speaker_label": "SPEAKER_01", "text": "Hello Vishal, this is Rajesh Sharma. I'm calling about my claim. I was admitted to Apollo Hospital last month for a cardiac procedure and my claim has been pending for 3 weeks now.", "start": 7.0, "end": 18.0},
                {"speaker_label": "SPEAKER_00", "text": "I'm sorry to hear about the delay, Mr. Sharma. Let me pull up your claim details. I can see the claim filed for cardiac catheterization at Apollo Hospital, amount of 4.5 lakhs.", "start": 19.0, "end": 30.0},
                {"speaker_label": "SPEAKER_01", "text": "Yes that's correct. The hospital told me everything was pre-approved but now your TPA is asking for additional documents. This is very frustrating.", "start": 31.0, "end": 40.0},
                {"speaker_label": "SPEAKER_00", "text": "I completely understand your frustration. Let me check what documents the TPA has flagged. They need a detailed discharge summary with procedure codes and the surgeon's notes.", "start": 41.0, "end": 52.0},
                {"speaker_label": "SPEAKER_01", "text": "But my policy covers cardiac procedures up to 10 lakhs. Why is this being delayed? I've been paying premiums for 6 years without a single claim.", "start": 53.0, "end": 63.0},
                {"speaker_label": "SPEAKER_00", "text": "You're absolutely right. The issue is that the discharge summary doesn't include the ICD-10 procedure codes required for claims above 3 lakhs. Let me help resolve this today.", "start": 64.0, "end": 76.0},
                {"speaker_label": "SPEAKER_01", "text": "I'm a senior citizen with a heart condition. Can't you call the hospital directly? I'm considering switching to another insurer.", "start": 77.0, "end": 86.0},
                {"speaker_label": "SPEAKER_00", "text": "Mr. Sharma, I'll escalate this to priority processing, coordinate with Apollo Hospital for the codes, and ensure your claim is processed within 48 hours. You'll receive an SMS confirmation within the hour.", "start": 87.0, "end": 98.0},
            ]
        }

        use_demo = st.button("🎬 Run Demo Call", key="demo_btn_agent", type="primary")

        # Determine mode
        run_transcription = False
        transcript_json = None
        file_name = "demo_call.wav"

        if use_demo:
            transcript_json = DEMO_TRANSCRIPT
            run_transcription = True

        # --- Common display logic for both demo and real transcription ---
        if run_transcription and transcript_json:
            segments = transcript_json.get("segments", [])
            audio_duration = transcript_json.get("audio_duration", 0)
            full_text = transcript_json.get("text", "")

            if not segments and full_text:
                segments = [{"speaker_label": "SPEAKER_00", "text": full_text, "start": 0, "end": audio_duration}]

            # Live audio waveform animation
            st.markdown("""
            <style>
            @keyframes wave-bar {
                0%, 100% { height: 8px; }
                50% { height: 28px; }
            }
            .live-audio-bar {
                display: flex; align-items: center; gap: 0.8rem;
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                border-radius: 12px; padding: 1rem 1.5rem; margin-bottom: 1rem;
                border: 1px solid rgba(59,130,246,0.3);
            }
            .wave-container { display: flex; align-items: center; gap: 3px; height: 32px; }
            .wave-bar {
                width: 4px; border-radius: 4px;
                background: linear-gradient(180deg, #3b82f6, #60a5fa);
                animation: wave-bar 0.8s ease-in-out infinite;
            }
            .wave-bar:nth-child(1) { animation-delay: 0s; height: 12px; }
            .wave-bar:nth-child(2) { animation-delay: 0.1s; height: 20px; }
            .wave-bar:nth-child(3) { animation-delay: 0.2s; height: 16px; }
            .wave-bar:nth-child(4) { animation-delay: 0.3s; height: 24px; }
            .wave-bar:nth-child(5) { animation-delay: 0.4s; height: 10px; }
            .wave-bar:nth-child(6) { animation-delay: 0.15s; height: 18px; }
            .wave-bar:nth-child(7) { animation-delay: 0.25s; height: 22px; }
            .wave-bar:nth-child(8) { animation-delay: 0.35s; height: 14px; }
            .live-badge {
                background: #ef4444; color: white; font-size: 0.7rem;
                padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 700;
                text-transform: uppercase; letter-spacing: 1px;
                animation: pulse-glow 1.5s ease-in-out infinite;
            }
            .live-timer { color: #94a3b8; font-size: 0.85rem; font-family: monospace; }
            </style>
            """, unsafe_allow_html=True)

            live_header = st.empty()
            st.divider()
            st.markdown("#### 🎬 Live Call Playback & Proactive AI Agent")

            # Speaker colors
            speaker_map = {
                "SPEAKER_00": ("🧑‍💼 Agent", "#3b82f6"),
                "SPEAKER_01": ("👤 Customer", "#10b981"),
                "SPEAKER_02": ("👥 Speaker 3", "#f59e0b"),
                "SPEAKER_03": ("👥 Speaker 4", "#ef4444"),
            }

            cumulative_text = ""
            last_insight = None

            for i, seg in enumerate(segments):
                speaker = seg.get("speaker_label", "SPEAKER_00")
                text = seg.get("text", "").strip()
                start = seg.get("start", 0)
                end = seg.get("end", 0)
                if not text:
                    continue

                label, color = speaker_map.get(speaker, (f"🗣️ {speaker}", "#94a3b8"))

                # Update live header with current time
                elapsed_min = int(end) // 60
                elapsed_sec = int(end) % 60
                live_header.markdown(f"""
                <div class="live-audio-bar">
                    <span class="live-badge">● LIVE</span>
                    <div class="wave-container">
                        <div class="wave-bar"></div><div class="wave-bar"></div>
                        <div class="wave-bar"></div><div class="wave-bar"></div>
                        <div class="wave-bar"></div><div class="wave-bar"></div>
                        <div class="wave-bar"></div><div class="wave-bar"></div>
                    </div>
                    <span class="live-timer">{elapsed_min:02d}:{elapsed_sec:02d} / {int(audio_duration)//60:02d}:{int(audio_duration)%60:02d}</span>
                    <span style="color:#e2e8f0; font-size:0.85rem; margin-left:auto;">Speaking: <strong style="color:{color};">{label}</strong></span>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div style="margin:0.5rem 0; padding:0.8rem 1.2rem; border-left:4px solid {color};
                            background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                            border-radius:8px; border:1px solid rgba({",".join([str(int(color[i:i+2],16)) for i in (1,3,5)])},0.2);">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <strong style="color:{color}; font-size:0.9rem;">{label}</strong>
                        <span style="color:#94a3b8; font-size:0.7rem; font-family:monospace;">{start:.1f}s → {end:.1f}s</span>
                    </div>
                    <p style="margin:0.4rem 0 0 0; color:#ffffff; line-height:1.6; font-size:0.95rem;">{text}</p>
                </div>
                """, unsafe_allow_html=True)

                cumulative_text += f"{label}: {text}\n"

                # Proactive AI: when customer mentions data (claim, policy, amount) or asks a question
                is_customer = speaker in ("SPEAKER_01", "SPEAKER_02", "SPEAKER_03")
                needs_data = is_customer and any(kw in text.lower() for kw in ["claim", "policy", "amount", "premium", "status", "pending", "approved", "rejected", "how much", "my plan", "coverage", "lakhs", "lakh"])
                is_analysis_point = (is_customer and (i % 3 == 2)) or (i == len(segments) - 1)

                if needs_data and not is_analysis_point:
                    try:
                        data_prompt = f"""You are a real-time AI copilot for a health insurance agent on a live call. The customer just said: "{text}"

Based on this, proactively provide the agent with relevant data they might need RIGHT NOW to respond. Format as a quick data card:
- **Relevant Data:** (pull specific numbers/status/dates the agent needs)
- **Suggested Response:** (one sentence the agent can say)

Keep it to 2-3 lines max. Be specific and actionable."""
                        data_response = ai_complete(data_prompt)
                        data_html = data_response.replace("\\n", "<br>").replace("\n", "<br>")
                        st.markdown(f"""<div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                            border-radius:10px; padding:0.8rem 1.2rem; margin:0.3rem 0 0.5rem 2rem;
                            border:1px solid rgba(96,165,250,0.3); border-left:4px solid #f59e0b;">
                            <div style="color:#fbbf24; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px;">⚡ AI Copilot — Proactive Data</div>
                            <div style="color:#e2e8f0; font-size:0.88rem; margin-top:0.3rem; line-height:1.6;">{data_html}</div>
                        </div>""", unsafe_allow_html=True)
                    except Exception:
                        pass

                if is_analysis_point:
                    try:
                        insight_prompt = f"""You are a health insurance call analytics AI monitoring a live call. Provide real-time analysis:
1) **Sentiment** (positive/neutral/negative with brief reason)
2) **Red Flags** (compliance, fraud, or escalation concerns - or "None")
3) **Recommended Action** (next best action for the agent)
4) **IRDAI Compliance** (any regulatory concern - or "Compliant")

Keep each point to one sentence. Transcript so far:
{cumulative_text}"""
                        insight_response = ai_complete(insight_prompt)
                        last_insight = insight_response
                        insight_html = insight_response.replace("\\n", "<br>").replace("\n", "<br>")

                        st.markdown(f"""<div style="background:linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
                            border-radius:10px; padding:0.8rem 1.2rem; margin:0.5rem 0;
                            border:1px solid rgba(129,140,248,0.3);">
                            <div style="color:#a5b4fc; font-size:0.75rem; font-weight:700; text-transform:uppercase; letter-spacing:1px;">🧠 AI Analysis — {end:.0f}s</div>
                            <div style="color:#e0e7ff; font-size:0.88rem; margin-top:0.3rem; line-height:1.6;">{insight_html}</div>
                        </div>""", unsafe_allow_html=True)
                    except Exception:
                        pass

                # Progressive delay simulating real-time
                if i < len(segments) - 1:
                    segment_duration = end - start
                    _time.sleep(min(max(segment_duration * 0.15, 0.5), 2.0))

            # Call ended
            live_header.markdown(f"""
            <div class="live-audio-bar" style="border-color:rgba(16,185,129,0.4);">
                <span style="background:#10b981; color:white; font-size:0.7rem; padding:0.2rem 0.5rem; border-radius:4px; font-weight:700;">✓ ENDED</span>
                <span class="live-timer">{int(audio_duration)//60:02d}:{int(audio_duration)%60:02d} / {int(audio_duration)//60:02d}:{int(audio_duration)%60:02d}</span>
                <span style="color:#10b981; font-size:0.85rem; margin-left:auto; font-weight:600;">Call Complete</span>
            </div>
            """, unsafe_allow_html=True)

            st.divider()
            st.markdown("#### 📋 Final Call Summary")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""<div style="background:linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                    border-radius:12px; padding:1rem 1.5rem; border:1px solid rgba(59,130,246,0.2);">
                    <div style="color:#93c5fd; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Call Stats</div>
                    <div style="color:#e2e8f0; margin-top:0.5rem; line-height:1.8;">
                        <strong>Duration:</strong> {audio_duration:.0f} seconds<br>
                        <strong>Segments:</strong> {len(segments)}<br>
                        <strong>File:</strong> {file_name}
                    </div>
                </div>""", unsafe_allow_html=True)
            with col2:
                if last_insight:
                    final_html = last_insight.replace("\\n", "<br>").replace("\n", "<br>")
                    st.markdown(f"""<div style="background:linear-gradient(135deg, #1e1b4b 0%, #312e81 100%);
                        border-radius:12px; padding:1rem 1.5rem; border:1px solid rgba(129,140,248,0.3);">
                        <div style="color:#a5b4fc; font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; font-weight:700;">Final AI Assessment</div>
                        <div style="color:#e0e7ff; margin-top:0.5rem; font-size:0.88rem; line-height:1.6;">{final_html}</div>
                    </div>""", unsafe_allow_html=True)

            with st.expander("📜 View Full Transcript"):
                st.text(cumulative_text)

        elif not use_demo:
            st.info("Click 'Run Demo Call' above to see a live call transcription and AI analysis demo.")



# --- MAIN ROUTING ---
if "Home" in page:
    render_home()
elif "Strategic" in page:
    render_manager_view()
elif "Claims" in page:
    render_supervisor_view()
elif "Service" in page:
    render_agent_view()
