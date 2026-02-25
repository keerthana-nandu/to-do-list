function completeTask(taskId) {
    fetch(`/complete/${taskId}`, {
        method: 'POST'
    }).then(() => {
        location.reload();
    });
}

function deleteTask(taskId) {
    fetch(`/delete/${taskId}`, {
        method: 'POST'
    }).then(() => {
        location.reload();
    });
}
