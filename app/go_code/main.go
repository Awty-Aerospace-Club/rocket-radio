package main

import (
	"rocket-radio/app/go_code/dbcrud"

	"github.com/gin-gonic/gin"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

func init() {
	dbcrud.Open("../go_code/database-cfg.yaml")
}

func main() {
	r := gin.Default()
	r.GET("/api/all")
	r.Run()
}
