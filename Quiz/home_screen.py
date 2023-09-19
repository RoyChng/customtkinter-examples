from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("585x550")
app.resizable(0,0)

set_appearance_mode("dark")

CTkLabel(master=app, text="Your Stats", font=("Arial Bold", 20), justify="left").pack(anchor="w", pady=(43, 18), padx=(56,0))

stats_frame = CTkFrame(master=app, fg_color="transparent")
stats_frame.pack( padx=(54, 0), pady=(18, 0), anchor="nw")

quizzes_taken_frame = CTkFrame(master=stats_frame, fg_color="#70179A", width=132, height=70, corner_radius=8)
quizzes_taken_frame.pack_propagate(0)
quizzes_taken_frame.pack(anchor="w", side="left", padx=(0, 20))

CTkLabel(master=quizzes_taken_frame, text="Quizzes Taken", font=("Arial Bold", 10), text_color="#F3D9FF").pack(anchor="nw", padx=(14,0))
CTkLabel(master=quizzes_taken_frame, text="71", justify="left",  font=("Arial Bold", 25), text_color="#F3D9FF").pack(anchor="nw", padx=(14, 0))

correct_qs_frame = CTkFrame(master=stats_frame, fg_color="#146C63", width=132, height=70, corner_radius=8)
correct_qs_frame.pack_propagate(0)
correct_qs_frame.pack(anchor="w", side="left", padx=(0, 20))

CTkLabel(master=correct_qs_frame, text="Correct Questions", font=("Arial Bold", 10), text_color="#D5FFFB").pack(anchor="nw", padx=(14,0))
CTkLabel(master=correct_qs_frame, text="23", justify="left",  font=("Arial Bold", 25), text_color="#D5FFFB").pack(anchor="nw", padx=(14, 0))

highest_score_frame = CTkFrame(master=stats_frame, fg_color="#9A1717", width=132, height=70, corner_radius=8)
highest_score_frame.pack_propagate(0)
highest_score_frame.pack(anchor="w", side="left", padx=(0, 20))

CTkLabel(master=highest_score_frame, text="Highest Score", font=("Arial Bold", 10), text_color="#FFCFCF").pack(anchor="nw", padx=(14,0))
CTkLabel(master=highest_score_frame, text="12", justify="left",  font=("Arial Bold", 25), text_color="#FFCFCF").pack(anchor="nw", padx=(14, 0))

CTkLabel(master=app, text="Take A Quiz", font=("Arial Bold", 20), justify="left").pack(anchor="nw", side="top",padx=(56,0), pady=(41, 0))

quizzes_frame = CTkFrame(master=app, fg_color="transparent")
quizzes_frame.pack(pady=(21, 0), padx=(50, 0), anchor="nw")

movies_img_data = Image.open("movies-quiz-bg.png")
movies_img = CTkImage(light_image=movies_img_data, dark_image=movies_img_data, size=(234,91))
CTkLabel(master=quizzes_frame, text="", image=movies_img,corner_radius=8).grid(row=0, column=0, sticky="nw")

sports_img_data = Image.open("sports-quiz-bg.png")
sports_img = CTkImage(light_image=sports_img_data, dark_image=sports_img_data, size=(234,91))
CTkLabel(master=quizzes_frame, text="", image=sports_img,corner_radius=8).grid(row=1, column=0, sticky="nw", pady=(30, 0))

geography_img_data = Image.open("geography-quiz-bg.png")
geography_img = CTkImage(light_image=geography_img_data, dark_image=geography_img_data, size=(175,210))
CTkLabel(master=quizzes_frame, text="", image=geography_img,corner_radius=8).grid(row=0, column=1, rowspan=2,  sticky="nw")

app.mainloop()