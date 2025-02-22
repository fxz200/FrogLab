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
func Update (tasks *[]Task, task_name string){
	j:=0
	for _,task := range *tasks {
		if task.Name == task_name {
			switch(task.Status){
			case "todo":
				task.Status = "ongoing"
			case "ongoing":
				task.Status = "done"
			case "done":
				fmt.Println("Task is already done!")
				return
			}
			task.UpdateTime = time.Now().Format("2006-01-02 15:04:05")
			(*tasks)[j] = task
			SaveTasks((*tasks))
			fmt.Println("Task Edit Success!")
			return
		}
		j++
	}
	fmt.Println("Wrong Task Name!")
}
func Delete (tasks *[]Task, task_name string){ 
	j := 0
	found := false
	for _,task := range *tasks {
		if task.Name != task_name {
			(*tasks)[j] = task
			j++
		}else{
			found = true
		}
	}
	if found {
        fmt.Println("Task Delete Success! Task Name: ", task_name)
        SaveTasks((*tasks)[:j])
    } else {
        fmt.Println("Task Delete Failed! Task Name not found")
    }
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
	case "update":
		if len(os.Args)<3 {
			fmt.Println("task name is required!")
			os.Exit(1)
		}
		task_name := os.Args[2]
		Update(&tasks,task_name)
    default:
        fmt.Println("unknown command")
        os.Exit(1)
    }
}