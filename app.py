import streamlit as st
import requests

# إعداد الصفحة
st.set_page_config(page_title="SolAI-DRT Pro", page_icon="☀️", layout="wide")

# --- جلب البيانات الحقيقية ---
API_KEY = "55ba7ec1a378127368b06a97d9c9be74"
CITY = "Errachidia"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL).json()
    temp = response['main']['temp']
    wind_speed = response['wind']['speed'] * 3.6
    weather_desc = response['weather'][0]['description']
except:
    temp, wind_speed, weather_desc = 30.0, 12.0, "صافية"

# --- الواجهة الرئيسية ---
st.title("☀️ SolAI-DRT: Intelligent Solar Assistant")
st.markdown(f"#### لوحة التحكم الذكية - {CITY} [Live]")

# الإحصائيات الفورية
c1, c2, c3 = st.columns(3)
c1.metric("الحرارة الآن", f"{temp}°C")
c2.metric("سرعة الرياح", f"{wind_speed:.1f} km/h")
c3.metric("حالة الجو", weather_desc.capitalize())

st.divider()

# --- 🤖 SolAI Chatbot (الجديد) ---
st.subheader("💬 SolAI Chat Assistant")
st.info("سولني أي حاجة على الألواح ديالك بناءً على جو اليوم!")

user_question = st.text_input("مثال: واش نغسل الألواح اليوم؟ أو واش الإنتاج غيكون مزيان؟")

if user_question:
    # منطق الذكاء الاصطناعي البسيط
    if "غسل" in user_question or "تنظيف" in user_question:
        if wind_speed > 25:
            st.write("🤖 **SolAI:** لا، ما كنصحكش تغسلهم دابا. الرياح مجهدة ({:.1f} km/h) وغيطلع الغبار تاني. تسنى حتى يبرد الحال.".format(wind_speed))
        else:
            st.write("🤖 **SolAI:** نعم، الجو هادئ حالياً. هاد الوقت مثالي للتنظيف باش تزيد في الكفاءة!")
    
    elif "إنتاج" in user_question or "كفاءة" in user_question:
        if temp > 35:
            st.write("🤖 **SolAI:** الحرارة طالعة ({:.1f}°C)، وهادشي كينقص شوية من كفاءة الألواح. واخا كاين الشمش، الإنتاج غيكون متوسط.".format(temp))
        else:
            st.write("🤖 **SolAI:** الجو مثالي! الحرارة والشمش متوازنين، الإنتاج غيكون في القمة اليوم.")
    
    else:
        st.write("🤖 **SolAI:** سؤال مهم! بناءً على المعطيات اللي عندي، ديما حاول تراقب سرعة الرياح قبل ما تبدأ أي صيانة.")

# --- الخريطة ---
st.write("---")
st.subheader("📍 موقع المحطة")
st.map({'lat': [31.9316], 'lon': [-4.4244]})

st.sidebar.markdown("### SolAI-DRT v2.0")
st.sidebar.write("نظام مبني بالذكاء الاصطناعي لخدمة جهة درعة تافيلالت.")
st.sidebar.write("---")
st.sidebar.write("By Atmane & Team")
