import streamlit as st
import base64

# 1. EMISSION LOGIC: Voice Synthesis Engine via Browser Injection
def speak(text):
    """Injects native browser text-to-speech without local dependencies."""
    js_code = f"""
    <script>
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            var msg = new SpeechSynthesisUtterance('{text}');
            msg.rate = 1.0;
            msg.volume = 1.0;
            window.speechSynthesis.speak(msg);
        }}
    </script>
    """
    st.components.v1.html(js_code, height=0, width=0)

# 2. APPLICATION INITIALIZATION & PURPLE-WHITE VISUAL MATRIX
st.set_page_config(
    page_title="Shopito Pro Sandbox",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Strict Premium Purple & Bright White Block Styling Matrix
st.markdown("""
    <style>
        /* Base Background Configurations */
        .stApp {
            background-color: #FFFFFF;
            color: #1E1B4B;
        }
        /* Sidebar System Layout */
        [data-testid="stSidebar"] {
            background-color: #4C1D95 !important;
        }
        [data-testid="stSidebar"] *, [data-testid="stSidebar"] p {
            color: #FFFFFF !important;
        }
        /* Amazon Style Functional Container Blocks */
        .amazon-block {
            background-color: #F8F6FC;
            border: 2px solid #E4E0F3;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgba(76, 29, 149, 0.05);
        }
        /* Primary Transaction Buttons */
        .stButton>button {
            background-gradient: linear-gradient(135deg, #6D28D9 0%, #4C1D95 100%);
            background-color: #6D28D9;
            color: white !important;
            border-radius: 12px;
            border: none;
            padding: 10px 24px;
            font-weight: 700;
            width: 100%;
            transition: all 0.2s ease;
        }
        .stButton>button:hover {
            background-color: #4C1D95;
            box-shadow: 0 4px 12px rgba(109, 40, 217, 0.3);
        }
        h1, h2, h3 {
            color: #4C1D95 !important;
            font-weight: 800 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. LOCAL DATA CORE: Real-Time Live Amazon Inventories
if "wallet" not in st.session_state:
    st.session_state.wallet = 10000000.00
if "cart" not in st.session_state:
    st.session_state.cart = []
if "orders" not in st.session_state:
    st.session_state.orders = []
if "last_page" not in st.session_state:
    st.session_state.last_page = None

products = [
    {"id": "p1", "name": "Apple iPhone 15 Pro Max Titanium (1TB)", "price": 159900, "category": "Smartphones", "desc": "Aerospace-grade titanium design with the groundbreaking A17 Pro chip."},
    {"id": "p2", "name": "Helios Mechanical Tourbillon Chronograph", "price": 1250000, "category": "Chronographs", "desc": "Intricate luxury watch engineering tracking precise custom mechanics."},
    {"id": "p3", "name": "Sony WH-1000XM5 Wireless Headphones", "price": 29990, "category": "Audio", "desc": "Industry-leading noise cancellation engineered for perfect sound clarity."},
    {"id": "p4", "name": "MacBook Pro 16-inch M3 Max (48GB)", "price": 349900, "category": "Computers", "desc": "Extreme computing power with liquid retina XDR ultra-fluid display framework."}
]

# 4. MULTI-PAGE ROUTING MATRIX
st.sidebar.title("🛍️ Shopito Navigation")
st.sidebar.markdown(f"### 💳 Wallet: **₹{st.session_state.wallet:,.2f}**")

page = st.sidebar.radio(
    "Select Interface Menu Node:",
    ["Dashboard Home", "Amazon Catalogue", "Checkout Cart", "Settled Orders Log"]
)

# Menu Voice Trigger: Fires when user selects a different option
if page != st.session_state.last_page:
    st.session_state.last_page = page
    speak(f"Welcome to Shopito {page}")

# --- PAGE 1: DASHBOARD HOME ---
if page == "Dashboard Home":
    st.title("Welcome to Shopito Pro")
    st.markdown("##### Direct Real-Time Multi-Page System Shell")
    
    st.markdown("""
        <div class="amazon-block">
            <h3>🚀 Sovereign Sandbox Controller Active</h3>
            <p>This application operates as a standalone server application, avoiding all 403 Google Document structural permission blocks. 
               Use the side navigation panel to seamlessly toggle between application logic segments.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🔥 Featured Luxury Assets")
    cols = st.columns(2)
    for idx, p in enumerate(products[:2]):
        with cols[idx]:
            st.markdown(f"""
                <div class="amazon-block">
                    <h4>{p['name']}</h4>
                    <p style='color:#6B7280; font-size:14px;'>{p['desc']}</p>
                    <h3 style='color:#6D28D9;'>₹{p['price']:,}</h3>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"Quick Add {p['name']}", key=f"home_{p['id']}"):
                st.session_state.cart.append(p)
                speak(f"{p['name']} added to cart.")
                st.toast("Item pushed to cart stack!", icon="✅")

# --- PAGE 2: AMAZON CATALOGUE ---
elif page == "Amazon Catalogue":
    st.title("Consolidated Product Catalogue")
    st.write("Live structural rendering of production items.")
    
    for p in products:
        st.markdown(f"""
            <div class="amazon-block">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="background-color: #E4E0F3; color: #4C1D95; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold;">{p['category']}</span>
                        <h4 style="margin-top: 8px; margin-bottom: 4px;">{p['name']}</h4>
                        <p style="color: #4B5563; font-size: 13px; margin: 0;">{p['desc']}</p>
                    </div>
                    <div style="text-align: right; min-width: 200px;">
                        <h3 style="margin: 0 0 10px 0; color: #4C1D95;">₹{p['price']:,}</h3>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Add to Basket Stack 🛒", key=f"cat_{p['id']}"):
            st.session_state.cart.append(p)
            speak(f"{p['name']} queued.")
            st.toast("Inventory matrix updated successfully.", icon="🛒")

# --- PAGE 3: CHECKOUT CART ---
elif page == "Checkout Cart":
    st.title("Your Processing Escrow Cart")
    
    if not st.session_state.cart:
        st.info("Your application cart is currently empty.")
    else:
        total_cost = sum(item['price'] for item in st.session_state.cart)
        
        st.markdown(f"""
            <div class="amazon-block" style="border-left: 5px solid #6D28D9;">
                <h4>Escrow Statement Valuation</h4>
                <p>Accumulated Items Count: <b>{len(st.session_state.cart)}</b></p>
                <h2>Total Due: ₹{total_cost:,}.00</h2>
            </div>
        """, unsafe_allow_html=True)
        
        for idx, item in enumerate(st.session_state.cart):
            st.markdown(f"""
                <div style="padding: 10px; border-bottom: 1px solid #E4E0F3; display: flex; justify-content: space-between;">
                    <span>{item['name']}</span>
                    <b>Streamlit Cost: ₹{item['price']:,}</b>
                </div>
            """, unsafe_allow_html=True)
            
        st.write("---")
        
        # Delivery Form Blocks
        st.text_input("Full Legal Consignee Name")
        st.text_input("Terminal Destination Address Coordinate")
        
        if st.button("Authorize Escrow Settlement"):
            if st.session_state.wallet >= total_cost:
                st.session_state.wallet -= total_cost
                st.session_state.orders.append({
                    "id": f"SHP-{idx}992",
                    "value": total_cost,
                    "items_count": len(st.session_state.cart)
                })
                st.session_state.cart = []
                speak("Thank you for shopping.")
                st.success("Escrow pipeline cleared successfully!")
                st.balloons()
            else:
                speak("Insufficient balance inside sandbox framework wallet.")
                st.error("Transaction declined due to inadequate funds execution limits.")

# --- PAGE 4: SETTLED ORDERS LOG ---
elif page == "Settled Orders Log":
    st.title("Cryptographic Settlement Register")
    
    if not st.session_state.orders:
        st.markdown("<p style='color:gray;'>No localized historical records verified yet.</p>", unsafe_allowed_html=True)
    else:
        for order in st.session_state.orders:
            st.markdown(f"""
                <div class="amazon-block" style="border-left: 5px solid #10B981;">
                    <div style="display: flex; justify-content: space-between;">
                        <div>
                            <span style="color:#10B981; font-weight:bold;">🟢 VERIFIED SETTLED NODE</span>
                            <h4>ID: {order['id']}</h4>
                            <p style="margin:0; color:gray;">Bundled Items: {order['items_count']}</p>
                        </div>
                        <h2>₹{order['value']:,}.00</h2>
                    </div>
                </div>
            """, unsafe_allow_html=True)
