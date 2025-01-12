package main

import (
	"fmt"
	"os"
)

func List (tasks []Task){ 
	fmt.Println("id | name | status | createTime | updateTime")
	for _,task := range tasks {
		fmt.Println(task.ID, task.Name, task.Status, task.CreateTime, task.UpdateTime)
	}
}

func main(){
	// tasks init
	tasks := TaskListInit()
    // 定義子命令
    // 檢查是否有子命令
    if len(os.Args) < 2 {
        fmt.Println("預期有 'list' 子命令")
        os.Exit(1)
    }

    // 解析子命令
    switch os.Args[1] {
    case "list":
		List(tasks)
	case "add":
		fmt.Println("add")
    default:
        fmt.Println("未知的子命令")
        os.Exit(1)
    }
}