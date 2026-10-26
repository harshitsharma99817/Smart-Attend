const today = new Date().toLocaleDateString("en-IN");

document.getElementById("today").textContent = today;

// Fake demo data only — no backend connection
let students = [
    { roll_number: "D001", name: "Demo Student 1" },
    { roll_number: "D002", name: "Demo Student 2" },
    { roll_number: "D003", name: "Demo Student 3" },
    { roll_number: "D004", name: "Demo Student 4" }
];

let attendance = [
    {
        roll_number: "D001",
        name: "Demo Student 1",
        date: today,
        time: "09:05 AM",
        status: "Present"
    },
    {
        roll_number: "D002",
        name: "Demo Student 2",
        date: today,
        time: "09:12 AM",
        status: "Present"
    },
    {
        roll_number: "D003",
        name: "Demo Student 3",
        date: today,
        time: "09:20 AM",
        status: "Present"
    },
    {
        roll_number: "D004",
        name: "Demo Student 4",
        date: today,
        time: "09:25 AM",
        status: "Absent"
    },
];

function renderStudents() {
    const table = document.getElementById("studentTable");
    table.innerHTML = "";

    students.forEach(student => {
        const row = document.createElement("tr");

        const roll = document.createElement("td");
        roll.textContent = student.roll_number;

        const name = document.createElement("td");
        name.textContent = student.name;

        row.append(roll, name);
        table.appendChild(row);
    });

    document.getElementById("totalStudents").textContent =
        students.length;
        updateDashboard();
}

function updateDashboard() {
  document.getElementById("totalStudents").textContent = students.length;

  const presentCount = attendance.filter(
    record => record.date === today && record.status === "Present"
  ).length;

  const absentCount = attendance.filter(
    record => record.date === today && record.status === "Absent"
  ).length;

  const totalMarked = presentCount + absentCount;

  document.getElementById("presentToday").textContent = presentCount;
  document.getElementById("absentToday").textContent = absentCount;

  document.getElementById("attendanceRate").textContent =
    totalMarked === 0
      ? "0%"
      : Math.round((presentCount / totalMarked) * 100) + "%";
}

function renderAttendance() {
    const table = document.getElementById("attendanceTable");
    table.innerHTML = "";

    if (attendance.length === 0) {
        table.innerHTML =
            '<tr><td colspan="5">No demo attendance records.</td></tr>';
    }

    const filterValue = document.getElementById("attendanceFilter").value;

const filteredAttendance = attendance.filter(record =>
    filterValue === "All" || record.status === filterValue
);


filteredAttendance.slice().reverse().forEach(record => {
        const row = document.createElement("tr");

        [
            record.roll_number,
            record.name,
            record.date,
            record.time,
            record.status
        ].forEach(value => {
            const cell = document.createElement("td");
            cell.textContent = value;
            row.appendChild(cell);
        });

        table.appendChild(row);
    });

    const presentToday = attendance.filter(record =>
        record.date === today && record.status === "Present"
    ).length;

    document.getElementById("presentToday").textContent =
        presentToday;

    const rate = students.length
        ? Math.round(presentToday / students.length * 100)
        : 0;

    document.getElementById("attendanceRate").textContent =
        Math.min(rate, 100) + "%";
}

document.getElementById("studentForm").addEventListener("submit", event => {
    event.preventDefault();

    const name = document.getElementById("studentName").value.trim();
    const roll = document.getElementById("rollNumber").value.trim();
    const message = document.getElementById("studentMessage");

    if (!name || !roll) return;

    if (students.some(student => student.roll_number === roll)) {
        message.textContent = "This roll number already exists.";
        return;
    }

    students.push({
        roll_number: roll,
        name: name
    });
    attendance.push({
  roll_number: roll,
  name: name,
  date: today,
  time: new Date().toLocaleTimeString("en-IN", {
    hour: "2-digit",
    minute: "2-digit"
  }),
  status: "Absent"
});

renderStudents();
renderAttendance();

    message.textContent = "Demo student added successfully!";
    event.target.reset();

});

document.getElementById("refreshButton").addEventListener("click", () => {
    renderStudents();
    renderAttendance();

    document.getElementById("attendanceMessage").textContent =
        "Demo records refreshed successfully.";
});

renderStudents();
renderAttendance();
document.getElementById("attendanceFilter").addEventListener("change", renderAttendance);

document.getElementById("resetDemoButton").addEventListener("click", () => {
  students = [
    { roll_number: "D001", name: "Demo Student 1" },
    { roll_number: "D002", name: "Demo Student 2" },
    { roll_number: "D003", name: "Demo Student 3" },
    { roll_number: "D004", name: "Demo Student 4" }
  ];

  attendance = [
    { roll_number: "D001", name: "Demo Student 1", date: today, time: "09:05 AM", status: "Present" },
    { roll_number: "D002", name: "Demo Student 2", date: today, time: "09:12 AM", status: "Present" },
    { roll_number: "D003", name: "Demo Student 3", date: today, time: "09:20 AM", status: "Present" },
    { roll_number: "D004", name: "Demo Student 4", date: today, time: "09:25 AM", status: "Absent" }
  ];

  document.getElementById("attendanceFilter").value = "All";

  renderStudents();
  renderAttendance();

  document.getElementById("studentMessage").textContent = "Demo data reset successfully!";
  document.getElementById("attendanceMessage").textContent = "";
});

document.getElementById("downloadReportButton").addEventListener("click", () => {
  const headers = ["Roll Number", "Name", "Date", "Time", "Status"];

  const rows = attendance.map(record => [
    record.roll_number,
    record.name,
    record.date,
    record.time,
    record.status
  ]);

  const csv = [headers, ...rows]
    .map(row => row.map(value =>
      `"${String(value).replace(/"/g, '""')}"`
    ).join(","))
    .join("\n");

  const blob = new Blob(["\uFEFF" + csv], {
    type: "text/csv;charset=utf-8;"
  });

  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "demo_attendance_report.csv";
  link.click();
  URL.revokeObjectURL(link.href);
});