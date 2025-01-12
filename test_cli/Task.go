package main

import (
	"encoding/json"
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
type Task struct {
	ID         int
	Name       string
	Status     string
	CreateTime string
	UpdateTime string
}


func SaveTasks(tasks []Task) {
	//err 變數會儲存任何可能發生的錯誤
    data, err := json.Marshal(tasks)
    if err != nil {
        fmt.Println("save error:", err)
        return
    }
	//0644是文件的權限設置
    err = os.WriteFile("tasks.json", data, 0644)
    if err != nil {
        fmt.Println("write error:", err)
    }
}
func LoadTasks() []Task {
    data, err := os.ReadFile("tasks.json")
    if err != nil {
        fmt.Println("read error:", err)

    }
    var tasks []Task
    err = json.Unmarshal(data, &tasks)
    if err != nil {
        fmt.Println("解析任務列表錯誤:", err)

    }
    return tasks
}