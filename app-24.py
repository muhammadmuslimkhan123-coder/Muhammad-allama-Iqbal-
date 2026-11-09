# Allama Iqbal Biography & Poetry Web App
# Created by Muhammad Muslim Abbas
# Python-only application (Streamlit). No HTML/C/C++/Java/JavaScript written.

import streamlit as st

st.set_page_config(page_title="Allama Iqbal | Biography & Poetry", page_icon="📚", layout="wide")

PHOTO_URL = "https://upload.wikimedia.org/wikipedia/commons/a/ac/Allama_Iqbal.jpg"

st.markdown("""
# علامہ محمد اقبال
### Allama Muhammad Iqbal — Biography, Books & Poetry
**Created by Muhammad Muslim Abbas**
""")

with st.sidebar:
    st.title("Menu")
    section = st.radio("Open section", [
        "Home", "Biography", "Education", "Family", "Books",
        "Urdu Poetry", "Persian Poetry", "Gallery", "Sources"
    ])

if section == "Home":
    c1, c2 = st.columns([1, 2])
    with c1:
        try:
            st.image(PHOTO_URL, caption="Allama Muhammad Iqbal (historical photograph)", use_container_width=True)
        except Exception:
            st.info("تصویر دیکھنے کے لیے انٹرنیٹ درکار ہے۔")
    with c2:
        st.subheader("شاعرِ مشرق")
        st.write("علامہ محمد اقبال شاعر، فلسفی، قانون دان اور مفکر تھے۔ ان کی شاعری میں خودی، علم، عمل، اتحاد اور بیداری کا پیغام نمایاں ہے۔")
        st.write("پیدائش: 9 نومبر 1877 — سیالکوٹ")
        st.write("وفات: 21 اپریل 1938 — لاہور")
        st.write("قبر: بادشاہی مسجد اور لاہور قلعہ کے درمیان، لاہور")
        st.caption("تعلیمی نمبروں کے مکمل سرکاری ریکارڈ دستیاب ذرائع میں نہیں ملتے؛ اس لیے غیر مصدقہ نمبر شامل نہیں کیے گئے۔")

elif section == "Biography":
    st.header("زندگی کا تعارف")
    st.write("""
علامہ اقبال 9 نومبر 1877 کو سیالکوٹ میں پیدا ہوئے۔ ان کے والد کا نام شیخ نور محمد اور والدہ کا نام امام بی بی تھا۔
انہوں نے ابتدائی تعلیم سیالکوٹ میں حاصل کی، پھر لاہور اور یورپ میں اعلیٰ تعلیم حاصل کی۔
وہ اردو اور فارسی کے بڑے شاعر اور فلسفی تھے۔ 21 اپریل 1938 کو لاہور میں وفات پائی۔
""")
    st.subheader("اہم معلومات")
    st.table([
        ["پورا نام", "ڈاکٹر سر محمد اقبال"],
        ["تاریخ پیدائش", "9 نومبر 1877"],
        ["جائے پیدائش", "سیالکوٹ، پنجاب"],
        ["تاریخ وفات", "21 اپریل 1938"],
        ["جائے وفات", "لاہور"],
        ["پیشہ", "شاعر، فلسفی، قانون دان"],
        ["زبانیں", "اردو، فارسی، انگریزی"]
    ])

elif section == "Education":
    st.header("تعلیم اور تعلیمی کامیابیاں")
    st.table([
        ["1893–1895", "اسکاچ مشن کالج، سیالکوٹ", "ہائی اسکول اور انٹرمیڈیٹ"],
        ["1897", "گورنمنٹ کالج، لاہور", "بی اے؛ عربی اور فلسفہ"],
        ["1899", "گورنمنٹ کالج، لاہور", "ایم اے فلسفہ؛ پنجاب میں اول پوزیشن"],
        ["1905–1907", "ٹرینٹی کالج، کیمبرج", "فلسفہ کی اعلیٰ تعلیم"],
        ["1907", "میونخ یونیورسٹی، جرمنی", "فلسفہ میں ڈاکٹریٹ (PhD)"],
        ["1908", "لنکنز اِن، لندن", "بار ایٹ لا"]
    ])
    st.subheader("ایوارڈز اور نمبر")
    st.write("معتبر سوانحی ذرائع کے مطابق اقبال نے بی اے میں عربی اور انگریزی میں گولڈ میڈل حاصل کیے، جبکہ ایم اے فلسفہ میں پنجاب میں پہلی پوزیشن حاصل کی۔")
    st.warning("ہر امتحان کے حاصل کردہ عددی مارکس/فیصد کا مستند مکمل ریکارڈ دستیاب نہیں؛ کوئی فرضی نمبر درج نہیں کیے گئے۔")

