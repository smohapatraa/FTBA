import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objects as go
from gtts import gTTS
from io import BytesIO

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Pocket Affirmation · Sacred Daily Ritual",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# AUTHENTICATION GATE
# ─────────────────────────────────────────────
def check_password():
    """Returns True if the user entered the correct username + password."""

    if st.session_state.get("authenticated", False):
        return True

    login_css = (
        "<style>"
        ".login-wrap{max-width:420px;margin:60px auto 0 auto;padding:40px 32px;"
        "background:#1E1A14;border:2px solid #4A3E22;"
        "border-radius:20px;box-shadow:0 16px 48px rgba(0,0,0,0.5);text-align:center;}"
        ".login-title{font-family:'Cormorant Garamond',serif;font-size:2rem;"
        "font-weight:700;color:#F5EBD8;margin:0 0 8px 0;letter-spacing:1px;}"
        ".login-sub{font-family:'Cormorant Garamond',serif;font-size:1.05rem;"
        "font-style:italic;color:#D4C8A8;margin:0 0 24px 0;}"
        ".login-divider{width:80px;height:1px;background:linear-gradient(90deg,"
        "transparent,#E8B96A,transparent);margin:16px auto 24px auto;}"
        "</style>"
    )
    st.markdown(login_css, unsafe_allow_html=True)

    st.markdown(
        '<div class="login-wrap">'
        '<p class="login-title">🌿 Pocket Affirmation</p>'
        '<p class="login-sub">A Sacred Daily Ritual</p>'
        '<div class="login-divider"></div>'
        '</div>',
        unsafe_allow_html=True,
    )

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input(
            "Username",
            key="username_input",
            placeholder="Enter your username",
        )
        password = st.text_input(
            "Password",
            key="password_input",
            type="password",
            placeholder="Enter your password",
        )
        submitted = st.form_submit_button("🔓 Unlock", use_container_width=True)

    if submitted:
        try:
            stored_passwords = st.secrets["passwords"]
            if username in stored_passwords and stored_passwords[username] == password:
                st.session_state["authenticated"] = True
                st.session_state["current_user"] = username
                st.session_state["auth_error"] = ""
                st.rerun()
            else:
                st.session_state["authenticated"] = False
                st.session_state["auth_error"] = "Invalid username or password."
        except Exception as e:
            st.session_state["authenticated"] = False
            st.session_state["auth_error"] = f"Auth error: {e}"

    if st.session_state.get("auth_error"):
        st.error(st.session_state["auth_error"])

    st.caption("🔒 This app is private. Only authorized users may enter.")
    return False


if not check_password():
    st.stop()

# ─────────────────────────────────────────────
# MONTHLY FINANCIAL TARGETS
# ─────────────────────────────────────────────
MONTHLY_TARGETS = [
    ("2026-10", "Oct 2026", 18_00_000),
    ("2026-11", "Nov 2026", 19_00_000),
    ("2026-12", "Dec 2026", 20_00_000),
    ("2027-01", "Jan 2027", 21_00_000),
    ("2027-02", "Feb 2027", 22_00_000),
    ("2027-03", "Mar 2027", 23_00_000),
    ("2027-04", "Apr 2027", 24_00_000),
    ("2027-05", "May 2027", 25_00_000),
    ("2027-06", "Jun 2027", 26_00_000),
    ("2027-07", "Jul 2027", 27_00_000),
    ("2027-08", "Aug 2027", 28_00_000),
    ("2027-09", "Sep 2027", 29_00_000),
    ("2027-10", "Oct 2027", 30_00_000),
    ("2027-11", "Nov 2027", 31_00_000),
    ("2027-12", "Dec 2027", 32_00_000),
    ("2028-01", "Jan 2028", 33_00_000),
    ("2028-02", "Feb 2028", 34_00_000),
    ("2028-03", "Mar 2028", 35_00_000),
    ("2028-04", "Apr 2028", 36_00_000),
    ("2028-05", "May 2028", 37_00_000),
    ("2028-06", "Jun 2028", 38_00_000),
    ("2028-07", "Jul 2028", 39_00_000),
    ("2028-08", "Aug 2028", 40_00_000),
    ("2028-09", "Sep 2028", 41_00_000),
    ("2028-10", "Oct 2028", 42_00_000),
    ("2028-11", "Nov 2028", 43_00_000),
    ("2028-12", "Dec 2028", 44_00_000),
    ("2029-01", "Jan 2029", 45_00_000),
    ("2029-02", "Feb 2029", 46_00_000),
    ("2029-03", "Mar 2029", 47_00_000),
    ("2029-04", "Apr 2029", 48_00_000),
    ("2029-05", "May 2029", 49_00_000),
]

def format_inr(n):
    s = str(int(n))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail

# ─────────────────────────────────────────────
# CAREER ROADMAP DATA
# ─────────────────────────────────────────────
CAREER_ROADMAP = [
    {
        "Month": "Month 1",
        "Focus": "Environment Setup",
        "Action": "Install Python, set up virtual environments, organize working directories.",
        "Status": "Completed",
    },
    {
        "Month": "Month 2",
        "Focus": "Pandas Data Mastery",
        "Action": "Import and clean raw Excel/CSV data dumps from Tally Prime.",
        "Status": "In Progress",
    },
    {
        "Month": "Month 3",
        "Focus": "Tally ITC Module",
        "Action": "Build automated GSTR-2B vs Purchase Register reconciliation script.",
        "Status": "Pending",
    },
    {
        "Month": "Month 4",
        "Focus": "Auto DMS & Aging Module",
        "Action": "Develop vehicle stock aging and workshop floorplan interest calculator.",
        "Status": "Pending",
    },
    {
        "Month": "Month 5",
        "Focus": "Security & Cloud Prep",
        "Action": "Optimize memory processing for zero data leakage and high confidentiality.",
        "Status": "Pending",
    },
    {
        "Month": "Month 6",
        "Focus": "Odisha Market Pitch",
        "Action": "Network in Angul/Bhubaneswar; secure first 3 retainer clients at ₹70k/month.",
        "Status": "Pending",
    },
]

CAREER_LEAKAGE_SAMPLE = pd.DataFrame({
    "Asset_ID": ["TRUCK-01", "SUV-09", "SPARE-BATCH-X", "RAW-STEEL-LOT"],
    "Category": ["Logistics", "Showroom Auto", "Workshop Parts", "Manufacturing"],
    "Tied_Capital_INR": [4500000, 1200000, 380000, 8500000],
    "Holding_Cost_Per_Month": [22500, 18000, 7600, 42500],
})

# ─────────────────────────────────────────────
# EMBEDDED SACRED TEXTS
# ─────────────────────────────────────────────
HANUMAN_CHALISA_DOHA = {
    "Doha 1": "Shri Guru Charan Saroj Raj, Nij Manu Mukur Sudhaari. Baranau Raghubar Vimal Jas, Jo Daayak Phal Chari.",
    "Doha 2": "Buddhiheen Tanu Jaankai, Sumiron Pavan-Kumar. Bal Buddhi Vidya Dehu Mohin, Harhu Kalesh Vikaari.",
}

