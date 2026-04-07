import streamlit as st
import requests

# إعداد الصفحة لتكون احترافية
st.set_page_config(page_title="SolAI-DRT Live", page_icon="☀️", layout="wide")

# --- الربط الحقيقي مع الأرصاد الجوية ---
API_KEY = "55ba7ec1a378127368b06a97d9c9be74" # الساروت ديالك من OpenWeather
CITY = "Errachidia"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL).json()
    temp = response['main']['temp']
    wind_speed = response['wind']['speed'] * 3.6 # تحويل من m/s لـ km/h
    weather_desc = response['weather'][0]['description']
except Exception:
    # قيم احتياطية في حالة تأخر تفعيل الساروت
    temp, wind_speed, weather_desc = 30.0, 12.0, "جاري جلب البيانات..."

# --- واجهة المستخدم ---
st.title("☀️ SolAI-DRT: Real-Time Intelligence")
st.markdown(f"#### مراقبة مباشرة لظروف الطقس في جهة درعة تافيلالت ({CITY})")

col1, col2, col3 = st.columns(3)
col1.metric("درجة الحرارة الآن", f"{temp}°C")
col2.metric("سرعة الرياح", f"{wind_speed:.1f} km/h")
col3.metric("حالة السماء", weather_desc.capitalize())

st.divider()

# --- نظام التنبؤ الذكي بالذكاء الاصطناعي ---
st.subheader("🤖 تحليل الذكاء الاصطناعي للظروف الجوية")

if wind_speed > 30:
    st.warning(f"🚨 **تنبيه:** سرعة الرياح ({wind_speed:.1f} km/h) مرتفعة! هناك احتمال كبير لتراكم الغبار على الألواح.")
    st.info("💡 **توصية AI:** ننصح ببرمجة تنظيف للألواح في الـ 24 ساعة القادمة لضمان أعلى كفاءة.")
else:
    st.success(f"✅ الجو هادئ حالياً ({wind_speed:.1f} km/h). كفاءة الامتصاص في أفضل مستوياتها.")

# خريطة الموقع
st.write("---")
st.subheader("📍 إحداثيات محطة الرصد")
st.map({'lat': [31.9316], 'lon': [-4.4244]}) # إحداثيات الرشيدية

st.sidebar.title("SolAI-DRT Pro")
st.sidebar.write("Project by: Atmane & Team")
