/* dbcrud handles all code that interacts with a database;
also holds the datastructures that the fetch api utilizes
*/
package dbcrud

import "github.com/jinzhu/gorm"

// DB is the instance of a gorm database
var DB *gorm.DB

// SensorData serves as the ORM abstraction for the SensorData sql table; it will also be used to marshal json
type SensorData struct {
	Time     float64 `gorm:"column:time" json:"time"`
	Altitude float64 `gorm:"column:altitude" json:altitude"`
	AccelX   float64 `gorm:"column:accelX" json:"accelX"`
	AccelY   float64 `gorm:"column:accelY" json:"accelY"`
	AccelZ   float64 `gorm:"column:accelZ" json:"accelZ"`
	GyroX    float64 `gorm:"column:gyroX" json:"gyroX"`
	GyroY    float64 `gorm:"column:gyroY" json:"gyroY"`
	GyroZ    float64 `gorm:"column:gyroZ" json:"gyroZ"`
}
