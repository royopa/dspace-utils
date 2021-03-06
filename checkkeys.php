<?php
if ($argc != 3) {
    echo "Usage: checkkeys.php <master> <tocheck>\n";
    exit(1);
}
 
$masterKeys  = getKeys($argv[1]);
$toCheckKeys = getKeys($argv[2]);
 
print "IN $argv[1] BUT NOT IN $argv[2]:\n\n";
printMissing($masterKeys, $toCheckKeys);
 
print "\n\n\nIN $argv[2] BUT NOT IN $argv[1]:\n\n";
printMissing($toCheckKeys, $masterKeys);
 
function printMissing($reference, $test)
{
    foreach ($test as $value) {
        if (! in_array($value, $reference)) {
            echo "$value \n";
        }
    }
}
 
function readFileMessage($path)
{
    if (! $fileContent = @file($path)) {
        echo "Can't open $path \n";
        exit(1);
    }
 
    return $fileContent;
}
 
function getKeys($path)
{
    $fileContent = readFileMessage($path);
 
    return readKeys($fileContent);
}
 
function readKeys($file)
{
    $keys = [];
 
    foreach ($file as $key => $line) {
        if (strpos($line, '<message key="') === false) {
            continue;
        }
 
        $key = getKey($line);
 
        $keys[] = $key;
    }
 
    return $keys;
}
 
function getKey($line)
{
    $line = trim($line);
 
    $line = substr($line, 14);
 
    $charEnd = strpos($line, '">');
 
    $key = substr($line, 0, $charEnd - strlen($line));
 
    return $key;
}
