// Fetchs data from the URL
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json())  // Parse the response to JSON
  .then(data => {
    // Selects the <div> element with the id 'hello' and update its content
    document.getElementById('hello').textContent = data.hello;
  })
  .catch(error => {
    // Handles errors that occur during the fetch
    console.error('Error fetching data:', error);
  });
