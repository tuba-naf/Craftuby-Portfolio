# import streamlit as st
# import os
# import base64
# from pathlib import Path

# st.set_page_config(page_title="TN PORTFOLIO", layout="wide")

# # --- Admin Password Protection ---
# st.sidebar.markdown("### Admin Access")
# password = st.sidebar.text_input("Enter admin password", type="password")
# ADMIN_PASSWORD = "your_secret_password"  # Change this to your actual password
# IS_ADMIN = password == ADMIN_PASSWORD

# # --- Upload directory ---
# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# def save_file(upload, subfolder, filename=None):
#     folder = Path(UPLOAD_DIR) / subfolder
#     folder.mkdir(parents=True, exist_ok=True)
#     path = folder / (filename or upload.name)
#     with open(path, "wb") as f:
#         f.write(upload.getbuffer())
#     return str(path)

# def load_saved_images(subfolder):
#     folder = Path(UPLOAD_DIR) / subfolder
#     if folder.exists():
#         return list(folder.glob("*"))
#     return []

# def delete_file(file_path):
#     os.remove(file_path)

# # --- Sidebar Logo Upload ---
# with st.sidebar:
#     st.markdown("### Upload Logo")
#     logo_file = st.file_uploader("Logo", type=["png", "jpg", "jpeg"], key="logo_upload")
#     if logo_file:
#         logo_path = save_file(logo_file, "logo", "logo.png")
#     else:
#         logo_path = os.path.join(UPLOAD_DIR, "logo", "logo.png")

# # --- Load and Encode Logo ---
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as f:
#         logo_b64 = base64.b64encode(f.read()).decode()
#         logo_img_html = f'<img src="data:image/png;base64,{logo_b64}" class="logo-img"/>'
# else:
#     logo_img_html = '<h3 class="logo-text">TN LOGO</h3>'

# # --- CSS + JS for Responsive Navbar ---
# st.markdown("""
# <style>
# .navbar {
#     background-color: black;
#     padding: 10px 20px;
#     color: white;
#     position: relative;
#     z-index: 999;
# }
# .navbar-container {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     flex-wrap: wrap;
# }
# .logo-img {
#     height: 40px;
# }
# .logo-text {
#     color: white;
#     font-size: 20px;
#     font-weight: bold;
# }
# #menu-toggle {
#     display: none;
# }
# .menu-icon {
#     display: none;
#     font-size: 24px;
#     cursor: pointer;
#     user-select: none;
#     color: white;
# }
# .nav-links {
#     display: flex;
#     gap: 15px;
#     flex-wrap: wrap;
# }
# .nav-links a {
#     color: white;
#     text-decoration: none;
#     font-weight: bold;
#     padding: 8px 12px;
# }
# .nav-links a:hover {
#     color: #60A5FA;
# }
# @media (max-width: 768px) {
#     .navbar-container {
#         flex-direction: column;
#         align-items: center;
#     }
#     .menu-icon {
#         display: block;
#         margin-top: 10px;
#     }
#     .nav-links {
#         display: none;
#         flex-direction: column;
#         width: 100%;
#         padding-top: 10px;
#         align-items: center;
#     }
#     #menu-toggle:checked + .menu-icon + .nav-links {
#         display: flex;
#     }
#     .navbar-logo {
#         display: none;
#     }
# }
# /* Offset anchor scroll position */
# a[name]::before {
#     display: block;
#     content: " ";
#     height: 70px;
#     margin-top: -70px;
#     visibility: hidden;
# }
# </style>
# """, unsafe_allow_html=True)

# # --- Navbar HTML ---
# nav_links = [
#     ("Home", "#home"),
#     ("About", "#about"),
#     ("Success Stories", "#success"),
#     ("Books", "#books"),
#     ("Poetries", "#poetries"),
#     ("News Articles", "#news"),
#     ("Magazine", "#magazine"),
#     ("Certifications", "#certifications"),
#     ("Contact", "#contact"),
# ]

