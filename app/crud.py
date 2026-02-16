from app.database import conn
from app.models import Task


def create_task(task: Task):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, completed, due_date) VALUES (%s, %s, %s, %s) RETURNING id;",
        (task.title, task.description, task.completed, task.due_date),
    )
    task_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return task_id


def get_tasks():
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, description, completed, due_date, created_at FROM tasks;"
    )
    tasks = cursor.fetchall()
    cursor.close()
    return tasks


def update_task(task_id: int, task: Task):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title=%s, description=%s, completed=%s, due_date=%s WHERE id=%s;",
        (task.title, task.description, task.completed, task.due_date, task_id),
    )
    conn.commit()
    cursor.close()


def delete_task(task_id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s;", (task_id,))
    conn.commit()
    cursor.close()
