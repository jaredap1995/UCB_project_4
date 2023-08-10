//main.js

function searchCars () {
    var query = document.getElementById('searchBar').value;
    var priceRange = document.getElementById('priceRange').value;
    var carSeats = document.getElementById('carSeats').value;

    //Redirect to results after search is made
    window.location.href = "/results?query=" + query + "&price" + priceRange + "&seats" + carSeats;
}