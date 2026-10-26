# SmartAttend – Multimodal Attendance and Engagement Agent

SmartAttend is a student attendance management project built using HTML, CSS, JavaScript, and Python. It provides a dashboard to manage student records and view attendance information.

## Features

* 📊 Dashboard with attendance statistics
* 👨‍🎓 Add and view student records
* 📋 View attendance records
* 🔍 Filter attendance by Present or Absent
* 🔄 Reset demo data
* 📥 Download attendance reports in CSV format
* 🎨 Responsive dashboard interface
* 🧪 Demo mode with sample student data

## Technologies Used

* HTML5
* CSS3
* JavaScript
* Python
* Flask
* Flask-CORS

## Project Structure

```text
MultimodalAttendanceAgent/
│
├── Backend/
│   ├── core/
│   ├── app.py
│   ├── student_registration.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── data/
├── .gitignore
└── README.md
```

## How to Run the Project

### 1. Open the Project

Open the `MultimodalAttendanceAgent` folder in Visual Studio Code.

### 2. Run the Frontend

Open `frontend/index.html` in your browser using the VS Code Live Server extension.

### 3. Run the Python Backend (Optional)

Open the VS Code terminal in the project folder.

Activate the virtual environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r Backend/requirements.txt
```

Start the Flask backend:

```bash
python Backend/app.py
```

If the backend starts successfully, open `http://127.0.0.1:5000/` in your browser to check its status.

## Demo Mode

The current frontend uses sample demo data for demonstration purposes.

* Students added through the demo interface are stored in browser memory.
* Refreshing the page may reset changes.
* Attendance records shown in the dashboard are demo records.
* The frontend is not currently connected to live webcam-based face recognition.

## Future Improvements

* Connect the frontend to the Python backend.
* Integrate face recognition for attendance.
* Store student and attendance records persistently.
* Generate detailed attendance reports.
* Add student engagement analysis.

## Project Status

The frontend dashboard and demo features are implemented. Backend integration and live face recognition are future improvements.

---

**Note:** This project is intended for learning, development, and demonstration purposes.
