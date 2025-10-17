import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class StatusLogger(Node):
    def init(self):
        super().init('status_logger')
        self.subscription = self.create_subscription(
            String,
            'robot_status',
            self.status_callback,
            10)
        self.get_logger().info('Status Logger Started.')

    def status_callback(self, msg):
        status = json.loads(msg.data)
        battery = status["battery"]
        task = status["task"]
        location = status["location"]

        self.get_logger().info(
            f"Status: Battery={battery}%, Task={task}, Location={location}"
        )

        if battery < 20:
            self.get_logger().warn("Battery low!")
        if task == "Charging" and battery > 90:
            self.get_logger().warn("Charging inefficiently (battery > 90%)!")

def main(args=None):
    rclpy.init(args=args)
    node = StatusLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()