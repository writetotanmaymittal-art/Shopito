import streamlit as st
import pandas as pd
import time
from typing import Dict, List, Any, Optional

# ==========================================
# 1. ENTERPRISE CONFIGURATION & COMPLEX THEME ENGINE
# ==========================================
st.set_page_config(
    page_title="Shopito Enterprise Hub",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep Purple High-Fidelity Enterprise Stylesheet
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-size: 16px;
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        }
        h1 { font-size: 2.8rem !important; font-weight: 800 !important; color: #4C1D95; letter-spacing: -0.03em; }
        h2 { font-size: 2.0rem !important; font-weight: 700 !important; color: #5B21B6; }
        h3 { font-size: 1.4rem !important; font-weight: 600 !important; color: #6D28D9; }
        
        /* Glassmorphism Profile Container */
        .premium-profile-box {
            text-align: center;
            padding: 24px;
            background: linear-gradient(135deg, #F5EDFF 0%, #FFF0F5 100%);
            border-radius: 20px;
            margin-bottom: 30px;
            border: 2px solid #E9D5FF;
            box-shadow: 0 10px 15px -3px rgba(109, 40, 217, 0.1);
        }
        .premium-avatar {
            width: 110px;
            height: 110px;
            border-radius: 50%;
            object-fit: cover;
            margin: 0 auto 15px auto;
            border: 4px solid #7C3AED;
            box-shadow: 0 0 15px rgba(124, 58, 237, 0.4);
        }
        .premium-profile-name {
            font-weight: 800;
            font-size: 1.4rem;
            color: #4C1D95;
            margin-bottom: 2px;
        }
        
        /* High-Impact Marketing Canvas */
        .marquee-banner {
            background: linear-gradient(135deg, #2E1065 0%, #4C1D95 50%, #7C3AED 100%);
            color: #F5F3FF;
            padding: 30px;
            border-radius: 18px;
            text-align: center;
            font-weight: 800;
            font-size: 1.8rem;
            margin-bottom: 35px;
            box-shadow: 0 20px 25px -5px rgba(124, 58, 237, 0.3);
            border-left: 8px solid #C084FC;
        }
        
        /* Advanced Dynamic Product Card Grid System */
        .matrix-card {
            background: #FFFFFF;
            padding: 25px;
            border-radius: 20px;
            border: 1px solid #F3E8FF;
            box-shadow: 0 4px 12px rgba(109, 40, 217, 0.03);
            margin-bottom: 30px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .matrix-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(109, 40, 217, 0.08);
            border-color: #DDD6FE;
        }
        
        /* Financial Analytics Micro-Layouts */
        .financial-metric-container {
            background: #FAFAFE;
            padding: 15px;
            border-radius: 12px;
            border-left: 4px solid #7C3AED;
            margin-bottom: 10px;
        }
        .fin-label { font-size: 0.85rem; color: #6B7280; text-transform: uppercase; font-weight: 600; }
        .fin-val { font-size: 1.4rem; font-weight: 700; color: #1F2937; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. ISOLATED RELATIONAL PRODUCT REGISTRY DATABASE
# ==========================================
GLOBAL_PRODUCT_REGISTRY: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    "electronics": [
        {"id": "macbook_16", "name": "Apple MacBook Pro 16\" (M3 Max, 48GB, 1TB SSD)", "price": 349900.0, "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"},
        {"id": "iphone_15", "name": "Apple iPhone 15 Pro Max Titanium Edition", "price": 159900.0, "img": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400"},
        {"id": "sony_wh1000", "name": "Sony WH-1000XM5 Premium Noise Cancelling Headphones", "price": 29990.0, "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"}
    ],
    "watches": [
        {"id": "tourbillon_chrono", "name": "Luxury Mechanical Tourbillon Chronograph Timepiece", "price": 850000.0, "img": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=400"}
    ]
}

# Helper method to safely pull entities across memory loops
def lookup_system_entity(uid: str) -> Optional[Dict[str, Any]]:
    for block in GLOBAL_PRODUCT_REGISTRY.values():
        for entity in block:
            if entity["id"] == uid:
                return entity
    return None

# ==========================================
# 3. OBJECT-ORIENTED APP STATE SUBSYSTEM
# ==========================================
class EnterpriseStateEngine:
    @staticmethod
    def initialize_state_matrices():
        # Session Registry Guard Checks
        if 'wallet_funds' not in st.session_state: st.session_state.wallet_funds = 50000.0
        if 'credit_max_limit' not in st.session_state: st.session_state.credit_max_limit = 0.0
        if 'credit_allocated_debt' not in st.session_state: st.session_state.credit_allocated_debt = 0.0
        if 'tier_pro_max_active' not in st.session_state: st.session_state.tier_pro_max_active = False
        if 'cart_quantities_map' not in st.session_state: st.session_state.cart_quantities_map = {}
        if 'transaction_ledger_records' not in st.session_state: st.session_state.transaction_ledger_records = []
        if 'dashboard_animation_trigger' not in st.session_state: st.session_state.dashboard_animation_trigger = True
        
        # User Config Registries
        if 'meta_profile_name' not in st.session_state: st.session_state.meta_profile_name = "Krishna Kumar"
        if 'meta_profile_phone' not in st.session_state: st.session_state.meta_profile_phone = "+91 98765 43210"
        if 'meta_profile_avatar' not in st.session_state: st.session_state.meta_profile_avatar = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400"

    @property
    def dynamic_available_credit(self) -> float:
        return max(0.0, st.session_state.credit_max_limit - st.session_state.credit_allocated_debt)

# Instantiate State Object Instance
state_controller = EnterpriseStateEngine()
state_controller.initialize_state_matrices()

# ==========================================
# 4. SIDEBAR IDENTITY MANAGEMENT & NAV MATRIX
# ==========================================
with st.sidebar:
    st.markdown(f"""
        <div class="premium-profile-box">
            <img src="{st.session_state.meta_profile_avatar}" class="premium-avatar">
            <div class="premium-profile-name">{st.session_state.meta_profile_name}</div>
            <div style="font-size:0.95rem; color:#7C3AED; font-weight:600; margin-top:2px;">{st.session_state.meta_profile_phone}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Operational Domain Engine")
    navigation_intent = st.radio("Execute View Route:", [
        "💼 Control Center Dashboard", 
        "🏛️ High-Value Catalog Ledger", 
        "🛒 High-Fidelity Checkout Core", 
        "📊 Capital Allocation & Credit Desk", 
        "📑 Audit-Trail Settlement Ledger",
        "⚙️ Core Identity Infrastructure"
    ])
    
    st.markdown("---")
    st.markdown("### Real-Time Financial Liquidity View")
    st.metric("Liquid Cash Holdings", f"₹{st.session_state.wallet_funds:,.2f}")
    if st.session_state.tier_pro_max_active:
        st.success("👑 Shopito Pro Max Profile Deployed")
        st.metric("Available Capital Runway", f"₹{state_controller.dynamic_available_credit:,.2f}")

# ==========================================
# ROUTE 1: CONTROL CENTER DASHBOARD
# ==========================================
if navigation_intent == "💼 Control Center Dashboard":
    if st.session_state.dashboard_animation_trigger:
        st.balloons()
        st.session_state.dashboard_animation_trigger = False
        
    st.title("Shopito Enterprise Control Center")
    
    st.markdown("""
        <div class="marquee-banner">
            🚀 ENTERPRISE PROTOCOLS ACTIVE: Dynamic Tier-Scaling Solutions & Capital Injections Enabled.
        </div>
    """, unsafe_allow_html=True)
    
    col_dash_1, col_dash_2, col_dash_3 = st.columns(3)
    with col_dash_1:
        st.markdown("""<div class="financial-metric-container">""", unsafe_allow_html=True)
        st.markdown('<p class="fin-label">System Tier Clearance</p>', unsafe_allow_html=True)
        if st.session_state.tier_pro_max_active:
            st.markdown('<p class="fin-val" style="color:#7C3AED;">👑 Pro Max Enterprise</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="fin-val">Standard Consumer</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_dash_2:
        st.markdown("""<div class="financial-metric-container">""", unsafe_allow_html=True)
        st.markdown('<p class="fin-label">Cart Structural Units</p>', unsafe_allow_html=True)
        total_units = sum(st.session_state.cart_quantities_map.values())
        st.markdown(f'<p class="fin-val">{total_units} Active Items</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_dash_3:
        st.markdown("""<div class="financial-metric-container">""", unsafe_allow_html=True)
        st.markdown('<p class="fin-label">Active Capital Index</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="fin-val">₹{st.session_state.wallet_funds:,.2f}</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# ROUTE 2: HIGH-VALUE CATALOG LEDGER
# ==========================================
elif navigation_intent == "🏛️ High-Value Catalog Ledger":
    st.title("Global Asset Matrix Ledger")
    st.session_state.dashboard_animation_trigger = True
    
    catalog_query = st.selectbox("Isolate Category View Model:", ["Display Complete Catalog", "Isolated Enterprise Electronics", "Isolated Luxury Mechanical Watch Units"])
    
    render_pipeline = []
    if catalog_query == "Display Complete Catalog" or catalog_query == "Isolated Enterprise Electronics":
        render_pipeline.extend(GLOBAL_PRODUCT_REGISTRY["electronics"])
    if catalog_query == "Display Complete Catalog" or catalog_query == "Isolated Luxury Mechanical Watch Units":
        render_pipeline.extend(GLOBAL_PRODUCT_REGISTRY["watches"])
        
    for asset in render_pipeline:
        st.markdown('<div class="matrix-card">', unsafe_allow_html=True)
        img_col, description_col, pipeline_controls_col = st.columns([1, 2, 1])
        
        with img_col:
            st.image(asset["img"], use_container_width=True)
        with description_col:
            st.markdown(f"### {asset['name']}")
            st.markdown(f'<p style="color:#6D28D9; font-weight:700; margin:0;">ASSET EVALUATION ID: {asset["id"].upper()}</p>', unsafe_allow_html=True)
            st.markdown(f'<p style="font-size:1.8rem; font-weight:900; color:#1E1B4B; margin-top:5px;">₹{asset["price"]:,.2f}</p>', unsafe_allow_html=True)
        with pipeline_controls_col:
            current_unit_depth = st.session_state.cart_quantities_map.get(asset["id"], 0)
            st.markdown(f"State Unit Vector Allocation: **{current_unit_depth}**")
            
            c_btn_1, c_btn_2 = st.columns(2)
            with c_btn_1:
                if current_unit_depth < 20:
                    if st.button("➕ Increment", key=f"add_{asset['id']}"):
                        st.session_state.cart_quantities_map[asset["id"]] = current_unit_depth + 1
                        st.rerun()
            with c_btn_2:
                if current_unit_depth > 0:
                    if st.button("➖ Decrement", key=f"sub_{asset['id']}"):
                        st.session_state.cart_quantities_map[asset["id"]] = current_unit_depth - 1
                        if st.session_state.cart_quantities_map[asset["id"]] == 0:
                            del st.session_state.cart_quantities_map[asset["id"]]
                        st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# ROUTE 3: HIGH-FIDELITY CHECKOUT CORE
# ==========================================
elif navigation_intent == "🛒 High-Fidelity Checkout Core":
    st.title("Consolidated Liability Ledger Settlement Matrix")
    st.session_state.dashboard_animation_trigger = True
    
    if not st.session_state.cart_quantities_map:
        st.info("System Alert: Transaction data pipeline empty. No liabilities detected.")
    else:
        aggregated_liability = 0.0
        st.markdown("### Current Valuation Stream Breakdown")
        
        for lookup_id, unit_volume in list(st.session_state.cart_quantities_map.items()):
            target_entity = lookup_system_entity(lookup_id)
            if target_entity:
                sub_total_liability = target_entity["price"] * unit_volume
                aggregated_liability += sub_total_liability
                
                b_col1, b_col2, b_col3, b_col4 = st.columns([3, 1, 1, 1])
                with b_col1: st.markdown(f"**{target_entity['name']}**")
                with b_col2: st.markdown(f"₹{target_entity['price']:,.2f}")
                with b_col3: st.markdown(f"Units: **{unit_volume}**")
                with b_col4:
                    if st.button("🗑️ Purge Line", key=f"purge_line_{lookup_id}"):
                        del st.session_state.cart_quantities_map[lookup_id]
                        st.rerun()
                st.markdown("<hr style='margin: 8px 0; border: 0; border-top: 1px solid #F3E8FF;'/>", unsafe_allow_html=True)
                
        st.markdown(f"## Net Settlement Overhead: **₹{aggregated_liability:,.2f}**")
        
        st.markdown("### Choose Financial Settlement Instrument Gateway")
        selected_instrument = st.radio("Asset Pool:", ["Liquid Core Cash Pools", "Pro Max Strategic Credit Allocation Engine"])
        
        if st.button("Authorize Core Escrow Release & Finalize Settlement Sequence"):
            if selected_instrument == "Liquid Core Cash Pools":
                if st.session_state.wallet_funds >= aggregated_liability:
                    st.session_state.wallet_funds -= aggregated_liability
                    st.session_state.transaction_ledger_records.append({
                        "id": f"TXN-{int(time.time())}",
                        "amount": aggregated_liability,
                        "instrument": "Liquid Core Cash Pool",
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    })
                    st.session_state.cart_quantities_map = {}
                    st.success("🎉 Escrow Release Authorization Confirmed! Transaction appended to ledger.")
                    st.rerun()
                else:
                    st.error("❌ Settlement Failure: Insufficient baseline liquid allocation reserves.")
            elif selected_instrument == "Pro Max Strategic Credit Allocation Engine":
                if not st.session_state.tier_pro_max_active:
                    st.error("❌ Escrow Refusal: Selected account structure lacks active high-tier strategic credit privileges.")
                else:
                    if state_controller.dynamic_available_credit >= aggregated_liability:
                        st.session_state.credit_allocated_debt += aggregated_liability
                        st.session_state.transaction_ledger_records.append({
                            "id": f"TXN-{int(time.time())}",
                            "amount": aggregated_liability,
                            "instrument": "0% Interest Credit Allocation",
                            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                        })
                        st.session_state.cart_quantities_map = {}
                        st.success("🎉 Escrow Release Authorization Confirmed! Corporate debt line tracking updated.")
                        st.rerun()
                    else:
                        st.error("❌ Settlement Failure: Requested overhead exceeds allowable net credit headroom limits.")

# ==========================================
# ROUTE 4: CAPITAL ALLOCATION & CREDIT DESK
# ==========================================
elif navigation_intent == "📊 Capital Allocation & Credit Desk":
    st.title("Advanced Financial Desk & Vault Architecture")
    st.session_state.dashboard_animation_trigger = True
    
    pane_1, pane_2 = st.columns(2)
    
    with pane_1:
        st.markdown("## 🪙 Liquid Reserves Vault")
        st.metric("Total Asset Valuation Level", f"₹{st.session_state.wallet_funds:,.2f}")
        
        st.markdown("---")
        st.markdown("### Cryptographic Capital Injector Node")
        admin_gate_key = st.text_input("Execute Security Level Override Token:", type="password")
        
        # CHANGED TO ALLOW DYNAMIC CAPITAL INJECTION ANY AMOUNT YOU WANT
        if admin_gate_key == "1234":
            st.success("🔒 Authorization Token Accepted. Advanced Injection Controls Mounted Below:")
            injection_quantum = st.number_input("Input Custom Capital Inflow Quantum (₹):", min_value=1.0, max_value=500000000.0, value=100000.0, step=50000.0)
            if st.button("Execute Stream Injection to Active Wallet"):
                st.session_state.wallet_funds += injection_quantum
                st.success(f"⚡ Allocation Engine Confirmed: Successfully added ₹{injection_quantum:,.2f} to liquid cash pools.")
                st.rerun()
        elif admin_gate_key != "":
            st.error("❌ Cryptographic Exception: Signature Mismatch. Injection matrix remains locked.")
            
    with pane_2:
        st.markdown("## 👑 Shopito Pro Max Privilege Portal")
        if not st.session_state.tier_pro_max_active:
            st.warning("Current Account Status Matrix: Standard Base Rank")
            st.markdown("""
                **Procurement Metrics for Pro Max Enterprise Access Architecture:**
                * **Operational Overhead Asset Purchase:** ₹1,00,00,000.00 (₹1 Crore)
                * **Unlocks Framework Feature:** Dynamic Activation of the Permanent **₹10 Lakhs Interest-Free Corporate Credit Facility**.
            """)
            if st.button("Purchase and Deploy Pro Max Framework Tier"):
                if st.session_state.wallet_funds >= 10000000.0:
                    st.session_state.wallet_funds -= 10000000.0
                    st.session_state.tier_pro_max_active = True
                    st.session_state.credit_max_limit = 1000000.0  # Deploy ₹10 Lakh Line
                    st.success("👑 Subscription Loop Completed: Shopito Pro Max features fully provisioned.")
                    st.rerun()
                else:
                    st.error("❌ Infrastructure Exception: Insufficient liquidity holdings available to settle transaction processing.")
        else:
            st.success("👑 System Clearance Level: Pro Max Active Framework Authorized")
            st.metric("Gross Credit Cap Allocation", f"₹{st.session_state.credit_max_limit:,.2f}")
            st.metric("Utilized Debt Drawdown Stack", f"₹{st.session_state.credit_allocated_debt:,.2f}")
            st.metric("Net Operational Headroom Runway", f"₹{state_controller.dynamic_available_credit:,.2f}")

# ==========================================
# ROUTE 5: AUDIT-TRAIL SETTLEMENT LEDGER
# ==========================================
elif navigation_intent == "📑 Audit-Trail Settlement Ledger":
    st.title("Audit Trail System Registry Logs")
    st.session_state.dashboard_animation_trigger = True
    
    if not st.session_state.transaction_ledger_records:
        st.info("System Tracking Note: Zero immutable operational sequence frames logged in current pipeline loops.")
    else:
        formal_audit_frame = pd.DataFrame(st.session_st)
