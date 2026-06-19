import streamlit as pd
import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="Shopito Corporate Marketplace", 
    page_icon="🛍️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Global CSS Styling (Unified Theme, Larger Fonts, Professional Layout) ---
st.markdown("""
    <style>
        /* Global font adjustments */
        html, body, [class*="css"] {
            font-size: 17px !important;
        }
        h1 { font-size: 2.5rem !important; font-weight: 700 !important; color: #1E293B; }
        h2 { font-size: 1.8rem !important; font-weight: 600 !important; color: #334155; }
        h3 { font-size: 1.4rem !important; font-weight: 600 !important; color: #475569; }
        
        /* Profile Section styling */
        .profile-container {
            text-align: center;
            padding: 15px;
            background-color: #F8FAFC;
            border-radius: 12px;
            margin-bottom: 20px;
            border: 1px solid #E2E8F0;
        }
        .profile-pic {
            width: 110px;
            height: 110px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 10px;
            border: 3px solid #3B82F6;
        }
        .profile-name {
            font-weight: bold;
            font-size: 1.2rem;
            color: #1E293B;
        }
        
        /* Advertisement Banner */
        .ad-banner {
            background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 1.5rem;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        
        /* Product Card */
        .product-card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        
        /* Price tag formatting vertically upward */
        .price-label {
            font-size: 0.9rem;
            color: #64748B;
            text-transform: uppercase;
            margin-bottom: -5px;
        }
        .price-value {
            font-size: 1.4rem;
            font-weight: bold;
            color: #0F172A;
        }
    </style>
""", unsafe_allow_html=True)

# --- Session State Initialization ---
if 'wallet_balance' not in st.session_state:
    st.session_state.wallet_balance = 50000.0
if 'credit_limit' not in st.session_state:
    st.session_state.credit_limit = 0.0
if 'credit_used' not in st.session_state:
    st.session_state.credit_used = 0.0
if 'is_pro_max' not in st.session_state:
    st.session_state.is_pro_max = False
if 'cart' not in st.session_state:
    st.session_state.cart = {}  # {product_id: quantity}
if 'settled_orders' not in st.session_state:
    st.session_state.settled_orders = []
if 'just_opened_dashboard' not in st.session_state:
    st.session_state.just_opened_dashboard = True

# Profile Defaults
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Krishna Kumar"
if 'user_phone' not in st.session_state:
    st.session_state.user_phone = "+91 98765 43210"
if 'user_pfp' not in st.session_state:
    st.session_state.user_pfp = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=80"