# st.markdown(f"""
# <div class="navbar">
#     <div class="navbar-container">
#         <div class="navbar-logo">{logo_img_html}</div>
#         <input type="checkbox" id="menu-toggle" />
#         <label class="menu-icon" for="menu-toggle">☰</label>
#         <div class="nav-links" id="navMenu">
#             {''.join([f'<a href="{link}">{name}</a>' for name, link in nav_links])}
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # --- Carousel Section ---
# st.markdown('<h3 id="carousel">Carousel</h3>', unsafe_allow_html=True)
# carousel_files = st.file_uploader("Upload carousel images", type=["png", "jpg", "jpeg"], accept_multiple_files=True, key="carousel_upload")
# if carousel_files:
#     for file in carousel_files:
#         save_file(file, "carousel")

# for img_path in load_saved_images("carousel"):
#     st.image(str(img_path), use_container_width=True)
#     if st.button(f"🗑️ Delete {img_path.name}", key=f"del_carousel_{img_path.name}"):
#         delete_file(img_path)
#         st.rerun()

# st.markdown("---")

# # --- Section Template ---
# def section_block(id_str, title):
#     st.markdown(f'<a name="{id_str}"></a>', unsafe_allow_html=True)
#     st.markdown(f"## {title}")
#     st.write(f"Welcome to the **{title}** section.")

#     uploaded = st.file_uploader(f"Upload image for {title}", type=["png", "jpg", "jpeg"], key=id_str)
#     if uploaded:
#         save_file(uploaded, id_str)

#     saved_imgs = load_saved_images(id_str)
#     for i in range(0, len(saved_imgs), 3):
#         cols = st.columns(3)
#         for j, col in enumerate(cols):
#             if i + j < len(saved_imgs):
#                 img_path = saved_imgs[i + j]
#                 with col:
#                     st.image(str(img_path), use_container_width=True)
#                     if st.button(f"🗑️ Delete {img_path.name}", key=f"del_{id_str}_{img_path.name}"):
#                         delete_file(img_path)
#                         st.rerun()
#     st.markdown("---")

# # --- Sections ---
# section_block("about", "About")
# section_block("success", "Success Stories")
# section_block("books", "Books")
# section_block("poetries", "Poetries")
# section_block("news", "News Articles")
# section_block("magazine", "Magazine")
# section_block("certifications", "Certifications")

# # --- Contact Section ---
# section_block("contact", "Contact")
# with st.form("contact_form"):
#     name = st.text_input("Your Name")
#     email = st.text_input("Your Email")
#     message = st.text_area("Message")
#     if st.form_submit_button("Send"):
#         st.success("Your message has been sent!")

# # --- Footer ---
# st.markdown("""
# <div class="footer" style="margin-top: 4rem; padding: 1rem; background-color: #f0f0f0; text-align: center; color: #333;">
#     &copy; 2025 TN PORTFOLIO. All rights reserved.
# </div>
# """, unsafe_allow_html=True)

# # 
# import streamlit as st
# import os
# import base64
# from pathlib import Path

# st.set_page_config(page_title="TN PORTFOLIO", layout="wide")

# # --- Admin Password Protection ---
# st.sidebar.markdown("### Admin Access")
# password = st.sidebar.text_input("Enter admin password", type="password")
# ADMIN_PASSWORD = "Sunshine404"  # Change this to your actual password
# IS_ADMIN = password == ADMIN_PASSWORD

# # --- Upload directory ---
# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# def save_file(upload, subfolder, filename=None):
#     folder = Path(UPLOAD_DIR) / subfolder
#     folder.mkdir(parents=True, exist_ok=True)
#     path = folder / (filename or upload.name)
#     with open(path, "wb") as f:
#         f.write(upload.getbuffer())
#     return str(path)

# def load_saved_images(subfolder):
#     folder = Path(UPLOAD_DIR) / subfolder
#     if folder.exists():
#         return list(folder.glob("*"))
#     return []

# def delete_file(file_path):
#     os.remove(file_path)

# # --- Sidebar Logo Upload ---
# with st.sidebar:
#     st.markdown("### Upload Logo")
#     if IS_ADMIN:
#         logo_file = st.file_uploader("Logo", type=["png", "jpg", "jpeg"], key="logo_upload")
#         if logo_file:
#             logo_path = save_file(logo_file, "logo", "logo.png")
#         else:
#             logo_path = os.path.join(UPLOAD_DIR, "logo", "logo.png")
#     else:
#         logo_path = os.path.join(UPLOAD_DIR, "logo", "logo.png")

