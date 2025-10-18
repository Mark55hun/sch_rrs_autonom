from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'robot_status_monitor'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='todo',
    maintainer_email='todo@todo.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'status_broadcaster_node = robot_status_monitor.status_broadcaster_node:main',
            'status_logger_node = robot_status_monitor.status_logger_node:main',
        ],
    },
)