# --- Mock Marketplace Catalog ---
CATALOG = {
    "electronics": [
        {"id": "macbook_16", "name": "Apple MacBook Pro 16\" (M3 Max, 48GB)", "price": 349900.0, "img": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"},
        {"id": "iphone_15", "name": "Apple iPhone 15 Pro Max Titanium", "price": 159900.0, "img": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400"},
        {"id": "sony_wh1000", "name": "Sony WH-1000XM5 Wireless Headphones", "price": 29990.0, "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"}
    ],
    "watches": [
        {"id": "tourbillon_chrono", "name": "Mechanical Tourbillon Chronograph", "price": 850000.0, "img": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=400"}
    ]
}

def get_product_by_id(pid):
    for cat in CATALOG.values():
        for prod in cat:
            if prod["id"] == pid:
                return prod
    return None

# --- SIDEBAR: Profile & Navigation ---
with st.sidebar:
    # Large, explicit profile space
    st.markdown(f"""
        <div class="profile-container">
            <img src="{st.session_state.user_pfp}" class="profile-pic">
            <div class="profile-name">{st.session_state.user_name}</div>
            <div style="font-size:0.85rem; color:#64748B;">{st.session_state.user_phone}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Navigation")
    page = st.radio("Go to:", [
        "🏠 Dashboard Home", 
        "📦 Product Marketplace", 
        "🛒 Checkout Cart", 
        "💳 Wallet & Credit Centre", 
        "📝 Settled Orders Log",
        "👤 Account Settings"
    ])
    
    st.markdown("---")
    # Quick Status Indicators
    st.metric("Wallet Balance", f"₹{st.session_state.wallet_balance:,.2f}")
    if st.session_state.is_pro_max:
        st.success("👑 Shopito Pro Max Active")
        available_credit = st.session_state.credit_limit - st.session_state.credit_used
        st.metric("Available Credit", f"₹{available_credit:,.2f}")


# --- PAGE 1: DASHBOARD HOME ---
if page == "🏠 Dashboard Home":
    # Birthday Popper Celebration Effect (triggers once when entering dashboard)
    if st.session_state.just_opened_dashboard:
        st.balloons()
        st.session_state.just_opened_dashboard = False
        
    st.title("Welcome to Shopito Dashboard")
    
    # Professional Dynamic Ad Banner
    st.markdown("""
        <div class="ad-banner">
            💥 SHOPITO MEGA SALE IS LIVE! Up to 40% Off on Premium Electronics & Luxury Timepieces! 💥
        </div>
    """, unsafe_allow_html=True)
    
    # Overview Layout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### Active Premium Status")
        if st.session_state.is_pro_max:
            st.markdown("**Plan:** Shopito Pro Max<br>**Access Level:** Fully Authorized Escrow & Interest-free Credit System", unsafe_allow_html=True)
        else:
            st.markdown("Standard Account. Upgrade to **Shopito Pro Max** to unlock the ₹10 Lakhs Interest-Free Credit System.", unsafe_allow_html=True)
            
    with col2:
        st.info("### Your Cart Quickview")
        total_items = sum(st.session_state.cart.values())
        st.markdown(f"**Total unique items:** {len(st.session_state.cart)}<br>**Total quantity:** {total_items} items", unsafe_allow_html=True)
        
    with col3:
        st.info("### Premium Club")
        if not st.session_state.is_pro_max:
            if st.button("Explore Shopito Pro Max"):
                st.info("Head over to the Wallet & Credit Centre to subscribe!")
        else:
            st.markdown("✅ You have full access to premium tiers.")


# --- PAGE 2: PRODUCT MARKETPLACE ---
elif page == "📦 Product Marketplace":
    st.title("Shopito Premium Marketplace Catalog")
    st.session_state.just_opened_dashboard = True # reset popper for next visit
    
    # Category Selection
    category = st.selectbox("Filter by Category:", ["All Categories", "Electronics", "Luxury Mechanical Timepieces"])
    
    items_to_show = []
    if category == "All Categories" or category == "Electronics":
        items_to_show.extend(CATALOG["electronics"])
    if category == "All Categories" or category == "Luxury Mechanical Timepieces":
        items_to_show.extend(CATALOG["watches"])
        
    # Render Products Grid
    for item in items_to_show:
        with st.container():
            st.markdown(f'<div class="product-card">', unsafe_allow_html=True)
            c1, c2, c3 = st.columns([1, 2, 1])
            
            with c1:
                st.image(item["img"], use_container_width=True)
                
            with c2:
                st.markdown(f"### {item['name']}")
                st.markdown('<p class="price-label">Price</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="price-value">₹{item["price"]:,.2f}</p>', unsafe_allow_html=True)
                
            with c3:
                # Cart management system
                current_qty = st.session_state.cart.get(item["id"], 0)
                st.write(f"In Cart: **{current_qty}**")
                
                # Add Option (Finite to 20 items maximum)
                if current_qty < 20:
                    if st.button(f"➕ Add to Cart", key=f"add_{item['id']}"):
                        st.session_state.cart[item["id"]] = current_qty + 1
                        st.rerun()
                else:
                    st.caption("Maximum quantity limit reached (20).")
                    
                # Remove Option
                if current_qty > 0:
                    if st.button(f"➖ Remove One", key=f"rem_{item['id']}"):
                        st.session_state.cart[item["id"]] = current_qty - 1
                        if st.session_state.cart[item["id"]] == 0:
                            del st.session_state.cart[item["id"]]
                        st.rerun()
                        
            st.markdown('</div>', unsafe_allow_html=True)


# --- PAGE 3: CHECKOUT CART ---
elif page == "🛒 Checkout Cart":
    st.title("Your Checkout Cart")
    st.session_state.just_opened_dashboard = True
    
    if not st.session_state.cart:
        st.warning("Your cart is currently empty. Head over to the Marketplace to add products!")
    else:
        grand_total = 0.0
        
        # Table list of Cart items
        st.markdown("### Reviewed Items")
        
        for pid, qty in list(st.session_state.cart.items()):
            prod = get_product_by_id(pid)
            if prod:
                item_total = prod["price"] * qty
                grand_total += item_total
                
                c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
                with c1:
                    st.markdown(f"**{prod['name']}**")
                with c2:
                    st.markdown(f"₹{prod['price']:,.2f}")
                with c3:
                    # Clean proper quantity column representation, no repeating text lines
                    st.markdown(f"**Qty: {qty}**")
                with c4:
                    if st.button("🗑️ Remove All", key=f"del_all_{pid}"):
                        del st.session_state.cart[pid]
                        st.rerun()
                st.markdown("---")
                
        st.markdown(f"### Total Payable Amount: **₹{grand_total:,.2f}**")
        
        # Payment Gateway Choice Layout
        st.markdown("### Choose Payment Source")
        payment_method = st.radio("Select Payment Option:", ["Standard Wallet Balance", "Pro Max Corporate Credit Line"])
        
        if st.button("Confirm Order and Settle Escrow"):
            if payment_method == "Standard Wallet Balance":
                if st.session_state.wallet_balance >= grand_total:
                    st.session_state.wallet_balance -= grand_total
                    st.session_state.settled_orders.append({
                        "id": f"ORD-{int(time.time())}",
                        "amount": grand_total,
                        "method": "Wallet",
                        "status": "Authorized & Released"
                    })
                    st.session_state.cart = {}
                    st.success("🎉 Payment successfully authorized via Wallet! Order has been moved to the Settled Log.")
                else:
                    st.error("❌ Insufficient funds inside standard wallet balance framework.")
                    
            elif payment_method == "Pro Max Corporate Credit Line":
                if not st.session_state.is_pro_max:
                    st.error("❌ Unauthorized. You need a Shopito Pro Max Subscription to use the credit line.")
                else:
                    available_credit = st.session_state.credit_limit - st.session_state.credit_used
                    if available_credit >= grand_total:
                        st.session_state.credit_used += grand_total
                        st.session_state.settled_orders.append({
                            "id": f"ORD-{int(time.time())}",
                            "amount": grand_total,
                            "method": "Interest-Free Credit",
                            "status": "Authorized & Released"
                        })
                        st.session_state.cart = {}
                        st.success("🎉 Payment successfully authorized via Credit! Order has been moved to the Settled Log.")
                    else:
                        st.error("❌ Insufficient credit limit available.")


# --- PAGE 4: WALLET & CREDIT CENTRE ---
elif page == "💳 Wallet & Credit Centre":
    st.title("Authorized Financial Centre")
    st.session_state.just_opened_dashboard = True
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🪙 Personal Wallet Details")
        st.metric("Available Wallet Balance", f"₹{st.session_state.wallet_balance:,.2f}")
        
        # Pin code secret bonus feature
        st.markdown("---")
        st.markdown("#### Secure Wallet Bonus Token")
        pin_input = st.text_input("Enter authorized authorization PIN code:", type="password")
        if st.button("Verify & Claim Bonus"):
            if pin_input == "1234":
                st.session_state.wallet_balance += 1000000.0  # Rs 10 Lakh
                st.success("⚡ Access Granted! ₹10,000,000.00 (₹10 Lakhs) loaded into your wallet balance successfully.")
                st.rerun()
            else:
                st.error("❌ Invalid PIN code credential.")
                
    with col2:
        st.markdown("### 👑 Shopito Pro Max Corporate Line")
        if not st.session_state.is_pro_max:
            st.warning("You are currently using a Standard Profile Tier.")
            st.markdown("""
                **Upgrade to Shopito Pro Max Subscription**
                * **Cost:** ₹1,00,00,000.00 (₹1 Crore)
                * **Benefit:** Grants instant perpetual access to the **₹10 Lakhs Interest-Free Credit System**.
            """)
            if st.button("Purchase Subscription (₹1 Crore)"):
                if st.session_state.wallet_balance >= 10000000.0:
                    st.session_state.wallet_balance -= 10000000.0
                    st.session_state.is_pro_max = True
                    st.session_state.credit_limit = 1000000.0 # Rs 10 Lakhs Credit Limit
                    st.success("👑 Congratulations! You are now a Shopito Pro Max member. ₹10 Lakhs Credit Line unlocked.")
                    st.rerun()
                else:
                    st.error("❌ Insufficient Wallet Balance to buy the premium tier subscription.")
        else:
            st.success("👑 Shopito Pro Max Tier Active")
            st.metric("Total Credit Limit", f"₹{st.session_state.credit_limit:,.2f}")
            st.metric("Credit Used", f"₹{st.session_state.credit_used:,.2f}")
            st.metric("Remaining Available Credit", f"₹{(st.session_state.credit_limit - st.session_state.credit_used):,.2f}")
            st.caption("Interest Rate: 0.00% Fixed (Perpetual)")


# --- PAGE 5: SETTLED ORDERS LOG ---
elif page == "📝 Settled Orders Log":
    st.title("Settled Orders Log")
    st.session_state.just_opened_dashboard = True
    st.markdown("Below is the formal ledger of all historically processed and authorized corporate escrow orders.")
    
    if not st.session_state.settled_orders:
        st.info("No orders settled in this cycle yet.")
    else:
        # Dynamic formal presentation table
        import pandas as pd_library
        df = pd_library.DataFrame(st.session_state.settled_orders)
        df.columns = ["Order Reference ID", "Authorized Total Amount (INR)", "Payment Settlement Mode", "Escrow Verification Status"]
        st.dataframe(df, use_container_width=True, hide_index=True)


# --- PAGE 6: ACCOUNT SETTINGS ---
elif page == "👤 Account Settings":
    st.title("Account & Profile Access Hub")
    st.session_state.just_opened_dashboard = True
    
    st.markdown("### Edit Profile Identification Credentials")
    
    new_name = st.text_input("Account Holder Full Name:", value=st.session_state.user_name)
    new_phone = st.text_input("Registered Contact Number:", value=st.session_state.user_phone)
    new_pfp = st.text_input("Profile Picture Web URL Link:", value=st.session_state.user_pfp)
    
    if st.button("Save Profile Modifications"):
        st.session_state.user_name = new_name
        st.session_state.user_phone = new_phone
        st.session_state.user_pfp = new_pfp
        st.success("📁 Account profile architecture updated successfully across the platform!")
        st.rerun()

st.sidebar.markdown("""
---
<div style='text-align: center; font-size: 0.8rem; color: #94A3B8;'>
    Shopito Corporate Suite v2.0<br>जय राधे कृष्ण
</div>
""", unsafe_allow_html=True)
    