# # --- Load and Encode Logo ---
# if os.path.exists(logo_path):
#     with open(logo_path, "rb") as f:
#         logo_b64 = base64.b64encode(f.read()).decode()
#         logo_img_html = f'<img src="data:image/png;base64,{logo_b64}" class="logo-img"/>'
# else:
#     logo_img_html = '<h3 class="logo-text">TN LOGO</h3>'

# # --- CSS + JS for Responsive Navbar ---
# st.markdown("""
# <style>
# .navbar {
#     background-color: black;
#     padding: 10px 20px;
#     color: white;
#     position: relative;
#     z-index: 999;
# }
# .navbar-container {
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     flex-wrap: wrap;
# }
# .logo-img {
#     height: 40px;
# }
# .logo-text {
#     color: white;
#     font-size: 20px;
#     font-weight: bold;
# }
# #menu-toggle {
#     display: none;
# }
# .menu-icon {
#     display: none;
#     font-size: 24px;
#     cursor: pointer;
#     user-select: none;
#     color: white;
# }
# .nav-links {
#     display: flex;
#     gap: 15px;
#     flex-wrap: wrap;
# }
# .nav-links a {
#     color: white;
#     text-decoration: none;
#     font-weight: bold;
#     padding: 8px 12px;
# }
# .nav-links a:hover {
#     color: #60A5FA;
# }
# @media (max-width: 768px) {
#     .navbar-container {
#         flex-direction: column;
#         align-items: center;
#     }
#     .menu-icon {
#         display: block;
#         margin-top: 10px;
#     }
#     .nav-links {
#         display: none;
#         flex-direction: column;
#         width: 100%;
#         padding-top: 10px;
#         align-items: center;
#     }
#     #menu-toggle:checked + .menu-icon + .nav-links {
#         display: flex;
#     }
#     .navbar-logo {
#         display: none;
#     }
# }
# a[name]::before {
#     display: block;
#     content: " ";
#     height: 70px;
#     margin-top: -70px;
#     visibility: hidden;
# }
# </style>
# """, unsafe_allow_html=True)

# # --- Navbar HTML ---
# nav_links = [
#     ("Home", "#home"),
#     ("About", "#about"),
#     ("Success Stories", "#success"),
#     ("Books", "#books"),
#     ("Poetries", "#poetries"),
#     ("News Articles", "#news"),
#     ("Magazine", "#magazine"),
#     ("Certifications", "#certifications"),
#     ("Contact", "#contact"),
# ]

# st.markdown(f"""
# <div class="navbar">
#     <div class="navbar-container">
#         <div class="navbar-logo">{logo_img_html}</div>
#         <input type="checkbox" id="menu-toggle" />
#         <label class="menu-icon" for="menu-toggle">☰</label>
#         <div class="nav-links" id="navMenu">
#             {''.join([f'<a href="{link}">{name}</a>' for name, link in nav_links])}
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # --- Carousel Section ---
# st.markdown('<h3 id="carousel">Carousel</h3>', unsafe_allow_html=True)
# if IS_ADMIN:
#     carousel_files = st.file_uploader("Upload carousel files", type=["png", "jpg", "jpeg", "pdf"], accept_multiple_files=True, key="carousel_upload")
#     if carousel_files:
#         for file in carousel_files:
#             save_file(file, "carousel")

# for img_path in load_saved_images("carousel"):
#     ext = img_path.suffix.lower()
#     if ext == ".pdf":
#         st.markdown(f"[📄 {img_path.name}](/{img_path})")
#     else:
#         st.image(str(img_path), use_container_width=True)
#     if IS_ADMIN and st.button(f"🗑️ Delete {img_path.name}", key=f"del_carousel_{img_path.name}"):
#         delete_file(img_path)
#         st.rerun()

# st.markdown("---")

# # --- Section Template ---
# def section_block(id_str, title):
#     st.markdown(f'<a name="{id_str}"></a>', unsafe_allow_html=True)
#     st.markdown(f"## {title}")
#     st.write(f"Welcome to the **{title}** section.")

