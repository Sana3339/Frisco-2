function initMap2(){
    const options2 = {
      zoom:12.2,
      center:{lat:37.7618, lng:-122.4432}
    };

    //create map instance
    const map2 = new google.maps.Map(document.getElementById('posting_map'), options2);

    //create an empty list to push marker data onto after fetching from database
    const markers = [];

    $(document).ready(function() {
        $.get('/neighborhood-details.json', (response) => {
          const neighborhood_array = (response);
          
          //creating an array of markers upon fetching data from database
          for (const neighborhood of neighborhood_array) {
            const neighborhoodDetails = {
                name: neighborhood.name,
                coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
                short_desc: neighborhood.short_desc
            };
            markers.push(neighborhoodDetails);
          }
          console.log(markers);
        
        alert('Click is working!');
    
    for(var i = 0;i < markers.length; i++){
        addMarker(markers[i]);
    }
    
    function addMarker(props){
    let marker = new google.maps.Marker({
        position:props.coords,
        map:map2
    });
        marker.addListener('click', function(){
        document.querySelector("#posting_desc")
        .innerHTML = props.short_desc;
    });
   }
  })
 })
}
