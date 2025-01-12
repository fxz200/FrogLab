package main

/**
task:{
	{
		id: 1,#unique
		name: "task1",
		status: "todo/done/inprogress",
		createTime: "2021-09-01 12:00:00",
		updateTime: "2021-09-01 12:00:00"
	}
}
**/
type Task struct {
	ID         int
	Name       string
	Status     string
	CreateTime string
	UpdateTime string
}

func TaskListInit() []Task {
	tasks := []Task{
		{1, "task1", "todo", "2021-09-01 12:00:00", "2021-09-01 12:00:00"},
		{2, "task2", "done", "2021-09-01 12:00:00", "2021-09-01 12:00:00"},
		{3, "task3", "inprogress", "2021-09-01 12:00:00", "2021-09-01 12:00:00"},
	}
	return tasks
}