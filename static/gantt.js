function drawGanttChart(tasks) {
    const container = document.getElementById("gantt-chart");
    container.innerHTML = "";

    tasks.forEach(task => {
        const block = document.createElement("div");
        block.className = "gantt-block";
        block.style.width = (task.completion_time - task.start_time) * 30 + "px"; // 30px per unit time
        block.innerHTML = `
            <div class="gantt-task">${task.name}</div>
            <div class="gantt-time">${task.start_time} - ${task.completion_time}</div>
        `;
        container.appendChild(block);
    });
}
