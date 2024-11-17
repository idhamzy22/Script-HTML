import os
import turtle
import time
import pygame  # Tambahkan pustaka pygame untuk fitur audio

# Ubah direktori kerja ke lokasi file "heart.mp3"
os.chdir("/root/perkuliahan/Script-HTML/Cann/html4")  # Sesuaikan dengan lokasi file Anda

# Inisialisasi pygame untuk audio
pygame.mixer.init()
audio_file = "heart.mp3"  # Nama file audio

# Pastikan file audio tersedia
try:
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(-1)  # Ulangi lagu tanpa batas (-1)
except pygame.error as e:
    print(f"Gagal memutar lagu: {e}")

# Setup screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("pink")

# Create heart drawer
t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")

def draw_heart(x, y, size, color, thickness):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pensize(thickness)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(size)
    
    for _ in range(100):
        t.right(2)
        t.forward(size * 0.018)
    
    t.left(120)
    
    for _ in range(100):
        t.right(2)
        t.forward(size * 0.018)
    
    t.forward(size)
    t.end_fill()
    t.setheading(0)

# Draw multiple hearts
hearts = [
    (0, -150, 300, "#FF9999", 5),
    (0, -135, 270, "#FFCCCC", 5),
    (0, -120, 240, "#FFE6E6", 5),
    (0, -105, 210, "#FFCCCC", 5),
    (0, -90, 180, "#FF99CC", 5),
    (0, -75, 150, "#FFCCFF", 5),
    (0, -50, 100, "#FF6666", 5)
]

for heart in hearts:
    draw_heart(*heart)

# Create text drawer
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("white")
text_turtle.goto(0, 200)  # Initial position of the text

def animate_text():
    y_direction = 2  # Movement direction
    while True:
        for _ in range(30):  # Move up
            text_turtle.clear()
            text_turtle.goto(0, text_turtle.ycor() + y_direction)
            text_turtle.write("Candini", align="center", font=("Arial", 36, "bold"))
            screen.update()  # Refresh the screen
            time.sleep(0.05)
        y_direction *= -1  # Change direction

# Enable animation
screen.tracer(0)  # Turn off automatic screen updates
animate_text()

screen.mainloop()
