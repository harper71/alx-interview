#!/usr/bin/node
const request = require('request');

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
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

getCharacters(1); // Replace with the desired movie ID
