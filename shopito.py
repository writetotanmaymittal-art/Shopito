import streamlit as st
import pandas as pd
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Shopito Corporate Marketplace", 
    page_icon="🛍️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Complex Theme & Global Style Sheet (Premium Purple Enterprise Theme) ---
st.markdown("""
    <style>
        /* Global Font Hierarchy & Sizing Rules */
        html, body, [class*="css"] {
            font-size: 18px !important;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        h1 { font-size: 2.6rem !important; font-weight: 700 !important; color: #4C1D95; }
        h2 { font-size: 1.9rem !important; font-weight: 600 !important; color: #5B21B6; }
        h3 { font-size: 1.5rem !important; font-weight: 600 !important; color: #6D28D9; }
        
        /* Profile Management Sidebar Container */
        .profile-container {
            text-align: center;
            padding: 20px;
            background: linear-gradient(145deg, #F3E8FF, #FAE8FF);
            border-radius: 16px;
            margin-bottom: 25px;
            border: 1px solid #E9D5FF;
            box-shadow: 0 4px 6px -1px rgba(109, 40, 217, 0.1);
        }
        .profile-pic {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 12px;
            border: 4px solid #7C3AED;
            box-shadow: 0 0 10px rgba(124, 58, 237, 0.3);
        }
        .profile-name {
            font-weight: 700;
            font-size: 1.3rem;
            color: #4C1D95;
        }
        
        /* Premium Live Enterprise Advertisement Banner */
        .ad-banner {
            background: linear-gradient(135deg, #4C1D95 0%, #7C3AED 50%, #C084FC 100%);
            color: white;
            padding: 25px;
            border-radius: 14px;
            text-align: center;
            font-weight: 800;
            font-size: 1.6rem;
            margin-bottom: 30px;
            box-shadow: 0 10px 15px -3px rgba(124, 58, 237, 0.3);
            border: 1px solid #A78BFA;
        }
        
        /* High-Fidelity Product Card Framework */
        .product-card {
            background: #FFFFFF;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #F3E8FF;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
            margin-bottom: 25px;
            transition: all 0.3s ease;
        }
        .product-card:hover {
            box-shadow: 0 10px 15px rgba(109, 40, 217, 0.08);
            border-color: #DDD6FE;
        }
        
        /* Professional Price Layout Engine */
        .price-label {
            font-size: 0.95rem;
            color: #7C3AED;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 2px;
            font-weight: 600;
        }
        .price-value {
            font-size: 1.6rem;
            font-weight: 800;
            color: #1E1B4B;
        }
    </style>
""", unsafe_allow_html=True)

# --- Enterprise Application Core State Manager ---
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 50000.0
if 'credit_limit' not in st.session_state:
    st.session_state.credit_limit = 0.0
if 'credit_used' not in st.session_state:
    st.session_state.credit_used = 0.0
if 'is_pro_max' not in st.session_state:
    st.session_state.is_pro_max = False
if 'cart_dict' not in st.session_state:
    st.session_state.cart_dict = {}  # Safe mapping architecture for tracking item quantities
if 'settled_orders' not in st.session_state:
    st.session_state.settled_orders = []
if 'trigger_celebration' not in st.session_state:
    st.session_state.trigger_celebration = True

# Account Holder Profile Defaults
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Krishna Kumar"
if 'user_phone' not in st.session_state:
    st.session_state.user_phone = "+91 98765 43210"
if 'user_pfp' not in st.session_state:
    st.session_state.user_pfp = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400"

