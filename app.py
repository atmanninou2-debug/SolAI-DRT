import streamlit as st

# إعداد الصفحة لتكون احترافية
st.set_page_config(page_title="SolAI-DRT Pro", page_icon="☀️", layout="wide")

st.title("☀️ SolAI-DRT: Intelligent Dashboard")
st.markdown("#### نظام التتبع الذكي للطاقة الشمسية - جهة درعة تافيلالت")

# صناديق الإحصائيات الفورية
col1, col2, col3 = st.columns(3)
col1.metric("درجة الحرارة (الرشيدية)", "31°C", "1.5°C")
col2.metric("إنتاج الطاقة اليوم", "485 kWh", "15%")
col3.metric("توفير الكربون", "1.4 Ton", "0.2")

st.divider()

# قسم التفاعل والذكاء الاصطناعي
st.subheader("🔍 مراقبة حالة الألواح")
panel = st.selectbox("اختر محطة المراقبة:", ["Errachidia-Main", "Ouarzazate-Solar-1", "Midelt-Tech"])

c1, c2 = st.columns([2, 1])
with c1:
    eff = st.slider(f"كفاءة محطة {panel} (%)", 0, 100, 92)
    if eff < 80:
        st.error(f"⚠️ تنبيه: كفاءة {panel} منخفضة! احتمال تراكم الغبار.")
    else:
        st.success(f"✅ الحالة: {panel} تعمل بكفاءة مثالية.")

with c2:
    st.info("💡 **توصية AI:** من المتوقع هبوب رياح رملية غداً في منطقة درعة تافيلالت. ننصح ببرمجة تنظيف آلي للألواح.")

st.sidebar.title("SolAI-DRT Settings")
st.sidebar.info("هذا التطبيق هو MVP لمشروع مراقبة الطاقة الشمسية بالذكاء الاصطناعي.")
st.sidebar.write("---")
st.sidebar.write("By Atmane & Team")