HANUMAN_CHALISA_CHAUPAI = [
    "Jai Hanuman Gyaan Gun Saagar, Jai Kapis Tihun Lok Ujaagar.",
    "Ram Doot Atulit Bal Dhaama, Anjani-Putra Pavan-Sut Naama.",
    "Mahabeer Vikram Bajrangi, Kumati Nivaar Sumati Ke Sangi.",
    "Kanchan Varn Biraj Subesa, Kanan Kundal Kunchit Kesa.",
    "Haath Vajra Au Dhwaja Birajai, Kaanhe Moonj Janeu Sajaai.",
    "Shankar Suvan Kesari Nandan, Tej Pratap Maha Jag Vandan.",
    "Vidyaavaan Guni Ati Chatur, Ram Kaaj Karibe Ko Aatur.",
    "Prabhu Charitra Sunibe Ko Rasiya, Ram Lakhan Sita Man Basiya.",
    "Sookshm Roop Dhari Siyaahi Dikhawa, Vikat Roop Dhari Lank Jaraawa.",
    "Bheem Roop Dhari Asur Sanhaare, Ramchandra Ke Kaaj Sanwaare.",
    "Laay Sanjeevani Lakhana Jiyaaye, Shri Raghubeer Harsh Ur Laye.",
    "Raghupati Keenee Bahut Badaai, Tum Mam Priya Bharatahi Sam Bhai.",
    "Sahas Badan Tumharo Yash Gaave, As Kahi Shri-Pati Kanth Lagaaave.",
    "Sanakaadik Brahmaadi Muneesa, Narad Saraswati Sahit Ahisa.",
    "Yam Kuber Dikpaal Jahan Te, Kavi Kobid Kahin Sake Kahan Te.",
    "Tum Upkaar Sugreevahin Keenha, Ram Milaye Raaj Pad Deenha.",
    "Tumharo Mantra Vibhishan Maana, Lankeshwar Bhaye Sab Jag Jaana.",
    "Jug Sahastra Yojan Par Bhanu, Leelyo Taahi Madhur Phal Jaana.",
    "Prabhu Mudrika Meli Mukh Maahi, Jaladhi Laanghi Gaye Acharaj Naahi.",
    "Durgam Kaaj Jagat Ke Jete, Sugam Anugrah Tumhare Tete.",
    "Ram Dware Tum Rakhwaare, Hot Na Aajna Binu Paisare.",
    "Sab Sukh Lahe Tumhaari Sarna, Tum Rakshak Kahu Ko Darna.",
    "Aapan Tej Samhaaro Aapai, Tino Lok Haank Te Kaampai.",
    "Bhoot Pishach Nikat Nahi Aave, Mahaveer Jab Naam Sunave.",
    "Naasai Rog Hare Sab Peera, Japat Nirantar Hanumat Beera.",
    "Sankat Te Hanuman Chudhaave, Man, Karm, Vachan Dhyaan Jo Laave.",
    "Sab Par Ram Tapasvi Raja, Tinke Kaaj Sakal Tum Saaja.",
    "Aur Manorath Jo Koi Laave, Sohi Amit Jeevan Phal Paave.",
    "Chaaron Yug Parataap Tumhaara, Hai Prasiddh Jagat Ujiyaara.",
    "Saadhu Sant Ke Tum Rakhwaare, Asur Nikandan Ram Dulaare.",
    "Asht Siddhi Nav Nidhi Ke Daata, As Var Deen Jaanaki Maata.",
    "Ram Rasayan Tumhare Paasa, Sadaa Raho Raghupati Ke Daasa.",
    "Tumhare Bhajan Ram Ko Paave, Janam Janam Ke Dukh Bisraave.",
    "Antkaal Raghubar Pur Jaai, Jahan Janm Haribhakt Kahai.",
    "Aur Devta Chit Na Dharai, Hanumat Sei Sarv Sukh Karai.",
    "Sankat Katai Mite Sab Peera, Jo Sumirai Hanumat Balbeera.",
    "Jai Jai Jai Hanuman Gosai, Kripa Karahu Gurudev Ki Naai.",
    "Jo Shat Baar Paath Kar Koi, Chhootahi Bandhi Maha Sukh Hoi.",
    "Jo Yah Padhe Hanuman Chalisa, Hoy Siddhi Saakhi Gaurisa.",
    "Tulsidas Sadaa Hari Chera, Keejai Naath Hriday Mah Dera.",
]

HANUMAN_CHALISA_CLOSING = "Pawan Tanay Sankat Haran, Mangal Moorti Roop. Ram Lakhan Sita Sahit, Hriday Basahu Sur Bhoop."

VISHNU_SAHASRANAMA_STOTRAM = [
    "Om Vaasudevah Param Brahma Paramatma Paraatparah, Param Dhaama Paramjyotih Param Tatwam Param Padam.",
    "Parah Shiva Parodhyeyah Param Jnaanam Paraagatih, Paramarthah Parashreshthah Paraanandah Parodayah.",
    "Parovyaktaaparam Vyoma Paramaadthah Pareshwarah, Niraamayo Nirvikaaro Nirvikalpo Niraashrayah.",
    "Niranjano Niraalambo Nirlopo Niravagrahah, Nirguno Nishkalonantobhayochintyochalochintah.",
    "Ateendrayomitopaaro Nityoneehovyayokshayah, Sarvagjnah Sarvagah Sarvabhavanah.",
    "Sarvashastaa Sarvasaakshi Pujyah Sarvasya Sarvadruk, Sarva Shaktih Sarvasaarah Sarvatmaa Sarvatomukhah.",
    "Sarvavaasah Sarvarupah Sarvaadih Sarva Duhkhahaa, Sarvaarthah Sarvatobhadrah Sarvakaaranakaaranam.",
    "Sarvaatishayitah Sarva-adhyakshah Sarveshvareshwarah, Shadvimshako Maha Vishnurmahaaguhyo Maha Vibhuh.",
    "Nityodito Nityayukto Nityaanandah Sanaatanah, Maayaapatiryogapatih Kaivalyapatiraatmabhuh.",
    "Janma-mrityu jaraateetah Kaalaateeto Bhavaatigah, Purnah Satyah Shuddha Buddha Swarupo Nitya-achintan mayah.",
    "Yogapriyo Yogagamyo Bhavabandhaikamochakah, Puraanapurushah Pratyak-chaitanyah Purushottamah.",
    "Vedaanantavedyo Durjayastraapatraya vivarjitah.",
]

VISHNU_SAHASRANAMA_SLOKAS = [
    "Om Namo Naraayanaaya Purushaaya Mahatmaney, Vishuddha Satwaaya Maha Hamsaaya Dheemahi Tanno Devah prachodayat.",
    "Kleem Krishnaaya vidmahey, Hreem Raamaaya dheemahey, Tanno Devah prachodayaat.",
    "Sham Nrisimhaaya vidmahey, Shrikanthaaya dheemahi, Tanno Vishnu prachodayat.",
    "Om Vasudaevaaya vidmahey Devaki sutaaya dheemahi, Tannah Krishnah prachodayat.",
]

# ─────────────────────────────────────────────
# BALENO CNG AGS — FACTS
# ─────────────────────────────────────────────
BALENO_FACTS = {
    "exterior": [
        ("Signature NEXWave Grille", "Chrome slats, Suzuki logo moved to bonnet."),
        ("NEXTre LED DRLs", "Tri-arrow daytime running lamps."),
        ("LED Projector Headlamps", "Zeta and Alpha trims."),
        ("Precision-Cut Alloys", "16-inch dual-tone on Alpha."),
        ("NEXTre Signature LED Tail Lamps", "L-shaped, distinctive at night."),
        ("Shark Fin Antenna", "Roof-mounted, replaces old pole antenna."),
    ],
    "interior": [
        ("Ventilated Front Seats", "Alpha (O) trims."),
        ("SmartPlay Pro+ Infotainment", "9-inch, wireless Android Auto & Apple CarPlay."),
        ("Clarion Premium Audio", "Alpha trims."),
        ("Cooled Wireless Charger", "Qi-certified."),
        ("Head-Up Display (HUD)", "Pop-up display for key info."),
        ("360-Degree Camera", "Top trims."),
    ],
    "cng_ags": [
        ("First in India", "CNG + AGS combination — a first for any Maruti car."),
        ("Engine", "Advanced Z12E 1.2L with Dual VVT and Idle Start-Stop."),
        ("CNG Power", "70 bhp & 101.8 Nm in CNG mode."),
        ("Mileage", "33.61 km/kg (CNG), 24.77 km/l (Petrol AGS)."),
        ("Variants", "Delta CNG AGS (₹8.32L), Zeta CNG AGS (₹9.32L)."),
        ("Transmission", "5-speed AGS (AMT) with manual override."),
    ],
}

# ─────────────────────────────────────────────
# IMAGE LIBRARY
# ─────────────────────────────────────────────
IMAGES = {
    "morning": {
        "hero": "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?w=1200&q=80",
        "caption": "Sunrise over calm waters · Photo by Federico Respini on Unsplash",
        "accent": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&q=80",
        "accent_caption": "Morning meditation · Photo by Jared Rice on Unsplash",
    },
    "afternoon": {
        "hero": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1200&q=80",
        "caption": "Open field, clear sky · Photo by Dawid Zawiła on Unsplash",
        "accent": "https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=800&q=80",
        "accent_caption": "Focused workspace · Photo by Andrew Neel on Pexels",
    },
    "night": {
        "hero": "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=1200&q=80",
        "caption": "Starry night sky · Photo by Jeremy Thomas on Unsplash",
        "accent": "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=800&q=80",
        "accent_caption": "Mountain under stars · Photo by Vincentiu Solomon on Unsplash",
    },
    "hanuman": {
        "hero": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?w=1200&q=80",
        "caption": "Temple lamps · Photo by Ashwini Chaudhary on Unsplash",
        "accent": "https://images.unsplash.com/photo-1600240644455-3edc55c375fe?w=800&q=80",
        "accent_caption": "Hanuman temple · Photo by Ashutosh Gaur on Unsplash",
    },
    "vishnu": {
        "hero": "https://images.unsplash.com/photo-1561365452-adb940139ffa?w=1200&q=80",
        "caption": "Temple architecture · Photo by Unsplash",
        "accent": "https://images.unsplash.com/photo-1545121649-0c8e0c8c8c8c?w=800&q=80",
        "accent_caption": "Sacred geometry · Photo by Unsplash",
    },
    "targets": {
        "hero": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1200&q=80",
        "caption": "Charting the climb · Photo by Lukas on Pexels",
        "accent": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=800&q=80",
        "accent_caption": "Coins stacked · Photo by Micheile Henderson on Unsplash",
    },
    "baleno": {
        "hero": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=1200&q=80",
        "caption": "The drive ahead · Photo by Clem Onojeghuo on Unsplash",
        "accent": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&q=80",
        "accent_caption": "Baleno waiting · Photo by Campbell on Unsplash",
        "exterior_1": "https://images.unsplash.com/photo-1502877338535-766e1452684a?w=800&q=80",
        "exterior_1_caption": "Exterior profile · Photo by Campbell on Unsplash",
        "interior_1": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&q=80",
        "interior_1_caption": "Cabin view · Photo by Campbell on Unsplash",
        "cng_1": "https://images.unsplash.com/photo-1615906655593-ad0386982a0f?w=800&q=80",
        "cng_1_caption": "CNG station · Photo by Artiom Vallat on Unsplash",
    },
    "career": {
        "hero": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1200&q=80",
        "caption": "Strategy in action · Photo by Campaign Creators on Unsplash",
        "accent": "https://images.unsplash.com/photo-1518186285589-2f7649de83e0?w=800&q=80",
        "accent_caption": "Data analytics · Photo by Luke Chesser on Unsplash",
    },
}