# --- Comprehensive Unified Marketplace Catalog ---
MARKETPLACE_CATALOG = {
    "electronics": [
        {"id": "macbook_16", "name": "Apple MacBook Pro 16\" (M3 Max, 48GB, 1TB SSD)", "price": 349900.0, "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"},
        {"id": "iphone_15", "name": "Apple iPhone 15 Pro Max Titanium Edition", "price": 159900.0, "img": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400"},
        {"id": "sony_wh1000", "name": "Sony WH-1000XM5 Premium Noise Cancelling Headphones", "price": 29990.0, "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"}
    ],
    "watches": [
        {"id": "tourbillon_chrono", "name": "Luxury Mechanical Tourbillon Chronograph Timepiece", "price": 850000.0, "img": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=400"}
    ]
}

def resolve_catalog_product(product_id):
    for category_list in MARKETPLACE_CATALOG.values():
        for product in category_list:
            if product["id"] == product_id:
                return product
    return None

# --- SIDEBAR NAV: Account Profile & Navigation Controller ---
with st.sidebar:
    # Dedicated Account Holder Access Profile Display
    st.markdown(f"""
        <div class="profile-container">
            <img src="{st.session_state.user_pfp}" class="profile-pic">
            <div class="profile-name">{st.session_state.user_name}</div>
            <div style="font-size:0.9rem; color:#6B28D9; font-weight:500;">{st.session_state.user_phone}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Navigation Matrix")
    selected_view = st.radio("Navigate to:", [
        "🏠 Dashboard Management Hub", 
        "📦 Enterprise Product Catalog", 
        "🛒 Consolidated Shopping Cart", 
        "💳 Multi-Tier Wallet & Credit Engine", 
        "📝 Authorized Settlement Ledger",
        "👤 Profile Access Configuration"
    ])
    
    st.markdown("---")
    # Live Real-time Asset Metrics
    st.metric("Liquid Wallet Balance", f"₹{st.session_state.wallet_balance:,.2f}")
    if st.session_state.is_pro_max:
        st.success("👑 Shopito Pro Max Authorized")
        net_credit_available = st.session_state.credit_limit - st.session_state.credit_used
        st.metric("Available Interest-Free Credit", f"₹{net_credit_available:,.2f}")


# --- PAGE 1: DASHBOARD MANAGEMENT HUB ---
if selected_view == "🏠 Dashboard Management Hub":
    # High-impact Birthday Popper Explosion System (Triggers automatically upon opening dashboard)
    if st.session_state.trigger_celebration:
        st.balloons()
        st.session_state.trigger_celebration = False
        
    st.title("Welcome to Shopito Corporate Dashboard")
    
    # Live Marketing Run Banner
    st.markdown("""
        <div class="ad-banner">
            🚀 EXCLUSIVE SHOPITO OPENING SPECIALS: Premium Access Tiers and Luxury Assets Are Now Live! 🚀
        </div>
    """, unsafe_allow_html=True)
    
    # Summary Dashboard Layout Matrix
    d_col1, d_col2, d_col3 = st.columns(3)
    with d_col1:
        st.info("### Core Access Tier Status")
        if st.session_state.is_pro_max:
            st.markdown("**Current Plan:** Shopito Pro Max<br>**System Access:** Full Premium Authorization & Interest-free Credit Activated", unsafe_allow_html=True)
        else:
            st.markdown("**Current Plan:** Standard Account Tier<br>Upgrade to *Shopito Pro Max* to activate the ₹10 Lakhs Interest-Free Credit Framework.", unsafe_allow_html=True)
            
    with d_col2:
        st.info("### Cart Summary Data")
        net_units = sum(st.session_state.cart_dict.values())
        st.markdown(f"**Unique Stock Keeping Units:** {len(st.session_state.cart_dict)} lines<br>**Gross Units Allocated:** {net_units} pieces", unsafe_allow_html=True)
        
    with d_col3:
        st.info("### Premium Options")
        if not st.session_state.is_pro_max:
            st.markdown("Subscribe to access immediate interest-free capital liquidity options.")
        else:
            st.markdown("✅ All high-limit credit and payment settlement architectures are fully accessible.")


# --- PAGE 2: ENTERPRISE PRODUCT CATALOG ---
elif selected_view == "📦 Enterprise Product Catalog":
    st.title("Shopito Premium Marketplace Catalog")
    st.session_state.trigger_celebration = True  # Queue celebration poppers for next dashboard visit
    
    market_filter = st.selectbox("Select Marketplace Category Matrix:", ["All Categorized Verticals", "Premium Consumer Electronics", "Luxury Mechanical Timepieces"])
    
    render_pool = []
    if market_filter == "All Categorized Verticals" or market_filter == "Premium Consumer Electronics":
        render_pool.extend(MARKETPLACE_CATALOG["electronics"])
    if market_filter == "All Categorized Verticals" or market_filter == "Luxury Mechanical Timepieces":
        render_pool.extend(MARKETPLACE_CATALOG["watches"])
        
    for item in render_pool:
        st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
        col_img, col_desc, col_actions = st.columns([1.2, 2, 1])
        
        with col_img:
            st.image(item["img"], use_container_width=True)
            
        with col_desc:
            st.markdown(f"### {item['name']}")
            st.markdown('<p class="price-label">MSRP Value</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="price-value">₹{item["price"]:,.2f}</p>', unsafe_allow_html=True)
            
        with col_actions:
            allocated_units = st.session_state.cart_dict.get(item["id"], 0)
            st.markdown(f"Allocated in Cart: **{allocated_units}**")
            
            # Formally Isolated Modification Controllers
            if allocated_units < 20:
                if st.button(f"➕ Add Unit", key=f"inc_{item['id']}"):
                    st.session_state.cart_dict[item["id"]] = allocated_units + 1
                    st.rerun()
            else:
                st.caption("Maximum unit allocation cap reached (20).")
                
            if allocated_units > 0:
                if st.button(f"➖ Remove Unit", key=f"dec_{item['id']}"):
                    st.session_state.cart_dict[item["id"]] = allocated_units - 1
                    if st.session_state.cart_dict[item["id"]] == 0:
                        del st.session_state.cart_dict[item["id"]]
                    st.rerun()
                    
        st.markdown('</div>', unsafe_allow_html=True)


# --- PAGE 3: CONSOLIDATED SHOPPING CART ---
elif selected_view == "🛒 Consolidated Shopping Cart":
    st.title("Your Consolidated Shopping Cart Ledger")
    st.session_state.trigger_celebration = True
    
    if not st.session_state.cart_dict:
        st.warning("Your transaction queue is empty. Please add items from the Enterprise Product Catalog.")
    else:
        calculated_grand_total = 0.0
        st.markdown("### Itemization Review Matrix")
        
        for p_id, unit_qty in list(st.session_state.cart_dict.items()):
            target_product = resolve_catalog_product(p_id)
            if target_product:
                line_total = target_product["price"] * unit_qty
                calculated_grand_total += line_total
                
                row_c1, row_c2, row_c3, row_c4 = st.columns([3, 1.2, 1, 1])
                with row_c1:
                    st.markdown(f"**{target_product['name']}**")
                with row_c2:
                    st.markdown(f"₹{target_product['price']:,.2f} each")
                with row_c3:
                    st.markdown(f"**Qty: {unit_qty}**")
                with row_c4:
                    if st.button("🗑️ Purge Item", key=f"purge_{p_id}"):
                        del st.session_state.cart_dict[p_id]
                        st.rerun()
                st.markdown("---")
                
        st.markdown(f"### Total Settlement Liability: **₹{calculated_grand_total:,.2f}**")
        
        st.markdown("### Select Payment Gateway Authorization Route")
        selected_route = st.radio("Authorization Source:", ["Standard Wallet Balance Core", "Pro Max Corporate Credit Facility"])
        
        if st.button("Execute Settlement & Authorize Escrow Release"):
            if selected_route == "Standard Wallet Balance Core":
                if st.session_state.wallet_balance >= calculated_grand_total:
                    st.session_state.wallet_balance -= calculated_grand_total
                    st.session_state.settled_orders.append({
                        "order_id": f"SPO-{int(time.time())}",
                        "amount": calculated_grand_total,
                        "mode": "Wallet Balance",
                        "status": "Settled & Released"
                    })
                    st.session_state.cart_dict = {}
                    st.success("🎉 Thank you for shopping from ShopClues Framework! Payment authorized and order logged.")
                else:
                    st.error("❌ Settlement Failed: Insufficient funds inside the wallet balance framework.")
                    
            elif selected_route == "Pro Max Corporate Credit Facility":
                if not st.session_state.is_pro_max:
                    st.error("❌ Settlement Denied: Your account profile does not possess Pro Max Credit Access authorization.")
                else:
                    current_credit_headroom = st.session_state.credit_limit - st.session_state.credit_used
                    if current_credit_headroom >= calculated_grand_total:
                        st.session_state.credit_used += calculated_grand_total
                        st.session_state.settled_orders.append({
                            "order_id": f"SPO-{int(time.time())}",
                            "amount": calculated_grand_total,
                            "mode": "0% Interest Corporate Credit",
                            "status": "Settled & Released"
                        })
                        st.session_state.cart_dict = {}
                        st.success("🎉 Thank you for shopping from ShopClues Framework! Premium Credit Settlement authorized successfully.")
                    else:
                        st.error("❌ Settlement Failed: Requested allocation exceeds your maximum available credit line headroom.")


# --- PAGE 4: MULTI-TIER WALLET & CREDIT CENTRE ---
elif selected_view == "💳 Multi-Tier Wallet & Credit Engine":
    st.title("Authorized Financial Liquidity Centre")
    st.session_state.trigger_celebration = True
    
    col_wallet, col_credit = st.columns(2)
    
    with col_wallet:
        st.markdown("## 🪙 Core Wallet Details")
        st.metric("Available Wallet Cash Reserves", f"₹{st.session_state.wallet_balance:,.2f}")
        
        st.markdown("---")
        st.markdown("### Secure Wallet Capital Injection Portal")
        auth_pin = st.text_input("Provide Administrator Authorization Key Code:", type="password")
        if st.button("Verify Key & Inject Liquidity"):
            if auth_pin == "1234":
                st.session_state.wallet_balance += 1000000.0  # Rs 10 Lakh manual injection
                st.success("⚡ Capital Injector Success: ₹10,000,000.00 successfully allocated to active liquid asset state.")
                st.rerun()
            else:
                st.error("❌ Security Warning: Invalid authorization token credential provided.")
                
    with col_credit:
        st.markdown("## 👑 Sopito Pro Max Premium Segment")
        if not st.session_state.is_pro_max:
            st.warning("Account Classification Status: Standard Access Profile Tier")
            st.markdown("""
                **Procure Shopito Pro Max Subscription Infrastructure**
                * **Capital Expenditure Requirement:** ₹1,00,00,000.00 (₹1 Crore)
                * **System Benefits Granted:** Activates permanent authorization for the **₹10 Lakhs Interest-Free Corporate Credit Framework**.
            """)
            if st.button("Purchase Pro Max Access (₹1 Crore)"):
                if st.session_state.wallet_balance >= 10000000.0:
                    st.session_state.wallet_balance -= 10000000.0
                    st.session_state.is_pro_max = True
                    st.session_state.credit_limit = 1000000.0  # ₹10 Lakh Limit Loaded
                    st.success("👑 Subscription Success: Sopito Pro Max Tier Active. ₹10 Lakhs Interest-Free Credit Facility fully deployed.")
                    st.rerun()
                else:
                    st.error("❌ Transaction Denied: Insufficient wallet cash allocation to execute the premium tier subscription purchase.")
        else:
            st.success("👑 Premium Access Status: Shopito Pro Max Active")
            st.metric("Total Corporate Credit Allocation", f"₹{st.session_state.credit_limit:,.2f}")
            st.metric("Utilized Debt Allocation", f"₹{st.session_state.credit_used:,.2f}")
            st.metric("Net Available Credit Headroom", f"₹{(st.session_state.credit_limit - st.session_state.credit_used):,.2f}")
            st.caption("Interest Rate Matrix: 0.00% Fixed Perpetual Interest System")


# --- PAGE 5: AUTHORIZED SETTLEMENT LEDGER ---
elif selected_view == "📝 Authorized Settlement Ledger":
    st.title("Authorized Settlement Order Log")
    st.session_state.trigger_celebration = True
    st.markdown("Formal, real estate standard operational ledger logging finalized transaction receipts.")
    
    if not st.session_state.settled_orders:
        st.info("No transaction sequences have finalized processing loops in this current session.")
    else:
        ledger_dataframe = pd.DataFrame(st.session_state.settled_orders)
        ledger_dataframe.columns = ["Order Reference ID", "Settled Liability (INR)", "Payment Architecture Mode", "Escrow Status Code"]
        st.dataframe(ledger_dataframe, use_container_width=True, hide_index=True)


# --- PAGE 6: PROFILE ACCESS CONFIGURATION ---
elif selected_view == "👤 Profile Access Configuration":
    st.title("Account Holder Role & Access Configuration Hub")
    st.session_state.trigger_celebration = True
    
    st.markdown("### Modify Identity Management Credentials")
    
    modified_name = st.text_input("Account Holder Verified Legal Name:", value=st.session_state.user_name)
    modified_phone = st.text_input("Registered Telephony Network Endpoint:", value=st.session_state.user_phone)
    modified_pfp = st.text_input("Identity Profile Image Asset Web URL Link:", value=st.session_state.user_pfp)
    
    if st.button("Commit Profile Transformations"):
        st.session_state.user_name = modified_name
        st.session_state.user_phone = modified_phone
        st.session_state.user_pfp = modified_pfp
        st.success("📁 Identity Profile configuration rewritten across the database registry framework!")
        st.rerun()

# --- Professional Global Signature Footnote ---
st.sidebar.markdown("""
---
<div style='text-align: center; font-size: 0.85rem; color: #7C3AED; font-weight: 600;'>
    Shopito Corporate Suite v3.2<br>जय राधे कृष्ण
</div>
""", unsafe_allow_html=True)
