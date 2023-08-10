//main.js

document.getElementById('carSeats').addEventListener('input', function() {
    document.getElementById('carSeatsValue').textContent = this.value;});

document.getElementById('priceRange').addEventListener('input', function() {
    document.getElementById('priceRangeValue').textContent = this.value;});



function searchCars () {
    var query = document.getElementById('searchBar').value;
    var priceRange = document.getElementById('priceRange').value;
    var carSeats = document.getElementById('carSeats').value;

    //Redirect to results after search is made
    window.location.href = "/results?query=" + query + "&price=" + priceRange + "&seats=" + carSeats;
}

function about(){
    window.location.href = "/about"
}