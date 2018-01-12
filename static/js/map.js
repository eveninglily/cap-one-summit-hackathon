var map;
var purchaseMarker;
var altMarkers;

function initMap() {
    let dc = {lat: 38.9, lng: -77.01};
    map = new google.maps.Map(document.getElementById("map"), {
        center: dc,
        zoom: 10
    });
}

function getSuggest(category) {
    $.getJSON('suggest', {'category': category}, function(data) {
        let $recommendations = $("#recommendations > .collection");
        for (let i=0; i<data.length; i++) {
            $recommendations.append("<a class='collection-item merchant-item'>"
                + data[i].name
                + "</a>");
        }
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

        if (altMarkers) {
            for (let i=0; i<altMarkers.length; i++) {
                altMarkers[i].setMap(null);
            }
        }

        altMarkers = [];
        $("#recommendations > .collection").empty();

        let category = $(this).find("div.category").text();
        if (category !== "other") {
            getSuggest(category);
        }
    });

    $("#recommendations .merchant-item").click(function() {
    });
});
