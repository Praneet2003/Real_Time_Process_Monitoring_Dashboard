import tkinter as tk
from tkinter import ttk
def create_labels(root):
    cpu_label = tk.Label(
        root,
        text="CPU Usage: 0.00%",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#0F2027",
        padx=10,
        pady=5
    )
    cpu_label.pack(anchor="w", padx=20, pady=5)
    memory_label = tk.Label(
        root,
        text="Memory Usage: 0.00%",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#0F2027",
        padx=10,
        pady=5
    )
    memory_label.pack(anchor="w", padx=20, pady=5)
    return cpu_label, memory_label


def create_process_table(root):
    process_tree = ttk.Treeview(
        root,
        columns=("PID", "Name", "Status", "CPU (%)"),
        show="headings",
        height=15
    )

    table_style = ttk.Style()
    table_style.theme_use("clam")
    table_style.configure(
        "Treeview.Heading",
        font=("Arial", 12, "bold"),
        background="#1ABC9C",
        foreground="white",
        padding=5
    )
    table_style.configure(
        "Treeview",
        font=("Arial", 10),
        background="#2C3E50",
        foreground="white",
        rowheight=30,
        fieldbackground="#2C3E50"
    )
    table_style.map(
        "Treeview",
        background=[("selected", "#3498DB")]
    )
    for column in ("PID", "Name", "Status", "CPU (%)"):
        process_tree.heading(column, text=column)
        process_tree.column(column, width=150, anchor="center")
    process_tree.pack(expand=True, fill="both", padx=20, pady=5)
    return process_tree


def create_buttons(root, start_monitoring, stop_monitoring, export_data):
    button_frame = tk.Frame(root, bg="#0F2027")
    button_frame.pack(pady=15)
    button_style = {
        "font": ("Arial", 11, "bold"),
        "bg": "#3498DB",
        "fg": "white",
        "activebackground": "#2980B9",
        "width": 18,
        "relief": "raised",
        "borderwidth": 2
    }
    start_button = tk.Button(
        button_frame,
        text="Start Monitoring",
        command=start_monitoring,
        **button_style
    )
    start_button.grid(row=0, column=0, padx=8)
    stop_button = tk.Button(
        button_frame,
        text="Stop Monitoring",
        command=stop_monitoring,
        state=tk.DISABLED,
        **button_style
    )
    stop_button.grid(row=0, column=1, padx=8)
    export_button = tk.Button(
        button_frame,
        text="Export Data",
        command=export_data,
        state=tk.DISABLED,
        **button_style
    )
    export_button.grid(row=0, column=2, padx=8)
    return start_button, stop_button, export_button