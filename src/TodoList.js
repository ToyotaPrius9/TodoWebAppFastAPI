import React, { useState, useEffect } from 'react';
import TodoItem from './TodoItem';

function TodoList() {
    const [tasks, setTasks] = useState([]);
    const [text, setText] = useState('');

    // Fetch tasks from backend on component mount
    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/tasks');
            if (!response.ok) {
                throw new Error(`Error fetching tasks: ${response.statusText}`);
            }
            const data = await response.json();
            setTasks(data);
        } catch (error) {
            console.error('Error fetching tasks:', error);
        }
    };

    const addTask = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });
            if (!response.ok) {
                throw new Error(`Error adding task: ${response.statusText}`);
            }
            setText('');
            fetchTasks(); // Fetch updated tasks after adding
        } catch (error) {
            console.error('Error adding task:', error);
        }
    };

    const deleteTask = async (taskId) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/tasks/${taskId}`, {
                method: 'DELETE',
            });
            if (!response.ok) {
                throw new Error(`Error deleting task: ${response.statusText}`);
            }
            fetchTasks(); // Fetch updated tasks after deletion
        } catch (error) {
            console.error('Error deleting task:', error);
        }
    };

    const toggleCompleted = async (taskId, completed) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/tasks/${taskId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ completed: !completed }),
            });
            if (!response.ok) {
                throw new Error(`Error updating task: ${response.statusText}`);
            }
            fetchTasks(); // Fetch updated tasks after completion status toggle
        } catch (error) {
            console.error('Error updating task:', error);
        }
    };

    return (
        <div className="todo-list-container">
            {/* Add task prompt */}
            <div className="add-prompt">
                <input
                    value={text}
                    onChange={e => setText(e.target.value)}
                />
                <button onClick={addTask}>Add</button>
            </div>

            {/* Render tasks */}
            <div className="todo-list">
                {tasks.map(task => (
                    <TodoItem
                        key={task.id}
                        task={task}
                        deleteTask={deleteTask}
                        toggleCompleted={toggleCompleted}
                    />
                ))}
            </div>
        </div>
    );
}

export default TodoList;
