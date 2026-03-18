import streamlit as st
import pandas as pd
import datetime


st.title("📊 Study Dashboard")

# ---------------- SESSION INIT ----------------

if "stats" not in st.session_state:

    st.session_state.stats = {
        "questions": 0,
        "pdf_queries": 0,
        "quizzes": 0,
        "notes": 0
    }

if "activity_log" not in st.session_state:
    st.session_state.activity_log = []


stats = st.session_state.stats


# ---------------- USER GREETING ----------------

if "user" in st.session_state:

    st.success(f"Welcome back **{st.session_state.user}** 👋")


# ---------------- METRIC CARDS ----------------

st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Questions Asked", stats["questions"])
col2.metric("PDF Queries", stats["pdf_queries"])
col3.metric("Quizzes Generated", stats["quizzes"])
col4.metric("Notes Created", stats["notes"])


# ---------------- BAR CHART ----------------

st.subheader("📊 Tool Usage")

chart_data = pd.DataFrame(
    {
        "Usage": [
            stats["questions"],
            stats["pdf_queries"],
            stats["quizzes"],
            stats["notes"]
        ]
    },
    index=[
        "Questions",
        "PDF Queries",
        "Quizzes",
        "Notes"
    ]
)

st.bar_chart(chart_data)


# ---------------- PIE CHART ----------------

st.subheader("📈 Usage Distribution")

pie_data = pd.DataFrame({
    "Activity": [
        "Questions",
        "PDF Queries",
        "Quizzes",
        "Notes"
    ],
    "Count": [
        stats["questions"],
        stats["pdf_queries"],
        stats["quizzes"],
        stats["notes"]
    ]
})

st.write(pie_data)


# ---------------- PRODUCTIVITY SCORE ----------------

st.subheader("🎯 Study Productivity Score")

total_actions = sum(stats.values())

if total_actions == 0:
    score = 0
else:
    score = min(100, total_actions * 5)

st.progress(score)

st.write(f"Your productivity score: **{score}/100**")


# ---------------- ACTIVITY LOG ----------------

st.subheader("🕒 Recent Activity")

if st.session_state.activity_log:

    df = pd.DataFrame(st.session_state.activity_log)

    st.dataframe(df)

else:

    st.info("No activity yet.")


# ---------------- ADD ACTIVITY ----------------

def log_activity(action):

    st.session_state.activity_log.append({
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "action": action
    })


# Example usage
# log_activity("Generated Quiz")


# ---------------- SESSION ANALYTICS ----------------

st.subheader("📚 Session Analytics")

session_data = pd.DataFrame(
    {
        "Metric": [
            "Questions",
            "PDF Queries",
            "Quizzes",
            "Notes"
        ],
        "Value": [
            stats["questions"],
            stats["pdf_queries"],
            stats["quizzes"],
            stats["notes"]
        ]
    }
)

st.table(session_data)


# ---------------- STUDY INSIGHTS ----------------

st.subheader("🧠 AI Study Insights")

if stats["questions"] > 5:

    st.success("Great job asking questions! Active learners retain more information.")

if stats["pdf_queries"] > 3:

    st.info("You are using PDF assistant effectively.")

if stats["quizzes"] > 2:

    st.success("Quizzes help reinforce memory. Keep going!")

if total_actions == 0:

    st.warning("Start using tools to build your learning analytics.")


# ---------------- EXPORT DATA ----------------

st.subheader("📥 Export Analytics")

csv = session_data.to_csv(index=False)

st.download_button(
    "Download Analytics CSV",
    csv,
    "analytics.csv",
    "text/csv"
)


# ---------------- RESET BUTTON ----------------

st.subheader("⚙ Session Controls")

if st.button("Reset Session Stats"):

    st.session_state.stats = {
        "questions": 0,
        "pdf_queries": 0,
        "quizzes": 0,
        "notes": 0
    }

    st.session_state.activity_log = []

    st.success("Session reset complete.")

    st.rerun()


# ---------------- FUTURE FEATURES ----------------

st.subheader("🚀 Upcoming Features")

st.markdown("""
- Study streak tracking  
- AI learning recommendations  
- Weekly progress reports  
- Personalized study plans  
- Course completion analytics  
""")