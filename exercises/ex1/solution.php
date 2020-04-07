<?php

function solution($A)
{
    $arraySize = count($A);
    if ($arraySize < 2) {
        return 0;
    } else {
        $A[0] = $A[0] + $A[1];
        unset($A[1]);
        $A = array_values($A);
        sort($A);
        return $A[0] + solution($A);
    }
}
