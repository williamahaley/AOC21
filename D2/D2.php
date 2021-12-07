<?php
// Your code here!
class Submarine{

    public $x = 0;
    public $y = 0;

    function follow_directions($file){
        $lines = file($file);
        foreach ($lines as $line){
           $parts = explode(' ', trim($line);
           print_r($parts)
        }
    }

    function move_it($direction, $n){
        switch($direction){
            case 'forward':
                $this->forward($n);
                break;
            case 'up':
                $this->up($n);
                break;
            case 'down':
                $this->down($n);
                break;
        }
    }

    function forward($n){
        $this->x = $this->x + $n;
    }

    function up($n){
        $this->x = $this->y - $n;
    }

    function down($n){
        $this->x = $this->x + $n;
    }

}


$sub = new Submarine();
$sub->follow_directions('/Users/whaley/Dev/')