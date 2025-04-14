document.getElementById('addTask').addEventListener('click', function() {
    const taskRow = document.createElement('div');
    taskRow.classList.add('row', 'mb-3', 'task');

    taskRow.innerHTML = `
        <div class="col-md-3">
            <input type="text" name="name" class="form-control" placeholder="Task Name" required>
        </div>
        <div class="col-md-2">
            <input type="number" name="arrival_time" class="form-control" placeholder="Arrival Time" required>
        </div>
        <div class="col-md-2">
            <input type="number" name="burst_time" class="form-control" placeholder="Burst Time" required>
        </div>
        <div class="col-md-2">
            <input type="number" name="priority" class="form-control" placeholder="Priority" required>
        </div>
        <div class="col-md-2 d-flex align-items-center">
            <button type="button" class="btn btn-danger remove-task">Remove</button>
        </div>
    `;

    // Append the new task row
    document.getElementById('tasks').appendChild(taskRow);

    // Add event listener to the remove button of the new task
    taskRow.querySelector('.remove-task').addEventListener('click', function() {
        taskRow.remove();
    });
});
