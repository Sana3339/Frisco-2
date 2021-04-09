function initMap(){
    const options = {
      zoom:11.95,
      center:{lat:37.7618, lng:-122.4432}
  }

  //New map
  const map = new google.maps.Map(document.getElementById('map'), options);

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
       });
      }
    }   

       // Array of makers
       let markers = [
        {
          coords: {lat:37.8037, lng:-122.4368},
          content: 'Marina'
          },
          {
          coords: {lat:37.7529, lng:-122.4474},
          content: 'Twin Peaks'
          },
          {coords: {lat:37.800415, lng:-122.417612},
          content: 'Russian Hill'}
        ];  
  
        //loop through markers
        for(let i=0; i<markers.length; i++){
          addMarker(markers[i]);
        };
    } 
