<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
$date_search = "q=date";
$sort_by = "o=-created";
$page = "page=1";
$url = "https://pypi.org/search/?{$date_search}&{$sort_by}&{$page}";

// Fetch HTML content from the URL
$html = file_get_contents($url);

// Create a DOMDocument object
$dom = new DOMDocument();
@$dom->loadHTML($html); // Suppress errors for malformed HTML

// Create a DOMXPath object
$xpath = new DOMXPath($dom);

// Find all links with class 'package-snippet'
$links = $xpath->query("//a[@class='package-snippet']");

// Output the href attribute of each link
$link_array = array();
foreach ($links as $link) {
    $href = $link->getAttribute("href");
    array_push( $link_array, $href);
    echo $href . PHP_EOL;
}
print_r($link_array);

$name_link = $xpath->query("//div[@class='package-header__left']//h1[@class='package-header__name']");

foreach ($link_array as $linke) {
    $name = $name_link->textContent;
}
?>

</body>
</html>