#include <Wire.h>
#include <MPU6050.h>

// Initialize MPU6050
MPU6050 mpu;

// Define calibration constants
float ax_zero, ay_zero, az_zero;
float gx_zero, gy_zero, gz_zero;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  
  // Initialize MPU6050
  mpu.initialize();
  mpu.setFullScaleAccelRange(0); // 0 = ±2g, 1 = ±4g, 2 = ±8g, 3 = ±16g
  mpu.setFullScaleGyroRange(0); // 0 = ±250 °/s, 1 = ±500 °/s, 2 = ±1000 °/s, 3 = ±2000 °/s
  
  // Calibrate MPU6050
  calibrateMPU6050();
}

void loop() {
  // Do nothing
}

void calibrateMPU6050() {
  // Define variables for summing sensor data
  float ax_sum = 0, ay_sum = 0, az_sum = 0;
  float gx_sum = 0, gy_sum = 0, gz_sum = 0;
  
  // Define number of samples
  const int num_samples = 1000;
  
  // Collect sensor data for calibration
  for (int i = 0; i < num_samples; i++) {
    int16_t ax_raw, ay_raw, az_raw;
    int16_t gx_raw, gy_raw, gz_raw;
    mpu.getAcceleration(&ax_raw, &ay_raw, &az_raw);
    mpu.getRotation(&gx_raw, &gy_raw, &gz_raw);
    
    ax_sum += (float)ax_raw / 16384.0;
    ay_sum += (float)ay_raw / 16384.0;
    az_sum += (float)az_raw / 16384.0;
    gx_sum += (float)gx_raw / 131.0;
    gy_sum += (float)gy_raw / 131.0;
    gz_sum += (float)gz_raw / 131.0;
    
    // Wait for a short time
    delay(1);
  }
  
  // Compute calibration constants
  ax_zero = ax_sum / num_samples;
  ay_zero = ay_sum / num_samples;
  az_zero = az_sum / num_samples;
  gx_zero = gx_sum / num_samples;
  gy_zero = gy_sum / num_samples;
  gz_zero = gz_sum / num_samples;
  
  // Print calibration constants
  Serial.print("ax_zero = ");
  Serial.println(ax_zero);
  Serial.print("ay_zero = ");
  Serial.println(ay_zero);
  Serial.print("az_zero = ");
  Serial.println(az_zero);
  Serial.print("gx_zero = ");
  Serial.println(gx_zero);
  Serial.print("gy_zero = ");
  Serial.println(gy_zero);
  Serial.print("gz_zero = ");
  Serial.println(gz_zero);
}
