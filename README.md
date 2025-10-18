# `robot_status_monitor` package
A package 2 nodeból áll. A `status_broadcaster_node` töltöttségi szintet, feladatot (Idle, Patrolling, Charging) és helyzet ID-t (1-től 5-ig) szimulál egy feltételezett robotnak. A `status_logger_node` ezeket az adatokat olvassa és figyelmeztetést küld akkor amikor a töltöttségi szint 20% alatt van, vagy akkor amikor a robot tölt (a feladat Charging) és a töltöttsége 90% felett van. Ezeket a nodeokat egy `launch_example1.launch.py` nevű launch fájl indítja el.

## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/Mark55hun/sch_rrs_autonom
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select robot_status_monitor
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch robot_status_monitor launch_example1.launch.py
```

