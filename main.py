import tkinter as tk
import time

root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("500x350")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Start typing the given text below:", font=("Arial", 14), bg="#f0f0f0")
label.pack(pady=10)

sample_text = "The quick brown fox jumps over the lazy dog."
text_label = tk.Label(root, text=sample_text, font=("Arial", 12), wraplength=400, bg="#f0f0f0")
text_label.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)
entry.focus_set()

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

start_time = None

# Function to start the timer
def start_timer(event):
    global start_time
    if start_time is None:
        start_time = time.time()

# Function to stop the timer, calculate WPM & accuracy
def stop_timer(event):
    global start_time
    if start_time is not None:
        end_time = time.time()
        time_taken = (end_time - start_time) / 60
        word_count = len(sample_text.split())
        wpm = word_count / time_taken

        user_text = entry.get()
        correct_chars = sum(1 for a, b in zip(user_text, sample_text) if a == b)
        total_chars = len(sample_text)

        accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0

        result_label.config(text=f"Typing Speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%")

        # Reset for next test
        start_time = None

# Function to reset the test manually
def reset_test():
    global start_time
    start_time = None
    entry.delete(0, tk.END)
    result_label.config(text="")

entry.bind("<KeyPress>", start_timer)
entry.bind("<Return>", stop_timer)

reset_button = tk.Button(root, text="Reset Test", font=("Arial", 12), command=reset_test, bg="#ff6666", fg="white")
reset_button.pack(pady=10)

root.mainloop()
