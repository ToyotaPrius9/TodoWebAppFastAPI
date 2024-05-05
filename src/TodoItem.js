import React from 'react';

function TodoItem({ task, deleteTask, toggleCompleted }) {
    function handleChange() {
        toggleCompleted(task.id);
    }

    function handleDelete() {
        deleteTask(task.id);
    }

    return (
        <div className="todo-item">
            <input
                type="checkbox"
                checked={task.completed}
                onChange={handleChange}
            />
            <p>{task.text}</p>
            <button onClick={handleDelete}>X</button>
        </div>
    );
}

export default TodoItem;
