


//
// Event handlers below:
//
$('.enter-site').on('click', () => {
  window.location.href='/map';
})

$('#find-housing').on('click', () => {
  alert('Take to find housing page!');
})

$('.post-housing').on('click', () => {
  alert('You must have an account to post housing');
  window.location.href='/login';
})

$('#back').on('click', () => {
  window.location.href='/map';
})

$('#test-button').on('click', () => {
  $.get('/quick-details/marina', (response) => {
    $('#test').html(response['name']);
    console.log(response);
  })
  alert('Click is working!');
})