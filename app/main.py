from todo import add_task, remove_task, list_tasks

add_task("Learn GitHub Actions")
add_task("Write test cases")

print("Tasks:", list_tasks())

remove_task(0)
print("Updated Tasks:", list_tasks())
