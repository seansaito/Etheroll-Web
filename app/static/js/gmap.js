function() {
  {% set counter = 1 %}
  {% for driver in drivers.items() %}
  var map{{ counter }};
  function initialize() {
   var mapOptions{{ counter }} = {
     zoom: 1,
     center: new google.maps.LatLng(driver[1]["location"][0], driver[1]["location"][1])
   };

   map{{ counter }} = new google.maps.Map(document.getElementById('map-canvas{{ counter }}'),
       mapOptions{{ counter }});

  }

  google.maps.event.addDomListener(window, 'load', initialize);

  {% set counter = counter + 1 %}
  {% endfor %}
}
