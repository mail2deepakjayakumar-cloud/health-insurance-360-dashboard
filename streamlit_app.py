import streamlit as st
import os
import time
import json
import re

st.set_page_config(page_title="Health Insurance 360", page_icon="🏥", layout="wide")

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""<style>
/* Sidebar */
section[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 50%, #334155 100%) !important;
}
section[data-testid="stSidebar"] * { color: #ffffff !important; }
section[data-testid="stSidebar"] .stSelectbox > div > div {
    background: rgba(37,99,235,0.12) !important;
    border: 2px solid #3b82f6 !important; border-radius: 10px !important;
}
section[data-testid="stSidebar"] .stSelectbox > div > div > div[data-baseweb="select"] > div {
    -webkit-text-fill-color: #60a5fa !important; color: #60a5fa !important; font-weight: 600 !important;
}
section[data-testid="stSidebar"] .stSelectbox svg { fill: #3b82f6 !important; color: #3b82f6 !important; }
section[data-testid="stSidebar"] .stRadio label {
    background: rgba(37,99,235,0.06) !important; border-radius: 8px !important;
    padding: 0.5rem 0.9rem !important; transition: all 0.3s !important;
    border: 1px solid transparent !important;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(37,99,235,0.15) !important; border-color: rgba(59,130,246,0.4) !important;
    transform: translateX(4px) !important;
}
/* AI response boxes */
.ai-response-box {
    background: linear-gradient(135deg, rgba(37,99,235,0.08), rgba(59,130,246,0.06));
    border-left: 5px solid #3b82f6; border-radius: 12px; padding: 1.2rem 1.5rem;
    box-shadow: 0 4px 12px rgba(37,99,235,0.1); margin: 0.5rem 0;
}
.ai-response-box h4 { color: #3b82f6 !important; }
/* KPI header banner */
.kpi-header {
    background: linear-gradient(135deg, #111827, #1f2937, #374151); border-radius: 16px;
    box-shadow: 0 8px 32px rgba(17,24,39,0.6); border: 1px solid rgba(96,165,250,0.15);
    padding: 1.5rem 2rem; position: relative; overflow: hidden; margin-bottom: 1.5rem;
}
.kpi-header::before {
    content:''; position:absolute; top:0; left:0; right:0; bottom:0;
    background: radial-gradient(ellipse at 30% 50%, rgba(96,165,250,0.08), transparent 70%);
}
.kpi-header h2 { color: #ffffff !important; margin:0; position:relative; z-index:1; }
.kpi-header p { color: #93c5fd !important; margin:0; position:relative; z-index:1; }
/* Welcome banner */
.welcome-banner {
    background: linear-gradient(135deg, #0f172a, #1e293b, #334155); border-radius: 16px;
    box-shadow: 0 8px 32px rgba(15,23,42,0.5); border: 1px solid rgba(96,165,250,0.15);
    padding: 2rem 2.5rem; text-align: center; margin-bottom: 1.5rem;
}
.welcome-banner h1 { color: #ffffff !important; font-size: 2.5rem !important; }
.welcome-banner p { color: #93c5fd !important; }
/* Section headers */
.section-header {
    background: linear-gradient(90deg, rgba(37,99,235,0.08), rgba(59,130,246,0.03));
    border-left: 4px solid #3b82f6; border-radius: 0 10px 10px 0; padding: 0.8rem 1.2rem; margin: 1rem 0;
}
/* Tab bar */
.stTabs [data-baseweb="tab-list"] {
    background: linear-gradient(135deg, #111827, #1f2937) !important; border-radius: 14px !important;
    padding: 6px !important; box-shadow: 0 4px 16px rgba(17,24,39,0.5) !important; gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    color: #9ca3af !important; border-radius: 10px !important; padding: 10px 20px !important;
    font-weight: 600 !important; background: transparent !important;
}
.stTabs [data-baseweb="tab"]:hover { background: rgba(96,165,250,0.1) !important; color: #bfdbfe !important; }
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #2563eb, #3b82f6) !important; color: #ffffff !important;
    box-shadow: 0 4px 12px rgba(37,99,235,0.4) !important;
}
.stTabs [data-baseweb="tab-highlight"] { display: none !important; }
.stTabs [data-baseweb="tab-border"] { display: none !important; }
/* Styled HTML tables */
.table-scroll-wrapper { max-height: 220px; overflow-y: auto; border-radius: 12px; }
.styled-table { width: 100%; border-collapse: separate; border-spacing: 0; }
.styled-table thead { position: sticky; top: 0; z-index: 1; }
.styled-table thead tr { background: linear-gradient(135deg, #1e293b, #334155); }
.styled-table th {
    color: #e0f2fe; font-weight: 700; font-size: 0.82rem; text-transform: uppercase;
    letter-spacing: 0.8px; padding: 0.75rem 1rem; border-bottom: 2px solid #3b82f6;
}
.styled-table tbody tr:nth-child(odd) { background: linear-gradient(135deg, #eff6ff, #f8fafc); }
.styled-table tbody tr:nth-child(even) { background: linear-gradient(135deg, #dbeafe, #eff6ff); }
.styled-table tbody tr:hover { background: linear-gradient(135deg, #bfdbfe, #dbeafe); }
.styled-table td {
    color: #1e293b; font-size: 0.88rem; padding: 0.65rem 1rem; border-bottom: 1px solid #e2e8f0;
}
/* Detail cards */
.detail-card {
    background: linear-gradient(135deg, #0f172a, #1e293b); border-radius: 14px;
    padding: 1.3rem 1.8rem; border: 1px solid rgba(59,130,246,0.2);
    box-shadow: 0 4px 20px rgba(15,23,42,0.3); margin: 0.5rem 0;
}
.detail-card .label { color: #93c5fd; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; }
.detail-card .value { color: #ffffff; }
.detail-card .amount { color: #60a5fa; font-size: 1.2rem; font-weight: 800; }
.detail-card .sla { color: #fbbf24; }
/* AI insight card */
.ai-insight-card {
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%); border-radius: 16px;
    padding: 1.5rem 2rem; border: 1px solid rgba(129,140,248,0.3);
    box-shadow: 0 4px 24px rgba(99,102,241,0.15); margin: 0.5rem 0;
}
.ai-insight-card p { color: #e0e7ff !important; font-size: 1rem; line-height: 1.8; margin: 0; }
.ai-insight-card strong { color: #fbbf24 !important; }
/* Home gradient cards */
.home-kpi-row { display:flex; gap:1rem; margin-bottom:1rem; flex-wrap:wrap; }
.home-kpi-card {
    flex:1; min-width:180px; border-radius:14px; padding:1.3rem 1.5rem; position:relative; overflow:hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
}
.home-kpi-card::before {
    content:''; position:absolute; top:-30%; right:-30%; width:120px; height:120px;
    background: radial-gradient(circle, rgba(255,255,255,0.12), transparent 70%); border-radius:50%;
}
.home-kpi-card .icon { font-size:1.8rem; margin-bottom:0.3rem; }
.home-kpi-card .val { color:#fff; font-size:1.8rem; font-weight:800; }
.home-kpi-card .lbl { color:rgba(255,255,255,0.85); font-size:0.78rem; text-transform:uppercase; letter-spacing:0.8px; font-weight:600; }
.home-kpi-card .badge {
    display:inline-block; margin-top:0.4rem; padding:0.15rem 0.6rem; border-radius:20px;
    font-size:0.72rem; font-weight:700;
}
.hkpi-1 { background: linear-gradient(135deg, #1e3a5f, #2563eb); }
.hkpi-2 { background: linear-gradient(135deg, #1e4035, #059669); }
.hkpi-3 { background: linear-gradient(135deg, #4a1d6b, #9333ea); }
.hkpi-4 { background: linear-gradient(135deg, #6b3a1d, #ea580c); }
.hkpi-5 { background: linear-gradient(135deg, #1d4e6b, #0891b2); }
.hkpi-6 { background: linear-gradient(135deg, #4a1d4a, #db2777); }
.hkpi-7 { background: linear-gradient(135deg, #1d3a6b, #2563eb); }
.hkpi-8 { background: linear-gradient(135deg, #3a1d1d, #dc2626); }
</style>""", unsafe_allow_html=True)

# ── Connection & Helpers ────────────────────────────────────────────────────
try:
    conn = st.connection("snowflake", ttl=os.getenv("SNOWFLAKE_CONNECTION_TTL"))
    session = conn.session()
except AttributeError:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()

def ai_complete(prompt):
    escaped = prompt.replace("'", "\\'")
    result = session.sql(f"SELECT SNOWFLAKE.CORTEX.COMPLETE('llama3.1-70b', '{escaped}') AS RESPONSE").collect()
    return result[0]["RESPONSE"]

def status_color(s):
    s = str(s).upper()
    if s in ("APPROVED", "RESOLVED", "DISCHARGED"): return "#10b981"
    if s in ("PENDING", "IN_PROGRESS", "IN TREATMENT", "ADMITTED"): return "#f59e0b"
    if s in ("REJECTED", "OPEN"): return "#ef4444"
    if s == "PARTIALLY APPROVED": return "#8b5cf6"
    return "#64748b"

def _agent_md_to_html(text):
    text = text.replace("\\n", "<br>").replace("\n", "<br>")
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return text

# ── Data Loaders ────────────────────────────────────────────────────────────
@st.cache_data(ttl=300)
def load_customers():
    return session.sql("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.CUSTOMERS").to_pandas()

@st.cache_data(ttl=300)
def load_policies():
    return session.sql("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.POLICIES").to_pandas()

@st.cache_data(ttl=300)
def load_claims():
    return session.sql("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.CLAIMS").to_pandas()

@st.cache_data(ttl=300)
def load_tickets():
    return session.sql("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.SERVICE_TICKETS").to_pandas()

@st.cache_data(ttl=300)
def load_agents():
    return session.sql("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.AGENTS").to_pandas()

@st.cache_data(ttl=300)
def load_conversations():
    return session.sql("SELECT * FROM HEALTH_INSURANCE_360.PUBLIC.CUSTOMER_CONVERSATIONS").to_pandas()

customers = load_customers()
policies = load_policies()
claims = load_claims()
tickets = load_tickets()
agents_df = load_agents()
conversations = load_conversations()

# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🏥 Health Insurance 360")
    st.markdown("---")
    agent_options = ["-- Select Agent --"] + agents_df["AGENT_NAME"].tolist()
    selected_agent = st.selectbox("Login As", agent_options, label_visibility="collapsed")

    if selected_agent == "-- Select Agent --":
        st.info("Please select an agent to login")

# ── Default State (no login) ───────────────────────────────────────────────
if selected_agent == "-- Select Agent --":
    st.markdown("""<div class="welcome-banner">
        <h1>🏥 Health Insurance 360</h1>
        <p>AI-Powered Insurance Operations Dashboard</p>
        <p style="color:#64748b; font-size:0.9rem;">Select an agent from the sidebar to begin</p>
    </div>""", unsafe_allow_html=True)

    total_cust = len(customers)
    active_pol = len(policies[policies["ACTIVE_STATUS"] == "TRUE"])
    total_claims = len(claims)
    open_tickets = len(tickets[tickets["STATUS"] == "OPEN"])

    st.markdown(f"""<div class="home-kpi-row">
        <div class="home-kpi-card hkpi-1"><div class="icon">👥</div><div class="val">{total_cust}</div><div class="lbl">Total Customers</div></div>
        <div class="home-kpi-card hkpi-2"><div class="icon">📋</div><div class="val">{active_pol}</div><div class="lbl">Active Policies</div></div>
        <div class="home-kpi-card hkpi-3"><div class="icon">🏥</div><div class="val">{total_claims}</div><div class="lbl">Total Claims</div></div>
        <div class="home-kpi-card hkpi-5"><div class="icon">🎫</div><div class="val">{open_tickets}</div><div class="lbl">Open Tickets</div></div>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        status_counts = claims["TPA_APPROVAL_STATUS"].value_counts().reset_index()
        status_counts.columns = ["Status", "Count"]
        st.bar_chart(status_counts, x="Status", y="Count")
    with c2:
        ticket_counts = tickets["STATUS"].value_counts().reset_index()
        ticket_counts.columns = ["Status", "Count"]
        st.bar_chart(ticket_counts, x="Status", y="Count")
    st.stop()

# ── Post-Login Setup ────────────────────────────────────────────────────────
agent_row = agents_df[agents_df["AGENT_NAME"] == selected_agent].iloc[0]
role = agent_row["ROLE_LEVEL"]
dept = agent_row["DEPARTMENT"]

with st.sidebar:
    role_colors = {"MANAGER": "#3b82f6", "SUPERVISOR": "#f59e0b", "AGENT": "#10b981"}
    st.markdown(f'<span style="background:{role_colors.get(role,"#64748b")}; color:#fff; padding:0.3rem 0.8rem; border-radius:8px; font-weight:700; font-size:0.85rem;">{role}</span>', unsafe_allow_html=True)
    st.caption(f"Department: {dept}")
    st.markdown("---")

    if role == "MANAGER":
        nav_options = ["📈 Strategic Analytics", "🏠 Home"]
    elif role == "SUPERVISOR":
        nav_options = ["📋 Claims & Tickets", "🏠 Home"]
    else:
        nav_options = ["🎧 Service Console", "🏠 Home"]

    page = st.radio("Navigation", nav_options, label_visibility="collapsed")


# ═══════════════════════════════════════════════════════════════════════════
# HOME PAGE
# ═══════════════════════════════════════════════════════════════════════════
def render_home():
    st.markdown("""<div class="kpi-header">
        <h2>🏠 Operations Dashboard</h2>
        <p>Real-time overview of Health Insurance 360 operations</p>
    </div>""", unsafe_allow_html=True)

    total_cust = len(customers)
    active_pol = len(policies[policies["ACTIVE_STATUS"] == "TRUE"])
    total_claims = len(claims)
    total_tickets = len(tickets)
    pending_claims = len(claims[claims["TPA_APPROVAL_STATUS"] == "Pending"])
    approved_claims = len(claims[claims["TPA_APPROVAL_STATUS"] == "Approved"])
    rejected_claims = len(claims[claims["TPA_APPROVAL_STATUS"] == "Rejected"])
    total_claim_val = claims["CLAIM_AMOUNT"].sum()
    approval_pct = round(approved_claims / total_claims * 100, 1) if total_claims > 0 else 0
    rejection_pct = round(rejected_claims / total_claims * 100, 1) if total_claims > 0 else 0
    claim_lakhs = round(float(total_claim_val) / 100000, 1)

    st.markdown(f"""<div class="home-kpi-row">
        <div class="home-kpi-card hkpi-1"><div class="icon">👥</div><div class="val">{total_cust}</div><div class="lbl">Total Customers</div></div>
        <div class="home-kpi-card hkpi-2"><div class="icon">📋</div><div class="val">{active_pol}</div><div class="lbl">Active Policies</div></div>
        <div class="home-kpi-card hkpi-3"><div class="icon">🏥</div><div class="val">{total_claims}</div><div class="lbl">Total Claims</div></div>
        <div class="home-kpi-card hkpi-4"><div class="icon">🎫</div><div class="val">{total_tickets}</div><div class="lbl">Service Tickets</div></div>
    </div>
    <div class="home-kpi-row">
        <div class="home-kpi-card hkpi-5"><div class="icon">⏳</div><div class="val">{pending_claims}</div><div class="lbl">Pending Claims</div><div class="badge" style="background:rgba(251,191,36,0.2);color:#fbbf24;">Action Needed</div></div>
        <div class="home-kpi-card hkpi-2"><div class="icon">✅</div><div class="val">{approved_claims}</div><div class="lbl">Approved Claims</div><div class="badge" style="background:rgba(16,185,129,0.2);color:#86efac;">{approval_pct}%</div></div>
        <div class="home-kpi-card hkpi-8"><div class="icon">❌</div><div class="val">{rejected_claims}</div><div class="lbl">Rejected Claims</div><div class="badge" style="background:rgba(239,68,68,0.2);color:#fca5a5;">{rejection_pct}%</div></div>
        <div class="home-kpi-card hkpi-6"><div class="icon">💰</div><div class="val">₹{claim_lakhs}L</div><div class="lbl">Total Claim Value</div></div>
    </div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        with st.container():
            st.markdown("**Claims by Status**")
            sc = claims["TPA_APPROVAL_STATUS"].value_counts().reset_index()
            sc.columns = ["Status", "Count"]
            st.bar_chart(sc, x="Status", y="Count")
    with c2:
        with st.container():
            st.markdown("**Top Claims by Amount**")
            top_cl = claims.nlargest(8, "CLAIM_AMOUNT")[["CLAIM_ID", "HOSPITAL_NAME", "CLAIM_AMOUNT", "TPA_APPROVAL_STATUS"]]
            rows_html = ""
            for _, r in top_cl.iterrows():
                sc2 = status_color(r["TPA_APPROVAL_STATUS"])
                rows_html += f'<tr><td>{r["CLAIM_ID"]}</td><td>{r["HOSPITAL_NAME"]}</td><td style="font-weight:700;color:#3b82f6;">₹{r["CLAIM_AMOUNT"]:,.0f}</td><td><span style="color:{sc2};font-weight:700;">{r["TPA_APPROVAL_STATUS"]}</span></td></tr>'
            st.markdown(f"""<div class="table-scroll-wrapper"><table class="styled-table">
                <thead><tr><th>Claim ID</th><th>Hospital</th><th>Amount</th><th>Status</th></tr></thead>
                <tbody>{rows_html}</tbody></table></div>""", unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        with st.container():
            st.markdown("**Ticket Pipeline**")
            tc = tickets["STATUS"].value_counts().reset_index()
            tc.columns = ["Status", "Count"]
            st.bar_chart(tc, x="Status", y="Count")
    with c4:
        with st.container():
            st.markdown("**Claims by Hospital (Top 8)**")
            hc = claims["HOSPITAL_NAME"].value_counts().head(8).reset_index()
            hc.columns = ["Hospital", "Count"]
            st.bar_chart(hc, x="Count", y="Hospital")


# ═══════════════════════════════════════════════════════════════════════════
# MANAGER VIEW
# ═══════════════════════════════════════════════════════════════════════════
def render_manager():
    st.markdown("""<div class="kpi-header">
        <h2>📈 Strategic Analytics & AI Insights</h2>
        <p>Executive-level intelligence for data-driven decisions</p>
    </div>""", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📊 YoY Metrics", "🤖 AI Strategy Hub"])

    with tab1:
        total_cust = len(customers)
        total_claims_ct = len(claims)
        avg_claim = float(claims["CLAIM_AMOUNT"].mean()) if total_claims_ct > 0 else 0
        approved_ct = len(claims[claims["TPA_APPROVAL_STATUS"] == "Approved"])
        approval_rate = round(approved_ct / total_claims_ct * 100, 1) if total_claims_ct > 0 else 0
        avg_sla = float(claims["SLA_MINUTES_ELAPSED"].mean()) if total_claims_ct > 0 else 0
        total_prem_cr = round(float(customers["TOTAL_PREMIUM_PAID"].sum()) / 10000000, 2)

        st.markdown("""<style>
        .yoy-row { display:flex; gap:1rem; margin-bottom:1rem; flex-wrap:wrap; }
        .yoy-card {
            flex:1; min-width:180px; border-radius:14px; padding:1.3rem 1.5rem; position:relative; overflow:hidden;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        .yoy-card::before {
            content:''; position:absolute; top:-30%; right:-20%; width:100px; height:100px;
            background: radial-gradient(circle, rgba(255,255,255,0.1), transparent 70%); border-radius:50%;
        }
        .yoy-card .val { color:#fff; font-size:1.8rem; font-weight:800; position:relative; }
        .yoy-card .lbl { color:rgba(255,255,255,0.85); font-size:0.8rem; text-transform:uppercase; letter-spacing:0.8px; font-weight:600; position:relative; }
        .yoy-card .delta {
            display:inline-block; margin-top:0.4rem; padding:0.15rem 0.6rem; border-radius:20px;
            font-size:0.72rem; font-weight:700; background:rgba(255,255,255,0.15); color:#86efac; position:relative;
        }
        </style>""", unsafe_allow_html=True)

        st.markdown(f"""<div class="yoy-row">
            <div class="yoy-card" style="background:linear-gradient(135deg,#1e3a5f,#2563eb);">
                <div class="val">{total_cust}</div><div class="lbl">Total Customers</div><div class="delta">▲ 15% YoY</div></div>
            <div class="yoy-card" style="background:linear-gradient(135deg,#1e4035,#059669);">
                <div class="val">{total_claims_ct}</div><div class="lbl">Claims Processed</div><div class="delta">▲ 8% YoY</div></div>
            <div class="yoy-card" style="background:linear-gradient(135deg,#4a1d6b,#9333ea);">
                <div class="val">₹{avg_claim:,.0f}</div><div class="lbl">Avg Claim Amount</div><div class="delta">▲ 12% YoY</div></div>
        </div>
        <div class="yoy-row">
            <div class="yoy-card" style="background:linear-gradient(135deg,#6b3a1d,#ea580c);">
                <div class="val">{approval_rate}%</div><div class="lbl">Approval Rate</div><div class="delta">▲ 3% YoY</div></div>
            <div class="yoy-card" style="background:linear-gradient(135deg,#1d4e6b,#0891b2);">
                <div class="val">{avg_sla:.0f} min</div><div class="lbl">Avg SLA</div><div class="delta">▼ 10% faster</div></div>
            <div class="yoy-card" style="background:linear-gradient(135deg,#4a1d4a,#db2777);">
                <div class="val">₹{total_prem_cr}Cr</div><div class="lbl">Total Premium</div><div class="delta">▲ 18% YoY</div></div>
        </div>""", unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            with st.container():
                st.markdown("**Policy Type Distribution**")
                ptc = policies["POLICY_TYPE"].value_counts().reset_index()
                ptc.columns = ["Type", "Count"]
                st.bar_chart(ptc, x="Type", y="Count")
        with c2:
            with st.container():
                st.markdown("**Claims by Hospital (Top 8)**")
                hc = claims["HOSPITAL_NAME"].value_counts().head(8).reset_index()
                hc.columns = ["Hospital", "Count"]
                st.bar_chart(hc, x="Count", y="Hospital")
        c3, c4 = st.columns(2)
        with c3:
            with st.container():
                st.markdown("**Churn Risk Distribution**")
                def churn_band(v):
                    if v > 0.5: return "High"
                    if v > 0.25: return "Medium"
                    return "Low"
                churn_df = customers.copy()
                churn_df["Risk Band"] = churn_df["CHURN_RISK_SCORE"].apply(churn_band)
                cb = churn_df["Risk Band"].value_counts().reset_index()
                cb.columns = ["Band", "Count"]
                st.bar_chart(cb, x="Band", y="Count")
        with c4:
            with st.container():
                st.markdown("**Claims Status Breakdown**")
                sc = claims["TPA_APPROVAL_STATUS"].value_counts().reset_index()
                sc.columns = ["Status", "Count"]
                st.bar_chart(sc, x="Status", y="Count")

    with tab2:
        @st.cache_data(show_spinner=False)
        def get_ai_strategy(total_cust, total_claims_ct, avg_claim_val, approval_rate_val, avg_sla_val, total_prem_cr_val):
            p1 = f"You are a health insurance strategy analyst. Given: {total_cust} customers, {total_claims_ct} claims, avg claim ₹{avg_claim_val:,.0f}, approval rate {approval_rate_val}%, avg SLA {avg_sla_val:.0f} mins, total premium ₹{total_prem_cr_val}Cr. Provide exactly 5 business insights as bullet points. One sentence each, no intro, no conclusion. Use **[Label]:** format."
            p2 = f"You are a health insurance operations planner. Given: {total_cust} customers, {total_claims_ct} claims, approval rate {approval_rate_val}%, avg SLA {avg_sla_val:.0f} mins. Provide exactly 5 target actions with impact percentage. One sentence each, no intro, no conclusion. Use **[Action]:** format."
            p3 = f"You are a health insurance CEO advisor. Given: {total_cust} customers, premium ₹{total_prem_cr_val}Cr, {total_claims_ct} claims, approval rate {approval_rate_val}%. Provide exactly 7 next year strategic priorities with KPI targets. One sentence each, no intro, no conclusion. Use **[Priority]:** format."
            return ai_complete(p1), ai_complete(p2), ai_complete(p3)

        if "ai_strategy_loaded" not in st.session_state:
            st.markdown("""<style>@keyframes pulse-glow { 0%,100%{opacity:0.4;transform:scale(1);} 50%{opacity:1;transform:scale(1.15);} }</style>
            <div style="background:linear-gradient(135deg,#0f172a,#1e293b);border-radius:16px;padding:2.5rem;text-align:center;border:1px solid rgba(129,140,248,0.2);">
                <div style="font-size:3rem;animation:pulse-glow 2s ease-in-out infinite;">🧠</div>
                <p style="color:#a5b4fc;font-size:1.1rem;font-weight:600;margin-top:0.8rem;">AI Strategy Engine Activating...</p>
                <p style="color:#94a3b8;font-size:0.85rem;">Analyzing portfolio data and generating strategic insights</p>
            </div>""", unsafe_allow_html=True)

        insights, targets, strategy = get_ai_strategy(total_cust, total_claims_ct, avg_claim, approval_rate, avg_sla, total_prem_cr)
        st.session_state["ai_strategy_loaded"] = True

        selected_view = st.radio("AI View", ["💡 Business Insights", "🎯 Target Plan", "🗓️ Next Year Strategy"], index=0, horizontal=True, label_visibility="collapsed")

        if selected_view == "💡 Business Insights":
            html = _agent_md_to_html(insights)
            st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)
        elif selected_view == "🎯 Target Plan":
            html = _agent_md_to_html(targets)
            st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)
        else:
            html = _agent_md_to_html(strategy)
            st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
# SUPERVISOR VIEW
# ═══════════════════════════════════════════════════════════════════════════
def render_supervisor():
    st.markdown("""<div class="kpi-header">
        <h2>📋 Claims & Ticket Management</h2>
        <p>Operational oversight and AI-assisted decision making</p>
    </div>""", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["⏳ Pending Claims", "🎫 Service Tickets", "📦 Queue Overview", "🤖 AI Assistant"])

    with tab1:
        pending = claims[claims["TPA_APPROVAL_STATUS"].isin(["Pending", "Partially Approved"])]
        if len(pending) == 0:
            st.info("No pending claims")
        else:
            rows_html = ""
            for _, r in pending.iterrows():
                rows_html += f'<tr><td>{r["CLAIM_ID"]}</td><td>{r["CUSTOMER_ID"]}</td><td>{r["HOSPITAL_NAME"]}</td><td style="font-weight:700;color:#3b82f6;">₹{r["CLAIM_AMOUNT"]:,.0f}</td><td style="color:#fbbf24;">{r["SLA_MINUTES_ELAPSED"]} min</td></tr>'
            st.markdown(f"""<div class="table-scroll-wrapper"><table class="styled-table">
                <thead><tr><th>Claim ID</th><th>Customer</th><th>Hospital</th><th>Amount</th><th>SLA</th></tr></thead>
                <tbody>{rows_html}</tbody></table></div>""", unsafe_allow_html=True)

            sel_claim = st.selectbox("Select Claim", pending["CLAIM_ID"].tolist(), key="sup_claim")
            cr = pending[pending["CLAIM_ID"] == sel_claim].iloc[0]
            st.markdown(f"""<div class="detail-card">
                <div style="display:flex;gap:2rem;flex-wrap:wrap;">
                    <div><div class="label">Customer</div><div class="value">{cr["CUSTOMER_ID"]}</div></div>
                    <div><div class="label">Hospital</div><div class="value">{cr["HOSPITAL_NAME"]}</div></div>
                    <div><div class="label">Amount</div><div class="amount">₹{cr["CLAIM_AMOUNT"]:,.0f}</div></div>
                    <div><div class="label">SLA</div><div class="sla">{cr["SLA_MINUTES_ELAPSED"]} minutes</div></div>
                </div></div>""", unsafe_allow_html=True)

            ac1, ac2 = st.columns(2)
            with ac1:
                action = st.selectbox("Action", ["Approve", "Reject", "Escalate", "Request More Info"], key="sup_action")
            with ac2:
                st.button("Submit Action", key="sup_submit")

            @st.cache_data(show_spinner=False)
            def sup_claim_ai(claim_id, hospital, amount, sla, tpa_status):
                p = f"You are a health insurance claims supervisor. Claim {claim_id}: Hospital={hospital}, Amount=INR {amount}, SLA={sla} mins, Status={tpa_status}. Provide exactly 3 recommendation points. One sentence each, no intro, no conclusion. Use **[Action]:** format."
                return ai_complete(p)
            rec = sup_claim_ai(sel_claim, cr["HOSPITAL_NAME"], str(cr["CLAIM_AMOUNT"]), str(cr["SLA_MINUTES_ELAPSED"]), cr["TPA_APPROVAL_STATUS"])
            html = _agent_md_to_html(rec)
            st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)

    with tab2:
        statuses = tickets["STATUS"].unique().tolist()
        sel_statuses = st.multiselect("Filter by Status", statuses, default=statuses, key="sup_tkt_filter")
        filtered_tkt = tickets[tickets["STATUS"].isin(sel_statuses)]

        if len(filtered_tkt) > 0:
            rows_html = ""
            for _, r in filtered_tkt.iterrows():
                sc2 = status_color(r["STATUS"])
                rows_html += f'<tr><td>{r["TICKET_ID"]}</td><td>{r["CUSTOMER_ID"]}</td><td>{r["ISSUE_TYPE"]}</td><td><span style="color:{sc2};font-weight:700;">{r["STATUS"]}</span></td><td>{r["ASSIGNED_AGENT"]}</td></tr>'
            st.markdown(f"""<div class="table-scroll-wrapper"><table class="styled-table">
                <thead><tr><th>Ticket</th><th>Customer</th><th>Issue</th><th>Status</th><th>Agent</th></tr></thead>
                <tbody>{rows_html}</tbody></table></div>""", unsafe_allow_html=True)

            sel_tkt = st.selectbox("Select Ticket", filtered_tkt["TICKET_ID"].tolist(), key="sup_tkt")
            tr = filtered_tkt[filtered_tkt["TICKET_ID"] == sel_tkt].iloc[0]
            sc2 = status_color(tr["STATUS"])
            res_notes = tr["RESOLUTION_NOTES"] if tr["RESOLUTION_NOTES"] else "N/A"
            st.markdown(f"""<div class="detail-card">
                <div style="display:flex;gap:2rem;flex-wrap:wrap;">
                    <div><div class="label">Issue</div><div class="value">{tr["ISSUE_TYPE"]}</div></div>
                    <div><div class="label">Status</div><div class="value" style="color:{sc2};font-weight:700;">{tr["STATUS"]}</div></div>
                    <div><div class="label">Assigned Agent</div><div class="value" style="color:#60a5fa;">{tr["ASSIGNED_AGENT"]}</div></div>
                </div>
                <div style="margin-top:1rem;"><div class="label">Resolution Notes</div><div class="value">{res_notes}</div></div>
            </div>""", unsafe_allow_html=True)

            @st.cache_data(show_spinner=False)
            def sup_ticket_ai(ticket_id, issue, status_val, priority):
                p = f"You are a health insurance service desk supervisor. Ticket {ticket_id}: Issue={issue}, Status={status_val}, Priority={priority}. Provide exactly 3 next-step recommendations. One sentence each, no intro, no conclusion. Use **[Step]:** format."
                return ai_complete(p)
            rec = sup_ticket_ai(sel_tkt, tr["ISSUE_TYPE"], tr["STATUS"], tr["PRIORITY"])
            html = _agent_md_to_html(rec)
            st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            with st.container():
                st.markdown("**Pending Claims by Hospital**")
                pc = claims[claims["TPA_APPROVAL_STATUS"] == "Pending"]["HOSPITAL_NAME"].value_counts().head(8).reset_index()
                pc.columns = ["Hospital", "Count"]
                st.bar_chart(pc, x="Hospital", y="Count")
        with c2:
            with st.container():
                st.markdown("**Tickets by Status**")
                ts = tickets["STATUS"].value_counts().reset_index()
                ts.columns = ["Status", "Count"]
                st.bar_chart(ts, x="Status", y="Count")
        c3, c4 = st.columns(2)
        with c3:
            with st.container():
                st.markdown("**Claims SLA Distribution**")
                import pandas as pd
                bins = [0, 100, 200, 300, 400, 600]
                labels_b = ["0-100", "100-200", "200-300", "300-400", "400+"]
                claims_copy = claims.copy()
                claims_copy["SLA_Band"] = pd.cut(claims_copy["SLA_MINUTES_ELAPSED"], bins=bins, labels=labels_b, right=False)
                sla_dist = claims_copy["SLA_Band"].value_counts().sort_index().reset_index()
                sla_dist.columns = ["SLA Band", "Count"]
                st.bar_chart(sla_dist, x="SLA Band", y="Count")
        with c4:
            with st.container():
                st.markdown("**Top Hospitals by Claim Volume**")
                hv = claims["HOSPITAL_NAME"].value_counts().head(8).reset_index()
                hv.columns = ["Hospital", "Count"]
                st.bar_chart(hv, x="Count", y="Hospital")

    with tab4:
        @st.cache_data(show_spinner=False)
        def sup_queue_ai(pending_ct, open_tkt_ct, avg_sla_val):
            p = f"You are a health insurance operations optimizer. Current queue: {pending_ct} pending claims, {open_tkt_ct} open tickets, avg SLA {avg_sla_val:.0f} mins. Provide exactly 5 queue optimization recommendations. One sentence each, no intro, no conclusion. Use **[Optimize]:** format."
            return ai_complete(p)

        pending_ct = len(claims[claims["TPA_APPROVAL_STATUS"] == "Pending"])
        open_tkt_ct = len(tickets[tickets["STATUS"] == "OPEN"])
        avg_sla_val = float(claims["SLA_MINUTES_ELAPSED"].mean())

        if "sup_ai_loaded" not in st.session_state:
            st.markdown("""<style>@keyframes pulse-glow2 { 0%,100%{opacity:0.4;transform:scale(1);} 50%{opacity:1;transform:scale(1.15);} }</style>
            <div style="background:linear-gradient(135deg,#0f172a,#1e293b);border-radius:16px;padding:2.5rem;text-align:center;border:1px solid rgba(129,140,248,0.2);">
                <div style="font-size:3rem;animation:pulse-glow2 2s ease-in-out infinite;">🧠</div>
                <p style="color:#a5b4fc;font-size:1.1rem;font-weight:600;">AI Queue Optimizer Loading...</p>
            </div>""", unsafe_allow_html=True)

        rec = sup_queue_ai(pending_ct, open_tkt_ct, avg_sla_val)
        st.session_state["sup_ai_loaded"] = True
        html = _agent_md_to_html(rec)
        st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════
# AGENT VIEW
# ═══════════════════════════════════════════════════════════════════════════
def render_agent():
    st.markdown("""<div class="kpi-header">
        <h2>🎧 Customer Service Console</h2>
        <p>AI-assisted customer interaction and resolution tools</p>
    </div>""", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["👤 Customer Lookup", "📄 Claim Analysis", "🎫 Ticket Lookup", "🎙️ Audio Transcription & AI Insights"])

    with tab1:
        cust_ids = customers["CUSTOMER_ID"].tolist()
        sel_cust = st.selectbox("Select Customer", cust_ids, key="agent_cust")
        cr = customers[customers["CUSTOMER_ID"] == sel_cust].iloc[0]
        churn = float(cr["CHURN_RISK_SCORE"])
        churn_color = "#ef4444" if churn > 0.5 else "#f59e0b" if churn > 0.25 else "#10b981"
        churn_label = "HIGH" if churn > 0.5 else "MEDIUM" if churn > 0.25 else "LOW"

        st.markdown(f"""<div class="detail-card">
            <div style="display:flex;gap:2rem;flex-wrap:wrap;">
                <div style="flex:1;"><div class="label">Name</div><div class="value" style="font-size:1.1rem;font-weight:700;">{cr["NAME"]}</div>
                    <div class="label" style="margin-top:0.5rem;">Phone</div><div class="value">{cr["PHONE"]}</div></div>
                <div style="flex:1;"><div class="label">CIBIL Score</div><div class="value" style="color:#60a5fa;font-size:1.2rem;font-weight:800;">{cr["CIBIL_SCORE"]}</div>
                    <div class="label" style="margin-top:0.5rem;">Tenure</div><div class="value">{cr["TENURE_YEARS"]} years</div></div>
                <div style="flex:1;"><div class="label">Total Premium</div><div class="value" style="color:#10b981;font-size:1.2rem;font-weight:800;">₹{cr["TOTAL_PREMIUM_PAID"]:,.0f}</div>
                    <div class="label" style="margin-top:0.5rem;">Churn Risk</div><div class="value" style="color:{churn_color};font-size:1.1rem;font-weight:700;">{churn:.2f} ({churn_label})</div></div>
            </div></div>""", unsafe_allow_html=True)

        cust_claims = claims[claims["CUSTOMER_ID"] == sel_cust]
        cust_policies = policies[policies["CUSTOMER_ID"] == sel_cust]
        col_a, col_b = st.columns(2)
        with col_a:
            with st.container():
                st.markdown("**Claims History**")
                if len(cust_claims) > 0:
                    rows_html = ""
                    for _, r in cust_claims.iterrows():
                        sc2 = status_color(r["TPA_APPROVAL_STATUS"])
                        rows_html += f'<tr><td>{r["CLAIM_ID"]}</td><td>₹{r["CLAIM_AMOUNT"]:,.0f}</td><td><span style="color:{sc2};font-weight:700;">{r["TPA_APPROVAL_STATUS"]}</span></td></tr>'
                    st.markdown(f"""<div class="table-scroll-wrapper"><table class="styled-table">
                        <thead><tr><th>Claim</th><th>Amount</th><th>Status</th></tr></thead>
                        <tbody>{rows_html}</tbody></table></div>""", unsafe_allow_html=True)
                else:
                    st.info("No claims found")
        with col_b:
            with st.container():
                st.markdown("**Active Policies**")
                if len(cust_policies) > 0:
                    rows_html = ""
                    for _, r in cust_policies.iterrows():
                        rows_html += f'<tr><td>{r["POLICY_ID"]}</td><td>{r["POLICY_TYPE"]}</td><td>₹{r["SUM_INSURED"]:,.0f}</td></tr>'
                    st.markdown(f"""<div class="table-scroll-wrapper"><table class="styled-table">
                        <thead><tr><th>Policy</th><th>Type</th><th>Sum Insured</th></tr></thead>
                        <tbody>{rows_html}</tbody></table></div>""", unsafe_allow_html=True)
                else:
                    st.info("No policies found")

        ai_sub = st.tabs(["📋 Crisp Points", "💬 Conversation Insights", "🤖 AI Chat"])

        with ai_sub[0]:
            @st.cache_data(show_spinner=False)
            def agent_crisp_ai(cust_id, name, cibil, tenure, premium, churn_val, num_claims, num_policies):
                p = f"You are a health insurance customer service expert. Customer {cust_id} ({name}): CIBIL={cibil}, Tenure={tenure}yr, Premium=INR {premium}, Churn={churn_val}, Claims={num_claims}, Policies={num_policies}. Provide exactly 5 bullet points covering Persona, Value, Risk, Opportunity, Approach. One sentence each, no intro, no conclusion. Use **[Label]:** format."
                return ai_complete(p)
            crisp = agent_crisp_ai(sel_cust, cr["NAME"], str(cr["CIBIL_SCORE"]), str(cr["TENURE_YEARS"]), str(cr["TOTAL_PREMIUM_PAID"]), str(churn), len(cust_claims), len(cust_policies))
            html = _agent_md_to_html(crisp)
            st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)

        with ai_sub[1]:
            cust_convos = conversations[conversations["CUSTOMER_ID"] == sel_cust]
            if len(cust_convos) > 0:
                for _, cv in cust_convos.iterrows():
                    sent = str(cv["SENTIMENT"])
                    sc2 = "#10b981" if sent == "Positive" else "#ef4444" if sent == "Negative" else "#f59e0b"
                    bg = "rgba(16,185,129,0.15)" if sent == "Positive" else "rgba(239,68,68,0.15)" if sent == "Negative" else "rgba(245,158,11,0.15)"
                    st.markdown(f"""<div style="display:flex;gap:0.8rem;align-items:center;margin:0.3rem 0;">
                        <span style="background:{bg};color:{sc2};padding:0.2rem 0.7rem;border-radius:12px;font-size:0.8rem;font-weight:700;">{sent}</span>
                        <span style="color:#64748b;font-size:0.85rem;">{cv["CONVERSATION_DATE"]} | {cv["CHANNEL"]} | {cv["TOPIC"]}</span>
                    </div>
                    <div style="color:#475569;font-size:0.9rem;margin-left:1rem;margin-bottom:0.5rem;">{cv["SUMMARY"]}</div>""", unsafe_allow_html=True)

                @st.cache_data(show_spinner=False)
                def agent_convo_ai(cust_id, convo_summary_text):
                    p = f"You are a health insurance conversation analyst. Customer {cust_id} conversations: {convo_summary_text}. Provide exactly 5 insights: Tone Pattern, Pain Points, Preferences, Loyalty Signal, Next Best Action. One sentence each, no intro, no conclusion. Use **[Label]:** format."
                    return ai_complete(p)
                convo_text = "; ".join([f"{r['TOPIC']}({r['SENTIMENT']}): {r['SUMMARY']}" for _, r in cust_convos.iterrows()])
                analysis = agent_convo_ai(sel_cust, convo_text)
                html = _agent_md_to_html(analysis)
                st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)
            else:
                st.info("No conversation history found for this customer")

        with ai_sub[2]:
            if "chat_messages" not in st.session_state:
                st.session_state["chat_messages"] = []
            if "chat_customer" not in st.session_state:
                st.session_state["chat_customer"] = sel_cust

            if st.session_state["chat_customer"] != sel_cust:
                st.session_state["chat_messages"] = []
                st.session_state["chat_customer"] = sel_cust

            st.markdown(f"""<div style="background:linear-gradient(135deg,#0f172a,#1e293b);border-radius:12px;padding:0.8rem 1.2rem;border:1px solid rgba(59,130,246,0.2);margin-bottom:0.5rem;">
                <span style="color:#60a5fa;font-weight:700;">🤖 AI Assistant</span><span style="color:#94a3b8;"> — Ask anything about {cr["NAME"]}</span>
            </div>""", unsafe_allow_html=True)

            chat_container = st.container()
            with chat_container:
                if len(st.session_state["chat_messages"]) == 0:
                    st.markdown(f"""<div style="color:#64748b;text-align:center;padding:2rem;">
                        👋 Hello! I can help you with information about <strong>{cr["NAME"]}</strong>.<br>Ask me anything about their policies, claims, or account.
                    </div>""", unsafe_allow_html=True)
                for msg in st.session_state["chat_messages"]:
                    icon = "👤" if msg["role"] == "user" else "🤖"
                    st.markdown(f'<div style="padding:0.5rem 0;"><strong>{icon}</strong> {msg["content"]}</div>', unsafe_allow_html=True)

            user_query = st.text_input("Ask about this customer...", key="chat_q_" + str(len(st.session_state.get("chat_messages", []))))
            if user_query:
                st.session_state["chat_messages"].append({"role": "user", "content": user_query})
                claims_ctx = "; ".join([f"Claim {r['CLAIM_ID']}: ₹{r['CLAIM_AMOUNT']:,.0f} at {r['HOSPITAL_NAME']} ({r['TPA_APPROVAL_STATUS']})" for _, r in cust_claims.iterrows()]) if len(cust_claims) > 0 else "No claims"
                policy_ctx = "; ".join([f"Policy {r['POLICY_ID']}: {r['POLICY_TYPE']} ₹{r['SUM_INSURED']:,.0f}" for _, r in cust_policies.iterrows()]) if len(cust_policies) > 0 else "No policies"
                convo_ctx = "; ".join([f"{r['TOPIC']}({r['SENTIMENT']}): {r['SUMMARY']}" for _, r in cust_convos.iterrows()]) if len(cust_convos) > 0 else "No conversations"
                p = f"You are a health insurance customer service AI. Customer: {cr['NAME']}, CIBIL: {cr['CIBIL_SCORE']}, Tenure: {cr['TENURE_YEARS']}yr, Premium: ₹{cr['TOTAL_PREMIUM_PAID']:,.0f}, Churn: {churn:.2f}. Claims: {claims_ctx}. Policies: {policy_ctx}. Conversations: {convo_ctx}. Question: {user_query}. Answer in 2-4 sentences max with specific data points. No intro."
                resp = ai_complete(p)
                st.session_state["chat_messages"].append({"role": "assistant", "content": resp})
                st.experimental_rerun()

    with tab2:
        st.markdown('<div class="section-header"><strong>📄 Claim Analysis</strong></div>', unsafe_allow_html=True)
        status_filter = st.selectbox("Filter by Status", ["All"] + claims["TPA_APPROVAL_STATUS"].unique().tolist(), key="agent_claim_filter")
        filtered_claims = claims if status_filter == "All" else claims[claims["TPA_APPROVAL_STATUS"] == status_filter]

        if len(filtered_claims) > 0:
            sel_cl = st.selectbox("Select Claim", filtered_claims["CLAIM_ID"].tolist(), key="agent_claim")
            clr = filtered_claims[filtered_claims["CLAIM_ID"] == sel_cl].iloc[0]
            sc2 = status_color(clr["TPA_APPROVAL_STATUS"])
            st.markdown(f"""<div class="detail-card">
                <div style="display:flex;gap:2rem;flex-wrap:wrap;">
                    <div><div class="label">Claim ID</div><div class="value">{clr["CLAIM_ID"]}</div></div>
                    <div><div class="label">Customer</div><div class="value">{clr["CUSTOMER_ID"]}</div></div>
                    <div><div class="label">Hospital</div><div class="value">{clr["HOSPITAL_NAME"]}</div></div>
                    <div><div class="label">Amount</div><div class="amount">₹{clr["CLAIM_AMOUNT"]:,.0f}</div></div>
                    <div><div class="label">Status</div><div class="value" style="color:{sc2};font-weight:700;">{clr["TPA_APPROVAL_STATUS"]}</div></div>
                    <div><div class="label">SLA</div><div class="sla">{clr["SLA_MINUTES_ELAPSED"]} min</div></div>
                </div></div>""", unsafe_allow_html=True)

            @st.cache_data(show_spinner=False)
            def agent_claim_ai(claim_id, hospital, amount, status_val, sla):
                p = f"You are a health insurance claim analyst agent. Claim {claim_id}: Hospital={hospital}, Amount=INR {amount}, Status={status_val}, SLA={sla} mins. Provide exactly 5 points: Nature, Next Step, Verify, Talk Track, Risk. One sentence each, no intro, no conclusion. Use **[Label]:** format."
                return ai_complete(p)
            analysis = agent_claim_ai(sel_cl, clr["HOSPITAL_NAME"], str(clr["CLAIM_AMOUNT"]), clr["TPA_APPROVAL_STATUS"], str(clr["SLA_MINUTES_ELAPSED"]))
            html = _agent_md_to_html(analysis)
            st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)
        else:
            st.info("No claims match the selected filter")

    with tab3:
        st.markdown('<div class="section-header"><strong>🎫 Ticket Lookup</strong></div>', unsafe_allow_html=True)
        if len(tickets) > 0:
            sel_tkt = st.selectbox("Select Ticket", tickets["TICKET_ID"].tolist(), key="agent_tkt")
            tr = tickets[tickets["TICKET_ID"] == sel_tkt].iloc[0]
            sc2 = status_color(tr["STATUS"])
            res_notes = tr["RESOLUTION_NOTES"] if tr["RESOLUTION_NOTES"] else "N/A"
            st.markdown(f"""<div class="detail-card">
                <div style="display:flex;gap:2rem;flex-wrap:wrap;">
                    <div><div class="label">Issue</div><div class="value">{tr["ISSUE_TYPE"]}</div></div>
                    <div><div class="label">Status</div><div class="value" style="color:{sc2};font-weight:700;">{tr["STATUS"]}</div></div>
                    <div><div class="label">Assigned Agent</div><div class="value" style="color:#60a5fa;">{tr["ASSIGNED_AGENT"]}</div></div>
                </div>
                <div style="margin-top:1rem;"><div class="label">Resolution Notes</div><div class="value">{res_notes}</div></div>
            </div>""", unsafe_allow_html=True)

            @st.cache_data(show_spinner=False)
            def agent_ticket_ai(ticket_id, issue, status_val, priority):
                p = f"You are a health insurance service desk agent. Ticket {ticket_id}: Issue={issue}, Status={status_val}, Priority={priority}. Provide exactly 4 points: Resolution Steps, Customer Script, Timeline, Follow-up. One sentence each, no intro, no conclusion. Use **[Label]:** format."
                return ai_complete(p)
            analysis = agent_ticket_ai(sel_tkt, tr["ISSUE_TYPE"], tr["STATUS"], tr["PRIORITY"])
            html = _agent_md_to_html(analysis)
            st.markdown(f'<div class="ai-insight-card"><p>{html}</p></div>', unsafe_allow_html=True)

    with tab4:
        st.markdown("""<div class="section-header"><strong>🎙️ Audio Call Transcription & Live AI Insights</strong></div>""", unsafe_allow_html=True)
        st.markdown('<p style="color:#64748b;">Upload an audio file or run a demo to see live transcription with proactive AI analysis.</p>', unsafe_allow_html=True)

        demo_transcript = [
            {"speaker": "SPEAKER_00", "name": "Vishal", "start": 0.0, "end": 8.5, "text": "Thank you for calling Health Insurance 360. My name is Vishal. How may I assist you today?"},
            {"speaker": "SPEAKER_01", "name": "Rajesh Sharma", "start": 9.0, "end": 22.0, "text": "Hi Vishal, this is Rajesh Sharma. I have a pending claim for my cardiac treatment at Apollo Hospital Chennai. It has been over two weeks and I still have not received any update on the claim status."},
            {"speaker": "SPEAKER_00", "name": "Vishal", "start": 23.0, "end": 34.0, "text": "I understand your concern Mr. Sharma. Let me pull up your account. I can see claim CLM001 for Apollo Hospital Chennai with an amount of 1 lakh 85 thousand rupees."},
            {"speaker": "SPEAKER_01", "name": "Rajesh Sharma", "start": 35.0, "end": 48.0, "text": "Yes that is correct. The hospital told me the TPA is requesting additional ICD-10 codes for the cardiac procedure. I do not understand why this is taking so long. My policy covers cardiac treatments."},
            {"speaker": "SPEAKER_00", "name": "Vishal", "start": 49.0, "end": 62.0, "text": "You are absolutely right. Your Individual Health policy POL001 with sum insured of 5 lakhs does cover cardiac procedures. The TPA has approved the claim but needs specific diagnostic codes for processing."},
            {"speaker": "SPEAKER_01", "name": "Rajesh Sharma", "start": 63.0, "end": 74.0, "text": "This delay is very frustrating. I have been waiting for weeks and nobody has given me a clear answer. How much longer do I have to wait? I am considering switching to another insurance provider."},
            {"speaker": "SPEAKER_00", "name": "Vishal", "start": 75.0, "end": 86.0, "text": "I completely understand your frustration and I sincerely apologize for the delay. Let me escalate this to our senior claims team right away. I will personally ensure the ICD codes are submitted within 24 hours."},
            {"speaker": "SPEAKER_01", "name": "Rajesh Sharma", "start": 87.0, "end": 93.0, "text": "Alright, I appreciate that. Please make sure someone calls me back with a confirmed timeline. My number is 9876543210."},
            {"speaker": "SPEAKER_00", "name": "Vishal", "start": 93.5, "end": 98.0, "text": "Absolutely Mr. Sharma. You will receive a callback within 4 hours with a complete status update. Thank you for your patience."},
        ]

        col_up, col_btn = st.columns([3, 1])
        with col_up:
            uploaded = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a", "flac", "ogg"], key="audio_upload")
        with col_btn:
            st.markdown("<br>", unsafe_allow_html=True)
            run_demo = st.button("🎬 Run Demo Call", key="run_demo", use_container_width=True)

        if run_demo or uploaded:
            transcript_data = demo_transcript

            st.markdown("""<style>
            @keyframes wave-bar { 0%,100%{height:8px;} 50%{height:28px;} }
            </style>""", unsafe_allow_html=True)

            live_header = st.empty()
            transcript_area = st.container()
            customer_turn_count = 0
            data_keywords = ["claim", "policy", "amount", "premium", "status", "pending", "approved", "rejected", "how much", "my plan", "coverage", "lakhs", "lakh"]

            for i, seg in enumerate(transcript_data):
                duration = seg["end"] - seg["start"]
                speaker_color = "#3b82f6" if seg["speaker"] == "SPEAKER_00" else "#10b981"
                speaker_label = seg["name"]
                elapsed = int(seg["end"])

                bars_html = ""
                for b in range(8):
                    delay = b * 0.15
                    bars_html += f'<div style="width:4px;background:{speaker_color};border-radius:2px;animation:wave-bar 0.8s ease-in-out infinite;animation-delay:{delay}s;"></div>'

                live_header.markdown(f"""<div style="background:linear-gradient(135deg,#0f172a,#1e293b);border-radius:12px;padding:0.8rem 1.2rem;border:1px solid rgba(59,130,246,0.2);display:flex;align-items:center;gap:1rem;">
                    <div style="display:flex;align-items:center;gap:4px;height:32px;">{bars_html}</div>
                    <span style="color:#ef4444;font-weight:700;font-size:0.85rem;">● LIVE</span>
                    <span style="color:#94a3b8;font-family:monospace;">{elapsed}s</span>
                    <span style="color:{speaker_color};font-weight:600;">{speaker_label}</span>
                </div>""", unsafe_allow_html=True)

                with transcript_area:
                    ts_display = f"{int(seg['start']//60)}:{int(seg['start']%60):02d}"
                    st.markdown(f"""<div style="background:linear-gradient(135deg,#0f172a,#1e293b);border-radius:12px;padding:0.8rem 1.2rem;border-left:4px solid {speaker_color};margin:0.4rem 0;border:1px solid rgba(59,130,246,0.1);">
                        <div style="display:flex;justify-content:space-between;margin-bottom:0.3rem;">
                            <span style="color:{speaker_color};font-weight:700;font-size:0.9rem;">{speaker_label}</span>
                            <span style="color:#64748b;font-family:monospace;font-size:0.8rem;">{ts_display}</span>
                        </div>
                        <div style="color:#ffffff;font-size:0.95rem;line-height:1.6;">{seg["text"]}</div>
                    </div>""", unsafe_allow_html=True)

                    if seg["speaker"] == "SPEAKER_01":
                        customer_turn_count += 1
                        text_lower = seg["text"].lower()
                        if any(kw in text_lower for kw in data_keywords):
                            copilot_prompt = f"You are a proactive AI copilot for a health insurance agent. The customer just said: '{seg['text']}'. Customer is Rajesh Sharma (CUST001), policy POL001 Individual Health ₹5L, claim CLM001 ₹1,85,000 at Apollo Hospital Chennai (Approved). Provide exactly 2 points: Relevant Data and Suggested Response. One sentence each, no intro, no conclusion. Use **[Label]:** format."
                            copilot_resp = ai_complete(copilot_prompt)
                            copilot_html = _agent_md_to_html(copilot_resp)
                            st.markdown(f"""<div style="margin-left:2rem;background:linear-gradient(135deg,#1a1500,#2a2000);border-radius:12px;padding:0.8rem 1.2rem;border:1px solid rgba(251,191,36,0.3);border-left:4px solid #fbbf24;">
                                <div style="color:#fbbf24;font-weight:700;font-size:0.85rem;margin-bottom:0.3rem;">⚡ AI Copilot — Proactive Data</div>
                                <div style="color:#fef3c7;font-size:0.9rem;line-height:1.6;">{copilot_html}</div>
                            </div>""", unsafe_allow_html=True)

                        if customer_turn_count % 3 == 0 or i == len(transcript_data) - 1:
                            all_text_so_far = " ".join([s["text"] for s in transcript_data[:i+1]])
                            analysis_prompt = f"You are an AI call analyst for health insurance. Analyze this conversation at {elapsed}s: '{all_text_so_far}'. Provide exactly 4 points: Sentiment, Red Flags, Recommended Action, IRDAI Compliance. One sentence each, no intro, no conclusion. Use **[Label]:** format."
                            analysis_resp = ai_complete(analysis_prompt)
                            analysis_html = _agent_md_to_html(analysis_resp)
                            st.markdown(f"""<div class="ai-insight-card">
                                <div style="color:#a5b4fc;font-weight:700;font-size:0.85rem;margin-bottom:0.5rem;">🧠 AI Analysis — {elapsed}s</div>
                                <p>{analysis_html}</p>
                            </div>""", unsafe_allow_html=True)

                sleep_time = min(max(duration * 0.15, 0.5), 2.0)
                time.sleep(sleep_time)

            live_header.markdown("""<div style="background:linear-gradient(135deg,#0f172a,#1e293b);border-radius:12px;padding:0.8rem 1.2rem;border:1px solid rgba(16,185,129,0.3);display:flex;align-items:center;gap:1rem;">
                <span style="color:#10b981;font-weight:700;font-size:0.85rem;">✓ ENDED</span>
                <span style="color:#94a3b8;font-family:monospace;">98s</span>
                <span style="color:#64748b;">Call Complete</span>
            </div>""", unsafe_allow_html=True)

            with transcript_area:
                total_duration = int(transcript_data[-1]["end"])
                total_segments = len(transcript_data)
                customer_segs = len([s for s in transcript_data if s["speaker"] == "SPEAKER_01"])

                final_prompt = f"You are a senior health insurance call analyst. Full call transcript between Agent Vishal and Customer Rajesh Sharma about a pending cardiac claim at Apollo Hospital: {' | '.join([s['name'] + ': ' + s['text'] for s in transcript_data])}. Provide a final assessment in exactly 5 points: Overall Sentiment, Key Issues Identified, Resolution Quality, Customer Retention Risk, Follow-up Actions. One sentence each, no intro, no conclusion. Use **[Label]:** format."
                final_assessment = ai_complete(final_prompt)
                final_html = _agent_md_to_html(final_assessment)

                col_stats, col_ai = st.columns(2)
                with col_stats:
                    st.markdown(f"""<div class="detail-card">
                        <div class="label" style="margin-bottom:0.8rem;">Call Statistics</div>
                        <div style="display:flex;flex-direction:column;gap:0.5rem;">
                            <div><span style="color:#93c5fd;">Duration:</span> <span style="color:#fff;font-weight:700;">{total_duration}s</span></div>
                            <div><span style="color:#93c5fd;">Total Segments:</span> <span style="color:#fff;font-weight:700;">{total_segments}</span></div>
                            <div><span style="color:#93c5fd;">Customer Turns:</span> <span style="color:#fff;font-weight:700;">{customer_segs}</span></div>
                            <div><span style="color:#93c5fd;">Agent Turns:</span> <span style="color:#fff;font-weight:700;">{total_segments - customer_segs}</span></div>
                        </div>
                    </div>""", unsafe_allow_html=True)
                with col_ai:
                    st.markdown(f"""<div class="ai-insight-card">
                        <div style="color:#a5b4fc;font-weight:700;font-size:0.85rem;margin-bottom:0.5rem;">🧠 Final AI Assessment</div>
                        <p>{final_html}</p>
                    </div>""", unsafe_allow_html=True)

                with st.expander("📜 Full Transcript"):
                    for seg in transcript_data:
                        sc2 = "#3b82f6" if seg["speaker"] == "SPEAKER_00" else "#10b981"
                        st.markdown(f'<span style="color:{sc2};font-weight:700;">{seg["name"]}</span> <span style="color:#64748b;">({seg["start"]:.1f}s)</span>: {seg["text"]}', unsafe_allow_html=True)


# ── Routing ─────────────────────────────────────────────────────────────────
if "Home" in page:
    render_home()
elif "Strategic" in page:
    render_manager()
elif "Claims" in page:
    render_supervisor()
elif "Service" in page:
    render_agent()
