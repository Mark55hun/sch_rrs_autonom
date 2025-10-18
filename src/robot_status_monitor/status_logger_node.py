import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json


class StatusLogger(Node):
    def __init__(self):
        super().__init__('status_logger')
        self.subscription = self.create_subscription(
            String,
            'robot_status',
            self.status_callback,
            10)
        self.get_logger().info('Status Logger Started.')

    def status_callback(self, msg):
        try:
            status = json.loads(msg.data)
        except (ValueError, TypeError, json.JSONDecodeError):
            self.get_logger().error('Received invalid JSON on "robot_status" topic')
            return

        battery = status.get("battery")
        task = status.get("task")
        location = status.get("location")

        self.get_logger().info(
            f"Status: Battery={battery}%, Task={task}, Location={location}"
        )

        if isinstance(battery, (int, float)) and battery < 20:
            self.get_logger().warning("Battery low!")
        if task == "Charging" and isinstance(battery, (int, float)) and battery > 90:
            self.get_logger().warning("Charging inefficiently (battery > 90%)!")


def main(args=None):
    rclpy.init(args=args)
    node = StatusLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
