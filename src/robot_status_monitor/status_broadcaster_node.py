import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import json


class StatusBroadcaster(Node):
    def __init__(self):
        super().__init__('status_broadcaster')
        self.publisher = self.create_publisher(String, 'robot_status', 10)
        self.timer = self.create_timer(2.0, self.publish_status)
        self.get_logger().info('Status Broadcaster Started.')

    def publish_status(self):
        status = {
            "battery": random.randint(10, 100),
            "task": random.choice(["Idle", "Patrolling", "Charging"]),
            "location": random.randint(1, 5)
        }
        msg = String()
        msg.data = json.dumps(status)
        self.publisher.publish(msg)
        self.get_logger().info(f"Published status: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = StatusBroadcaster()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
