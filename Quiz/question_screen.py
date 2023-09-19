from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("585x550")
# app.resizable(0,0)

set_appearance_mode("dark")

CTkProgressBar(master=app, progress_color="#2A55B8").pack(fill="x", anchor="n", pady=(46, 0), padx=50)

CTkLabel(master=app, text="Q4: Example Question", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(33, 0), padx=(50,0))

q1_frame = CTkFrame(master=app, corner_radius=8, fg_color="#2A55B8")
q1_frame.pack(fill="x", anchor="w", pady=(39, 0), padx=50)

CTkCheckBox(master=q1_frame, fg_color="#A6C1FF", checkmark_color="#2A55B8", border_color="#fff", hover_color="#A6C1FF", text="Answer 1").pack(side="left", padx=(16,20), pady=(8,8))

q2_frame = CTkFrame(master=app, corner_radius=8, fg_color="#fff")
q2_frame.pack(fill="x", anchor="w", pady=(20, 0), padx=50)

CTkCheckBox(master=q2_frame, text_color="#2A55B8", fg_color="#2A55B8", checkmark_color="#fff",hover_color="#2A55B8", text="Answer 2").pack(side="left", padx=(16,20), pady=(8,8))

q3_frame = CTkFrame(master=app, corner_radius=8, fg_color="#fff")
q3_frame.pack(fill="x", anchor="w", pady=(20, 0), padx=50)

CTkCheckBox(master=q3_frame, text_color="#2A55B8", fg_color="#2A55B8", checkmark_color="#fff",hover_color="#2A55B8", text="Answer 3").pack(side="left", padx=(16,20), pady=(8,8))

q4_frame = CTkFrame(master=app, corner_radius=8, fg_color="#fff")
q4_frame.pack(fill="x", anchor="w", pady=(20, 0), padx=50)

CTkCheckBox(master=q4_frame, text_color="#2A55B8", fg_color="#2A55B8", checkmark_color="#fff",hover_color="#2A55B8", text="Answer 4").pack(side="left", padx=(16,20), pady=(8,8))

CTkButton(master=app, text="Next Question", font=("Arial Bold", 20), hover_color="#299039", fg_color="#35B248").pack(fill="x", ipady=15, pady=(50, 0), padx=50)

app.mainloop()