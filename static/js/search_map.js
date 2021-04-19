$(document).ready(function() {
  $.get('/neighborhood-details.json', (response) => {
    const neighborhood_array = (response);
    console.log(response);
  })
  alert('Click is working!');
})


function initMap(){
    const options = {
      zoom:12.2,
      center:{lat:37.7618, lng:-122.4432}
  }

  //Create new map
  const map = new google.maps.Map(document.getElementById('search_map'), options);

  function addMarker(props){
     
    let marker = new google.maps.Marker({
      position: props.coords,
      map:map
   });

    //Check content
    if(props.content){
        let infoWindow = new google.maps.InfoWindow({
        content: props.content
    });
    

        marker.addListener('click', function(){
          infoWindow.open(map, marker);
        document.querySelector("#neighborhood-desc")
        .innerHTML = `<h3>This is the ${props.content} district.
        <a href="/neighborhood/${props.content}">Click to learn more</a>
        Click on another marker to learn about a different neighborhood.`;
      });
      }
    }       

       // Array of makers
       let markers = [
        {
          coords: {lat:37.8037, lng:-122.4368},
          content: '<b>Marina</b>'
          },
          {
          coords: {lat:37.7529, lng:-122.4474},
          content: 'Twin Peaks'
          },
          {coords: {lat:37.800415, lng:-122.417612},
          content: 'Russian Hill'
          },
          {coords: {lat:37.7941, lng:-122.4078},
          content: 'Chinatown'
          },
        ];  
  
        //loop through markers
        for(let i=0; i<markers.length; i++){
          addMarker(markers[i]);
        };
    } 