<?php
// scraper.php — Executes Python script and returns JSON
// additional data validation required

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["url"])) {
    $url = escapeshellarg($_POST["url"]);

    // Execute the Python scraper and capture output
    $command = "python3 text_image_scraper.py $url";
    $output = shell_exec($command);
    
    header("Content-Type: application/json");
    echo $output;
} else {
    http_response_code(400);
    echo json_encode(["error" => "Invalid request."]);
}
