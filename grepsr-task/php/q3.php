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
            ),
            'Accessories' => array(
            'items' => array(
            array (
            'title' => 'DJI OM 5 Smartphone Gimbal
            Stabilizer',
            'price' => '129.99'
            ),
            array (
            'title' => 'SAMSUNG Galaxy SmartTag',
            'price' => '30.00'
            )
            )
            )
            )
            )
            );

        //print_r($products);

        function print_info($products, $category='') {
            foreach ($products as $key => $value) {

                if ($key == "items") {
                    foreach ($value as $item) {
                        echo "Title: {$item['title']}, Price: {$item['price']}, Category: $category <br>";
                    }
                }

                else {
                    print_info($key, $value);
                }
            }
        }

        print_info($products);

    ?>
</body>
</html>