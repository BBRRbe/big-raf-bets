
import streamlit as st
import pandas as pd
import datetime

# --- APP CONFIG ---
st.set_page_config(page_title="Big Raf Bets™", layout="wide")

# --- SIDEBAR ---
view_option = st.sidebar.radio("Select View:", ["Today", "Tomorrow"])

# --- DYNAMIC DATE LOGIC ---
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
selected_date = today if view_option == "Today" else tomorrow

# --- BRANDING ---
st.markdown("<h1 style='color:#FF69B4; font-size: 48px;'>Big Raf Bets™</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color:#555;'>Powered by <strong>RAFI™</strong>: Risk Analysis + Forecast Intelligence</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- MOCK PICKS DATA ---
picks_data = [
    # May 2 (Today)
    {"Game": "Jets vs Blues", "Bet Type": "Total Goals", "Pick": "Under 5.5", "Confidence": 312, "Date": str(today)},
    {"Game": "Warriors vs Rockets", "Bet Type": "Moneyline", "Pick": "Warriors ML", "Confidence": 281, "Date": str(today)},
    {"Game": "Warriors vs Rockets", "Bet Type": "Points", "Player": "Stephen Curry", "Pick": "Over 27+", "Confidence": 245, "Date": str(today)},
    {"Game": "Warriors vs Rockets", "Bet Type": "Threes", "Player": "Stephen Curry", "Pick": "Over 5+", "Confidence": 215, "Date": str(today)},
    {"Game": "Warriors vs Rockets", "Bet Type": "Assists", "Player": "Fred VanVleet", "Pick": "Over 4+", "Confidence": 201, "Date": str(today)},

    # May 3 (Tomorrow)
    {"Game": "Knicks vs Pacers", "Bet Type": "Moneyline", "Pick": "Knicks ML", "Confidence": 198, "Date": str(tomorrow)},
    {"Game": "Stars vs Avalanche", "Bet Type": "Total Goals", "Pick": "Over 6", "Confidence": 180, "Date": str(tomorrow)},
]

df = pd.DataFrame(picks_data)
df = df[df["Date"] == str(selected_date)]

# --- CONFIDENCE SCALE ---
def confidence_to_emoji(score):
    if score > 300:
        return "🔥 Extremely high"
    elif 200 <= score <= 299:
        return "✅ Very reliable"
    elif 100 <= score <= 199:
        return "👍 Good"
    elif 70 <= score <= 99:
        return "⚠️ Borderline"
    else:
        return "❌ No bet"

df["Confidence Rating"] = df["Confidence"].apply(confidence_to_emoji)

# --- DISPLAY ---
st.subheader(f"Model Picks for {'Today' if view_option == 'Today' else 'Tomorrow'} ({selected_date.strftime('%b %d')})")
st.dataframe(df.drop(columns=['Date']), use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("<small style='color:#888;'>© Big Raf Bets™ | Updated daily by RAFI™</small>", unsafe_allow_html=True)
