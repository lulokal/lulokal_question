const mytuples = [
  ('John', '20', '90'),
  ('Json', '21', '85'),
  ('Jony', '17', '93'),
  ('Tom', '19', '80'),
  ('Jony', '17', '91')
];

function compare(a, b) {
  const genreA = a.genre.toUpperCase();
  const genreB = b.genre.toUpperCase();

  let comparison = 0;
  if (genreA > genreB) {
    comparison = 1;
  } else if (genreA < genreB) {
    comparison = -1;
  }
  return comparison;
}

console.log(mytuples.sort(compare));
