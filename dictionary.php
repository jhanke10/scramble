#!/usr/bin/php
<?php
//Checks if the word is in the Dictionary API
$url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/" . urlencode($argv[1]) . "?key=" . urlencode($argv[2]);
$xml = file_get_contents($url);
$xml = str_replace(' & ', 'amp', $xml);
$file = simplexml_load_string($xml);
//If it's not a word the Dictionary API will have suggestions
if ($file -> suggestion -> getName() == NULL)
	echo "True";
else
	echo "False";
?>