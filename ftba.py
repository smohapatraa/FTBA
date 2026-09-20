import streamlit as st
from datetime import datetime
import io

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
# IMAGE LIBRARY — Free from Unsplash & Pexels
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
}

# ─────────────────────────────────────────────
# PREMIUM DESIGN SYSTEM — CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

    :root {
        --cream:        #FBF6EC;
        --cream-deep:   #F5EBD8;
        --ink:          #2E2A22;
        --ink-soft:     #4A4438;
        --gold:         #B8893A;
        --gold-soft:    #D4AF37;
        --gold-pale:    #E8D9A8;
        --card:         #FFFFFF;
        --shadow-sm:    0 2px 12px rgba(74, 63, 42, 0.06);
        --shadow-md:    0 6px 24px rgba(74, 63, 42, 0.10);
        --shadow-lg:    0 16px 48px rgba(74, 63, 42, 0.15);
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--ink);
    }

    .stApp {
        background:
            radial-gradient(1200px 600px at 50% -10%, #FFFDF7 0%, transparent 60%),
            radial-gradient(800px 400px at 100% 100%, #F5EBD8 0%, transparent 50%),
            linear-gradient(180deg, var(--cream) 0%, var(--cream-deep) 100%);
        background-attachment: fixed;
    }

    .main .block-container {
        max-width: 760px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* ═══ HERO IMAGE ═══ */
    .hero-image-wrap {
        position: relative;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 24px;
        box-shadow: var(--shadow-lg);
        animation: fadeUp 0.6s cubic-bezier(.2,.8,.2,1) both;
    }
    .hero-image-wrap img {
        width: 100%;
        height: 260px;
        object-fit: cover;
        display: block;
    }
    .hero-image-wrap .overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(46,42,34,0.05) 0%, rgba(46,42,34,0.55) 100%);
    }
    .hero-image-wrap .text {
        position: absolute;
        bottom: 24px;
        left: 28px;
        right: 28px;
        color: #FFFDF7;
    }
    .hero-image-wrap .text .eyebrow {
        font-family: 'Inter', sans-serif;
        font-size: 0.7rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: var(--gold-pale);
        font-weight: 600;
        margin-bottom: 8px;
    }
    .hero-image-wrap .text h2 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.15;
        text-shadow: 0 2px 12px rgba(0,0,0,0.4);
    }
    .hero-image-wrap .text h2 .accent {
        color: var(--gold-pale);
        font-style: italic;
    }
    .hero-image-wrap .caption {
        position: absolute;
        bottom: 6px;
        right: 12px;
        font-size: 0.55rem;
        color: rgba(255,255,255,0.55);
        font-family: 'Inter', sans-serif;
    }

    /* ═══ HEADER ═══ */
    .hero {
        text-align: center;
        padding: 8px 0 20px 0;
    }
    .hero-eyebrow {
        font-size: 0.7rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 600;
        margin-bottom: 12px;
    }
    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.4rem;
        font-weight: 700;
        color: var(--ink);
        line-height: 1.1;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .hero-title .accent {
        color: var(--gold);
        font-style: italic;
        font-weight: 600;
    }
    .hero-divider {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin: 16px 0 12px 0;
        color: var(--gold);
    }
    .hero-divider .line {
        width: 60px;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--gold), transparent);
    }
    .hero-divider .dot {
        font-size: 0.7rem;
        letter-spacing: 6px;
    }
    .hero-sub {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1rem;
        font-style: italic;
        color: var(--ink-soft);
        margin: 0;
    }

    /* ═══ RITUAL SELECTOR ═══ */
    .ritual-label {
        text-align: center;
        font-size: 0.7rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: var(--gold);
        font-weight: 600;
        margin: 8px 0 14px 0;
    }

    div[data-testid="column"] .stButton > button {
        width: 100%;
        border-radius: 16px;
        padding: 20px 12px;
        border: 2px solid transparent;
        background: var(--card);
        box-shadow: var(--shadow-sm);
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem;
        font-weight: 600;
        color: var(--ink);
        letter-spacing: 0.5px;
        transition: all 0.25s cubic-bezier(.2,.8,.2,1);
        white-space: pre-line;
        line-height: 1.5;
        min-height: 90px;
    }
    div[data-testid="column"] .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-md);
        border-color: var(--gold-pale);
        color: var(--gold);
    }
    div[data-testid="column"] .stButton > button:focus:not(:active) {
        color: var(--gold);
        border-color: var(--gold);
    }

    /* ═══ CARDS ═══ */
    .card {
        background: var(--card);
        border-radius: 18px;
        padding: 26px 28px;
        margin: 16px 0;
        box-shadow: var(--shadow-md);
        border: 1px solid rgba(212, 175, 55, 0.15);
        animation: fadeUp 0.5s cubic-bezier(.2,.8,.2,1) both;
    }
    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    .card-hero {
        text-align: center;
        padding: 32px 28px;
        background:
            radial-gradient(circle at 50% 0%, rgba(212,175,55,0.08), transparent 70%),
            var(--card);
        border: 2px solid var(--gold-pale);
    }
    .card-hero .badge {
        display: inline-block;
        font-size: 0.65rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: var(--gold);
        background: rgba(212, 175, 55, 0.10);
        padding: 6px 14px;
        border-radius: 100px;
        font-weight: 600;
        margin-bottom: 16px;
    }
    .card-hero .salutation {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.9rem;
        font-weight: 700;
        color: var(--ink);
        margin: 0 0 8px 0;
        line-height: 1.2;
    }
    .card-hero .salutation .accent { color: var(--gold); font-style: italic; }
    .card-hero .prompt {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.1rem;
        font-style: italic;
        color: var(--ink-soft);
        margin: 0;
        line-height: 1.6;
    }

    /* Section cards */
    .section {
        background: var(--card);
        border-radius: 14px;
        padding: 20px 24px;
        margin: 14px 0;
        box-shadow: var(--shadow-sm);
        border-left: 4px solid var(--gold);
        animation: fadeUp 0.5s cubic-bezier(.2,.8,.2,1) both;
    }
    .section h3 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem;
        letter-spacing: 2px;
        color: var(--gold);
        margin: 0 0 12px 0;
        font-weight: 700;
        text-transform: uppercase;
    }
    .section p {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem;
        line-height: 1.75;
        color: var(--ink-soft);
        margin: 0;
    }
    .section .bold-line {
        display: block;
        font-weight: 700;
        color: var(--ink);
        margin-top: 10px;
        font-style: italic;
    }

    /* HRCM grid */
    .hrcm-row {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 8px 0;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem;
        color: var(--ink-soft);
        border-bottom: 1px dashed var(--gold-pale);
    }
    .hrcm-row:last-child { border-bottom: none; }
    .hrcm-row .k {
        color: var(--gold);
        font-weight: 700;
        min-width: 110px;
    }

    /* Vow card */
    .vow {
        background: linear-gradient(135deg, #FFFDF6 0%, #F7EBCB 100%);
        border: 2px dashed var(--gold);
        border-radius: 16px;
        padding: 24px 22px;
        text-align: center;
        margin: 16px 0;
        animation: fadeUp 0.5s cubic-bezier(.2,.8,.2,1) both;
    }
    .vow h3 {
        font-family: 'Cormorant Garamond', serif;
        color: var(--gold);
        font-size: 1.05rem;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin: 0 0 12px 0;
        font-weight: 700;
    }
    .vow p {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.05rem;
        color: var(--ink);
        line-height: 1.9;
        margin: 0;
    }

    /* Scripture verse card */
    .verse-card {
        background: linear-gradient(135deg, #FFFDF6 0%, #FAF1D9 100%);
        border-left: 4px solid var(--gold);
        border-radius: 12px;
        padding: 16px 20px;
        margin: 10px 0;
        box-shadow: var(--shadow-sm);
        animation: fadeUp 0.4s cubic-bezier(.2,.8,.2,1) both;
    }
    .verse-card .verse-num {
        font-family: 'Inter', sans-serif;
        font-size: 0.7rem;
        letter-spacing: 2px;
        color: var(--gold);
        text-transform: uppercase;
        font-weight: 700;
        margin-bottom: 6px;
    }
    .verse-card .verse-text {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.1rem;
        line-height: 1.7;
        color: var(--ink);
        font-style: italic;
        margin: 0;
    }

    /* Seal / footer */
    .seal {
        background: linear-gradient(135deg, #2E2A22 0%, #4A4438 100%);
        color: var(--cream);
        border-radius: 18px;
        padding: 30px 26px;
        text-align: center;
        margin: 28px 0 12px 0;
        box-shadow: var(--shadow-lg);
        position: relative;
        overflow: hidden;
    }
    .seal::before {
        content: "";
        position: absolute;
        inset: 8px;
        border: 1px solid rgba(212, 175, 55, 0.35);
        border-radius: 12px;
        pointer-events: none;
    }
    .seal h3 {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
        letter-spacing: 3px;
        color: var(--gold-soft);
        margin: 0 0 12px 0;
        font-weight: 700;
        position: relative;
    }
    .seal p {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1rem;
        font-style: italic;
        color: var(--cream);
        line-height: 1.7;
        margin: 0;
        position: relative;
    }
    .seal .sign {
        font-family: 'Cormorant Garamond', serif;
        color: var(--gold-soft);
        font-size: 0.9rem;
        margin-top: 14px;
        letter-spacing: 1px;
        position: relative;
    }

    /* Streak pill */
    .streak-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: var(--card);
        border: 1px solid var(--gold-pale);
        border-radius: 100px;
        padding: 10px 20px;
        font-size: 0.85rem;
        font-weight: 500;
        color: var(--ink-soft);
        box-shadow: var(--shadow-sm);
    }
    .streak-pill .num {
        color: var(--gold);
        font-weight: 700;
        font-size: 1rem;
    }

    /* Hide streamlit chrome */
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

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

if "auto_set" not in st.session_state:
    hour = datetime.now().hour
    if hour < 12:
        st.session_state.mode = "morning"
    elif hour < 17:
        st.session_state.mode = "afternoon"
    else:
        st.session_state.mode = "night"
    st.session_state.auto_set = True

# ─────────────────────────────────────────────
# HERO HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">A Sacred Daily Ritual</div>
    <h1 class="hero-title">Pocket <span class="accent">Affirmation</span></h1>
    <div class="hero-divider">
        <span class="line"></span>
        <span class="dot">✦ ✦ ✦</span>
        <span class="line"></span>
    </div>
    <p class="hero-sub">Fold. Carry. Read three times a day.</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# RITUAL SELECTOR — 5 BUTTONS (3 + 2 sacred)
# ─────────────────────────────────────────────
st.markdown('<div class="ritual-label">Choose Your Moment</div>', unsafe_allow_html=True)

# Row 1: Morning / Afternoon / Night
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

# Row 2: Hanuman Chalisa / Vishnu Sahasranama
st.markdown('<div class="ritual-label" style="margin-top:18px;">Sacred Recitations</div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)

with col4:
    if st.button("🙏\nHanuman Chalisa", key="btn_hanuman", use_container_width=True):
        st.session_state.mode = "hanuman"
        st.rerun()

with col5:
    if st.button("🕉️\nVishnu Sahasranama", key="btn_vishnu", use_container_width=True):
        st.session_state.mode = "vishnu"
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HERO IMAGE — Changes per mode
# ─────────────────────────────────────────────
mode = st.session_state.mode
img = IMAGES[mode]

EYEBROW = {
    "morning":   "🌅 Morning Ritual",
    "afternoon": "☀️ Midday Reset",
    "night":     "🌙 Night Reflection",
    "hanuman":   "🙏 Hanuman Chalisa",
    "vishnu":    "🕉️ Vishnu Sahasranama",
}[mode]

HEADLINE = {
    "morning":   'Begin with <span class="accent">stillness</span>.',
    "afternoon": 'Pause. <span class="accent">Breathe</span>. Return.',
    "night":     'Rest now. <span class="accent">You did well</span>.',
    "hanuman":   'Forty verses of <span class="accent">strength</span>.',
    "vishnu":    'The thousand <span class="accent">names</span>.',
}[mode]

st.markdown(f"""
<div class="hero-image-wrap">
    <img src="{img['hero']}" alt="{mode} hero image">
    <div class="overlay"></div>
    <div class="text">
        <div class="eyebrow">{EYEBROW}</div>
        <h2>{HEADLINE}</h2>
    </div>
    <div class="caption">{img['caption']}</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONTENT: MORNING
# ─────────────────────────────────────────────
if mode == "morning":
    st.markdown("""
    <div class="card card-hero">
        <div class="badge">🌅 Morning Ritual</div>
        <h2 class="salutation">Good morning, <span class="accent">beautiful soul</span>.</h2>
        <p class="prompt">Today, you become.</p>
    </div>

    <div class="section">
        <h3>🌿 Feeling</h3>
        <p>
            I feel, but I am not my feelings.<br>
            Anxiety visits — I don't let it stay.<br>
            Fear knocks — I open, and it shrinks.
            <span class="bold-line">I am calm. I am centered. I am still.</span>
        </p>
    </div>

    <div class="section">
        <h3>💭 Thought</h3>
        <p>
            I release the need to be right.<br>
            <em>"What if I'm 10% wrong?"</em><br>
            Their opinion is data, not verdict.
            <span class="bold-line">I think clearly. I think freely.</span>
        </p>
    </div>

    <div class="section">
        <h3>🕊️ Belief</h3>
        <p>
            I am worthy of ₹2 Lakhs/month.<br>
            I am reliable to authority.<br>
            I am a peaceful resolver.<br>
            I am valuable. My voice matters.
            <span class="bold-line">I believe in my becoming.</span>
        </p>
    </div>

    <div class="vow">
        <h3>✦ Today's Vow ✦</h3>
        <p>
            I am not faking. I am becoming.<br>
            Every breath — a reset.<br>
            Every word — a seed.<br>
            Every action — a brick.<br>
            <strong>Building my Baleno life, one calm day at a time.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONTENT: AFTERNOON
# ─────────────────────────────────────────────
elif mode == "afternoon":
    st.markdown("""
    <div class="card card-hero">
        <div class="badge">☀️ Afternoon Check-In</div>
        <h2 class="salutation">Realign with <span class="accent">who you're becoming</span>.</h2>
        <p class="prompt">The day is half-lived. Return to focus.</p>
    </div>

    <div class="section">
        <h3>⚡ Action</h3>
        <p>
            I speak once — clearly, kindly.<br>
            I don't gossip — I elevate.<br>
            I face authority with respect, not fear.<br>
            I take one fearless step daily.
            <span class="bold-line">I act. I build. I become.</span>
        </p>
    </div>

    <div class="section">
        <h3>🎯 My HRCM</h3>
        <div class="hrcm-row"><span class="k">🌿 Health</span><span>Peace is my priority.</span></div>
        <div class="hrcm-row"><span class="k">🤝 Relationship</span><span>Respect. Listen. Love.</span></div>
        <div class="hrcm-row"><span class="k">💼 Career</span><span>I solve problems fearlessly.</span></div>
        <div class="hrcm-row"><span class="k">💰 Money</span><span>₹2L/month. Baleno. Self-reliant.</span></div>
    </div>

    <div class="section">
        <h3>🧭 Midday Alignment</h3>
        <p>
            Have I gossiped today? <em>Return to focus.</em><br>
            Have I reacted? <em>Return to calm.</em><br>
            Have I moved toward ₹2L? <em>Take one step now.</em>
            <span class="bold-line">Realign. Resume. Rise.</span>
        </p>
    </div>

    <div class="vow">
        <h3>✦ Midday Reset ✦</h3>
        <p>
            The morning is gone — that's okay.<br>
            The evening is coming — I'll be ready.<br>
            Right now, in this breath,
            <strong>I return to my becoming.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONTENT: NIGHT
# ─────────────────────────────────────────────
elif mode == "night":
    st.markdown("""
    <div class="card card-hero">
        <div class="badge">🌙 Night Reflection</div>
        <h2 class="salutation">Rest now, <span class="accent">you did well</span>.</h2>
        <p class="prompt">Release the day. Tomorrow, you rise again.</p>
    </div>

    <div class="section">
        <h3>🌙 Night Reflection</h3>
        <p>
            I did my best today.<br>
            I forgive my stumbles.<br>
            I release what I can't control.<br>
            I rest in gratitude.
            <span class="bold-line">Tomorrow, I rise calmer, clearer, stronger.</span>
        </p>
    </div>

    <div class="section">
        <h3>🙏 Three Gratitudes</h3>
        <p>
            One — for the breath in my body.<br>
            Two — for the lessons of today.<br>
            Three — for the person I am becoming.
            <span class="bold-line">Thank you. Thank you. Thank you.</span>
        </p>
    </div>

    <div class="section">
        <h3>🕊️ Release</h3>
        <p>
            I release the "I am right" trap.<br>
            I release the fear of authority.<br>
            I release the pull of gossip.<br>
            I release the need for approval.
            <span class="bold-line">I am free. I am light. I am peace.</span>
        </p>
    </div>

    <div class="vow">
        <h3>✦ Before Sleep ✦</h3>
        <p>
            I close this day with grace.<br>
            I did more than I think.<br>
            I am exactly where I need to be,
            <strong>one calm night closer to my Baleno life.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONTENT: HANUMAN CHALISA
# ─────────────────────────────────────────────
elif mode == "hanuman":
    st.markdown("""
    <div class="card card-hero">
        <div class="badge">🙏 Hanuman Chalisa</div>
        <h2 class="salutation">Forty Verses of <span class="accent">Strength</span>.</h2>
        <p class="prompt">Recite with devotion. Hanuman removes all obstacles.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label">Doha — Opening Invocation</div>', unsafe_allow_html=True)
    for i, (title, verse) in enumerate(HANUMAN_CHALISA_DOHA.items(), 1):
        st.markdown(f"""
        <div class="verse-card">
            <div class="verse-num">{title}</div>
            <p class="verse-text">{verse}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:24px;">Chaupai — Forty Verses</div>', unsafe_allow_html=True)
    for i, verse in enumerate(HANUMAN_CHALISA_CHAUPAI, 1):
        st.markdown(f"""
        <div class="verse-card">
            <div class="verse-num">Verse {i}</div>
            <p class="verse-text">{verse}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:24px;">Closing Doha</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="verse-card">
        <div class="verse-num">Doha — Closing</div>
        <p class="verse-text">{HANUMAN_CHALISA_CLOSING}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="vow" style="margin-top:24px;">
        <h3>✦ Jai Hanuman ✦</h3>
        <p>
            Where Hanuman is remembered,<br>
            fear dissolves and courage rises.<br>
            <strong>Bolo Jai Shri Ram.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONTENT: VISHNU SAHASRANAMA
# ─────────────────────────────────────────────
elif mode == "vishnu":
    st.markdown("""
    <div class="card card-hero">
        <div class="badge">🕉️ Vishnu Sahasranama</div>
        <h2 class="salutation">The Thousand <span class="accent">Names</span>.</h2>
        <p class="prompt">Chant the names of the Preserver. Find peace in His glory.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label">Dhyana Slokas — Meditation Verses</div>', unsafe_allow_html=True)
    for i, verse in enumerate(VISHNU_SAHASRANAMA_SLOKAS, 1):
        st.markdown(f"""
        <div class="verse-card">
            <div class="verse-num">Dhyana Sloka {i}</div>
            <p class="verse-text">{verse}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="ritual-label" style="margin-top:24px;">Stotram — Opening Verses (Excerpt)</div>', unsafe_allow_html=True)
    for i, verse in enumerate(VISHNU_SAHASRANAMA_STOTRAM, 1):
        st.markdown(f"""
        <div class="verse-card">
            <div class="verse-num">Verse {i}</div>
            <p class="verse-text">{verse}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="vow" style="margin-top:24px;">
        <h3>✦ Om Namo Narayanaya ✦</h3>
        <p>
            The Preserver sustains all.<br>
            In His names, the mind finds rest.<br>
            <strong>Om Shanti. Om Shanti. Om Shanti.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("Note: The complete Vishnu Sahasranama contains 1,000 names across 107 verses. This is a representative excerpt. For full traditional recitation, please refer to dedicated publications.")

# ─────────────────────────────────────────────
# ACCENT IMAGE — Small, per mode
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.image(img["accent"], caption=img["accent_caption"], use_container_width=True)

# ─────────────────────────────────────────────
# MARK COMPLETE + STREAK
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)

LABELS = {
    "morning":   "✨ I've Completed My Morning Ritual",
    "afternoon": "✨ I've Completed My Midday Reset",
    "night":     "✨ I've Completed My Night Reflection",
    "hanuman":   "🙏 I've Recited the Hanuman Chalisa",
    "vishnu":    "🕉️ I've Chanted the Vishnu Sahasranama",
}

if not st.session_state.completed[mode]:
    if st.button(LABELS[mode], use_container_width=True, key=f"complete_{mode}"):
        st.session_state.completed[mode] = True
        st.session_state.streak += 1
        st.balloons()
        st.rerun()
else:
    st.success(f"✅ {mode.capitalize()} complete. Well done.")
    if st.button("🔄 Reset This Session", use_container_width=True, key=f"reset_{mode}"):
        st.session_state.completed[mode] = False
        st.session_state.streak = max(0, st.session_state.streak - 1)
        st.rerun()

# ─────────────────────────────────────────────
# STREAK + PROGRESS
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
done_count = sum(st.session_state.completed.values())

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
# SEAL / FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="seal">
    <h3>✦ I AM THE AUTHOR OF MY LIFE ✦</h3>
    <p>
        The pen is in my hand. The page is blank.<br>
        I write a beautiful story — starting now.
    </p>
    <div class="sign">— Your Future Self</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# EXPANDER: PRINT / SAVE AS PDF
# ─────────────────────────────────────────────
with st.expander("🖨️  Print or Save as PDF"):
    st.markdown("""
    **To save this as a PDF:**
    1. Press `Ctrl + P` (Windows) or `Cmd + P` (Mac)
    2. Choose **Save as PDF**
    3. Paper size: **A6 or A5** (pocket fit)
    4. Margins: **Narrow**
    5. Enable **Background graphics**
    6. Print 3 copies → wallet · desk · car
    """)

st.caption("🌿 Speak it until you believe it. Believe it until you live it. Live it until you become it.")
