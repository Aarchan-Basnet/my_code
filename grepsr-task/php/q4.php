<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        //read json file
        $json = file_get_contents("laptop.json");

        //decode json
        $json_data = json_decode($json, true);

        //opencsv file
        $fcsv = fopen('q4.csv', 'w');
        
        //write column names to csv
        fputcsv($fcsv, array('Title', 'Price', 'Brand'));

        //loop through json and write required data to csv
        $product = $json_data["products"];
        foreach ($product as $key => $value) {
            //print($value["title"]);
            $title = $value["title"];
            $price = $value["price"];
            $brand = $value["brand"];
            //print($brand);
            fputcsv($fcsv, array($title, $price, $brand));
        }
        //close csv file
        fclose($fcsv);

        
    ?>
</body>
</html>