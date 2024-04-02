<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        //load html file
        $html = file_get_contents("table.html");

        //create dom object
        $dom = new DOMDocument();

        //load html to dom
        $dom->loadHTML($html);

        //open csv file
        $fcsv = fopen("table.csv", "w");

        //write column names to csv
        $col_array = array();
        $cols = $dom->getElementsByTagName("th");
        foreach ($cols as $col) {
            $data = $col->textContent;
            array_push($col_array, $data);
        }
        fputcsv($fcsv, $col_array);

        //write row elements to csv
        $rows = $dom->getElementsByTagName("tr");
        foreach ($rows as $row) {
            $cells = $row->getElementsByTagName("td");
            print_r($cells);

            $row_array = array();
            foreach ($cells as $cell) {
                $data = $cell->textContent;
                array_push($row_array, $data);
            }
            fputcsv($fcsv, $row_array);
        }
        fclose($fcsv);

        //csv data to array
        $csv = array_map('str_getcsv', file('table.csv'));
        echo '<pre>';
        print_r($csv);
        echo '</pre>';
    ?>
</body>
</html>