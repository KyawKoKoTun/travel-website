// default map layer
let map = L.map('map', {
    layers: MQ.mapLayer(),
    center: [21.9162, 95.9560],
    zoom: 6
});

function runDirection(start, end) {
    [lat, lng] = start.split(',');
    [lat1, lng1] = end.split(',');

    // lat, lng, lat1, lng1 = parseFloat(lat), parseFloat(lng), parseFloat(lat1), parseFloat(lng1)
    console.log(lat, lng, lat1, lng1)
    map = L.map('map', {
        layers: MQ.mapLayer(),
        center: [21.9162, 95.9560],
        zoom: 6
    });

    var dir = MQ.routing.directions();

    var routeOptions = {
        routeType: 'pedestrian',
        mustAvoidLinkIds: [],
        narrativeType: 'none',
        routeColor: '0000FF', // Blue color in hexadecimal
        routeWidth: 5,
        maxRoutes: 1
    };
    
    dir.route({
        locations: [
            { latLng: { lat: lat, lng: lng } },
            { latLng: { lat: lat1, lng: lng1 } }
        ]
    });


    CustomRouteLayer = MQ.Routing.RouteLayer.extend({
        createStartMarker: (location) => {
            var custom_icon;
            var marker;

            custom_icon = L.icon({
                iconUrl: 'static/img/red.png',
                iconSize: [20, 29],
                iconAnchor: [10, 29],
                popupAnchor: [0, -29]
            });

            marker = L.marker(location.latLng, { icon: custom_icon }).addTo(map);

            return marker;
        },

        createEndMarker: (location) => {
            var custom_icon;
            var marker;

            custom_icon = L.icon({
                iconUrl: 'static/img/blue.png',
                iconSize: [20, 29],
                iconAnchor: [10, 29],
                popupAnchor: [0, -29]
            });

            marker = L.marker(location.latLng, { icon: custom_icon }).addTo(map);

            return marker;
        },

    });

    map.addLayer(new MQ.Routing.RouteLayer({
        directions: dir,
        fitBounds: true
    }));
}

// function that runs when form submitted
function submitForm(event) {
    event.preventDefault();

    // delete current map layer
    map.remove();

    // getting form data
    start = document.getElementById("start").value;
    end = document.getElementById("destination").value;
    console.log(start, end)
        // run directions function
    runDirection(start, end);

    // reset form
    document.getElementById("form").reset();
}

// asign the form to form variable
const form = document.getElementById('form');

// call the submitForm() function when submitting the form
form.addEventListener('submit', submitForm);