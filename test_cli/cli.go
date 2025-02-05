package main

import (
	"fmt"
	"os"
	"time"
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
	*tasks = append(*tasks, Task{ID: len(*tasks)+1, Name: task_name, Status: "todo", CreateTime: time.Now().Format("2006-01-02 15:04:05"), UpdateTime: time.Now().Format("2006-01-02 15:04:05")})
	SaveTasks(*tasks)
}

func Delete (tasks *[]Task, task_name string){ 
	fmt.Println("Task Delete Success! Task Name: ", task_name)
	j := 0
	for _,task := range *tasks {
		if task.Name != task_name {
			(*tasks)[j] = task
			j++
		}
	}
	SaveTasks((*tasks)[:j])
}

func main(){
    if len(os.Args) < 2 {
        fmt.Println("subcommand is required")
        os.Exit(1)
    }

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
	case "delete":
		if len(os.Args)<3 {
			fmt.Println("task name is required!")
			os.Exit(1)
		}
		task_name := os.Args[2]
		Delete(&tasks,task_name)
    default:
        fmt.Println("unknown command")
        os.Exit(1)
    }
}