# ─────────────────────────────────────────────
# STATE INIT
# ─────────────────────────────────────────────
if "mode" not in st.session_state:
    st.session_state.mode = "morning"
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "completed" not in st.session_state:
    st.session_state.completed = {
        "morning": False,
        "afternoon": False,
        "night": False,
        "hanuman": False,
        "vishnu": False,
    }
if "completion_history" not in st.session_state:
    st.session_state.completion_history = {}
if "auto_set" not in st.session_state:
    hour = datetime.now().hour
    if hour < 12:
        st.session_state.mode = "morning"
    elif hour < 17:
        st.session_state.mode = "afternoon"
    else:
        st.session_state.mode = "night"
    st.session_state.auto_set = True

if "theme" not in st.session_state:
    h = datetime.now().hour
    if 5 <= h < 8:
        st.session_state.theme = "dawn"
    elif 8 <= h < 17:
        st.session_state.theme = "day"
    elif 17 <= h < 20:
        st.session_state.theme = "dusk"
    else:
        st.session_state.theme = "night"

# ─────────────────────────────────────────────
# THEME TOKENS — ALL DARK PALETTES
# ─────────────────────────────────────────────
THEMES = {
    "dawn": {
        "name": "Dawn", "icon": "🌅",
        "cream": "#1A0F14", "cream_deep": "#241620",
        "ink": "#F5E0E8", "ink_soft": "#D4B8C4",
        "gold": "#E89A7C", "gold_soft": "#F5B89C", "gold_pale": "#4A2A30",
        "card": "#261820", "card_soft": "#2E1E28",
        "verse_bg": "linear-gradient(135deg, #261820 0%, #2E1E28 100%)",
        "vow_bg": "linear-gradient(135deg, #2E1E28 0%, #3A2430 100%)",
        "seal_bg": "linear-gradient(135deg, #3A2430 0%, #4A2E3C 100%)",
        "seal_text": "#F5E0E8", "seal_accent": "#F5B89C",
        "body_grad": "radial-gradient(1200px 600px at 50% -10%, #241620 0%, transparent 60%), radial-gradient(800px 400px at 100% 100%, #1A0F14 0%, transparent 50%), linear-gradient(180deg, #1A0F14 0%, #241620 100%)",
        "shadow_sm": "0 2px 12px rgba(0, 0, 0, 0.40)",
        "shadow_md": "0 6px 24px rgba(0, 0, 0, 0.55)",
        "shadow_lg": "0 16px 48px rgba(0, 0, 0, 0.70)",
    },
    "day": {
        "name": "Day", "icon": "☀️",
        "cream": "#12100C", "cream_deep": "#1A1712",
        "ink": "#F5EBD8", "ink_soft": "#D4C8A8",
        "gold": "#D4A857", "gold_soft": "#E8C070", "gold_pale": "#4A3E22",
        "card": "#1E1A14", "card_soft": "#262018",
        "verse_bg": "linear-gradient(135deg, #1E1A14 0%, #262018 100%)",
        "vow_bg": "linear-gradient(135deg, #262018 0%, #2E2618 100%)",
        "seal_bg": "linear-gradient(135deg, #2E2618 0%, #3A3222 100%)",
        "seal_text": "#F5EBD8", "seal_accent": "#E8C070",
        "body_grad": "radial-gradient(1200px 600px at 50% -10%, #1A1712 0%, transparent 60%), radial-gradient(800px 400px at 100% 100%, #12100C 0%, transparent 50%), linear-gradient(180deg, #12100C 0%, #1A1712 100%)",
        "shadow_sm": "0 2px 12px rgba(0, 0, 0, 0.40)",
        "shadow_md": "0 6px 24px rgba(0, 0, 0, 0.55)",
        "shadow_lg": "0 16px 48px rgba(0, 0, 0, 0.70)",
    },
    "dusk": {
        "name": "Dusk", "icon": "🌇",
        "cream": "#14101A", "cream_deep": "#1E1826",
        "ink": "#F0E4F5", "ink_soft": "#C8B8D4",
        "gold": "#D9886A", "gold_soft": "#E8A87C", "gold_pale": "#3E2A42",
        "card": "#221A2C", "card_soft": "#2A2034",
        "verse_bg": "linear-gradient(135deg, #221A2C 0%, #2A2034 100%)",
        "vow_bg": "linear-gradient(135deg, #2A2034 0%, #32263C 100%)",
        "seal_bg": "linear-gradient(135deg, #32263C 0%, #3E2E48 100%)",
        "seal_text": "#F0E4F5", "seal_accent": "#E8A87C",
        "body_grad": "radial-gradient(1200px 600px at 50% -10%, #1E1826 0%, transparent 60%), radial-gradient(800px 400px at 100% 100%, #14101A 0%, transparent 50%), linear-gradient(180deg, #14101A 0%, #1E1826 100%)",
        "shadow_sm": "0 2px 12px rgba(0, 0, 0, 0.40)",
        "shadow_md": "0 6px 24px rgba(0, 0, 0, 0.55)",
        "shadow_lg": "0 16px 48px rgba(0, 0, 0, 0.70)",
    },
    "night": {
        "name": "Night", "icon": "🌙",
        "cream": "#0A0908", "cream_deep": "#12100C",
        "ink": "#F5EBD8", "ink_soft": "#C8BC9C",
        "gold": "#E8B96A", "gold_soft": "#F5C97A", "gold_pale": "#3E3620",
        "card": "#16140F", "card_soft": "#1E1A14",
        "verse_bg": "linear-gradient(135deg, #16140F 0%, #1E1A14 100%)",
        "vow_bg": "linear-gradient(135deg, #1E1A14 0%, #262018 100%)",
        "seal_bg": "linear-gradient(135deg, #262018 0%, #322A1E 100%)",
        "seal_text": "#F5EBD8", "seal_accent": "#F5C97A",
        "body_grad": "radial-gradient(1200px 600px at 50% -10%, #12100C 0%, transparent 60%), radial-gradient(800px 400px at 100% 100%, #0A0908 0%, transparent 50%), linear-gradient(180deg, #0A0908 0%, #12100C 100%)",
        "shadow_sm": "0 2px 12px rgba(0, 0, 0, 0.45)",
        "shadow_md": "0 6px 24px rgba(0, 0, 0, 0.60)",
        "shadow_lg": "0 16px 48px rgba(0, 0, 0, 0.75)",
    },
}

T = THEMES[st.session_state.theme]

