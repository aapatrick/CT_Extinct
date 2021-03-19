 <!doctype html>
<html lang="en">
  <head>
    <title>Home</title>
    <?php require_once "../includes/headLinks_view.php"?>
  </head>

  <body>
    <div class="container-fluid">
      <?php require_once "../includes/navigation_view.php"?>
      <div id ="slideshow" class="carousel slide" data-ride="carosel">
        <ul class="carousel-indicators"><!--4 buttons at the bottom to switch between slides-->
          <li data-target="#slideshow" data-slide-to="0" class=active></li>
          <li data-target="#slideshow" data-slide-to="1"></li>
          <li data-target="#slideshow" data-slide-to="2"></li>
          <li data-target="#slideshow" data-slide-to="3"></li>
        </ul>
        <div class="carousel-inner"><!--The different slides of the slideshow-->
          <div class="carousel-item active" id="slideimg">
            <img src="../assets/images/londonBus.jpg">
            <div class="carousel-caption">
              <h1 class="display-2">BerWyn Buses Hire<h1><!--makes title a bootsrap size of 2 (large)-->
              <h3>Since 1982</h3>
              <form method= "POST" action = "../controller/fleet_controller.php" >
                <button name="startBooking" type="submit" class="btn btn-lg btn-primary btn-light">Start Booking</button>
              </form>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../assets/images/childrenWaving.jpg">
          </div>
          <div class="carousel-item">
            <img src="../assets/images/toyBus.jpg">
          </div>
          <div class="carousel-item">
            <img src="../assets/images/map.jpg">
          </div>
        </div>
      </div>
      <div class="container">
        <br/><h1 class="d-flex justify-content-center">Valid Promotions, grab them now while they last!</h1><br/>
        <div class="row">
          <?php foreach ($recentPromo as $promo): ?>
          <div class="col-lg 3 col-md-3 col-sm-12 col-xs-12">
            <div class="card text-center cardWidth">
              <img class="card-img-top" src="../assets/images/purpleSpeaker.jpg" alt="Image for promotion: <?= $promo->vehicle_id?>">
              <div class="card-body">
                  PromoCode: <?= $promo->promotion_code ?><br/>
                  Discount: <?= $promo->discount ?>% OFF!<br/>
                  Valid From: <?= $promo->b_start_date ?><br/>
                  Expires: <?= $promo->b_end_date ?><br/>     
              </div>
            </div>
          </div>
          <?php endforeach ?>
        </div>
      
        <br/><h1 class="d-flex justify-content-center">New to the Garage</h1><br/>
        <div class="row">
            <?php foreach ($recentVehi as $vehicle): ?>
            <div class="col-lg 3 col-md-3 col-sm-12 col-xs-12">
              <div class="card text-center cardWidth" >
                <img class="card-img-top" src="../assets/images/blackSpeaker.jpg" alt="Image for Vehicle ID: <?= $vehicle->vehicle_id?>">
                <div class="card-body">
                  Make: <?= $vehicle->make ?><br/>
                  Model: <?= $vehicle->model ?><br/>
                  Colour: <?= $vehicle->colour?><br/>
                  Seats: <?= $vehicle->num_of_seats ?><br/>  
                  Registered: <?= $vehicle->date_of_registration ?><br/>
                  Price: £<?= $vehicle->price ?><br/>
                </div>
              </div>
            </div>
            <?php endforeach ?>
        </div>
        <br/>
      </div>
    </div>
    <!-- jQuery-->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <!-- Bootstrap JS-->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>
    <!--Our Own JavaScript-->
    <script src="../assets/js/script.js"></script>
  </body>
  <?php require_once "../includes/footer_view.php"?> 
</html>

