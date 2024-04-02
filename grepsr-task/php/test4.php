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
$pages = array("page=1", "page=2", "page=3");


// Fetch HTML content from the URL


// Create a DOMDocument object
$dom = new DOMDocument();
// Suppress errors for malformed HTML

// Create a DOMXPath object


// Find all links with class 'package-snippet'


// Initialize an array to store package names
$packageNames = array();
foreach ($pages as $page) {
$url = "https://pypi.org/search/?{$date_search}&{$sort_by}&{$page}";
$html = file_get_contents($url);
@$dom->loadHTML($html); 
$xpath = new DOMXPath($dom);
$links = $xpath->query("//a[@class='package-snippet']");
// Output the href attribute of each link and store package names
foreach ($links as $link) {
    $href = $link->getAttribute("href");
    $packageNames[] = $href;
    //echo $href . PHP_EOL;
}
}

$num = count($packageNames);
//echo $num;
// Output package names array
//print_r($packageNames);

// Find package names
// Find package names
$fcsv = fopen('q6.csv', 'w');
fputcsv($fcsv, array('Name', 'Install Instruction', 'Release Date', 'Description', 'Author'));

for ($x = 0; $x < $num; $x++) {

    $url = "https://pypi.org{$packageNames[$x]}";

    // Fetch HTML content from the URL
    $html_package = file_get_contents($url);

    // Create a DOMDocument object
    $dom_package = new DOMDocument();
    @$dom_package->loadHTML($html_package); // Suppress errors for malformed HTML

    // Create a DOMXPath object
    $xpath_package = new DOMXPath($dom_package);

    // Query for the package name within the context of the package link node
    $name_link = $xpath_package->query(".//div[@class='package-header__left']//h1[@class='package-header__name']");
    $ins_link = $xpath_package->query("//span[@id='pip-command']");
    $release_link = $xpath_package->query("//p[@class='package-header__date']//time");
    $desc_link = $xpath_package->query("//p[@class='package-description__summary']");
    $author_link = $xpath_package->query("//div[@class='sidebar-section'][4]//p[2]//a");

    // Check if query returned a non-null result
    if ($name_link->length > 0 && $ins_link->length > 0 && $release_link->length > 0 && $desc_link->length > 0 && $author_link->length > 0) {
        $name = $name_link->item(0)->textContent;
        $install = $ins_link->item(0)->textContent;
        $release_date = $release_link->item(0)->getAttribute('datetime');
        $description = $desc_link->item(0)->textContent;
        $author = $author_link->item(0)->textContent;

        fputcsv($fcsv, array($name, $install, $release_date, $description, $author));

        echo "Name: " . $name . PHP_EOL;
        echo "Install command: " . $install . PHP_EOL;
        echo "Release date: " . $release_date . PHP_EOL;
        echo "Description: " . $description . PHP_EOL;
        echo "Author: " . $author . "<br>";
    } /*else {
        echo "Package details not found." . PHP_EOL;
    }*/
}
fclose($fcsv);


?>


</body>
</html>