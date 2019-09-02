<?php

$moves = [
  'UP    5',
  'DOWN  3',
  'LEFT  3',
  'RIGHT 2'
];

$start    = [0, 0];
$current  = [0, 0];
$distance = 0;

echo 'Moves:<br>';
foreach ($moves as $m) {
    move ($m);
    echo $m, '<br>';
}
echo '<br>Distance: ', round ($distance);

function move ($m) {
    global $current,
           $start,
           $distance;
    switch (strtok ($m, ' ')) {
        case 'UP':
            $current[1] += strtok (' ');
            break;
        case 'DOWN':
            $current[1] -= strtok (' ');
            break;
        case 'LEFT':
            $current[0] += strtok (' ');
            break;
        case 'RIGHT':
            $current[0] -= strtok (' ');
            break;
    }
    $distance = sqrt (($current[0]-$start[0])**2 +
                      ($current[1]-$start[1])**2);
}

?>
