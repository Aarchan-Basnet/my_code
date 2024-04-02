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

// Initialize an array to store package names
$packageNames = array();

// Output the href attribute of each link and store package names
foreach ($links as $link) {
    $href = $link->getAttribute("href");
    $packageNames[] = $href;
    //echo $href . PHP_EOL;
}

$num = count($packageNames);
// Output package names array
//print_r($packageNames);

// Find package names
for ($x=0; $x<$num; $x++) {

    $url = "https://pypi.org{$packageName[$x]}";

// Fetch HTML content from the URL
$html = file_get_contents($url);

// Create a DOMDocument object
$dom = new DOMDocument();
@$dom->loadHTML($html); // Suppress errors for malformed HTML

// Create a DOMXPath object
$xpath = new DOMXPath($dom);

        // Query for the package name within the context of the package link node
        $name_link = $xpath->query(".//div[@class='package-header__left']//h1[@class='package-header__name']");
        $ins_link = $xpath->query("//span[@id='pip-command']");
        $release_link = $xpath->query("//p[@class='package-header__date']//time");
        $desc_link = $xpath->query("//p[@class='package-description__summary']");
        $author_link = $xpath->query("//div[@class='sidebar-section'][4]//p[2]//a");
        
        $name = $name_link->textContent;
        echo $name. PHP_EOL;
}
?>


</body>
</html>