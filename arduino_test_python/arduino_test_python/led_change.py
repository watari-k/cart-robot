import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import serial

class ArduinoTestPython(Node):
    def __init__(self):
        super().__init__("arduino_test_python")
        self.pub_ = self.create_publisher(Int32MultiArray, "/received_val", 10)
        self.sub_ = self.create_subscription(Int32MultiArray, "/send_val", self.val_callback, 10)
        self.serial_port = serial.Serial("/dev/ttyACM0", baudrate=9600)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def val_callback(self, msg):
        send_data = bytes(msg.data)
        self.serial_port.write(send_data)

    def timer_callback(self):
        if self.serial_port.in_waiting >= 8:
            received_data = Int32MultiArray()
            received_data.data = list(self.serial_port.read(8))
            self.pub_.publish(received_data)
            

def main():
    rclpy.init()
    node = ArduinoTestPython()
    rclpy.spin(node)
    node.destory_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
