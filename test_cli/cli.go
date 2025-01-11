package main

import (
	"fmt"
	"os"
)

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
func List (tasks []string){ 
	fmt.Println("id | name | status | createTime | updateTime")
	for _,task := range tasks {
		fmt.Println(task)
	}
}

func main(){
	// tasks init
	tasks := []string{"task1", "task2", "task3"}
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