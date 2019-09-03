// e.g node problem1.js without,hello,bag,world
const expl = (params) => {
  return params.split(',');
}
console.log(expl(process.argv[2]).sort().join(','));