from flask import Flask, render_template, request
from collections import deque

app = Flask(__name__)

# FCFS function
def fcfs(tasks):
    tasks.sort(key=lambda x: x['arrival_time'])
    current_time = 0
    for task in tasks:
        if task['arrival_time'] > current_time:
            current_time = task['arrival_time']
        task['start_time'] = current_time
        current_time += task['burst_time']
        task['completion_time'] = current_time
        task['turnaround_time'] = task['completion_time'] - task['arrival_time']
        task['waiting_time'] = task['turnaround_time'] - task['burst_time']
    return tasks

# SJF function
def sjf(tasks):
    tasks.sort(key=lambda x: x['burst_time'])
    current_time = 0
    for task in tasks:
        if task['arrival_time'] > current_time:
            current_time = task['arrival_time']
        task['start_time'] = current_time
        current_time += task['burst_time']
        task['completion_time'] = current_time
        task['turnaround_time'] = task['completion_time'] - task['arrival_time']
        task['waiting_time'] = task['turnaround_time'] - task['burst_time']
    return tasks

# Priority Scheduling function
def priority_scheduling(tasks):
    tasks.sort(key=lambda x: x['priority'])
    current_time = 0
    for task in tasks:
        if task['arrival_time'] > current_time:
            current_time = task['arrival_time']
        task['start_time'] = current_time
        current_time += task['burst_time']
        task['completion_time'] = current_time
        task['turnaround_time'] = task['completion_time'] - task['arrival_time']
        task['waiting_time'] = task['turnaround_time'] - task['burst_time']
    return tasks

# Round Robin function with start time calculation
def round_robin(tasks, time_quantum):
    queue = deque(tasks)
    result = []
    current_time = 0

    while queue:
        task = queue.popleft()
        
        # If this is the first time the task is being processed, set start time
        if task['remaining_burst_time'] == task['burst_time']:
            task['start_time'] = max(current_time, task['arrival_time'])
        
        if task['remaining_burst_time'] > time_quantum:
            task['remaining_burst_time'] -= time_quantum
            current_time += time_quantum
            queue.append(task)  # Task is added back to queue
        else:
            current_time += task['remaining_burst_time']
            task['completion_time'] = current_time
            task['turnaround_time'] = task['completion_time'] - task['arrival_time']
            task['waiting_time'] = task['turnaround_time'] - task['burst_time']
            task['remaining_burst_time'] = 0  # Task is done
            result.append(task)
    
    return result

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Schedule route
@app.route('/schedule', methods=['POST'])
def schedule():
    tasks = []
    # Fetch task data
    task_count = len(request.form.getlist('name'))
    for i in range(task_count):
        task = {
            'name': request.form.getlist('name')[i],
            'arrival_time': int(request.form.getlist('arrival_time')[i]),
            'burst_time': int(request.form.getlist('burst_time')[i]),
            'priority': int(request.form.getlist('priority')[i]),
            'remaining_burst_time': int(request.form.getlist('burst_time')[i]),  # Initialize remaining burst time
        }
        tasks.append(task)
    
    algorithm = request.form['algorithm']
    if algorithm == 'FCFS':
        result = fcfs(tasks)
    elif algorithm == 'SJF':
        result = sjf(tasks)
    elif algorithm == 'Priority':
        result = priority_scheduling(tasks)
    elif algorithm == 'RR':
        time_quantum = int(request.form['time_quantum'])
        result = round_robin(tasks, time_quantum)

    # Calculate ATAT and AWT
    total_tat = sum(task['turnaround_time'] for task in result)
    total_wt = sum(task['waiting_time'] for task in result)
    avg_tat = total_tat / len(result)
    avg_wt = total_wt / len(result)

    # Pass these values to the template
    return render_template('result.html', tasks=result, avg_tat=avg_tat, avg_wt=avg_wt)

if __name__ == '__main__':
    app.run(debug=True)