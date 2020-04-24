package main

import (
	"street-show/app/go_code/dbcrud"

	"github.com/gin-gonic/gin"
)

func init() {
	dbcrud.Open("../go_code/database-cfg.yaml")
}

func main() {
	r := gin.Default()
	r.GET("/api/all")
	r.Run()
}
