import streamlit as st
import requests

# إعداد الصفحة
st.set_page_config(page_title="SolAI-DRT Enterprise", page_icon="☀️", layout="wide")

# --- الربط مع الأرصاد الجوية ---
API_KEY = "55ba7ec1a378127368b06a97d9c9be74" #
CITY = "Errachidia"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL).json()
    temp = response['main']['temp']
    wind_speed = response['wind']['speed'] * 3.6
    weather_desc = response['weather'][0]['description']
except:
    temp, wind_speed, weather_desc = 29.0, 10.0, "صافية"

# --- الواجهة الرئيسية ---
st.title("☀️ SolAI-DRT: Enterprise Solar Management")
st.markdown(f"#### لوحة التحكم الذكية - جهة درعة تافيلالت ({CITY})")

# المؤشرات الحقيقية
c1, c2, c3 = st.columns(3)
c1.metric("الحرارة الآن", f"{temp}°C")
c2.metric("سرعة الرياح", f"{wind_speed:.1f} km/h")
c3.metric("حالة الجو", weather_desc.capitalize())

st.divider()

# --- 💰 حاسبة الأرباح (ROI Calculator) - الجديد ---
st.subheader("📊 حاسبة العائد على الاستثمار (ROI)")
with st.container():
    col_input, col_res = st.columns([1, 1])
    
    with col_input:
        panels = st.number_input("عدد الألواح الشمسية:", min_value=1, value=10)
        bill = st.number_input("فاتورة الكهرباء الشهرية المتوسطة (DH):", min_value=100, value=500)
    
    # حسابات تقديرية
    savings_monthly = bill * 0.7  # توفير 70% بفضل التحسين
    co2_saved = panels * 0.5 # كيلوغرام من الكاربون
    
    with col_res:
        st.write("### التوقعات الشهرية مع SolAI-DRT:")
        st.success(f"💰 التوفير المالي المتوقع: {savings_monthly:.2f} DH")
        st.info(f"🌱 تقليل انبعاثات الكاربون: {co2_saved:.1f} KG")

st.divider()

# --- 🤖 الشات بوت التفاعلي ---
st.subheader("💬 SolAI Chat Assistant")
user_question = st.text_input("سولني على حالة الألواح ديالك اليوم:")

if user_question:
    if "غسل" in user_question or "تنظيف" in user_question:
        if wind_speed > 25:
            st.write(f"🤖 **SolAI:** لا، الرياح مجهدة ({wind_speed:.1f} km/h). تسنى حتى تهدأ العاصفة.")
        else:
            st.write("🤖 **SolAI:** نعم، الجو مثالي للتنظيف الآن!")
    elif "إنتاج" in user_question:
        st.write(f"🤖 **SolAI:** مع حرارة {temp}°C، الإنتاج غيكون ممتاز، حاول تستغل الذروة.")
    else:
        st.write("🤖 **SolAI:** سؤال ممتاز! ديما راقب المؤشرات الفوق قبل ما تاخد أي قرار.")

# --- الخريطة ---
st.write("---")
st.subheader("📍 مواقع المحطات المراقبة")
st.map({'lat': [31.9316], 'lon': [-4.4244]})

st.sidebar.title("SolAI-DRT v3.0")
st.sidebar.info("هذا التطبيق هو MVP متكامل لمشروع RamadnIA 2026") #
st.sidebar.write("---")
st.sidebar.write("Developed by Atmane & Team")
