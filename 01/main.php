<?php

$content = file_get_contents('input.txt');
$content = explode("\n", $content);

$elves = [
	0 => 0,
];
$elf_no = 0;

foreach ($content as $line)
{
	if (trim($line) === '') {
		$elf_no++;
		$elves[$elf_no] = 0;
		continue;
	}

	$elves[$elf_no] += $line;
}

sort($elves);

echo 'Highest single calorie value: ' . max($elves) . "\n";

$top_3_total = 0;

for ($i = 0; $i < 3; $i++)
{
	$top_3_total += array_pop($elves);
}

echo 'Top 3 total: ' . $top_3_total . "\n";
