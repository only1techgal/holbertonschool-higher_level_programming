// Uses the Fetch API to get the data from the provided URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())  // Parse the response as JSON
  .then(data => {
    // Extracts the character's name from the response data
    const characterName = data.name;

    // Displays the character's name in the div with id "character"
    document.querySelector('#character').textContent = characterName;
  })
  .catch(error => {
    // Handles errors that occur during the fetch
    console.error('Error fetching data:', error);
  });
