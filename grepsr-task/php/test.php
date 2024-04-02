<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php

$products = array(
    'Home' => array(
        'Electronics & Accessories' => array(
            'items' => array(
                array(
                    'title' => 'SanDisk 256',
                    'price' => '24.45'
                ),
                array(
                    'title' => 'Jabra Wireless Headset',
                    'price' => '55.12'
                )
            )
        ),
        'Accessories' => array(
            'items' => array(
                array (
                    'title' => 'DJI OM 5 Smartphone Gimbal Stabilizer',
                    'price' => '129.99'
                ),
                array (
                    'title' => 'SAMSUNG Galaxy SmartTag',
                    'price' => '30.00'
                )
            )
        )
    )
);

// Recursive function to print title, price, and category
function printProductInfo($products, $category = '') {
    foreach ($products as $key => $value) {
        echo $key;
        if ($key == 'items') {
            echo "$key";
        }
        else {
            printProductInfo($key, $value);
        }
    }
}

// Call the recursive function
//printProductInfo($products);
var_dump($products);

?>

</body>
</html>