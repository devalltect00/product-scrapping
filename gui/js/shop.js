let {PythonShell} = require('python-shell')
var path = require("path")

function get_message(){
        var options = {
        scriptPath : path.join(__dirname, '/../engine/model')
    }

    let pyshell = new PythonShell('product.py', options)
    pyshell.on('message', function(message) {
        swal(message)
    })

    console.log("roger that")
}

PRODUCT_JSON = "../data/products.json"

// Using XMLHttpRequest
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var jsonData = JSON.parse(this.responseText);
        console.log(jsonData);
    }
};
xhr.open("GET", PRODUCT_JSON, true);
xhr.send();

// Using fetch() API
fetch(PRODUCT_JSON)
    .then(response => response.json())
    .then(jsonData => {
        var productListTableBody = document.getElementById("productList").getElementsByTagName("tbody")[0];
        
        for (var i = 0; i < jsonData.items.length; i++) {
            
            var row = productListTableBody.insertRow(i)
            row.insertCell(0).innerHTML = jsonData.items[i].index;
            row.insertCell(1).innerHTML = jsonData.items[i].name;
            row.insertCell(2).innerHTML = "<img src='" + jsonData.items[i].pictureLink + "' alt='" + jsonData.items[i].name + "'>";
            row.insertCell(3).innerHTML = jsonData.items[i].price;
            row.insertCell(4).innerHTML = jsonData.items[i].rating;
            row.insertCell(5).innerHTML = jsonData.items[i].status;
            row.insertCell(6).innerHTML = jsonData.items[i].location;
        }
        console.log(jsonData.items)})
    .catch(error => console.error(error));