# ─────────────────────────────────────────────
# PREMIUM DESIGN SYSTEM — CSS
# ─────────────────────────────────────────────
CSS = (
    "<style>"
    "@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');"
    f":root{{"
    f"--cream:{T['cream']};--cream-deep:{T['cream_deep']};"
    f"--ink:{T['ink']};--ink-soft:{T['ink_soft']};"
    f"--gold:{T['gold']};--gold-soft:{T['gold_soft']};--gold-pale:{T['gold_pale']};"
    f"--card:{T['card']};--card-soft:{T['card_soft']};"
    f"--shadow-sm:{T['shadow_sm']};--shadow-md:{T['shadow_md']};--shadow-lg:{T['shadow_lg']};"
    "}"
    "html,body,[class*='css']{font-family:'Inter',sans-serif;font-size:17px;color:var(--ink);}"
    f".stApp,[data-testid='stAppViewContainer'],[data-testid='stHeader']{{background:{T['body_grad']} !important;background-attachment:fixed;color:var(--ink);}}"
    "[data-testid='stSidebar']{background:var(--card);}"
    ".main .block-container{max-width:800px;padding-top:2rem;padding-bottom:4rem;}"
    ".hero-image-wrap{position:relative;border-radius:20px;overflow:hidden;margin-bottom:24px;box-shadow:var(--shadow-lg);animation:fadeUp 0.6s cubic-bezier(.2,.8,.2,1) both;}"
    ".hero-image-wrap img{width:100%;height:280px;object-fit:cover;display:block;}"
    ".hero-image-wrap .overlay{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0.15) 0%,rgba(0,0,0,0.75) 100%);}"
    ".hero-image-wrap .text{position:absolute;bottom:26px;left:30px;right:30px;color:#FFFDF7;}"
    f".hero-image-wrap .text .eyebrow{{font-size:0.85rem;letter-spacing:3px;text-transform:uppercase;color:{T['gold_soft']};font-weight:600;margin-bottom:10px;}}"
    ".hero-image-wrap .text h2{font-family:'Cormorant Garamond',serif;font-size:2.4rem;font-weight:700;margin:0;line-height:1.15;text-shadow:0 2px 12px rgba(0,0,0,0.7);}"
    f".hero-image-wrap .text h2 .accent{{color:{T['gold_soft']};font-style:italic;}}"
    ".hero-image-wrap .caption{position:absolute;bottom:8px;right:14px;font-size:0.65rem;color:rgba(255,255,255,0.55);}"
    ".hero{text-align:center;padding:8px 0 20px 0;}"
    ".hero-eyebrow{font-size:0.85rem;letter-spacing:4px;text-transform:uppercase;color:var(--gold);font-weight:600;margin-bottom:12px;}"
    ".hero-title{font-family:'Cormorant Garamond',serif;font-size:3rem;font-weight:700;color:var(--ink);line-height:1.1;margin:0;letter-spacing:-0.5px;}"
    ".hero-title .accent{color:var(--gold);font-style:italic;font-weight:600;}"
    ".hero-divider{display:flex;align-items:center;justify-content:center;gap:12px;margin:18px 0 14px 0;color:var(--gold);}"
    ".hero-divider .line{width:70px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);}"
    ".hero-divider .dot{font-size:0.85rem;letter-spacing:6px;}"
    ".hero-sub{font-family:'Cormorant Garamond',serif;font-size:1.2rem;font-style:italic;color:var(--ink-soft);margin:0;}"
    ".ritual-label{text-align:center;font-size:0.85rem;letter-spacing:3px;text-transform:uppercase;color:var(--gold);font-weight:600;margin:10px 0 16px 0;}"
    "div[data-testid='column'] .stButton > button{width:100%;border-radius:16px;padding:22px 14px;border:2px solid transparent;background:var(--card);box-shadow:var(--shadow-sm);font-family:'Cormorant Garamond',serif;font-size:1.25rem;font-weight:600;color:var(--ink);letter-spacing:0.5px;transition:all 0.25s cubic-bezier(.2,.8,.2,1);white-space:pre-line;line-height:1.5;min-height:100px;}"
    "div[data-testid='column'] .stButton > button:hover{transform:translateY(-3px);box-shadow:var(--shadow-md);border-color:var(--gold-soft);color:var(--gold-soft);}"
    "div[data-testid='column'] .stButton > button:focus:not(:active){color:var(--gold-soft);border-color:var(--gold);}"
    ".stButton > button{background:var(--card);color:var(--ink);border:1px solid var(--gold-pale);font-size:1.05rem;padding:14px 18px;border-radius:12px;}"
    ".stButton > button:hover{border-color:var(--gold-soft);color:var(--gold-soft);}"
    ".card{background:var(--card);border-radius:18px;padding:28px 30px;margin:18px 0;box-shadow:var(--shadow-md);border:1px solid var(--gold-pale);animation:fadeUp 0.5s cubic-bezier(.2,.8,.2,1) both;}"
    "@keyframes fadeUp{from{opacity:0;transform:translateY(12px);}to{opacity:1;transform:translateY(0);}}"
    ".card-hero{text-align:center;padding:36px 30px;background:var(--card);border:2px solid var(--gold-pale);}"
    ".card-hero .badge{display:inline-block;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase;color:var(--gold);background:rgba(232,185,106,0.12);padding:8px 16px;border-radius:100px;font-weight:600;margin-bottom:18px;}"
    ".card-hero .salutation{font-family:'Cormorant Garamond',serif;font-size:2.3rem;font-weight:700;color:var(--ink);margin:0 0 10px 0;line-height:1.2;}"
    ".card-hero .salutation .accent{color:var(--gold);font-style:italic;}"
    ".card-hero .prompt{font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-style:italic;color:var(--ink-soft);margin:0;line-height:1.6;}"
    ".section{background:var(--card);border-radius:14px;padding:22px 26px;margin:16px 0;box-shadow:var(--shadow-sm);border-left:4px solid var(--gold);animation:fadeUp 0.5s cubic-bezier(.2,.8,.2,1) both;}"
    ".section h3{font-family:'Cormorant Garamond',serif;font-size:1.3rem;letter-spacing:2px;color:var(--gold);margin:0 0 14px 0;font-weight:700;text-transform:uppercase;}"
    ".section p{font-family:'Cormorant Garamond',serif;font-size:1.25rem;line-height:1.8;color:var(--ink-soft);margin:0;}"
    ".section .bold-line{display:block;font-weight:700;color:var(--ink);margin-top:12px;font-style:italic;font-size:1.3rem;}"
    ".hrcm-row{display:flex;align-items:flex-start;gap:12px;padding:10px 0;font-family:'Cormorant Garamond',serif;font-size:1.25rem;color:var(--ink-soft);border-bottom:1px dashed var(--gold-pale);}"
    ".hrcm-row:last-child{border-bottom:none;}"
    ".hrcm-row .k{color:var(--gold);font-weight:700;min-width:130px;}"
    f".vow{{background:{T['vow_bg']};border:2px dashed var(--gold);border-radius:16px;padding:28px 26px;text-align:center;margin:18px 0;animation:fadeUp 0.5s cubic-bezier(.2,.8,.2,1) both;}}"
    ".vow h3{font-family:'Cormorant Garamond',serif;color:var(--gold);font-size:1.3rem;letter-spacing:3px;text-transform:uppercase;margin:0 0 14px 0;font-weight:700;}"
    ".vow p{font-family:'Cormorant Garamond',serif;font-size:1.25rem;color:var(--ink);line-height:2;margin:0;}"
    f".verse-card{{background:{T['verse_bg']};border-left:4px solid var(--gold);border-radius:12px;padding:20px 24px;margin:12px 0;box-shadow:var(--shadow-sm);animation:fadeUp 0.4s cubic-bezier(.2,.8,.2,1) both;}}"
    ".verse-card .verse-num{font-size:0.85rem;letter-spacing:2px;color:var(--gold);text-transform:uppercase;font-weight:700;margin-bottom:8px;}"
    ".verse-card .verse-text{font-family:'Cormorant Garamond',serif;font-size:1.3rem;line-height:1.75;color:var(--ink);font-style:italic;margin:0;}"
    f".seal{{background:{T['seal_bg']};color:{T['seal_text']};border-radius:18px;padding:34px 30px;text-align:center;margin:30px 0 14px 0;box-shadow:var(--shadow-lg);position:relative;overflow:hidden;}}"
    ".seal::before{content:'';position:absolute;inset:8px;border:1px solid rgba(232,185,106,0.35);border-radius:12px;pointer-events:none;}"
    f".seal h3{{font-family:'Cormorant Garamond',serif;font-size:1.5rem;letter-spacing:3px;color:{T['seal_accent']};margin:0 0 14px 0;font-weight:700;position:relative;}}"
    f".seal p{{font-family:'Cormorant Garamond',serif;font-size:1.25rem;font-style:italic;color:{T['seal_text']};line-height:1.8;margin:0;position:relative;}}"
    f".seal .sign{{font-family:'Cormorant Garamond',serif;color:{T['seal_accent']};font-size:1.1rem;margin-top:16px;letter-spacing:1px;position:relative;}}"
    ".streak-pill{display:inline-flex;align-items:center;gap:10px;background:var(--card);border:1px solid var(--gold-pale);border-radius:100px;padding:12px 24px;font-size:1.05rem;font-weight:500;color:var(--ink-soft);box-shadow:var(--shadow-sm);}"
    ".streak-pill .num{color:var(--gold);font-weight:700;font-size:1.2rem;}"
    ".targets-table{width:100%;border-collapse:collapse;font-family:'Inter',sans-serif;font-size:1.05rem;margin-top:8px;}"
    ".targets-table th{text-align:left;font-family:'Cormorant Garamond',serif;font-size:1.15rem;letter-spacing:2px;text-transform:uppercase;color:var(--gold);font-weight:700;padding:12px 14px;border-bottom:1px solid var(--gold-pale);}"
    ".targets-table td{padding:12px 14px;border-bottom:1px dashed var(--gold-pale);color:var(--ink-soft);}"
    ".targets-table tr:last-child td{border-bottom:none;}"
    ".targets-table .month-col{font-family:'Cormorant Garamond',serif;font-size:1.2rem;color:var(--ink);font-weight:600;}"
    ".targets-table .amount-col{font-family:'Inter',sans-serif;font-size:1.15rem;color:var(--gold);font-weight:600;text-align:right;letter-spacing:0.3px;}"
    ".targets-table tr.current td{background:rgba(232,185,106,0.10);}"
    ".targets-table tr.current .month-col{color:var(--gold);}"
    ".targets-table tr.current .amount-col{color:var(--gold-soft);font-weight:700;}"
    ".targets-table tr.past td{opacity:0.55;}"
    ".target-summary{display:flex;gap:18px;flex-wrap:wrap;margin:8px 0 20px 0;}"
    ".target-chip{flex:1;min-width:160px;background:var(--card);border:1px solid var(--gold-pale);border-radius:14px;padding:16px 20px;text-align:center;box-shadow:var(--shadow-sm);}"
    ".target-chip .label{font-family:'Inter',sans-serif;font-size:0.75rem;letter-spacing:2px;text-transform:uppercase;color:var(--gold);font-weight:600;margin-bottom:6px;}"
    ".target-chip .value{font-family:'Cormorant Garamond',serif;font-size:1.6rem;color:var(--ink);font-weight:700;}"
    ".target-chip .sub{font-size:0.9rem;color:var(--ink-soft);margin-top:4px;}"
    ".stSelectbox label{font-size:1rem !important;color:var(--ink-soft) !important;}"
    ".stCaption,[data-testid='stCaptionContainer']{font-size:0.95rem !important;color:var(--ink-soft) !important;}"
    ".stMarkdown p,.stMarkdown li{font-size:1.05rem;}"
    "footer{visibility:hidden;}#MainMenu{visibility:hidden;}header{visibility:hidden;}"
    "</style>"
)

