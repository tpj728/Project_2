var map = L.map("map", {
  style: 'mapbox://styles/mapbox/dark-v10',
  center: [39.5, -98.35], // starting position
  zoom: 5 // starting zoom
  });

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  // attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.dark",
  accessToken: API_KEY
}).addTo(map);

var link = "https://raw.githubusercontent.com/tpj728/Project_2/master/state_car_info.json";

function chooseColor(body) {
  switch (body) {
  case "Truck":
    return "lightcoral";
  case "SUV/Crossover":
    return "yellow";
  default:
    return "lightgreen";
  }
}

// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  // Creating a geoJSON layer with the retrieved data
  L.geoJson(data, {
    // Style each feature (state)
    style: function(feature) {
      return {
        color: "grey",
        // Call the chooseColor function to decide state color (color based on vehicle body style)
        // fillColor: "lightblue",
        fillColor: chooseColor(feature.properties.BODY),
        fillOpacity: 0.3,
        weight: 1.5
      };
    },
    // Called on each feature
    onEachFeature: function(feature, layer) {
      // Set mouse events to change map styling
      layer.on({
        // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 60% so that it stands out
        mouseover: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.6
          });
        },
        // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 30%
        mouseout: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.3
          });
        },
        // When a feature (state) is clicked, it is enlarged to fit the screen
        click: function(event) {
          map.fitBounds(event.target.getBounds());
        }
      });
      // Giving each feature a pop-up with information pertinent to it
      layer.bindPopup(`<div id="marker-panel"><h1> ${feature.properties.NAME} </h1><hr><br>
      	<a href="https://www.motortrend.com/cars/${feature.properties.MAKE}/${feature.properties.MODEL}/2016/" target="_blank">
      	<img src = "${feature.properties.IMGURL}" id="car-image"></a>
      	<div id = "marker-panel-text">
      	<br> <b>Make:</b> ${feature.properties.MAKE} <br> <b>Model:</b> ${feature.properties.MODEL}
      	<br> <b>MSRP:</b> ${feature.properties.MSRP} <br> <b>Class:</b> ${feature.properties.CLASS} 
      	<br> <b>MPG:</b> ${feature.properties.MPG} <br> <b>Body:</b> ${feature.properties.BODY}<div></div>`);

    }
  }).addTo(map);

});