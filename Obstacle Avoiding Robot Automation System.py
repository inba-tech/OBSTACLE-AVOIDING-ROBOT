import random
import time

# --- INITIAL SETUP ---
robot_position = (0, 0)
robot_status = {
    "battery": 100,
    "mode": "manual",
    "task_count": 0
}
obstacles = [(3, 4), (7, 2), (5, 6), (2, 8)]
grid_limit = 9

print("\n🤖 Welcome to the Obstacle Avoiding Robot Automation System 🤖")
print("----------------------------------------------------")
print("Available Commands:")
print("move up/down/left/right | auto | status | charge | exit\n")


# --- FUNCTION DEFINITIONS ---

def move_robot(direction):
    """Move robot in the given direction if possible."""
    global robot_position, robot_status

    x, y = robot_position

    # Determine new position
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    else:
        print("❌ Invalid direction!")
        return

    # Check grid boundaries
    if not (0 <= x <= grid_limit and 0 <= y <= grid_limit):
        print("🚫 Robot cannot move outside the grid!")
        return

    # Check for obstacle
    if (x, y) in obstacles:
        print(f"⚠ Obstacle detected at {(x, y)} - movement blocked!")
        return

    # Move robot
    robot_position = (x, y)
    robot_status["battery"] -= 5
    robot_status["task_count"] += 1

    print(f"✅ Robot moved {direction}. New position: {robot_position}")

    # Low battery warning
    if robot_status["battery"] <= 20:
        print("⚠ Warning: Battery low! Please recharge soon.")


def auto_mode():
    """Automatically moves robot randomly until battery is low."""
    global robot_status
    robot_status["mode"] = "auto"
    print("\n🤖 Auto Mode Activated... Robot is exploring.\n")

    directions = ["up", "down", "left", "right"]

    while robot_status["battery"] > 20:
        move_robot(random.choice(directions))
        time.sleep(0.5)  # adjust speed for testing

    print("🔋 Battery low! Auto Mode stopped.")
    robot_status["mode"] = "manual"


def show_status():
    """Displays current robot status."""
    print("\n📊 --- ROBOT STATUS ---")
    print(f"Position     : {robot_position}")
    print(f"Battery      : {robot_status['battery']}%")
    print(f"Mode         : {robot_status['mode']}")
    print(f"Tasks Done   : {robot_status['task_count']}")
    print("---------------------------\n")


def charge_robot():
    """Recharge robot if at base (0,0)."""
    global robot_status
    if robot_position == (0, 0):
        robot_status["battery"] = 100
        robot_status["mode"] = "manual"
        print("⚡ Robot successfully charged to 100%!")
    else:
        print("❌ You must return to base (0,0) to charge!")


# --- MAIN PROGRAM LOOP ---
while True:
    command = input("Enter command: ").lower().strip()

    if command in ["up", "down", "left", "right"]:
        move_robot(command)

    elif command == "auto":
        auto_mode()

    elif command == "status":
        show_status()

    elif command == "charge":
        charge_robot()

    elif command == "exit":
        print("👋 Shutting down robot system. Goodbye!")
        break

    else:
        print("❌ Invalid command! Type 'status' to check robot or 'exit' to quit.")