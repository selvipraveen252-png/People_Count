import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import people_count
import sys

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("People Tracking System")
root.geometry("560x420")
root.configure(bg="#0f172a")
root.resizable(False, False)

# ---------------- TITLE ----------------
tk.Label(
    root,
    text="People Tracking System",
    font=("Segoe UI", 22, "bold"),
    bg="#0f172a",
    fg="white"
).pack(pady=(25, 5))

tk.Label(
    root,
    text="YOLOv8 • Desktop Application",
    font=("Segoe UI", 10),
    bg="#0f172a",
    fg="#94a3b8"
).pack(pady=(0, 20))

# ---------------- STATUS ----------------
status = tk.StringVar(value="Idle")

tk.Label(
    root,
    textvariable=status,
    bg="#020617",
    fg="#38bdf8",
    font=("Segoe UI", 10),
    height=2
).pack(fill="x", padx=20, pady=10)

# ---------------- FUNCTIONS ----------------
def start_webcam():
    status.set("Webcam running...")
    threading.Thread(
        target=people_count.run,
        args=(0,),
        daemon=True
    ).start()

def choose_video():
    path = filedialog.askopenfilename(
        filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
    )
    if path:
        status.set("Processing video...")
        threading.Thread(
            target=people_count.run,
            args=(path,),
            daemon=True
        ).start()

def stop_processing():
    people_count.stop()
    status.set("Stopped")

def exit_app():
    people_count.stop()
    root.destroy()
    sys.exit()

# ---------------- BUTTON STYLE ----------------
def styled_button(text, command, color):
    return tk.Button(
        root,
        text=text,
        command=command,
        bg=color,
        fg="white",
        font=("Segoe UI", 12, "bold"),
        width=22,
        bd=0,
        cursor="hand2",
        activebackground="#1e40af"
    )

# ---------------- BUTTONS ----------------
styled_button("▶ Start Webcam", start_webcam, "#2563eb").pack(pady=8)
styled_button("▶ Choose Video", choose_video, "#16a34a").pack(pady=8)
styled_button("⛔ Stop Processing", stop_processing, "#dc2626").pack(pady=8)
styled_button("❌ Exit", exit_app, "#475569").pack(pady=12)

# ---------------- FOOTER ----------------
tk.Label(
    root,
    text="ESC also stops • Clean Exit Enabled",
    bg="#0f172a",
    fg="#64748b",
    font=("Segoe UI", 9)
).pack(side="bottom", pady=10)

root.mainloop()
