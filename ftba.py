import streamlit as st
from datetime import datetime

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Pocket Affirmation Card",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# CUSTOM CSS — Cream, Elegant, Sacred Feel
# ─────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background — cream */
    .stApp {
        background: linear-gradient(180deg, #FFF8E7 0%, #FDF3DC 100%);
    }

    /* Main container */
    .main .block-container {
        max-width: 720px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Header card */
    .header-card {
        background: #FFFFFF;
        border: 2px solid #D4AF37;
        border-radius: 16px;
        padding: 24px 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(212, 175, 55, 0.15);
        margin-bottom: 24px;
    }
    .header-title {
        font-family: Georgia, serif;
        font-size: 1.5rem;
        color: #4A3F2A;
        letter-spacing: 2px;
        margin: 0;
        font-weight: 700;
    }
    .header-sub {
        font-family: Georgia, serif;
        font-size: 0.95rem;
        color: #8B7355;
        font-style: italic;
        margin-top: 8px;
    }

    /* Section cards */
    .section-card {
        background: #FFFFFF;
        border-left: 5px solid #D4AF37;
        border-radius: 12px;
        padding: 18px 22px;
        margin-bottom: 16px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    }
    .section-title {
        font-family: Georgia, serif;
        font-size: 1.05rem;
        color: #8B6F2A;
        letter-spacing: 1.5px;
        font-weight: 700;
        margin: 0 0 10px 0;
    }
    .section-body {
        font-family: Georgia, serif;
        font-size: 0.98rem;
        color: #3D3323;
        line-height: 1.7;
        margin: 0;
    }
    .section-body em {
        color: #8B6F2A;
        font-style: italic;
    }
    .bold-line {
        color: #4A3F2A;
        font-weight: 700;
        display: block;
        margin-top: 8px;
    }

    /* HRCM grid */
    .hrcm-item {
        font-family: Georgia, serif;
        font-size: 0.95rem;
        color: #3D3323;
        padding: 6px 0;
        border-bottom: 1px dashed #E8D9A8;
    }
    .hrcm-item:last-child { border-bottom: none; }
    .hrcm-key { color: #8B6F2A; font-weight: 700; }

    /* Vow card */
    .vow-card {
        background: linear-gradient(135deg, #FFFDF6 0%, #FBF0D2 100%);
        border: 2px dashed #D4AF37;
        border-radius: 12px;
        padding: 20px 22px;
        margin-bottom: 16px;
        text-align: center;
    }
    .vow-title {
        font-family: Georgia, serif;
        color: #8B6F2A;
        font-size: 1.05rem;
        letter-spacing: 1.5px;
        font-weight: 700;
        margin-bottom: 12px;
    }
    .vow-body {
        font-family: Georgia, serif;
        color: #4A3F2A;
        font-size: 0.98rem;
        line-height: 1.8;
        margin: 0;
    }

    /* Footer seal */
    .footer-seal {
        background: #4A3F2A;
        color: #FFF8E7;
        border-radius: 12px;
        padding: 22px 20px;
        text-align: center;
        margin-top: 24px;
        box-shadow: 0 6px 24px rgba(74, 63, 42, 0.25);
    }
    .footer-seal-title {
        font-family: Georgia, serif;
        font-size: 1.15rem;
        letter-spacing: 2px;
        font-weight: 700;
        margin: 0;
    }
    .footer-seal-body {
        font-family: Georgia, serif;
        font-size: 0.92rem;
        font-style: italic;
        color: #E8D9A8;
        margin-top: 10px;
        line-height: 1.6;
    }
    .footer-sign {
        font-family: Georgia, serif;
        font-size: 0.9rem;
        color: #D4AF37;
        margin-top: 12px;
        font-style: italic;
    }

    /* Greeting banner */
    .greeting {
        text-align: center;
        font-family: Georgia, serif;
        color: #8B6F2A;
        font-size: 1rem;
        font-style: italic;
        margin-bottom: 18px;
    }

    /* Hide Streamlit default footer */
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }

    /* Print button styling */
    .stButton > button {
        background: #4A3F2A;
        color: #FFF8E7;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-family: Georgia, serif;
        font-size: 1rem;
        letter-spacing: 1px;
        width: 100%;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background: #8B6F2A;
        color: #FFFFFF;
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(74, 63, 42, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# GREETING BASED ON TIME OF DAY
# ─────────────────────────────────────────────
hour = datetime.now().hour
if hour < 12:
    greeting = "🌅 Good Morning — Begin with stillness."
elif hour < 17:
    greeting = "☀️ Good Afternoon — Pause. Breathe. Return."
else:
    greeting = "🌙 Good Evening — Reflect and rest."

st.markdown(f'<p class="greeting">{greeting}</p>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-card">
    <p class="header-title">✦ POCKET AFFIRMATION CARD ✦</p>
    <p class="header-sub">Fold. Carry. Read 3× Daily.</p>
    <p class="header-sub" style="margin-top: 14px; color: #4A3F2A; font-style: normal; font-weight: 700;">
        I AM BECOMING THE PERSON<br>I WAS BORN TO BE.
    </p>
    <p class="header-sub" style="font-size: 0.85rem;">
        Not by force. Not by luck. By daily, deliberate design.
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SECTION: FEELING
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <p class="section-title">🌿 FEELING</p>
    <p class="section-body">
        I feel, but I am not my feelings.<br>
        Anxiety visits — I don't let it stay.<br>
        Fear knocks — I open, and it shrinks.
        <span class="bold-line">I am calm. I am centered. I am still.</span>
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SECTION: THOUGHT
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <p class="section-title">💭 THOUGHT</p>
    <p class="section-body">
        I release the need to be right.<br>
        <em>"What if I'm 10% wrong?"</em><br>
        Their opinion is data, not verdict.
        <span class="bold-line">I think clearly. I think freely.</span>
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SECTION: BELIEF
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <p class="section-title">🕊️ BELIEF</p>
    <p class="section-body">
        I am worthy of ₹2 Lakhs/month.<br>
        I am reliable to authority.<br>
        I am a peaceful resolver.<br>
        I am valuable. My voice matters.
        <span class="bold-line">I believe in my becoming.</span>
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SECTION: ACTION
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <p class="section-title">⚡ ACTION</p>
    <p class="section-body">
        I speak once — clearly, kindly.<br>
        I don't gossip — I elevate.<br>
        I face authority with respect, not fear.<br>
        I take one fearless step daily.
        <span class="bold-line">I act. I build. I become.</span>
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SECTION: HRCM
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <p class="section-title">🎯 MY HRCM</p>
    <div class="hrcm-item"><span class="hrcm-key">🌿 Health</span> → Peace is my priority.</div>
    <div class="hrcm-item"><span class="hrcm-key">🤝 Relationship</span> → Respect. Listen. Love.</div>
    <div class="hrcm-item"><span class="hrcm-key">💼 Career</span> → I solve problems fearlessly.</div>
    <div class="hrcm-item"><span class="hrcm-key">💰 Money</span> → ₹2L/month. Baleno. Self-reliant.</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SECTION: DAILY VOW
# ─────────────────────────────────────────────
st.markdown("""
<div class="vow-card">
    <p class="vow-title">✦ DAILY VOW ✦</p>
    <p class="vow-body">
        I am not faking. I am becoming.<br>
        Every breath — a reset.<br>
        Every word — a seed.<br>
        Every action — a brick.<br>
        <strong>Building my Baleno life, one calm day at a time.</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SECTION: MORNING
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <p class="section-title">🌅 MORNING</p>
    <p class="section-body">
        Today I choose:<br>
        Peace over proving.<br>
        Clarity over confusion.<br>
        Courage over comfort.<br>
        Service over self-doubt.
        <span class="bold-line">One step closer to ₹2L. One step closer to me.</span>
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SECTION: NIGHT
# ─────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <p class="section-title">🌙 NIGHT</p>
    <p class="section-body">
        I did my best.<br>
        I forgive my stumbles.<br>
        I release what I can't control.<br>
        I rest in gratitude.
        <span class="bold-line">Tomorrow, I rise calmer, clearer, stronger.</span>
    </p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FOOTER SEAL
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer-seal">
    <p class="footer-seal-title">✦ I AM THE AUTHOR OF MY LIFE ✦</p>
    <p class="footer-seal-body">
        The pen is in my hand. The page is blank.<br>
        I write a beautiful story — starting now.
    </p>
    <p class="footer-sign">— Your Future Self</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# INTERACTIVE: 30-SECOND RITUAL TRACKER
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🌿 30-Second Daily Ritual")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🌅 Morning\nRead Aloud", use_container_width=True):
        st.success("✅ Morning ritual complete. You are calm.")
with col2:
    if st.button("☀️ Midday\nCheck HRCM", use_container_width=True):
        st.info("🧭 Ask: Am I living my HRCM today?")
with col3:
    if st.button("🌙 Night\nGratitude", use_container_width=True):
        st.success("🌙 One breath of gratitude. Rest well.")

# ─────────────────────────────────────────────
# STREAK COUNTER (Session-based)
# ─────────────────────────────────────────────
if "streak" not in st.session_state:
    st.session_state.streak = 0

if st.button("✨ Mark Today Complete (+1 Streak)", use_container_width=True):
    st.session_state.streak += 1
    st.balloons()
    st.success(f"🔥 Streak: {st.session_state.streak} day(s). Keep becoming!")

st.caption(f"🔥 Current Streak: **{st.session_state.streak} day(s)**")

# ─────────────────────────────────────────────
# PRINTABLE VIEW TOGGLE
# ─────────────────────────────────────────────
with st.expander("🖨️ Print / Save as PDF Instructions"):
    st.markdown("""
    **To save this as PDF:**
    1. Press `Ctrl + P` (Windows) or `Cmd + P` (Mac)
    2. Choose **Save as PDF**
    3. Paper size: **A6 or A5** (pocket fit)
    4. Margins: **Narrow**
    5. Enable **Background graphics**
    6. Save & print 3 copies → wallet, desk, car
    """)

st.markdown("<br>", unsafe_allow_html=True)
st.caption("🌿 Speak it until you believe it. Believe it until you live it. Live it until you become it.")
