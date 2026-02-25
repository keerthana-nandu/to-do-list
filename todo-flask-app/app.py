from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')  # Update if using cloud MongoDB
db = client.todo_db
tasks = db.tasks

@app.route('/')
def index():
    active_tasks = list(tasks.find({"status": "active"}))
    completed_tasks = list(tasks.find({"status": "completed"}))
    return render_template('index.html', tasks=active_tasks, completed=completed_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['content']
    if task_content:
        tasks.insert_one({"content": task_content, "status": "active"})
    return redirect('/')

@app.route('/complete/<task_id>', methods=['POST'])
def complete_task(task_id):
    tasks.update_one({"_id": ObjectId(task_id)}, {"$set": {"status": "completed"}})
    return jsonify({"success": True})

@app.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    tasks.delete_one({"_id": ObjectId(task_id)})
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)
