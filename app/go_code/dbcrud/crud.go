/* dbcrud handles all code that interacts with a database;
also holds the datastructures that the fetch api utilizes
*/
package dbcrud

import (
	"fmt"
	"io/ioutil"
	"log"

	"github.com/jinzhu/gorm"
	"gopkg.in/yaml.v2"
)

// DB is the instance of a gorm database
var DB *gorm.DB

// SensorData serves as the ORM abstraction for the SensorData sql table; it will also be used to marshal json
type SensorData struct {
	Time     float64 `gorm:"column:time" json:"time"`
	Altitude float64 `gorm:"column:altitude" json:"altitude"`
	AccelX   float64 `gorm:"column:accelX" json:"accelX"`
	AccelY   float64 `gorm:"column:accelY" json:"accelY"`
	AccelZ   float64 `gorm:"column:accelZ" json:"accelZ"`
	GyroX    float64 `gorm:"column:gyroX" json:"gyroX"`
	GyroY    float64 `gorm:"column:gyroY" json:"gyroY"`
	GyroZ    float64 `gorm:"column:gyroZ" json:"gyroZ"`
}

// DBInfo contains fields which correspond to the YAML keys in the database config file
type DBInfo struct {
	Host     string `yaml:"host"`
	Username string `yaml:"username"`
}

// Open reads from the database config file (db_info.yaml), then accordingly establishes a localhost connection to the database
func Open(filename string) {
	infoStruct := &DBInfo{}
	file, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatalf("database info file error: %s\n", err)
	}
	err = yaml.Unmarshal(file, infoStruct)
	if err != nil {
		log.Fatalf("unmarshalling problem: %s\n", err)
	}
	DB, err = gorm.Open("mysql", fmt.Sprintf("%s@tcp(localhost:3306)/RocketRadio", infoStruct.Username))
	if err != nil {
		log.Fatalf("database opening error: %s\n", err)
	}
}

// SelectAll returns all SensorData rows in a table
func (sd *SensorData) SelectAll() error {
	if err := DB.Where("ORDER BY time").Find(&sd).Error; err != nil {
		return err
	}
	return nil
}
