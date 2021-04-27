<nav class="navbar navbar-expand-lg  navbar-dark bg-primary sticky-top" id="topheader">
  <!--Breakpoint reference-> xs,sm,md,lg,xl-->
  <div class="container-fluid">
    <!--Logo-->
    <a class="navbar-brand" href="../controller/index_controller.php">BerWyn Buses Hire</a>

    <!--Mobile Menu 3 Dashes Navigation Button-->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent">
      <span class="navbar-toggler-icon"></span>
    </button>
    <!--collapsable navigation menu-->
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ml-auto">
        <!--navigation to the right-->
        <li class="nav-link" id="nav-home">
          <a class="nav-link" href="../controller/index_controller.php">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-link" id="nav-aboutUs">
          <a class="nav-link" href="../controller/aboutUs_controller.php">About Us</a>
        </li>
        <li class="nav-link" id="nav-fleet">
          <a class="nav-link" href="../controller/fleet_controller.php">Fleet</a>
        </li>
        <li class="nav-link" id="nav-contactUs">
          <a class="nav-link" href="../controller/contactUs_controller.php">Contact Us</a>
        </li>
        <?php if(isset($_SESSION["loggedin"])):?>
        <li class="nav-link" id="nav-logout">
          <form method = 'post' action="../controller/logout_controller.php">
            <button name= 'user_logout'class="nav-link" type= 'submit'>Logout</button>
        </form>
        </li>
        <?php else : ?>
        <li class="nav-link" id="nav-login">
          <a class="nav-link" href="../controller/login_controller.php">Login</a>
          <?php endif ?>
        </li>
        <li class="nav-link">
          <form method="post" action="../controller/basket_controller.php">
            <button name="basket" type="submit" class="btn btn-primary">
              <i class="fa fa-shopping-cart" aria-hidden="true"><span id="badgeAmount" class="badge">
                  <?php if(sizeof($_SESSION["basket"]) > 0): ?>
                  <?= sizeof($_SESSION["basket"]); ?>
                  <?php else: ?>
                  0
                  <?php endif ?>
                </span></i>
            </button>
          </form>
        </li>
      </ul>
    </div>
  </div>
</nav>