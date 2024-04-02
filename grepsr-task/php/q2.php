<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        function func_a($str){
            $pattern = "/([^\@]*)\@([^.]*).(.*)/i";
            preg_match($pattern, $str, $strarr);
            array_shift($strarr);
            print_r($strarr);
        }

        function func_b($str){
            $pattern = "/^.{2}(.{3})/";
            preg_match($pattern, $str, $strarr);
            echo "<br>" .$strarr[1];
            //print_r($strarr);
        }

        $str1 = "abc@grepsr.com";
        $str2 = "734rn3242";
        func_a($str1);
        func_b($str2);

    ?>
</body>
</html>