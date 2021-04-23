//Load Google map instance and add neighborhood markers with click and hover interactivity

function initMap(){
    const options = {
      zoom:12.2,
      center:{lat:37.7618, lng:-122.4432}
  }

  //Create new map instance
  const map = new google.maps.Map(document.getElementById('search_map'), options);

  //create an empty list to push marker data onto after fetching from database
  const neighborhoodMarkers = [];

  //AJAX request to fetch neighborhood data from database
  $(document).ready(function() {
    $.get('/neighborhood-details.json', (response) => {
      const neighborhood_array = (response);

  //creating an array of markers populated with neighborhood data from database
    for (const neighborhood of neighborhood_array) {
      const detailsOfNeighborhood = {
        name: neighborhood.name,
        coords: {lat:neighborhood.latitude, lng:neighborhood.longitude},
        short_desc: neighborhood.short_desc,
        neighborhood_id: neighborhood.neighborhood_id
      };
      neighborhoodMarkers.push(detailsOfNeighborhood);
    }
    
  //This function adds the neighborhood markers, info windows and click/mouseover events
  function addMarker(props){
     
    let marker = new google.maps.Marker({
      position: props.coords,
      map:map
   });

  //Create info windows for markers
    let infoWindow = new google.maps.InfoWindow({
    content: props.short_desc
    });
    
  //When user hovers over a marker, text at the top of the page will be replaced with neighborhood details
    //   marker.addListener('mouseover', function(){
    //   document.querySelector("#neighborhood-desc")
    //   .innerHTML = props.short_desc;
    // });

  //When user click on a marker, they are taken to the neighborhood details page
      marker.addListener('dblclick', function(){
        window.location.href = `/neighborhood/${props.neighborhood_id}`
    });

  //When user hovers over marker, info window with neighborhood name opens
      marker.addListener('click', function(){
        infoWindow.open(map, marker);
      });

  //When user stops hovering over marker, info window with neighborhood name closes
    //   marker.addListener('mouseout', function(){
    //     infoWindow.close(map, marker);
    // });
  }       
  
    //loop through marker array to add markers to Google map
    for(let i=0; i<neighborhoodMarkers.length; i++){
      addMarker(neighborhoodMarkers[i]);
    };
  })
 })
} 