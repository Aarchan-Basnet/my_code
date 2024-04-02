<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        function generate_date($start_date, $end_date, $interval, $format) {
            $date_list = [];
            $current_date = strtotime($start_date);
            $end_date = strtotime($end_date);

            while ($current_date <= $end_date) {
                $date_list[] = date($format, $current_date);
                $current_date = strtotime("+$interval days", $current_date);
            }
            //print_r($date_list);
            return $date_list;
        }

        $start_date = "2023-01-01";
        $end_date = "2023-01-31";
        $interval = 2;
        $format = "Y-m-d";

        $result = generate_date($start_date, $end_date, $interval, $format);
        print_r($result);
    ?>
</body>
</html>