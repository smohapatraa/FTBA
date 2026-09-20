import streamlit as st
from datetime import datetime

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
        "hero": "https://images.unsplash.com/photo-1545121649-0c8e0c8c8c8c?w=1200&q=80",
        "caption": "Sacred geometry · Photo by Unsplash",
        "accent": "https://images.unsplash.com/photo-1561365452-adb940139ffa?w=800&q=80",
        "accent_caption": "Temple architecture · Photo by Unsplash",
    },
}
