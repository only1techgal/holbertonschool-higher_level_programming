// Fetchs the list of movies from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())  // Parse the response to JSON
  .then(data => {
    // Selects the <ul> element where movie titles will be listed
    const movieList = document.querySelector('#list_movies');
    
    // Loops through the movies array in the data and creates <li> elements
    data.results.forEach(movie => {
      // Creates a new <li> element for each movie title
      const listItem = document.createElement('li');
      
      // Sets the text content of the <li> to the movie's title
      listItem.textContent = movie.title;
      
      // Appends the <li> to the <ul> with the id 'list_movies'
      movieList.appendChild(listItem);
    });
  })
  .catch(error => {
    // Handles errors that occur during the fetch
    console.error('Error fetching data:', error);
  });
