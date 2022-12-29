## --- Day 15: Beacon Exclusion Zone ---

You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable **sensors** that you imagine were originally built to locate lost Elves.


The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.


Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source **beacon**. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can **determine the position of a beacon precisely**; however, sensors can only lock on to the one beacon **closest to the sensor** as measured by the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry). (There is never a tie where two beacons are the same distance to a sensor.)


It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:



```
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
```

So, consider the sensor at `2,18`; the closest beacon to it is at `-2,15`. For the sensor at `9,16`, the closest beacon to it is at `10,16`.


Drawing sensors as `S` and beacons as `B`, the above arrangement of sensors and beacons looks like this:



```
               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
```

This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at `8,7`:


<pre><code>               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########<b>S</b>#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....<b>B</b>############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
</code></pre>

This sensor's closest beacon is at `2,10`, and so you know there are no beacons that close or closer (in any positions marked `#`).


None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress beacon is by working out where it **isn't**. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.


So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where `y=10`, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:


<pre><code>                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
<b>10 ..####B######################..</b>
11 .###S#############.###########.
</code></pre>

In this example, in the row where `y=10`, there are **`26`** positions where a beacon cannot be present.


Consult the report from the sensors you just deployed. **In the row where `y=2000000`, how many positions cannot contain a beacon?**


<details>
    <summary>Solution</summary>

This is a tricky problem. My first approach was to save all the impossible points and finally check for the asked row, but the program ran out of memory.

In my second try, I realized that I didn't have to save all the points, only the points in the asked row.

First of all, I parse the input as a list of elements `sensor, beacon, distance`.

```python
def manhattan_distance(p1: (int, int), p2: (int, int)) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_sensors(area: list) -> list:
    sensors = []
    for line in area:
        aux_dict = dict()
        nums = re.findall(r'-?\d+', line)
        aux_dict['sensor'] = int(nums[0]), int(nums[1])
        aux_dict['beacon'] = int(nums[2]), int(nums[3])
        aux_dict['distance'] = manhattan_distance(aux_dict['sensor'], aux_dict['beacon'])
        sensors.append(aux_dict)

    return sensors
```

Once I have already parsed the input, I loop through all the sensors checking if that sensor can modify the asked row.
If it is not the case, I skip the sensor. On the other hand, if it does modify the row, I update the impossible points in the row with these new ones.
Lastly, I remove the possible sensors or beacons in the row.


```python
sensors = parse_sensors(input_lines)
row = 2_000_000

impossible_points = set()
for sensor in sensors:
    sensor_point, beacon_point, distance = sensor.values()
    if (offset := abs(row - sensor_point[1])) <= distance:
        signal_range = range(sensor_point[0] - distance, sensor_point[0] + distance + 1)
        if offset == 0:
            impossible_points.update(signal_range)
        else:
            if sensor_point[1] + offset == row:
                impossible_points.update(signal_range[offset:-offset])
            elif sensor_point[1] - offset == row:
                impossible_points.update(signal_range[offset:-offset])

        try:
            if sensor_point[1] == row:
                impossible_points.remove(sensor_point[0])
            if beacon_point[1] == row:
                impossible_points.remove(beacon_point[0])
        except KeyError:
            pass

print(f'{len(impossible_points)=}')
```

The answer is: `4876693`.

</details>



## --- Part Two ---

Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have `x` and `y` coordinates each no lower than `0` and no larger than `4000000`.


To isolate the distress beacon's signal, you need to determine its **tuning frequency**, which can be found by multiplying its `x` coordinate by `4000000` and then adding its `y` coordinate.


In the example above, the search space is smaller: instead, the `x` and `y` coordinates can each be at most `20`. With this reduced search area, there is only a single position that could have a beacon: `x=14, y=11`. The tuning frequency for this distress beacon is **`56000011`**.


Find the only possible position for the distress beacon. **What is its tuning frequency?**

<details>
    <summary>Solution</summary>

My approach is to check the points of intersection between the lines which compose the diamonds of the figure that represent the Manhattan distance (I use the lines which are a unit apart from the diamond).
I only use integer solutions.

```python
sensors = parse_sensors(input_lines)
minimum, maximum = 0, 4_000_000
possible_points = []
for sensor in sensors:
    sensors_copy = deepcopy(sensors)
    sensors_copy.remove(sensor)
    for other in sensors_copy:
        lines1 = sensor['lines']
        lines2 = other['lines']
        for line1 in lines1.values():
            for line2 in lines2.values():
                if point := point_of_intersection(line1, line2):
                    possible_points.append(point)

possible_points = list(filter(lambda p: check_in_range(p, minimum, maximum), possible_points))
```

Lastly, I check the only point which is far enough from every sensor and I compute the tuning frequency.
```python
for point in possible_points:
    if check_distance(sensors, point):
        break

tuning_frequency = 4_000_000 * point[0] + point[1]
exec_time = (time_ns() - start) / 1_000_000
print(f'{point[0]=}, {point[1]=}, {tuning_frequency=}, {exec_time=}ms')
```

This solution seems to be quite slow, but because I use the points of intersection the execution time is low. My solution takes around 15ms.

The answer is: `11645454855041`.

</details>