st.markdown(CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TOP BAR — Logout + User + Theme
# ─────────────────────────────────────────────
top_left, top_mid, top_right = st.columns([2, 1, 1])

with top_mid:
    user = st.session_state.get("current_user", "")
    if user:
        st.caption(f"👤 {user}")

with top_right:
    if st.button("🚪 Logout", key="logout_btn", use_container_width=True):
        st.session_state["authenticated"] = False
        st.session_state["current_user"] = ""
        st.rerun()

# ─────────────────────────────────────────────
# THEME SELECTOR
# ─────────────────────────────────────────────
top_left2, top_right2 = st.columns([3, 2])

with top_right2:
    theme_options = list(THEMES.keys())
    theme_labels = [f"{THEMES[t]['icon']} {THEMES[t]['name']}" for t in theme_options]
    current_idx = theme_options.index(st.session_state.theme)

    selected = st.selectbox(
        "Theme",
        options=range(len(theme_options)),
        format_func=lambda i: theme_labels[i],
        index=current_idx,
        label_visibility="collapsed",
        key="theme_selector",
    )
    if theme_options[selected] != st.session_state.theme:
        st.session_state.theme = theme_options[selected]
        st.rerun()

# ─────────────────────────────────────────────
# HERO HEADER
# ─────────────────────────────────────────────
st.markdown(
    '<div class="hero">'
    '<div class="hero-eyebrow">A Sacred Daily Ritual</div>'
    '<h1 class="hero-title">Pocket <span class="accent">Affirmation</span></h1>'
    '<div class="hero-divider">'
    '<span class="line"></span>'
    '<span class="dot">✦ ✦ ✦</span>'
    '<span class="line"></span>'
    '</div>'
    '<p class="hero-sub">Fold. Carry. Read three times a day.</p>'
    '</div>',
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# RITUAL SELECTOR — 8 BUTTONS
# ─────────────────────────────────────────────
st.markdown('<div class="ritual-label">Choose Your Moment</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌅\nMorning", key="btn_morning", use_container_width=True):
        st.session_state.mode = "morning"
        st.rerun()
with col2:
    if st.button("☀️\nAfternoon", key="btn_afternoon", use_container_width=True):
        st.session_state.mode = "afternoon"
        st.rerun()
with col3:
    if st.button("🌙\nNight", key="btn_night", use_container_width=True):
        st.session_state.mode = "night"
        st.rerun()

st.markdown('<div class="ritual-label" style="margin-top:20px;">Sacred Recitations</div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    if st.button("🙏\nHanuman Chalisa", key="btn_hanuman", use_container_width=True):
        st.session_state.mode = "hanuman"
        st.rerun()
with col5:
    if st.button("🕉️\nVishnu Sahasranama", key="btn_vishnu", use_container_width=True):
        st.session_state.mode = "vishnu"
        st.rerun()

st.markdown('<div class="ritual-label" style="margin-top:20px;">Your Future</div>', unsafe_allow_html=True)

col6, col7, col8 = st.columns(3)

with col6:
    if st.button("🎯\nMonthly Targets", key="btn_targets", use_container_width=True):
        st.session_state.mode = "targets"
        st.rerun()
with col7:
    if st.button("🚗\nBaleno CNG AGS", key="btn_baleno", use_container_width=True):
        st.session_state.mode = "baleno"
        st.rerun()
with col8:
    if st.button("💼\nCareer Roadmap", key="btn_career", use_container_width=True):
        st.session_state.mode = "career"
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HERO IMAGE
# ─────────────────────────────────────────────
mode = st.session_state.mode
img = IMAGES[mode]

EYEBROW = {
    "morning":   "🌅 Morning Ritual",
    "afternoon": "☀️ Midday Reset",
    "night":     "🌙 Night Reflection",
    "hanuman":   "🙏 Hanuman Chalisa",
    "vishnu":    "🕉️ Vishnu Sahasranama",
    "targets":   "🎯 Monthly Financial Targets",
    "baleno":    "🚗 Baleno CNG AGS",
    "career":    "💼 Executive AI Career Roadmap",
}[mode]

HEADLINE = {
    "morning":   'Begin with <span class="accent">stillness</span>.',
    "afternoon": 'Pause. <span class="accent">Breathe</span>. Return.',
    "night":     'Rest now. <span class="accent">You did well</span>.',
    "hanuman":   'Forty verses of <span class="accent">strength</span>.',
    "vishnu":    'The thousand <span class="accent">names</span>.',
    "targets":   'The climb from <span class="accent">18 to 49 Lakhs</span>.',
    "baleno":    'The drive to <span class="accent">your Baleno</span>.',
    "career":    '₹2 Lakhs/month from <span class="accent">Odisha</span>.',
}[mode]

hero_html = (
    '<div class="hero-image-wrap">'
    f'<img src="{img["hero"]}" alt="{mode} hero image">'
    '<div class="overlay"></div>'
    '<div class="text">'
    f'<div class="eyebrow">{EYEBROW}</div>'
    f'<h2>{HEADLINE}</h2>'
    '</div>'
    f'<div class="caption">{img["caption"]}</div>'
    '</div>'
)

st.markdown(hero_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# AUDIO RECITATION — gTTS + st.audio
# ─────────────────────────────────────────────
if mode in ["hanuman", "vishnu"]:
    st.markdown('<div class="ritual-label">🔊 Listen to Recitation</div>', unsafe_allow_html=True)

    if mode == "hanuman":
        recitation_text = (
            " ".join(HANUMAN_CHALISA_DOHA.values())
            + " "
            + " ".join(HANUMAN_CHALISA_CHAUPAI)
            + " "
            + HANUMAN_CHALISA_CLOSING
        )
    else:
        recitation_text = (
            " ".join(VISHNU_SAHASRANAMA_SLOKAS)
            + " "
            + " ".join(VISHNU_SAHASRANAMA_STOTRAM)
        )

    cache_key = f"audio_{mode}"
    if cache_key not in st.session_state:
        st.session_state[cache_key] = None

    col_play, col_clear = st.columns(2)

    with col_play:
        if st.button(
            "▶️ Generate & Play Recitation",
            use_container_width=True,
            key=f"play_{mode}",
        ):
            with st.spinner("Generating audio... (may take a few seconds)"):
                try:
                    tts = gTTS(text=recitation_text[:3000], lang="en", slow=False)
                    audio_buffer = BytesIO()
                    tts.write_to_fp(audio_buffer)
                    audio_buffer.seek(0)
                    st.session_state[cache_key] = audio_buffer.getvalue()
                except Exception as e:
                    st.error(f"Audio generation failed: {e}")

    with col_clear:
        if st.button(
            "🔄 Clear Audio",
            use_container_width=True,
            key=f"clear_{mode}",
        ):
            st.session_state[cache_key] = None
            st.rerun()

    if st.session_state[cache_key] is not None:
        st.audio(st.session_state[cache_key], format="audio/mp3")
        st.caption(
            "Tap ▶️ on the player above to listen. "
            "Use the browser controls to pause or replay."
        )

# ─────────────────────────────────────────────
# CONTENT — MORNING
# ─────────────────────────────────────────────
if mode == "morning":
    st.markdown(
        '<div class="card card-hero">'
        '<div class="badge">🌅 Morning Ritual</div>'
        '<h2 class="salutation">Good morning, <span class="accent">beautiful soul</span>.</h2>'
        '<p class="prompt">Today, you become.</p>'
        '</div>'
        '<div class="section">'
        '<h3>🌿 Feeling</h3>'
        '<p>'
        'I feel, but I am not my feelings.<br>'
        'Anxiety visits — I don\'t let it stay.<br>'
        'Fear knocks — I open, and it shrinks.'
        '<span class="bold-line">I am calm. I am centered. I am still.</span>'
        '</p>'
        '</div>'
        '<div class="section">'
        '<h3>💭 Thought</h3>'
        '<p>'
        'I release the need to be right.<br>'
        '<em>"What if I\'m 10% wrong?"</em><br>'
        'Their opinion is data, not verdict.'
        '<span class="bold-line">I think clearly. I think freely.</span>'
        '</p>'
        '</div>'
        '<div class="section">'
        '<h3>🕊️ Belief</h3>'
        '<p>'
        'I am worthy of my target — month by month.<br>'
        'I am reliable to authority.<br>'
        'I am a peaceful resolver.<br>'
        'I am valuable. My voice matters.'
        '<span class="bold-line">I believe in my becoming.</span>'
        '</p>'
        '</div>'
        '<div class="vow">'
        '<h3>✦ Today\'s Vow ✦</h3>'
        '<p>'
        'I am not faking. I am becoming.<br>'
        'Every breath — a reset.<br>'
        'Every word — a seed.<br>'
        'Every action — a brick.<br>'
        '<strong>Building my Baleno life, one calm day at a time.</strong>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# CONTENT — AFTERNOON
# ─────────────────────────────────────────────
elif mode == "afternoon":
    st.markdown(
        '<div class="card card-hero">'
        '<div class="badge">☀️ Afternoon Check-In</div>'
        '<h2 class="salutation">Realign with <span class="accent">who you\'re becoming</span>.</h2>'
        '<p class="prompt">The day is half-lived. Return to focus.</p>'
        '</div>'
        '<div class="section">'
        '<h3>⚡ Action</h3>'
        '<p>'
        'I speak once — clearly, kindly.<br>'
        'I don\'t gossip — I elevate.<br>'
        'I face authority with respect, not fear.<br>'
        'I take one fearless step daily.'
        '<span class="bold-line">I act. I build. I become.</span>'
        '</p>'
        '</div>'
        '<div class="section">'
        '<h3>🎯 My HRCM</h3>'
        '<div class="hrcm-row"><span class="k">🌿 Health</span><span>Peace is my priority.</span></div>'
        '<div class="hrcm-row"><span class="k">🤝 Relationship</span><span>Respect. Listen. Love.</span></div>'
        '<div class="hrcm-row"><span class="k">💼 Career</span><span>I solve problems fearlessly.</span></div>'
        '<div class="hrcm-row"><span class="k">💰 Money</span><span>My monthly target — tracked and hit.</span></div>'
        '</div>'
        '<div class="section">'
        '<h3>🧭 Midday Alignment</h3>'
        '<p>'
        'Have I gossiped today? <em>Return to focus.</em><br>'
        'Have I reacted? <em>Return to calm.</em><br>'
        'Have I moved toward this month\'s target? <em>Take one step now.</em>'
        '<span class="bold-line">Realign. Resume. Rise.</span>'
        '</p>'
        '</div>'
        '<div class="vow">'
        '<h3>✦ Midday Reset ✦</h3>'
        '<p>'
        'The morning is gone — that\'s okay.<br>'
        'The evening is coming — I\'ll be ready.<br>'
        'Right now, in this breath,'
        '<strong>I return to my becoming.</strong>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# CONTENT — NIGHT
# ─────────────────────────────────────────────
elif mode == "night":
    st.markdown(
        '<div class="card card-hero">'
        '<div class="badge">🌙 Night Reflection</div>'
        '<h2 class="salutation">Rest now, <span class="accent">you did well</span>.</h2>'
        '<p class="prompt">Release the day. Tomorrow, you rise again.</p>'
        '</div>'
        '<div class="section">'
        '<h3>🌙 Night Reflection</h3>'
        '<p>'
        'I did my best today.<br>'
        'I forgive my stumbles.<br>'
        'I release what I can\'t control.<br>'
        'I rest in gratitude.'
        '<span class="bold-line">Tomorrow, I rise calmer, clearer, stronger.</span>'
        '</p>'
        '</div>'
        '<div class="section">'
        '<h3>🙏 Three Gratitudes</h3>'
        '<p>'
        'One — for the breath in my body.<br>'
        'Two — for the lessons of today.<br>'
        'Three — for the person I am becoming.'
        '<span class="bold-line">Thank you. Thank you. Thank you.</span>'
        '</p>'
        '</div>'
        '<div class="section">'
        '<h3>🕊️ Release</h3>'
        '<p>'
        'I release the "I am right" trap.<br>'
        'I release the fear of authority.<br>'
        'I release the pull of gossip.<br>'
        'I release the need for approval.'
        '<span class="bold-line">I am free. I am light. I am peace.</span>'
        '</p>'
        '</div>'
        '<div class="vow">'
        '<h3>✦ Before Sleep ✦</h3>'
        '<p>'
        'I close this day with grace.<br>'
        'I did more than I think.<br>'
        'I am exactly where I need to be,'
        '<strong>one calm night closer to my Baleno life.</strong>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="ritual-label" style="margin-top:24px;">🎧 Night Listening</div>', unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=v9AHBtbk-E0")
    st.video("https://www.youtube.com/watch?v=0FR8PNcazKk")

    st.caption("Let this night sound carry you into stillness. Close your eyes. Breathe.")

# ─────────────────────────────────────────────
# CONTENT — HANUMAN CHALISA
# ─────────────────────────────────────────────
elif mode == "hanuman":
    st.markdown(
        '<div class="card card-hero">'
        '<div class="badge">🙏 Hanuman Chalisa</div>'
        '<h2 class="salutation">Forty Verses of <span class="accent">Strength</span>.</h2>'
        '<p class="prompt">Recite with devotion. Hanuman removes all obstacles.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="ritual-label">Doha — Opening Invocation</div>', unsafe_allow_html=True)
    for title, verse in HANUMAN_CHALISA_DOHA.items():
        card_html = (
            '<div class="verse-card">'
            f'<div class="verse-num">{title}</div>'
            f'<p class="verse-text">{verse}</p>'
            '</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:26px;">Chaupai — Forty Verses</div>', unsafe_allow_html=True)
    for i, verse in enumerate(HANUMAN_CHALISA_CHAUPAI, 1):
        card_html = (
            '<div class="verse-card">'
            f'<div class="verse-num">Verse {i}</div>'
            f'<p class="verse-text">{verse}</p>'
            '</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:26px;">Closing Doha</div>', unsafe_allow_html=True)
    closing_html = (
        '<div class="verse-card">'
        '<div class="verse-num">Doha — Closing</div>'
        f'<p class="verse-text">{HANUMAN_CHALISA_CLOSING}</p>'
        '</div>'
    )
    st.markdown(closing_html, unsafe_allow_html=True)

    st.markdown(
        '<div class="vow" style="margin-top:26px;">'
        '<h3>✦ Jai Hanuman ✦</h3>'
        '<p>'
        'Where Hanuman is remembered,<br>'
        'fear dissolves and courage rises.<br>'
        '<strong>Bolo Jai Shri Ram.</strong>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# CONTENT — VISHNU SAHASRANAMA
# ─────────────────────────────────────────────
elif mode == "vishnu":
    st.markdown(
        '<div class="card card-hero">'
        '<div class="badge">🕉️ Vishnu Sahasranama</div>'
        '<h2 class="salutation">The Thousand <span class="accent">Names</span>.</h2>'
        '<p class="prompt">Chant the names of the Preserver. Find peace in His glory.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="ritual-label">Dhyana Slokas — Meditation Verses</div>', unsafe_allow_html=True)
    for i, verse in enumerate(VISHNU_SAHASRANAMA_SLOKAS, 1):
        card_html = (
            '<div class="verse-card">'
            f'<div class="verse-num">Dhyana Sloka {i}</div>'
            f'<p class="verse-text">{verse}</p>'
            '</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:26px;">Stotram — Opening Verses (Excerpt)</div>', unsafe_allow_html=True)
    for i, verse in enumerate(VISHNU_SAHASRANAMA_STOTRAM, 1):
        card_html = (
            '<div class="verse-card">'
            f'<div class="verse-num">Verse {i}</div>'
            f'<p class="verse-text">{verse}</p>'
            '</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown(
        '<div class="vow" style="margin-top:26px;">'
        '<h3>✦ Om Namo Narayanaya ✦</h3>'
        '<p>'
        'The Preserver sustains all.<br>'
        'In His names, the mind finds rest.<br>'
        '<strong>Om Shanti. Om Shanti. Om Shanti.</strong>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.caption("Note: The complete Vishnu Sahasranama contains 1,000 names across 107 verses. This is a representative excerpt.")

# ─────────────────────────────────────────────
# CONTENT — TARGETS
# ─────────────────────────────────────────────
elif mode == "targets":
    st.markdown(
        '<div class="card card-hero">'
        '<div class="badge">🎯 Monthly Targets</div>'
        '<h2 class="salutation">The <span class="accent">Climb</span>.</h2>'
        '<p class="prompt">From ₹18 Lakhs in Oct 2026 to ₹49 Lakhs in May 2029. One month at a time.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    now = datetime.now()
    current_key = now.strftime("%Y-%m")

    first_label, first_amount = MONTHLY_TARGETS[0][1], MONTHLY_TARGETS[0][2]
    last_label, last_amount = MONTHLY_TARGETS[-1][1], MONTHLY_TARGETS[-1][2]

    current_entry = None
    next_entry = None
    for key, label, amount in MONTHLY_TARGETS:
        if key == current_key:
            current_entry = (key, label, amount)
            break
        if key > current_key:
            next_entry = (key, label, amount)
            break

    active_entry = current_entry or next_entry or MONTHLY_TARGETS[0]
    active_label = "This Month" if current_entry else "Next Target"

    chips_html = (
        '<div class="target-summary">'
        '<div class="target-chip">'
        '<div class="label">Start</div>'
        f'<div class="value">₹{format_inr(first_amount)}</div>'
        f'<div class="sub">{first_label}</div>'
        '</div>'
        '<div class="target-chip">'
        f'<div class="label">{active_label}</div>'
        f'<div class="value">₹{format_inr(active_entry[2])}</div>'
        f'<div class="sub">{active_entry[1]}</div>'
        '</div>'
        '<div class="target-chip">'
        '<div class="label">Final</div>'
        f'<div class="value">₹{format_inr(last_amount)}</div>'
        f'<div class="sub">{last_label}</div>'
        '</div>'
        '</div>'
    )
    st.markdown(chips_html, unsafe_allow_html=True)

    rows_html = ""
    for key, label, amount in MONTHLY_TARGETS:
        row_class = ""
        if key == current_key:
            row_class = "current"
        elif key < current_key:
            row_class = "past"
        rows_html += (
            f'<tr class="{row_class}">'
            f'<td class="month-col">{label}</td>'
            f'<td class="amount-col">₹{format_inr(amount)}</td>'
            '</tr>'
        )

    table_html = (
        '<div class="section">'
        '<h3>📅 Month-by-Month Ladder</h3>'
        '<table class="targets-table">'
        '<thead><tr>'
        '<th>Month</th>'
        '<th style="text-align:right;">Target</th>'
        '</tr></thead>'
        f'<tbody>{rows_html}</tbody>'
        '</table>'
        '</div>'
    )
    st.markdown(table_html, unsafe_allow_html=True)

    chart_labels = [label for _, label, _ in MONTHLY_TARGETS]
    chart_values = [amount for _, _, amount in MONTHLY_TARGETS]

    fig_targets = go.Figure()
    fig_targets.add_trace(go.Scatter(
        x=chart_labels,
        y=chart_values,
        mode="lines+markers",
        line=dict(color=T["gold"], width=3, shape="spline"),
        marker=dict(size=7, color=T["gold_soft"], line=dict(color=T["gold"], width=2)),
        fill="tozeroy",
        fillcolor="rgba(232, 185, 106, 0.12)",
        hovertemplate="<b>%{x}</b><br>Target: ₹%{y:,.0f}<extra></extra>",
    ))

    fig_targets.update_layout(
        height=380,
        margin=dict(l=40, r=20, t=20, b=60),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", size=12, color=T["ink_soft"]),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=10, color=T["ink_soft"]),
            tickangle=-45,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(232, 185, 106, 0.10)",
            tickfont=dict(size=11, color=T["ink_soft"]),
            tickprefix="₹",
            tickformat=",",
        ),
        showlegend=False,
    )

    st.markdown('<div class="ritual-label" style="margin-top:24px;">📈 Growth Curve</div>', unsafe_allow_html=True)
    st.plotly_chart(fig_targets, use_container_width=True, config={"displayModeBar": False})

    st.markdown(
        '<div class="vow" style="margin-top:24px;">'
        '<h3>✦ One Month at a Time ✦</h3>'
        '<p>'
        'I do not climb the whole mountain today.<br>'
        'I climb one month. One target. One step.<br>'
        '<strong>₹18 Lakhs. Then ₹19. Then ₹20. Then free.</strong>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# CONTENT — BALENO CNG AGS
# ─────────────────────────────────────────────
elif mode == "baleno":
    st.markdown(
        '<div class="card card-hero">'
        '<div class="badge">🚗 Baleno CNG AGS</div>'
        '<h2 class="salutation">The <span class="accent">Drive</span>.</h2>'
        '<p class="prompt">India\'s first CNG + Automatic in a Maruti hatchback.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="ritual-label" style="margin-top:24px;">🚗 Exterior</div>', unsafe_allow_html=True)
    st.image(IMAGES["baleno"]["exterior_1"], caption=IMAGES["baleno"]["exterior_1_caption"], use_container_width=True)
    exterior_rows = ""
    for name, desc in BALENO_FACTS["exterior"]:
        exterior_rows += (
            '<div class="hrcm-row">'
            f'<span class="k">{name}</span><span>{desc}</span>'
            '</div>'
        )
    st.markdown(f'<div class="section"><h3>Exterior Highlights</h3>{exterior_rows}</div>', unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:24px;">🪑 Interior</div>', unsafe_allow_html=True)
    st.image(IMAGES["baleno"]["interior_1"], caption=IMAGES["baleno"]["interior_1_caption"], use_container_width=True)
    interior_rows = ""
    for name, desc in BALENO_FACTS["interior"]:
        interior_rows += (
            '<div class="hrcm-row">'
            f'<span class="k">{name}</span><span>{desc}</span>'
            '</div>'
        )
    st.markdown(f'<div class="section"><h3>Interior Highlights</h3>{interior_rows}</div>', unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:24px;">⛽ CNG + AGS</div>', unsafe_allow_html=True)
    st.image(IMAGES["baleno"]["cng_1"], caption=IMAGES["baleno"]["cng_1_caption"], use_container_width=True)
    cng_rows = ""
    for name, desc in BALENO_FACTS["cng_ags"]:
        cng_rows += (
            '<div class="hrcm-row">'
            f'<span class="k">{name}</span><span>{desc}</span>'
            '</div>'
        )
    st.markdown(f'<div class="section"><h3>CNG + AGS — Why It Matters</h3>{cng_rows}</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="vow" style="margin-top:24px;">'
        '<h3>✦ The Baleno Vow ✦</h3>'
        '<p>'
        'I will sit in this driver\'s seat.<br>'
        'I will press the start button.<br>'
        'I will drive it home — CNG, AGS, and all.<br>'
        '<strong>₹18 Lakhs. Then ₹19. Then ₹20. Then the keys.</strong>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# CONTENT — CAREER ROADMAP
# ─────────────────────────────────────────────
elif mode == "career":
    st.markdown(
        '<div class="card card-hero">'
        '<div class="badge">💼 Career Roadmap</div>'
        '<h2 class="salutation">The <span class="accent">AI Advantage</span>.</h2>'
        '<p class="prompt">27 years of domain expertise + AI = ₹2 Lakhs/month from Odisha.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section">'
        '<h3>🎯 The Career Goal</h3>'
        '<p>'
        'To achieve <strong>₹2 Lakhs per month in Odisha</strong> (Angul, Bhubaneswar, Jharsuguda corridor) '
        'by leveraging 27 years of deep domain accounting expertise, supercharged with modern AI, '
        'Python, Pandas, and Streamlit analytics workflows.'
        '<span class="bold-line">3 local retainers × ₹70,000/month = ₹2.1 Lakhs/month.</span>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section">'
        '<h3>⚡ Why This Works</h3>'
        '<div class="hrcm-row"><span class="k">Domain Monopoly</span><span>Standard programmers do not understand GST ITC, floorplan interest, or shop-floor inventory leakages.</span></div>'
        '<div class="hrcm-row"><span class="k">High-Value Retainers</span><span>3 local manufacturing or auto-dealer groups paying ₹70,000/month securely meets the target.</span></div>'
        '<div class="hrcm-row"><span class="k">Strategic Positioning</span><span>Industrial Financial Systems Consultant — not an entry-level coder.</span></div>'
        '<div class="hrcm-row"><span class="k">Tech Stack</span><span>Light, secure intelligence layers on top of Tally Prime and Dealer Management Systems (DMS).</span></div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section">'
        '<h3>🏭 Target Industry Verticals</h3>'
        '<div class="hrcm-row"><span class="k">Manufacturing</span><span>Angul/Kalinganagar steel, power, and logistics units.</span></div>'
        '<div class="hrcm-row"><span class="k">Auto Showrooms</span><span>Floorplan financing cost optimization and workshop leakages.</span></div>'
        '<div class="hrcm-row"><span class="k">Corporate Auditing</span><span>Automated Benford\'s Law anomaly and GST GSTR-2B scans.</span></div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="ritual-label" style="margin-top:26px;">🗓️ 6-Month Execution Roadmap</div>', unsafe_allow_html=True)

    for item in CAREER_ROADMAP:
        status_icon = {
            "Completed": "✅",
            "In Progress": "🔄",
            "Pending": "⏳",
        }.get(item["Status"], "⏳")

        roadmap_html = (
            '<div class="verse-card">'
            f'<div class="verse-num">{status_icon} {item["Month"]} · {item["Status"]}</div>'
            f'<p class="verse-text"><strong>{item["Focus"]}</strong><br>{item["Action"]}</p>'
            '</div>'
        )
        st.markdown(roadmap_html, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:26px;">📋 Roadmap Overview</div>', unsafe_allow_html=True)
    df_roadmap = pd.DataFrame(CAREER_ROADMAP)
    st.dataframe(df_roadmap, use_container_width=True, hide_index=True)

    st.markdown('<div class="ritual-label" style="margin-top:26px;">⚙️ Live Tally/DMS Logic Simulation</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section">'
        '<h3>Capital Leakage Preview</h3>'
        '<p>A quick demonstration of how your code intercepts capital leakage '
        '(e.g., untracked showroom holding costs). This is what you present to '
        'regional business owners during your consultation calls.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.dataframe(CAREER_LEAKAGE_SAMPLE, use_container_width=True, hide_index=True)

    total_leakage = int(CAREER_LEAKAGE_SAMPLE["Holding_Cost_Per_Month"].sum())
    total_tied = int(CAREER_LEAKAGE_SAMPLE["Tied_Capital_INR"].sum())

    st.markdown(
        '<div class="section">'
        '<h3>💰 Identified Monthly Capital Drag</h3>'
        f'<div class="hrcm-row"><span class="k">Tied Capital</span><span>₹{format_inr(total_tied)}</span></div>'
        f'<div class="hrcm-row"><span class="k">Monthly Drag</span><span>₹{format_inr(total_leakage)}</span></div>'
        f'<div class="hrcm-row"><span class="k">Annual Drag</span><span>₹{format_inr(total_leakage * 12)}</span></div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.error(f"⚠️ Total Preventable Monthly Capital Drag Identified by Python Engine: ₹{format_inr(total_leakage)}")

    st.markdown(
        '<div class="vow" style="margin-top:24px;">'
        '<h3>✦ The Consultant\'s Vow ✦</h3>'
        '<p>'
        'I do not compete with programmers.<br>'
        'I do not compete with accountants.<br>'
        'I combine 27 years of domain wisdom with modern AI.<br>'
        '<strong>₹70,000 × 3 retainers = ₹2.1 Lakhs/month.</strong>'
        '</p>'
        '</div>',
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# ACCENT IMAGE
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.image(img["accent"], caption=img["accent_caption"], use_container_width=True)

# ─────────────────────────────────────────────
# MARK COMPLETE + STREAK + HISTORY
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

LABELS = {
    "morning":   "✨ I've Completed My Morning Ritual",
    "afternoon": "✨ I've Completed My Midday Reset",
    "night":     "✨ I've Completed My Night Reflection",
    "hanuman":   "🙏 I've Recited the Hanuman Chalisa",
    "vishnu":    "🕉️ I've Chanted the Vishnu Sahasranama",
    "targets":   "🎯 I've Reviewed My Monthly Targets",
    "baleno":    "🚗 I've Visualized My Baleno",
    "career":    "💼 I've Reviewed My Career Roadmap",
}

today = datetime.now().date().isoformat()

if mode not in ["targets", "baleno", "career"]:
    if not st.session_state.completed.get(mode, False):
        if st.button(LABELS[mode], use_container_width=True, key=f"complete_{mode}"):
            st.session_state.completed[mode] = True
            st.session_state.streak += 1
            st.session_state.completion_history[today] = st.session_state.completion_history.get(today, 0) + 1
            st.balloons()
            st.rerun()
    else:
        st.success(f"✅ {mode.capitalize()} complete. Well done.")
        if st.button("🔄 Reset This Session", use_container_width=True, key=f"reset_{mode}"):
            st.session_state.completed[mode] = False
            st.session_state.streak = max(0, st.session_state.streak - 1)
            if today in st.session_state.completion_history:
                st.session_state.completion_history[today] = max(0, st.session_state.completion_history[today] - 1)
            st.rerun()
else:
    if st.button(LABELS[mode], use_container_width=True, key=f"complete_{mode}"):
        st.balloons()
        st.success("✨ Review complete. Keep building.")

# ─────────────────────────────────────────────
# STREAK + PROGRESS
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
done_count = sum(1 for k, v in st.session_state.completed.items() if v)

c1, c2 = st.columns(2)
with c1:
    st.markdown(
        f'<div class="streak-pill">🔥 Streak &nbsp;<span class="num">{st.session_state.streak}</span> days</div>',
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        f'<div class="streak-pill">✅ Today &nbsp;<span class="num">{done_count}/5</span> rituals</div>',
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────
# 90-DAY STREAK HEATMAP
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="ritual-label">🗓️ 90-Day Practice Heatmap</div>', unsafe_allow_html=True)

end_date = datetime.now().date()
start_date = end_date - timedelta(days=89)
date_range = [start_date + timedelta(days=i) for i in range(90)]

heatmap_data = []
for d in date_range:
    iso = d.isoformat()
    count = st.session_state.completion_history.get(iso, 0)
    heatmap_data.append({
        "date": d,
        "week": d.isocalendar()[1],
        "weekday": d.weekday(),
        "count": count,
    })

df_heatmap = pd.DataFrame(heatmap_data)
week_min = df_heatmap["week"].min()
df_heatmap["week_index"] = df_heatmap["week"] - week_min

pivot = df_heatmap.pivot_table(
    index="weekday",
    columns="week_index",
    values="count",
    fill_value=0,
)

fig = go.Figure(data=go.Heatmap(
    z=pivot.values,
    x=[f"W{i+1}" for i in range(len(pivot.columns))],
    y=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    colorscale=[
        [0.0, "#1E1A14"],
        [0.25, T["gold_pale"]],
        [0.5, T["gold_soft"]],
        [0.75, T["gold"]],
        [1.0, "#F5C97A"],
    ],
    showscale=False,
    hovertemplate="Day: %{y}<br>Week: %{x}<br>Rituals: %{z}<extra></extra>",
    xgap=3,
    ygap=3,
))

fig.update_layout(
    height=250,
    margin=dict(l=50, r=20, t=10, b=30),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", size=12, color=T["ink_soft"]),
    xaxis=dict(showgrid=False, showticklabels=True, side="bottom", tickfont=dict(size=10, color=T["ink_soft"])),
    yaxis=dict(showgrid=False, autorange="reversed", tickfont=dict(size=11, color=T["ink_soft"])),
)

st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

legend_html = (
    '<div style="text-align:center; font-family:\'Inter\',sans-serif; '
    f'font-size:0.85rem; color:{T["ink_soft"]}; margin-top:-10px;">'
    'Less &nbsp;'
    '<span style="display:inline-block; width:14px; height:14px; background:#1E1A14; border-radius:2px; vertical-align:middle;"></span>'
    f'<span style="display:inline-block; width:14px; height:14px; background:{T["gold_pale"]}; border-radius:2px; vertical-align:middle;"></span>'
    f'<span style="display:inline-block; width:14px; height:14px; background:{T["gold_soft"]}; border-radius:2px; vertical-align:middle;"></span>'
    f'<span style="display:inline-block; width:14px; height:14px; background:{T["gold"]}; border-radius:2px; vertical-align:middle;"></span>'
    '<span style="display:inline-block; width:14px; height:14px; background:#F5C97A; border-radius:2px; vertical-align:middle;"></span>'
    '&nbsp; More'
    '</div>'
)
st.markdown(legend_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SEAL / FOOTER
# ─────────────────────────────────────────────
st.markdown(
    '<div class="seal">'
    '<h3>✦ I AM THE AUTHOR OF MY LIFE ✦</h3>'
    '<p>'
    'The pen is in my hand. The page is blank.<br>'
    'I write a beautiful story — starting now.'
    '</p>'
    '<div class="sign">— Your Future Self</div>'
    '</div>',
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────
# EXPANDER: PRINT
# ─────────────────────────────────────────────
with st.expander("🖨️  Print or Save as PDF"):
    st.markdown(
        "**To save this as a PDF:**\n"
        "1. Press `Ctrl + P` (Windows) or `Cmd + P` (Mac)\n"
        "2. Choose **Save as PDF**\n"
        "3. Paper size: **A6 or A5** (pocket fit)\n"
        "4. Margins: **Narrow**\n"
        "5. Enable **Background graphics**\n"
        "6. Print 3 copies → wallet · desk · car"
    )

st.caption("🌿 Speak it until you believe it. Believe it until you live it. Live it until you become it.")
