package main

import (
	"fmt"
	"os"
)
var tasks = LoadTasks()

func List (tasks []Task){ 
	fmt.Println("id | name | status | createTime | updateTime")
	for _,task := range tasks {
		fmt.Println(task.ID, task.Name, task.Status, task.CreateTime, task.UpdateTime)
	}
}
func Add (tasks *[]Task , task_name string){ 
	fmt.Println("Task Add Success! Task Name: ", task_name)
	*tasks = append(*tasks, Task{ID: len(*tasks)+1, Name: task_name, Status: "todo", CreateTime: "2021-09-01 12:00:00", UpdateTime: "2021-09-01 12:00:00"})
	SaveTasks(*tasks)
}

func main(){
    // 檢查是否有子命令
    if len(os.Args) < 2 {
        fmt.Println("subcommand is required")
        os.Exit(1)
    }

    // 解析子命令
    switch os.Args[1] {
    case "list":
		List(tasks)
	case "add":
		if len(os.Args)<3 {
			fmt.Println("task name is required!")
			os.Exit(1)
		}
		task_name := os.Args[2]
		Add(&tasks,task_name)
    default:
        fmt.Println("unknown command")
        os.Exit(1)
    }
}