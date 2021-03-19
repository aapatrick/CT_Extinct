<?php
$pdo = new PDO(
    "mysql:host=kunet;dbname=db_k1739510",
    "k1739510",
    "elephant001",
    [PDO::ATTR_ERRMODE=> PDO::ERRMODE_EXCEPTION]
);

//////////////////////////
//FUNCTIONS FOR SECURITY//
//////////////////////////

function newCustomer($customer)
{
    global $pdo;
    $statement =$pdo->prepare("INSERT INTO addresses (addressln1,addressln2,city,postcode) 
    VALUES(?,?,?,?); 
    INSERT INTO customers (first_name,last_name,dob,company_name,contact_number,email_address,customer_pw,address_id) 
    VALUES (?,?,?,?,?,?,?,LAST_INSERT_ID());");
    $statement->execute([$customer->address->addressln1,
                         $customer->address->addressln2,
                         $customer->address->city,
                         $customer->address->postcode,
                         $customer->first_name,
                         $customer->last_name,
                         $customer->dob,
                         $customer->company_name,
                         $customer->contact_number,
                         $customer->email_address,
                         $customer->customer_pw]);
   //if (!$statement->fetch()) throw new PDOException("Failed to insert into the database new Customer:".$statement->queryString);  
}

function getLoginInfo($email_address, $customer_pw)
{
    global $pdo;
    $statement = $pdo->prepare ("SELECT * FROM customers 
                        WHERE email_address = ? AND customer_pw = ?");
    $statement->execute([$email_address, $customer_pw]);
    $results = $statement->fetchAll (PDO::FETCH_CLASS, 'Customer');
    return $results;
    
}

function getAdminLoginInfo($admin_id, $admin_pw)
{
    global $pdo;
    $statement = $pdo->prepare ("SELECT * FROM admins 
                        WHERE admin_id = ? AND admin_pw = ?");
    $statement->execute([$admin_id, $admin_pw]);
    $results = $statement->fetchAll (PDO::FETCH_CLASS, 'Admin');
    return $results;
}

// function newCustomerAddress($address)
// {
//     if ($address == "")
//     {
//         return true;
//     }
//     global $pdo;
//     $statement=$pdo->prepare("INSERT INTO addresses (Addressln1, Addressln2, city, postcode) VALUES (?,?,?,?)");
//     $statement->execute([$address->Addressln1,
//                          $address->Addressln2,
//                          $address->city,
//                          $address->postcode]);
// }

// function checkEmail($email_address)
// {
//     global $pdo;
//     $statement = $pdo->prepare("SELECT email_address FROM customers WHERE email_address = ?");
//     $statement->execute([$email_address]);
//     $results = $statement->fetchAll (PDO::FETCH_CLASS, 'Customer');
//     return $results;
//     if (count($results)>0)
//     {
//         return true;
//     }
//     else
//     {
//         return false;
//     }
// }


///////////////////////
//FUNCTIONS FOR ADMIN//
///////////////////////

function addVehicle($vehicle)
{
    global $pdo;
    $statement =$pdo->prepare("INSERT INTO vehicles 
    (make, model, colour, num_of_seats, date_of_registration, 
    licence_plate, price, licence_type) VALUES (?,?,?,?,?,?,?,?)");
    $statement->execute([$vehicle->make,
                         $vehicle->model,
                         $vehicle->colour,
                         $vehicle->num_of_seats,
                         $vehicle->date_of_registration,
                         $vehicle->licence_plate,
                         $vehicle->price,
                         $vehicle->licence_type]);
   if (!$statement->fetch()) throw new PDOException("Failed to insert into the database new vehicle:".$statement->queryString);//queryString returns the query that triggered the error, so it will return "INSERT INTO vehicles (...."                                
}

function addPromotion($promotion)
{
    global $pdo;
    $statement =$pdo->prepare("INSERT INTO promotions 
    (promotion_code, discount, vehicle_id, b_start_date, b_end_date) VALUES (?,?,?,?,?)");
    $statement->execute([$promotion->promotion_code,
                         $promotion->discount,
                         $promotion->vehicle_id,
                         $promotion->b_start_date,
                         $promotion->b_end_date]);
   if (!$statement->fetch()) throw new PDOException("Failed to insert into the database new promotion:".$statement->queryString);//If $statement->fetch() returns true the if statement would be false, if the fetch returned a false the if statement would be true and throw a PDOException which will be later caught in the controller. 
}


function getAllBookings()
{
    global $pdo;
    $statement =$pdo->prepare("SELECT * FROM bookings");
    $statement->execute();
    $results = $statement->fetchAll(PDO::FETCH_CLASS,"Booking");
    return $results;
}
//The following is a simple function that returns all vehicles as objects of the class vehicle.
function getAllVehicles()
{
    global $pdo;
    $statement = $pdo->prepare("SELECT * FROM vehicles");
    $statement->execute();
    $results = $statement->fetchAll (PDO::FETCH_CLASS, "Vehicle");
    return $results;
}

function getAllPromotions()
{
    global $pdo;
    $statement = $pdo->prepare("SELECT * FROM promotions");
    $statement->execute();
    $results = $statement->fetchAll (PDO::FETCH_CLASS, "Promotion");
    return $results;
}

function getRecentPromotions()
{
    global $pdo;
    $statement = $pdo->prepare("SELECT * FROM promotions WHERE CURDATE()  >= b_start_date AND CURDATE()<= b_end_date");
    $statement-> execute();
    $results = $statement->fetchAll (PDO::FETCH_CLASS, "Promotion");
    return $results;
}

function getRecentVehicles()
{
    global $pdo;
    $statement = $pdo->prepare("SELECT * FROM vehicles WHERE date_of_registration >= NOW() - INTERVAL 7 DAY");
    $statement-> execute();
    $results = $statement->fetchAll (PDO::FETCH_CLASS, "Vehicle");
    return $results;
}
function deleteVehicleById($vehicle_id)
{
    global $pdo;
    $statement =$pdo->prepare("DELETE FROM promotions WHERE vehicle_id = :id; 
                               DELETE FROM bookings WHERE vehicle_id = :id; 
                               DELETE FROM vehicles WHERE vehicle_id = :id");
    $statement->bindValue(":id",$vehicle_id,PDO::PARAM_INT);
    $statement->execute();
    return 'true';
}

function deletePromotionById($promotion_code)
{
    global $pdo;
    $statement =$pdo->prepare("DELETE FROM promotions WHERE promotion_code=?");
    $statement->execute([$promotion_code]);
    return 'true';
}

function getAllVehicleIds()
{
    global $pdo;
    $statement =$pdo->prepare("SELECT vehicle_id FROM vehicles");
    $statement->execute();
    $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
    return $results;
}

function getSingleVehicleById($vehicle_id)
{
    global $pdo;
    $statement =$pdo->prepare("SELECT * FROM vehicles WHERE vehicle_id=?");
    $statement->execute([$vehicle_id]);
    $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
    return $results;
}


function getSinglePromoById($promotion_code)
{
    global $pdo;
    $statement =$pdo->prepare("SELECT * FROM promotions WHERE promotion_code=?");
    $statement->execute([$promotion_code]);
    $results = $statement->fetchAll(PDO::FETCH_CLASS,"Promotion");
    return $results;
}

function updateVehicle($vehicle, $vehicle_id)
{
    global $pdo;
    $statement =$pdo->prepare("UPDATE vehicles SET 
                               make = ?, model = ?, colour=?, num_of_seats=?, date_of_registration=?, 
                               licence_plate=?, price=?, licence_type=? WHERE vehicle_id = ?");
    $statement->execute([$vehicle->make,
                         $vehicle->model,
                         $vehicle->colour,
                         $vehicle->num_of_seats,
                         $vehicle->date_of_registration,
                         $vehicle->licence_plate,
                         $vehicle->price,
                         $vehicle->licence_type,
                         $vehicle_id]);

    if (!$statement->fetch()) throw new PDOException("Failed to update into the database the vehicle:".$statement->queryString);
}

function updatePromo($promotion, $promotion_code)
{
    global $pdo;
    $statement =$pdo->prepare("UPDATE promotions SET 
                               promotion_code = ?, discount = ?, vehicle_id=?, b_start_date=?, b_end_date=?, 
                               WHERE promotion_code = ?");
    $statement->execute([$promotion->promotion_code,
                         $promotion->discount,
                         $promotion->vehicle_id,
                         $promotion->b_start_date,
                         $promotion->b_end_date,
                         $promotion_code]);

    if (!$statement->fetch()) throw new PDOException("Failed to update into the database the promotion:".$statement->queryString);
}
//////////////////////////////
//FUNCTIONS FOR FLEET SEARCH//
//////////////////////////////
//The following function is responsible for looking through the database depending on the criteria enterred and return an
//object of the class Vehicle that responds to the criteria supplied.
function getVehicleBySearch($s_date,$e_date,$l_type,$p_numb,$price)
{
    global $pdo;
    if ($s_date!="1799-12-03"&&$e_date!="1799-12-03"&&$l_type!=""&&$p_numb!=0&&$price!=0)
    {
    //If the user filled out all the criteria then this statement is used.
    $statement =$pdo->prepare("SELECT * FROM vehicles WHERE (vehicle_id NOT IN (SELECT vehicle_id FROM bookings WHERE b_start_date > ? OR b_end_date < ?)) AND licence_type = ? AND num_of_seats >= ? AND price <= ?");
    $statement->execute([$s_date,$e_date,$l_type,$p_numb,$price]);
    $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
    return $results;
    }
    else if ($s_date!="1799-12-03"&&$e_date!="1799-12-03"&&$l_type!=""&&$p_numb==0&&$price!=0)
    {
    //If the user filled out all the criteria except for Maximum passengers then this statement is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE (vehicle_id NOT IN (SELECT vehicle_id FROM bookings WHERE b_start_date > ? OR b_end_date < ?)) AND (licence_type = ?) AND price <= ?");
        $statement->execute([$s_date,$e_date,$l_type,$price]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date!="1799-12-03"&&$e_date!="1799-12-03"&&$l_type==""&&$p_numb!=0&&$price!=0)
    {
    //If the user filled out all the criteria except for Licence Type then this statement is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE (vehicle_id NOT IN (SELECT vehicle_id FROM bookings WHERE b_start_date > ? OR b_end_date < ?)) AND (num_of_seats >= ?) AND price <= ?");
        $statement->execute([$s_date,$e_date,$p_numb,$price]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date!="1799-12-03"&&$e_date!="1799-12-03"&&$l_type!=""&&$p_numb!=0&&$price==0)
    {
    //If the user filled out all the criteria except for Maximum Price then this statement is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE (vehicle_id NOT IN (SELECT vehicle_id FROM bookings WHERE b_start_date > ? OR b_end_date < ?))AND licence_type = ? AND (num_of_seats >= ?)");
        $statement->execute([$s_date,$e_date,$l_type,$p_numb]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date=="1799-12-03"&&$e_date=="1799-12-03"&&$l_type!=""&&$p_numb!=0&&$price!=0)
    {
    //If the user filled out all the criteria except for thr dates then this statement is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE num_of_seats >= ? AND licence_type = ? AND price <= ?");
        $statement->execute([$p_numb,$l_type,$price]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date=="1799-12-03"&&$e_date=="1799-12-03"&&$l_type!=""&&$p_numb!=0&&$price==0)
    {
    //If the user filled out only Maximum Passengers and Licence Type then this statement is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE num_of_seats >= ? AND licence_type = ? ");
        $statement->execute([$p_numb,$l_type]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date!="1799-12-03"&&$e_date!="1799-12-03"&&$l_type!=""&&$p_numb==0&&$price==0)
    {
    //If the user only filled out the dates and Licence Type then this statemnt is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE (vehicle_id NOT IN (SELECT vehicle_id FROM bookings WHERE b_start_date > ? OR b_end_date < ?)) AND licence_type = ? ");
        $statement->execute([$s_date,$e_date,$l_type]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date!="1799-12-03"&&$e_date!="1799-12-03"&&$l_type!=""&&$p_numb==0&&$price==0)
    {
    //If the user only filled out dates and Maximum Passengers then this statement is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE (vehicle_id NOT IN (SELECT vehicle_id FROM bookings WHERE b_start_date > ? OR b_end_date < ?)) AND num_of_seats >= ?");
        $statement->execute([$s_date,$e_date,$p_numb]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date!="1799-12-03"&&$e_date!="1799-12-03"&&$l_type==""&&$p_numb==0&&$price!=0)
    {
    //If the user only filled out dates and price then this statement is used 
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE (vehicle_id NOT IN (SELECT vehicle_id FROM bookings WHERE b_start_date > ? OR b_end_date < ?)) AND price <= ?");
        $statement->execute([$s_date,$e_date,$price]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date=="1799-12-03"&&$e_date=="1799-12-03"&&$l_type==""&&$p_numb!=0&&$price!=0)
    {
    //if the user only filled out Maximum Passengers and price then this statement is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE num_of_seats >=? AND price <= ?");
        $statement->execute([$p_numb,$price]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date=="1799-12-03"&&$e_date=="1799-12-03"&&$l_type!=""&&$p_numb!=0&&$price==0)
    {
    //if the user only filled out Maximum Passengers and Licence type then this statement is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE num_of_seats >=? AND price <= ?");
        $statement->execute([$p_numb,$l_type]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date=="1799-12-03"&&$e_date=="1799-12-03"&&$l_type==""&&$p_numb!=0&&$price==0)
    {
    //If the user only fillet out Maximum Passengers then this statemnt is used
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE num_of_seats >= ?");
        $statement->execute([$p_numb]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date=="1799-12-03"&&$e_date=="1799-12-03"&&$l_type!=""&&$p_numb==0&&$price==0)
    {
    
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE licence_type = ?");
        $statement->execute([$l_type]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date!="1799-12-03"&&$e_date!="1799-12-03"&&$l_type==""&&$p_numb==0&&$price==0)
    {


        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE vehicle_id NOT IN (SELECT vehicle_id FROM bookings WHERE b_start_date > ? OR b_end_date < ?)");
        $statement->execute([$s_date,$e_date]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    else if ($s_date=="1799-12-03"&&$e_date=="1799-12-03"&&$l_type==""&&$p_numb==0&&$price!=0)
    {
        $statement =$pdo->prepare("SELECT * FROM vehicles WHERE price <= ?");
        $statement->execute([$price]);
        $results = $statement->fetchAll(PDO::FETCH_CLASS,"Vehicle");
        return $results;
    }
    
    $statement = $pdo->prepare("SELECT * FROM vehicles");
    $statement->execute();
    $results = $statement->fetchAll (PDO::FETCH_CLASS, "Vehicle");
    return $results;
}
?>