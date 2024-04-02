<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
//link name and values as variable
$date_search = "q=date";
$sort_by = "o=-created";
$pages = array("page=1", "page=2", "page=3");

//create a dom object
$dom = new DOMDocument();

$packageNames = array();

//for all 3 pages extract packages url
foreach ($pages as $page) {
$url = "https://pypi.org/search/?{$date_search}&{$sort_by}&{$page}";
//fetch content from url
$html = file_get_contents($url);
//suppress errors for malformed html
@$dom->loadHTML($html); 
//create domxpath object
$xpath = new DOMXPath($dom);

//find all package links using xpath
$links = $xpath->query("//a[@class='package-snippet']");
//get href attribute and store in array
foreach ($links as $link) {
    $href = $link->getAttribute("href");
    $packageNames[] = $href;
    //echo $href . PHP_EOL;
}
}
//count total number of packages
$num = count($packageNames);
//echo $num;
//print_r($packageNames);

//open csv file and write columns
$fcsv = fopen('q6.csv', 'w');
fputcsv($fcsv, array('Name', 'Install Instruction', 'Release Date', 'Description', 'Author'));

//loop for all packages
for ($x = 0; $x < $num; $x++) {

    $url = "https://pypi.org{$packageNames[$x]}";

    $html_package = file_get_contents($url);

    $dom_package = new DOMDocument();
    @$dom_package->loadHTML($html_package);

    $xpath_package = new DOMXPath($dom_package);

    //list all xpath for given labels
    $name_link = $xpath_package->query(".//div[@class='package-header__left']//h1[@class='package-header__name']");
    $ins_link = $xpath_package->query("//span[@id='pip-command']");
    $release_link = $xpath_package->query("//p[@class='package-header__date']//time");
    $desc_link = $xpath_package->query("//p[@class='package-description__summary']");
    $author_link = $xpath_package->query("//div[@class='sidebar-section'][4]//p[2]//a");

    // Check if query returned a non-null result
    if ($name_link->length > 0 && $ins_link->length > 0 && $release_link->length > 0 && $desc_link->length > 0 && $author_link->length > 0) {
        //extract required values
        $name = $name_link->item(0)->textContent;
        $install = $ins_link->item(0)->textContent;
        $release_date = $release_link->item(0)->getAttribute('datetime');
        $description = $desc_link->item(0)->textContent;
        $author = $author_link->item(0)->textContent;

        //put values into csv
        fputcsv($fcsv, array($name, $install, $release_date, $description, $author));

        //print values
        echo "Name: " . $name . PHP_EOL;
        echo "Install command: " . $install . PHP_EOL;
        echo "Release date: " . $release_date . PHP_EOL;
        echo "Description: " . $description . PHP_EOL;
        echo "Author: " . $author . "<br>";
    }
}
fclose($fcsv);


?>


</body>
</html>