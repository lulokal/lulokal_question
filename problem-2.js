//email: philipbryan1412@gmail.com

class Robot {
  constructor(x, y) {
    this.x = x
    this.y = y
  }

  walk_up(steps) {
    this.x += steps
  }

  walk_down(steps) {
    this.x -= steps
  }

  walk_right(steps) {
   this.y += steps
  }

  walk_left(steps) {
   this.y -= steps
  }

  get_distance() {
    return this.calculate_distance()
  }

  calculate_distance() {
    return Math.abs(this.x) + Math.abs(this.y)
  }
}

const robot = new Robot(0, 0)

robot.walk_up(5)
robot.walk_down(3)
robot.walk_left(3)
robot.walk_right(2)

console.log(robot.get_distance())
