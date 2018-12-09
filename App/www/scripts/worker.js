// Initialize the platform object:
var platform = new H.service.Platform({
    'app_id': 'YVx7VH25wvkdlUFvGjC8',
    'app_code': '_DmLSgB2oR1uQ1LrG0GbVQ'
});
var pixelRatio = window.devicePixelRatio || 1;
var defaultLayers = platform.createDefaultLayers({
    tileSize: pixelRatio === 1 ? 256 : 512,
    ppi: pixelRatio === 1 ? undefined : 320
});

// Obtain the default map types from the platform object
var maptypes = platform.createDefaultLayers();
// Instantiate (and display) a map object:
var map = new H.Map(self.document.getElementById('mapContainer'),
    defaultLayers.normal.map, defaultLayers.normal.map, { pixelRatio: pixelRatio });

//Step 3: make the map interactive
// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

// Create the default UI components
var ui = H.ui.UI.createDefault(map, defaultLayers);

function enableTrafficInfo(map) {
    // Show traffic tiles
    map.setBaseLayer(defaultLayers.normal.traffic);

    // Enable traffic incidents layer
    map.addLayer(defaultLayers.incidents);
}
// Now enable traffic tiles and traffic incidents
enableTrafficInfo(map);

// onError Callback receives a [PositionError](PositionError/positionError.html) object
function onError(error) {
    alert('code: ' + error.code + '\n' +
        'message: ' + error.message + '\n');
}

function onSuccess(position) {
    var element = document.getElementById('geolocation');
    element.innerHTML = 'Latitude: ' + position.coords.latitude + '<br />' +
        'Longitude: ' + position.coords.longitude + '<br />' +
        '<hr />' + element.innerHTML;
}

onmessage = function (event) {
    var watchID = navigator.geolocation.watchPosition(onSuccess, onError, { timeout: 30000 });
};
