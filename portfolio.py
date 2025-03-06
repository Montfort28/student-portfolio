import streamlit as st  
import pandas as pd  

# Set page configuration  
st.set_page_config(page_title="Student Portfolio", page_icon="🎓", layout="wide")  

# Sidebar navigation  
st.sidebar.title("📌 Navigation")  
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Customized Profile", "Contact"])  

# Owner credentials  
USERNAME = "montfort28"  
PASSWORD = "montfort@123"  
OWNER_NAME = "Mugisha Louis Marie de Monfort"  
OWNER_EMAIL = "Mugishamontfort28@gmail.com"  
LINKEDIN_PROFILE = "https://www.linkedin.com/in/sample-profile"  

# Authentication function  
def authenticate():  
    username = st.text_input("Enter Username")  
    password = st.text_input("Enter Password", type="password")  
    if username == USERNAME and password == PASSWORD:  
        return True  
    else:  
        return False  

# Home Section  
if page == "Home":  
    st.title("🎓 Student Portfolio")  

    # Button to enter authentication and update profile picture  
    if st.button("🔒 Update Profile Info"):  
        if authenticate():  
            uploaded_image = st.file_uploader("Upload profile picture", type=["jpg", "png"])  
            if uploaded_image:  
                st.image(uploaded_image, width=150, caption="Profile Pic")  
            else:  
                st.image("mont.jpg", width=150, caption="Default")  
        else:  
            st.warning("Invalid credentials!")  
    else:  
        st.image("mont.jpg", width=150, caption="Profile Pic (Owner Only)")  

    # Student Details  
    st.write(f"👤 **Name:** {OWNER_NAME}")  
    st.write(f"📧 **Email:** {OWNER_EMAIL}")  
    st.write(f"🔗 **LinkedIn:** [View Profile]({LINKEDIN_PROFILE})")  

    location = "Kigali, Rwanda"  
    field_of_study = "BSc Software Engineering"  
    university = "INES - Ruhengeri"  

    st.write(f"📌 {location}")  
    st.write(f"📚 {field_of_study}")  
    st.write(f"🌐 {university}")  

    # Download resume  
    with open("CV.pdf", "rb") as file:  
        resume_bytes = file.read()  
    st.download_button(label="📄 Download Resume",  
                       data=resume_bytes, file_name="CV.pdf", mime="application/pdf")  

    st.markdown("---")  

    # About Me section  
    st.subheader("About Me")  
    about_me = st.text_area("Write a short description about yourself", "I am an aspiring software engineer.")  
    st.write(about_me)  

# Projects Section  
elif page == "Projects":  
    st.title("💻 My Projects")  

    # Project Filtering  
    project_filter = st.selectbox("Filter projects by year:", ["All", "Year 1", "Year 2", "Year 3", "Final Year Project"])  

    projects = [  
        {"title": "Weather Forecast App", "year": "Year 1", "type": "Individual", "tech": "Python, API, Tkinter"},  
        {"title": "Student Grade Management System", "year": "Year 2", "type": "Group", "tech": "Java, MySQL"},  
        {"title": "E-commerce Website", "year": "Year 3", "type": "Individual", "tech": "PHP, HTML, CSS, JavaScript"},  
        {"title": "Inventory Management System", "year": "Year 3", "type": "Individual", "tech": "Python, Django"},  
        {"title": "Online Bus Ticket Booking System", "year": "Final Year Project", "type": "Individual", "tech": "React.js, Node.js, MongoDB"},  
    ]  

    df = pd.DataFrame(projects)  

    # Display filtered projects  
    if project_filter != "All":  
        df = df[df["year"] == project_filter]  

    for _, project in df.iterrows():  
        with st.expander(f"📊 {project['title']} ({project['year']})"):  
            st.write(f"**Type:** {project['type']}")  
            st.write(f"**Technologies:** {project['tech']}")  
            st.write("🔗 GitHub: [Link Not Available]")  

# Skills & Achievements  
elif page == "Skills":  
    st.title("🚀 Skills & Achievements")  

    st.subheader("Technical Skills")  
    st.progress(85)  # Python  
    st.write("Python: ⭐⭐⭐⭐⭐")  

    st.progress(80)  # JavaScript  
    st.write("JavaScript: ⭐⭐⭐⭐")  

    st.progress(70)  # Java  
    st.write("Java: ⭐⭐⭐")  

    st.progress(90)  # HTML & CSS  
    st.write("HTML & CSS: ⭐⭐⭐⭐⭐")  

    st.markdown("---")  

    st.subheader("Achievements")  
    st.write("✅ Built an E-commerce website from scratch")  
    st.write("✅ Developed a student grade management system")  
    st.write("✅ Created an online bus ticket booking system as a final year project")  

# Customize Profile  
elif page == "Customized Profile":  
    st.title("🛠️ Customize Your Profile")  

    if authenticate():  
        new_name = st.text_input("Edit Name", OWNER_NAME)  
        new_bio = st.text_area("Edit Bio", "I am an aspiring software engineer.")  

        if st.button("Save Changes"):  
            st.success("Profile Updated Successfully!")  
    else:  
        st.warning("You are not authorized to edit this profile.")  

# Contact Section  
elif page == "Contact":  
    st.title("📞 Contact Me")  

    st.write(f"📧 **Email:** {OWNER_EMAIL}")  
    st.write(f"🔗 **LinkedIn:** [View Profile]({LINKEDIN_PROFILE})")  

    name = st.text_input("Your Name")  
    email = st.text_input("Your Email")  
    message = st.text_area("Your Message")  

    if st.button("Send Message"):  
        st.success("Message Sent Successfully!")  

    st.markdown("---")  

    st.subheader("🔗 Connect With Me")  
    st.write("[LinkedIn](#) | [GitHub](#) | [Portfolio](#) | [Email](#)")  

# Sidebar Extras  
st.sidebar.markdown("---")  
st.sidebar.subheader("🗣️ Testimonials")  
st.sidebar.write("✅ 'Montfort is a brilliant problem solver!' - Mentor")  
st.sidebar.write("✅ 'Always delivers high-quality projects!' - Classmate")  

# Timeline  
st.sidebar.subheader("⏳ Academic Timeline")  
st.sidebar.write("📌 Year 1: Built a Weather Forecast App")  
st.sidebar.write("📌 Year 2: Developed a Grade Management System")  
st.sidebar.write("📌 Year 3: Created an E-commerce Website")  
st.sidebar.write("📌 Final Year: Working on an Online Bus Ticket System")  
