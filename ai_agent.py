import streamlit as st

# Function to handle user queries
def agent_response(query):
    responses = {
        "intro": (
            "### Meet Gowthami Bankuru - Your AI Candidate\n"
            "Welcome 😊!\n\n"
            "This AI agent introduces Gowthami Bankuru, showcasing her background, skills, experience, and understanding of the role. "
            "Feel free to explore using the menu items below or ask custom questions!"
        ),
        "tell me about yourself": (
            "Hello! I'm Gowthami Bankuru, a recent graduate with a Master's degree in Computer Software Engineering from the University of Maryland Baltimore County (UMBC), completed in December 2024."
            "I have a strong foundation in software engineering, cloud computing, and machine learning, coupled with experience in mentoring students "
            "and contributing to real-world projects. I am passionate about leveraging technology to solve complex challenges and drive innovation."
        ),
        "experience": (
            "I bring a wealth of professional experience, having worked as a Software Engineer at Cognizant, where I managed AWS cloud deployments, "
            "implemented ServiceNow modules, and developed scalable microservices. My efforts reduced downtime by 30% and enhanced system stability. "
            "Additionally, as a Graduate Teaching and Research Assistant at UMBC, I mentored students in software engineering principles and implemented "
            "a machine learning model to enhance program selection processes, improving data analysis and accessibility."
        ),
        "skills": (
            "My technical experience includes programming in Python, Java, C++, and frameworks such as Spring Boot, Flask, and RESTful APIs. "
            "I have proficiency in cloud platforms like AWS and Azure, and tools such as Docker, Jenkins, Postman, and Databricks. "
            "I'm experienced in working with databases like MySQL, PostgreSQL, MongoDB, and Neo4j, as well as working on both Windows and MacOS environments."
        ),
        "projects": (
            "I have worked on a variety of impactful projects, including:\n"
            "- **UMBC COEIT Undergraduate Program Selection-A Digital Mentor**: Designed a machine learning model deployed on AWS and Azure to streamline the program selection process.\n"
            "- **Real-time Twitter Sentiment Analysis**: Developed a system using NLP, Kafka, Flask, and MongoDB to analyze tweet sentiments in real-time.\n"
            "- **Airlines Delay Prediction**: Conducted flight delay analysis over four years of data using Python, PySpark, and Databricks to produce insightful visualizations.\n"
            "- **Operation Good Neighbor Website**: Built a community volunteering platform using Java, Android, MySQL, and MongoDB, with gamified features to encourage participation."
        ),
        "certifications": (
            "I have earned certifications in:\n"
            "- Apache Spark Programming with Databricks (February 2024)\n"
            "- AWS Cloud Quest: Cloud Practitioner (July 2024)\n"
            "- Core Java from Udemy (July 2020 - November 2020)"
        ),
        "education": (
            "I have earned a Master's degree in Computer Software Engineering at UMBC, with a strong GPA of 3.67, graduated in December 2024. "
            "Previously, I earned a Bachelor of Technology in Electrical and Electronics Engineering from Lovely Professional University, India, with a GPA of 3.23."
        ),
        "achievements": (
            "During my time at Cognizant, I achieved significant milestones, such as reducing downtime by 30% through proactive monitoring and bug fixes, "
            "and streamlining restaurant management systems with Docker-based deployments. At UMBC, as a research assistant, I implemented a machine learning model to improve graduate and undergraduate program selection, "
            "demonstrating my ability to apply cutting-edge technology to address institutional challenges."
        ),
        "understanding of the role": (
            "I understand that FutureMakers aims to prepare individuals and organizations for emerging challenges and opportunities. "
            "With my expertise in automation, AI, and agile methodologies, I can contribute to FutureMakers' goal of readiness by implementing "
            "efficient systems, optimizing processes, and ensuring scalability. My experience in managing cloud infrastructure and developing data-driven "
            "solutions positions me to anticipate and address readiness challenges proactively."
        ),
        "addressing futuremakers' goals for readiness": (
            "To address FutureMakers' goals for readiness, I would:\n"
            "- Leverage AI and machine learning to design predictive models that assess and enhance readiness levels.\n"
            "- Implement scalable cloud-based solutions using AWS and Azure to ensure agility and adaptability.\n"
            "- Collaborate cross-functionally to identify key readiness metrics and develop customized dashboards for monitoring progress.\n"
            "- Use my expertise in automation to streamline workflows and reduce bottlenecks, ensuring preparedness for dynamic challenges."
        )
    }
    return responses.get(query.lower(), "I can share about my background, skills, projects, certifications, or my understanding of the role. Please ask a specific question.")

# Sidebar menu for navigation
def sidebar_menu():
    # Accessible pages
    accessible_pages = {
        "Intro": lambda: st.markdown(agent_response("intro"), unsafe_allow_html=True),
        "About Me": lambda: st.write(agent_response("tell me about yourself")),
        "Experience": lambda: st.write(agent_response("experience")),
        "Skills": lambda: st.write(agent_response("skills")),
        "Projects": lambda: st.write(agent_response("projects")),
        "Certifications": lambda: st.write(agent_response("certifications")),
        "Education": lambda: st.write(agent_response("education")),
        "Achievements": lambda: st.write(agent_response("achievements")),
        "Role Understanding": lambda: st.write(agent_response("understanding of the role")),
        "Goals for Readiness": lambda: st.write(agent_response("addressing futuremakers' goals for readiness"))
    }

    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Intro"

    # CSS for light green buttons
    CSS = """
    <style>
    .stSidebar .stButton>button {
        background-color: #90ee90; /* Light Green */
        color: black;
        border: none;
        border-radius: 5px;
        padding: 8px;
        font-size: 14px;
        margin: 5px 0;
        cursor: pointer;
    }
    .stSidebar .stButton>button:hover {
        background-color: #76c776; /* Darker Green */
        color: white;
    }
    </style>
    """
    st.markdown(CSS, unsafe_allow_html=True)

    # Sidebar menu
    for option, func in accessible_pages.items():
        if st.sidebar.button(option):
            st.session_state["current_page"] = option

    # Execute the selected page
    accessible_pages[st.session_state["current_page"]]()

# Run the app
st.title("Meet Gowthami Bankuru - Your AI Candidate")
st.sidebar.title("Explore Gowthami's Profile")
sidebar_menu()

# Input field for custom questions
st.markdown("### Or ask a custom question below:")
user_input = st.text_input("Your question:")

if user_input:
    response = agent_response(user_input)
    st.write(response)
