//main.js

//Helper Functions: 

// Function to generate ranges and populate selectbox for nums
function generateOptions(start, end, increment) {
    var options = [];
    for (let i = start; i <= end; i += increment) {
        options.push(`<option value="${i}">${i}</option>`);
    }
    options.reverse()
    return options.join('');
}

// Same function but for string values
function generateStringOptions (array) {
    var options=[]
    for (let choice of array) {
        options.push(`<option value= "${choice}">${choice}</option>`)
    }
    return options.join('')
}


///////////////////////////////////////



// Populating initial values
document.getElementById('maxPriceRange').innerHTML = generateOptions(5000, 200000, 5000)

let conditionsArray = ['any','good', 'excellent', 'fair', 'like new', 'new', 'salvage']
let newConditionsArray = conditionsArray.map(function(x) { return x.charAt(0).toUpperCase() + x.slice(1,)})
document.getElementById('condition').innerHTML = generateStringOptions(newConditionsArray)


let stateArray = ['any','az', 'ar', 'fl', 'ma', 'nc', 'ny', 'or', 'pa', 'tx', 'wa', 'wi',
'al', 'ak', 'ca', 'co', 'ct', 'dc', 'de', 'ga', 'hi', 'id', 'il',
'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'mi', 'mn', 'ms', 'mo',
'mt', 'ne', 'nv', 'nj', 'nm', 'nh', 'nd', 'oh', 'ok', 'ri', 'sc',
'sd', 'tn', 'ut', 'vt', 'va', 'wv', 'wy']
let newStateArray = stateArray.map(function(x){return x.toUpperCase()})
document.getElementById('state').innerHTML=generateStringOptions(newStateArray)


let brandArray = ['any', 'gmc', 'chevrolet', 'toyota', 'ford', 'jeep', 'nissan', 'ram',
'mazda', 'cadillac', 'honda', 'dodge', 'lexus', 'jaguar', 'buick',
'chrysler', 'volvo', 'audi', 'infiniti', 'lincoln', 'alfa-romeo',
'subaru', 'acura', 'hyundai', 'mercedes-benz', 'bmw', 'mitsubishi',
'volkswagen', 'porsche', 'kia', 'rover', 'ferrari', 'mini',
'pontiac', 'fiat', 'tesla', 'saturn', 'mercury', 'harley-davidson',
'datsun', 'aston-martin', 'land rover', 'morgan']
let newBrands = brandArray.map(function(x) { return x.charAt(0).toUpperCase() + x.slice(1,)})
document.getElementById('manufacturer').innerHTML = generateStringOptions(newBrands)

let size = ['any', 'full-size', 'mid-size', 'compact', 'sub-compact']
let newSize = size.map(function(x) { return x.charAt(0).toUpperCase() + x.slice(1,)})
document.getElementById('size').innerHTML = generateStringOptions(newSize)

let transmissionArray = ['any', 'other', 'automatic', 'manual']
let newTransmissionArray = transmissionArray.map(function(x) {return x.charAt(0).toUpperCase() + x.slice(1,)})
document.getElementById('transmission').innerHTML = generateStringOptions(newTransmissionArray)

let odometerAraray = ['Less than 200000', 'Less than 400000', 'Less than 600000', 'Less than 800000']
document.getElementById('odometer').innerHTML = generateStringOptions(odometerAraray)

let cylinderArray = ['Any', '8 cylinders', '6 cylinders', '4 cylinders', '5 cylinders', '3 cylinders', '10 cylinders', '12 cylinders']
document.getElementById('cylinder').innerHTML = generateStringOptions(cylinderArray)

// Populates the text Value upon change
// document.getElementById('maxPriceRange').addEventListener('input', function() {
//     document.getElementById('maxPriceRangeValue').textContent = this.value;});

///////////////



// Hit Search button based on query options
function searchCars () {
    var query = document.getElementById('searchBar').value;
    var priceMax = document.getElementById('maxPriceRange').value;
    var condition = document.getElementById('condition').value;
    var manufacturer = document.getElementById('manufacturer').value;
    var size = document.getElementById('size').value;
    var odometer = document.getElementById('odometer').value;
    var state = document.getElementById('state').value;
    var transmission = document.getElementById('transmission').value;
    var cylinders = document.getElementById('cylinder').value;


    //Redirect to results after search is made
    window.location.href = "/results?query=" + query + "&maxPrice=" + priceMax + "&condition=" + condition + "&state" + state + "&manufacturer=" + manufacturer + "&size=" + size + "&ododmeter=" + odometer + "&transmission=" + transmission + "&cylinders=" + cylinders;
}

// Navigate to pages Buttons
function team(){
    window.location.href = "/team"
}

function about(){
    window.location.href = "/about"
}

//Sign Up Notification
document.getElementById('notificationForm').addEventListener('submit', function(e){
    e.preventDefault();

    const email = document.getElementById('formEmail').value
    //Build Backend API to send email


    //Send Alert for email
    $('#notificationModal').modal('hide');
    alert(`Thank you for signing up! Updates will be sent to ${email}`)
})



//Hitting enter for search bar
document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    searchCars()
})

document.addEventListener('DOMContentLoaded', function () {
    loadChart();
});

// Load chart data from the server and display the chart
function loadChart() {
    // Load chart data
    fetch('/load_chart')
        .then(response => response.json())
        .then(data => {
            const chartLabels = data.map(item => item.manufacturer);
            const chartData = data.map(item => item.avg_price);

            // Create chart
            var ctx = document.getElementById('chartContainer').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: chartLabels,
                    datasets: [{
                        label: 'Average Price',
                        data: chartData,
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
}