elif section == "Family":
    st.header("خاندان")
    st.write("والد: شیخ نور محمد")
    st.write("والدہ: امام بی بی")
    st.write("اقبال کی پہلی شادی کریم بی بی سے ہوئی۔ ان کے بچوں میں آفتاب اقبال اور معراج بیگم کے نام معروف ہیں۔ بعض سوانح میں ایک تیسرے بچے کا بھی ذکر ملتا ہے جو بچپن میں وفات پا گیا۔")
    st.write("اقبال کے خاندانی حالات اور رشتوں کی تفصیل کے لیے مستند سوانحی ماخذ ملاحظہ کریں۔")
    st.link_button("International Iqbal Society — Life of Iqbal", "https://www.iqbal.com.pk/iqbal/life-of-iqbal.html")
    st.info("خاندان کے افراد کی غیر مصدقہ تصاویر یا نجی تفصیلات شامل نہیں کی گئیں۔")

elif section == "Books":
    st.header("کتابیں — ہر کتاب کا الگ مطالعہ لنک")
    books = [
        ("Ilm-ul-Iqtisad (1903)", "https://www.iqbalcyberlibrary.net/"),
        ("Asrar-e-Khudi (1915)", "https://www.iqbalcyberlibrary.net/"),
        ("Rumuz-e-Bekhudi (1918)", "https://www.iqbalcyberlibrary.net/"),
        ("Payam-e-Mashriq (1923)", "https://www.iqbalcyberlibrary.net/"),
        ("Bang-e-Dara (1924)", "https://www.iqbalcyberlibrary.net/"),
        ("Zabur-e-Ajam (1927)", "https://www.iqbalcyberlibrary.net/"),
        ("Javid Nama (1932)", "https://www.iqbalcyberlibrary.net/"),
        ("Musafir (1934)", "https://www.iqbalcyberlibrary.net/"),
        ("Bal-e-Jibril (1935/1936)", "https://www.iqbalcyberlibrary.net/"),
        ("Zarb-e-Kalim (1936)", "https://www.iqbalcyberlibrary.net/"),
        ("Pas Cheh Bayad Kard (1936)", "https://www.iqbalcyberlibrary.net/"),
        ("Armaghan-e-Hijaz (1938, بعد از وفات شائع)", "https://www.iqbalcyberlibrary.net/"),
        ("The Reconstruction of Religious Thought in Islam", "https://www.iqbalcyberlibrary.net/")
    ]
    for name, url in books:
        st.markdown(f"- **{name}** — [کتابوں کی لائبریری میں کھولیں]({url})")
    st.caption("یہ لنکس اقبال سائبر لائبریری کے مجموعے کی طرف رہنمائی کرتے ہیں؛ ہر کتاب کا الگ مستقل صفحہ وہاں تلاش کیا جا سکتا ہے۔")

elif section == "Urdu Poetry":
    st.header("اردو شاعری")
    poems = [
        ("شکوہ", "https://www.iqbal.com.pk/"),
        ("جوابِ شکوہ", "https://www.iqbal.com.pk/"),
        ("لب پہ آتی ہے دعا", "https://www.iqbal.com.pk/"),
        ("مسجدِ قرطبہ", "https://www.iqbal.com.pk/"),
        ("طلوعِ اسلام", "https://www.iqbal.com.pk/"),
        ("سارے جہاں سے اچھا", "https://www.iqbal.com.pk/")
    ]
    for title, url in poems:
        st.markdown(f"- **{title}** — [کلامِ اقبال میں کھولیں]({url})")

elif section == "Persian Poetry":
    st.header("فارسی شاعری")
    for title in ["اسرارِ خودی", "رموزِ بے خودی", "پیامِ مشرق", "زبورِ عجم", "جاوید نامہ", "پس چہ باید کرد"]:
        st.markdown(f"- **{title}** — [اقبال سائبر لائبریری میں تلاش کریں](https://www.iqbalcyberlibrary.net/)")

elif section == "Gallery":
    st.header("تصویری گیلری")
    st.image(PHOTO_URL, caption="علامہ محمد اقبال — تاریخی تصویر (Wikimedia Commons)", use_container_width=True)
    st.markdown("[اصل JPG تصویر Wikimedia Commons پر کھولیں](https://commons.wikimedia.org/wiki/File:Allama_Iqbal.jpg)")
    st.caption("اس ایپ میں نیٹ ورک دستیاب ہونے پر اصل تاریخی تصویر آن لائن لوڈ ہوتی ہے۔")

elif section == "Sources":
    st.header("مستند معلومات کے ذرائع")
    st.markdown("""
- [Iqbal Academy Pakistan — Biography](https://www.allamaiqbal.com/biography/en/index.php)
- [Iqbal Academy Pakistan — Chronology](https://www.allamaiqbal.com/biography/en/chronology.php)
- [International Iqbal Society — Life of Iqbal](https://www.iqbal.com.pk/iqbal/life-of-iqbal.html)
- [International Iqbal Society — Timeline](https://www.iqbal.com.pk/iqbal/time-line.html)
- [Iqbal Cyber Library](https://www.iqbalcyberlibrary.net/)
- [Wikimedia Commons — Allama Iqbal JPG and licensing](https://commons.wikimedia.org/wiki/File:Allama_Iqbal.jpg)
""")

st.divider()
st.caption("Created by Muhammad Muslim Abbas | Educational project")
