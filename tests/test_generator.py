from ensurepip import version
import os
import sys
import pytest
from pprint import pprint

# Add relevant ranger module to PATH... there surely is a better way to do this...
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pymycobot import MycobotCommandGenerater

mg: MycobotCommandGenerater


@pytest.fixture(scope="module")
def setup():
    global mg
    print("")
    DEBUG = False
    mg = MycobotCommandGenerater(debug=DEBUG)
    print("")


def test_generator(setup):
    print("")
    pprint(mg.send_coords([-160, 160, 160, 0, 0, 0], 7, 2))
    print("")
    pprint(mg.version())
    print("")
    pprint(mg.power_on())
    print("")
    pprint(mg.power_off())
    print("")
    pprint(mg.release_all_servos())
    print("")
    pprint(mg.is_controller_connected())
    print("")
    pprint(mg.get_angles())
    print("")
    pprint(mg.send_angle(1, 0, 10))
    print("")
    pprint(mg.send_angles([0, 0, 0, 0, 0, 0], 5))
    print("")
    pprint(mg.get_coords())
    print("")
    pprint(mg.send_coord(1, 110.5, 8))
    print("pause")
    pprint(mg.pause())
    print("is_paused")
    pprint(mg.is_paused())
    print("resume")
    pprint(mg.resume())
    print("stop")
    pprint(mg.stop())
    print("is_in_position")
    pprint(mg.is_in_position([0, 0, 0, 0, 0, 0], 0))
    print("")
    pprint(mg.is_moving())
    print("")
    pprint(mg.jog_angle(1, 0, 1))
    print("")
    pprint(mg.jog_coord(2, 1, 3))
    print("")
    pprint(mg.jog_stop())
    print("set_encoder")
    pprint(mg.set_encoder(1, 1024))
    print("get_encoder")
    pprint(mg.get_encoder(2))
    print("get_speed")
    pprint(mg.get_speed())
    print("set_speed")
    pprint(mg.set_speed(100))
    print("get_joint_min_angle")
    pprint(mg.get_joint_min_angle(1))
    print("get_joint_max_angle")
    pprint(mg.get_joint_max_angle(2))
    print("is_servo_enable")
    pprint(mg.is_servo_enable(6))
    print("is_all_servo_enable")
    pprint(mg.is_all_servo_enable())
    print("set_servo_data")
    pprint(mg.set_servo_data(0, 1, 2))
    print("get_servo_data")
    pprint(mg.get_servo_data(1, 2))
    print("set_servo_calibration")
    pprint(mg.set_servo_calibration(1))
    print("release_servo")
    pprint(mg.release_servo(1))
    print("focus_servo")
    pprint(mg.focus_servo(1))
    print("set_color")
    pprint(mg.set_color(255, 255, 0))
    print("set_pin_mode")
    pprint(mg.set_pin_mode(1, 0))
    print("set_digital_output")
    pprint(mg.set_digital_output(0, 1))
    pprint(mg)
