#!/usr/bin/node
// prints all characters of a Star Wars Movie.
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

if (process.argv.length === 3) {
  request(url, async (err, response, body) => {
    if (err) {
      console.error(err);
    }
    const charArr = JSON.parse(body).characters;
    try {
      const characterPromises = charArr.map(charUrl => {
        return new Promise((resolve, reject) => {
          request(charUrl, (err, response, body) => {
            if (err) {
              reject(err);
            } else {
              resolve(JSON.parse(body).name);
            }
          });
        });
      });

      const characters = await Promise.all(characterPromises);
      characters.forEach(character => console.log(character));
    } catch (error) {
      console.error(error);
    }
  });
}
