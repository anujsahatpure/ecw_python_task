from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory task list
tasks = []

# Home route - Loads UI
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

#Get all tasks (API)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

#Add a new task (API)
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    if not data or "task" not in data or not data["task"].strip():
        return jsonify({"error": "Task cannot be empty"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "task": data["task"].strip(),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

#Mark task as done (API)
@app.route('/tasks/<int:task_id>/done', methods=['PUT'])
def mark_task_done(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found or already done"}), 404

    task["done"] = True
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found or already exists"}), 404

    task.update(request.json)
    return jsonify(task)


# Delete task (API)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task_to_delete = next((t for t in tasks if t["id"] == task_id), None)
    if not task_to_delete:
        return jsonify({"error": "Task not found"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

#Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
