var map;
var purchaseMarker;

function initMap() {
    let dc = {lat: 38.9, lng: -77.01};
    map = new google.maps.Map(document.getElementById("map"), {
        center: dc,
        zoom: 10
    });
}

function getSuggest(category) {
    $.getJSON('suggest', {'category': category}, data => {
        console.log(data);
    });
}

$(document).ready(function() {
    $("#purchase-history .purchase-item").click(function() {
        if (purchaseMarker) {
            purchaseMarker.setMap(null);
        }

        let geocodeStr = $(this).find("div.geocode").text();
        let commaPos = geocodeStr.indexOf(",");
        let latlng = {lat: parseFloat(geocodeStr.slice(0, commaPos)), lng: parseFloat(geocodeStr.slice(commaPos+1))};
        purchaseMarker = new google.maps.Marker({
            position: latlng,
            map: map,
        })

        map.panTo(latlng);
    });
});