#     if IS_ADMIN:
#         uploaded = st.file_uploader(f"Upload image or PDF for {title}", type=["png", "jpg", "jpeg", "pdf"], key=id_str)
#         if uploaded:
#             save_file(uploaded, id_str)

#     saved_files = load_saved_images(id_str)
#     for i in range(0, len(saved_files), 3):
#         cols = st.columns(3)
#         for j, col in enumerate(cols):
#             if i + j < len(saved_files):
#                 file_path = saved_files[i + j]
#                 ext = file_path.suffix.lower()
#                 with col:
#                     if ext in [".png", ".jpg", ".jpeg"]:
#                         st.image(str(file_path), use_container_width=True)
#                     elif ext == ".pdf":
#                         st.markdown(f"[📄 {file_path.name}](/{file_path})")
#                     if IS_ADMIN and st.button(f"🗑️ Delete {file_path.name}", key=f"del_{id_str}_{file_path.name}"):
#                         delete_file(file_path)
#                         st.rerun()
#     st.markdown("---")

# # --- Sections ---
# section_block("about", "About")
# st.markdown("""
# **Co-Author – English Poetic and Prose Anthologies**  
# *Published by Series of Words (2023–2025)*  
# Books:  
# 1. *Lost in Solitude*  
# 2. *Brushing the Pages*  
# 3. *Hope*  
# 4. *Reverie*  
# 5. *Memento Mori*

# **Co-Author – Urdu Poetic Anthology**  
# *Moj-e-Dill*, published by *Iqbal-e-Sukhan* (2023)

# **Author – Express Tribune**  
# Contributor to opinion section *The Way I Think* (2023)

# **Content Writing Trainee – NS Training Pvt. Ltd.**  
# Completed training in content development and writing (2022)
# """)
# section_block("success", "Success Stories")
# section_block("books", "Books")
# section_block("poetries", "Poetries")
# section_block("news", "News Articles")
# section_block("magazine", "Magazine")
# section_block("certifications", "Certifications")

# # --- Contact Section ---
# section_block("contact", "Contact")
# with st.form("contact_form"):
#     name = st.text_input("Your Name")
#     email = st.text_input("Your Email")
#     message = st.text_area("Message")
#     if st.form_submit_button("Send"):
#         st.success("Your message has been sent!")

# # --- Footer ---
# st.markdown("""
# <div class="footer" style="margin-top: 4rem; padding: 1rem; background-color: #f0f0f0; text-align: center; color: #333;">
#     &copy; 2025 TN PORTFOLIO. All rights reserved.
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import os
import base64
from pathlib import Path

st.set_page_config(page_title="TN PORTFOLIO", layout="wide")

# --- Admin Password Protection ---
st.sidebar.markdown("### Admin Access")
password = st.sidebar.text_input("Enter admin password", type="password")

# ✅ Secure password using Streamlit secrets
ADMIN_PASSWORD = st.secrets["admin"]["password"]
IS_ADMIN = password == ADMIN_PASSWORD


# # --- Admin Password Protection ---
# st.sidebar.markdown("### Admin Access")
# password = st.sidebar.text_input("Enter admin password", type="password")
# ADMIN_PASSWORD = "Sunshine404"
# IS_ADMIN = password == ADMIN_PASSWORD

# --- Upload directory ---
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_file(upload, subfolder, filename=None):
    folder = Path(UPLOAD_DIR) / subfolder
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / (filename or upload.name)
    with open(path, "wb") as f:
        f.write(upload.getbuffer())
    return str(path)

def load_saved_images(subfolder):
    folder = Path(UPLOAD_DIR) / subfolder
    if folder.exists():
        return list(folder.glob("*"))
    return []

def delete_file(file_path):
    os.remove(file_path)

# --- Sidebar Logo Upload ---
with st.sidebar:
    st.markdown("### Upload Logo")
    if IS_ADMIN:
        logo_file = st.file_uploader("Logo", type=["png", "jpg", "jpeg"], key="logo_upload")
        if logo_file:
            logo_path = save_file(logo_file, "logo", "logo.png")
        else:
            logo_path = os.path.join(UPLOAD_DIR, "logo", "logo.png")
    else:
        logo_path = os.path.join(UPLOAD_DIR, "logo", "logo.png")

