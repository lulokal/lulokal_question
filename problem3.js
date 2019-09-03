const args = require('minimist')(process.argv.slice(2));

const arr = args.tuples.split('-');
const newArr = [];
arr.forEach(element => {
  newArr.push(element.split(','));
});

console.log(newArr.sort());