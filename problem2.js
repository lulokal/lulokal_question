//e.g node problem2.js --up 5 --down 3 --left 3 --right 2
const args = require('minimist')(process.argv.slice(2));

class Robot {
  constructor(x, y) {
    this.x = x; this.y = y;
  }

  up(givenStep) {
    this.y += givenStep;
  }

  down(givenStep) {
    this.y -= givenStep;
  }

  left(givenStep) {
    this.x -= givenStep
  }

  right(givenStep) {
    this.x += givenStep
  }

  computeDistance() {
    const x = this.x - 0;
    const y = this.y - 0;

    return Math.round(Math.sqrt(x * x + y * y));
  }
}

const robot = new Robot(0,0);
robot.up(args.up);
robot.down(args.down);
robot.left(args.left);
robot.right(args.right);

console.log(robot.computeDistance());