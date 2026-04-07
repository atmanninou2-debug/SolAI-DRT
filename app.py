import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="SolAI-DRT", page_icon="☀️")

st.title("☀️ SolAI-DRT: Intelligent Solar Monitoring")
st.markdown("### مراقبة ذكية للألواح الشمسية - جهة درعة تافيلالت")

# واجهة تفاعلية للتجريب
st.info("قم بتحريك المؤشر لمحاكاة كفاءة الألواح")
efficiency = st.slider("كفاءة الألواح الحالية (%)", 0, 100, 85)

if efficiency < 80:
    st.error(f"⚠️ تنبيه: الكفاءة منخفضة ({efficiency}%). احتمال وجود غبار!")
    st.button("إرسال طلب تنظيف 🧹")
else:
    st.success(f"✅ الحالة ممتازة! الكفاءة هي {efficiency}%")

st.divider()
st.write("📍 موقع المشروع: الرشيدية / ورزازات")
