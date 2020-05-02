package main

import (
	"log"
	"net/http"
	"rocket-radio/app/go_code/dbcrud"

	"github.com/gin-gonic/gin"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

func init() {
	dbcrud.Open("../../configs/database-cfg.yaml")
}

func main() {
	r := gin.Default()
	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "../templates/index.html", "")
	})
	r.GET("/api/all", func(c *gin.Context) {
		scanTo := &dbcrud.SensorData{}
		err := scanTo.SelectAll()
		if err != nil {
			log.Fatalf("SelectAll err: %s\n", err)
			c.Status(404)
		}
		c.JSON(200, scanTo)
	})
	r.Run()
}
