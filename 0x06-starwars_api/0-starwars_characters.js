#!/usr/bin/node
const request = require('request');
function requestPromise (url) {
  const urlPromise = new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
  return urlPromise;
}

async function getCharacters (movieId) {
  try {
    const movie = await requestPromise(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    const characters = movie.characters;

    for (const characterUrl of characters) {
      const character = await requestPromise(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}
const movieId = process.argv[2];
getCharacters(movieId);