# --- Load and Encode Logo ---
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode()
        logo_img_html = f'<img src="data:image/png;base64,{logo_b64}" class="logo-img"/>'
else:
    logo_img_html = '<h3 class="logo-text">TN LOGO</h3>'

# --- CSS for Navbar ---
st.markdown("""
<style>
.navbar {
    background-color: black;
    padding: 10px 20px;
    color: white;
    position: relative;
    z-index: 999;
}
.navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}
.logo-img {
    height: 40px;
}
.logo-text {
    color: white;
    font-size: 20px;
    font-weight: bold;
}
#menu-toggle {
    display: none;
}
.menu-icon {
    display: none;
    font-size: 24px;
    cursor: pointer;
    user-select: none;
    color: white;
}
.nav-links {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
}
.nav-links a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    padding: 8px 12px;
}
.nav-links a:hover {
    color: #60A5FA;
}
@media (max-width: 768px) {
    .navbar-container {
        flex-direction: column;
        align-items: center;
    }
    .menu-icon {
        display: block;
        margin-top: 10px;
    }
    .nav-links {
        display: none;
        flex-direction: column;
        width: 100%;
        padding-top: 10px;
        align-items: center;
    }
    #menu-toggle:checked + .menu-icon + .nav-links {
        display: flex;
    }
    .navbar-logo {
        display: none;
    }
}
a[name]::before {
    display: block;
    content: " ";
    height: 70px;
    margin-top: -70px;
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# --- Navbar HTML ---
nav_links = [
    ("Home", "#home"),
    ("About", "#about"),
    ("Success Stories", "#success"),
    ("Books", "#books"),
    ("Poetry", "#poetry"),
    ("News Articles", "#news"),
    ("Magazine", "#magazine"),
    ("Certifications", "#certifications"),
    ("Contact", "#contact"),
]

st.markdown(f"""
<div class="navbar">
    <div class="navbar-container">
        <div class="navbar-logo">{logo_img_html}</div>
        <input type="checkbox" id="menu-toggle" />
        <label class="menu-icon" for="menu-toggle">☰</label>
        <div class="nav-links" id="navMenu">
            {''.join([f'<a href="{link}">{name}</a>' for name, link in nav_links])}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Carousel Section ---
# st.markdown('<h3 id="carousel">Carousel</h3>', unsafe_allow_html=True)
st.markdown('<h3 id="carousel" style="display:none;"></h3>', unsafe_allow_html=True)
if IS_ADMIN:
    carousel_files = st.file_uploader("Upload carousel files", type=["png", "jpg", "jpeg", "pdf"], accept_multiple_files=True, key="carousel_upload")
    if carousel_files:
        for file in carousel_files:
            save_file(file, "carousel")

for img_path in load_saved_images("carousel"):
    ext = img_path.suffix.lower()
    if ext == ".pdf":
        with open(img_path, "rb") as pdf_file:
            base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
            pdf_view = f"""
                <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="400px"></iframe>
                <br><a href="data:application/pdf;base64,{base64_pdf}" download="{img_path.name}" target="_blank">📄 Download {img_path.name}</a>
            """
            st.markdown(pdf_view, unsafe_allow_html=True)
    else:
        st.image(str(img_path), use_container_width=True)
    if IS_ADMIN and st.button(f"🗑️ Delete {img_path.name}", key=f"del_carousel_{img_path.name}"):
        delete_file(img_path)
        st.rerun()

st.markdown("---")

# --- Section Template ---

def section_block(id_str, title, description=None):
    st.markdown(f'<a name="{id_str}"></a>', unsafe_allow_html=True)
    st.markdown(f"## {title}")

    if description:
        st.markdown(description)

    if IS_ADMIN:
        uploaded = st.file_uploader(f"Upload image or PDF for {title}", type=["png", "jpg", "jpeg", "pdf"], key=id_str)
        if uploaded:
            save_file(uploaded, id_str)

    saved_files = load_saved_images(id_str)
    for i in range(0, len(saved_files), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(saved_files):
                file_path = saved_files[i + j]
                ext = file_path.suffix.lower()
                with col:
                    if ext in [".png", ".jpg", ".jpeg"]:
                        st.image(str(file_path), use_container_width=True)
                    elif ext == ".pdf":
                        with open(file_path, "rb") as pdf_file:
                            base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
                            pdf_view = f"""
                                <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="400px"></iframe>
                                <br><a href="data:application/pdf;base64,{base64_pdf}" download="{file_path.name}" target="_blank">📄 Download {file_path.name}</a>
                            """
                            st.markdown(pdf_view, unsafe_allow_html=True)
                    if IS_ADMIN and st.button(f"🗑️ Delete {file_path.name}", key=f"del_{id_str}_{file_path.name}"):
                        delete_file(file_path)
                        st.rerun()
    st.markdown("---")

# --- Sections ---
section_block("about", "About")
st.markdown("""
**Research article accepted for publication in the Pakistan Journal of Botany (2025); galley proof received.**
            
**Led Project Management and Marketing for the Research Magazine at SBA in 2025.**
                        
**Served on the Editorial Board of Life Chronicles Research Magazine at SBA in 2024.**
            
**Co-Author – English Poetic and Prose Anthologies.(2023–2025)**  
**Books:Published by Series of Words.**
  
1. **Lost in Solitude**  
2. **Brushing the Pages**  
3. **Hope**  
4. **Reverie**  
5. **Memento Mori**

**Co-Author – Urdu Poetic Anthology (2023)**  
*Moj-e-Dill*, published by *Iqbal-e-Sukhan.* 

**Author – Express Tribune (2023)**  
Contributor to opinion section *The Way I Think.* 

**Content Writing Trainee – NS Training Pvt. Ltd. (2022)**  
Completed training in content development and writing. 
            
**Carried out thesis research in the field of Plant Tissue Culture (PTC) at the Department of Biotechnology, University of Karachi (UoK) in 2019.**            
""")
section_block("success", 
              "Success Stories",
              description="""
   **Research article accepted for publication in the Pakistan Journal of Botany (2025); galley proof received.**         

- **Poem _Biotech to Biocon_**  
  Presented at the *Second International Conference of Biotechnology, Biocon 2.0 (2024)*

- **First Position Award**  
  Poetry Competition, conducted by *Spirit Financial Enterprises (2023)*

- **Independent Winner Award**  
  Creative Writing Open Contest on *Biodiversity of Pakistan*, organized by *ACP & Collaborators (2023)*
"""
              )
section_block(
    "books",
    "Books",
    description="""
    Co-authored five English anthologies—*Lost in Solitude*, *Brushing the Pages*, *Hope*, *Reverie*, and *Memento Mori*—published by Series of Words (2023–2025). Each volume weaves poetic and reflective prose that explores emotional resilience, introspection, and the passage of time.
    Featured books include:
    - *Lost in Solitude*
    - *Brushing the Pages*
    - *Hope*
    - *Reverie*
    - *Memento Mori*
 
    """
)
st.write("View full book content at Series of Words(https://seriesofwords.com.pk/)  ")
section_block("poetry", 
              "Poetry",
              description="""
              Co-author of several English anthologies (2023–2025) and the Urdu poetic anthology *Moj-e-Dill* (2023), published by *Iqbal-e-Sukhan*. These collections feature original poems reflecting diverse emotional and cultural themes.
""")
section_block("news", 
              "News Articles",
              description="""
Contributed opinion pieces to *The Express Tribune* in 2023 under the column *The Way I Think*, addressing social and cultural topics. Also completed formal training in content writing at NS Training Pvt. Ltd. in 2022.
""")
section_block("magazine", 
              "Magazine",
              description="""
Led project management and marketing for the Research Magazine at SBA in 2025 and served on the editorial board of *Life Chronicles* magazine in 2024. These publications focus on scientific and academic contributions lifescience especially in biotechnology research.
"""
              )
st.write("View magazine content at https://www.sindhbiotech.com")
section_block("certifications", "Certifications")

# --- Contact Section ---
section_block("contact", "Contact")

"""**DM or email at tuba.nafees4@gmail.com**"""

# --- Footer ---
st.markdown("""
<div class="footer" style="margin-top: 4rem; padding: 1rem; background-color: #f0f0f0; text-align: center; color: #333;">
    &copy; 2025 TN PORTFOLIO. All rights reserved.
</div>
""", unsafe_allow_html=True)
