<?php 
require_once ("../controller/startup.php");
if(!isset($_SESSION)) session_start();
if(!isset($_SESSION['basket'])){
    $_SESSION['basket'] = [];
}

$error = false;
$msg ="";

$recentVehi = getRecentVehicles();
$recentPromo= getRecentPromotions();
require_once ("../view/index.php");
?>