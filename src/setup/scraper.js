// Parks were scraped by running this script in the browser console at this URL:
// https://en.wikipedia.org/wiki/List_of_Colorado_state_parks

/** @function fetchGeoCoords - Given a park's wikipedia URL, fetch its latitude and longitude
 *  @param {string} parkPageUrl - for example, 'https://en.wikipedia.org/wiki/Trinidad_Lake_State_Park'
 */
function fetchGeoCoords (parkPageUrl) {
  // parkPageUrl will point to a specific park's wikipediate page
  return new Promise(function (resolve, reject) {
    let request = new XMLHttpRequest();
    request.addEventListener('load', function (request) {
      resolve(new DOMParser()
              .parseFromString(request.target.response, 'text/html')
              .querySelector('.geo-dms')
              .innerText);
    });
    request.open('GET', parkPageUrl);
    request.send();
  });
}

/** @function buildSqlInsertString - Create a string like ('MyPark', 37.146, 104.57)
 *  @param {string} parkName - the park's name, as pulled from its link text
 *  @param {string} latLongDms - the park's location, example '37°08′44″N 104°34′13″W'
 */
function parseCoords (latLongDms) {
  // latLongDms will be a string like '37°08′44″N 104°34′13″W'
  return latLongDms.match(/(\d+)°(\d+)′([\d.]+)″/g)
    .map(dms => {
      let [d, m, s] = /(\d+)°(\d+)′([\d.]+)″/.exec(dms)
      .slice(1)
      .map(c => parseFloat(c));
      return d + m / 60 + s / 3600;
    })
    .map(coord => Math.round(coord * 1000, 0) / 1000);
}

/** @function printAllCoordinates - Follow each link in Wikipedia's list of
 *    Colorado state parks, extracting the park name and coordinates. Then
 *    print all that data to the console, formatted as a SQL INSERT statement
 */
async function printAllCoordinates () {
  const parks = Array.from(document.querySelector('.wikitable').querySelectorAll('tr'))
    .slice(2) // skip the table header, which is a 2-part row
    .map(row => row.querySelector('a'))
    .map(a => fetchGeoCoords(a.href)
      .then(coords => {
        let [lat, long] = parseCoords(coords);
        return `('${a.innerText}', ${lat}, ${long}, '${a.href}')`;
      }));
    
  const sqlRows = await Promise.all(parks);
  console.log(sqlRows.join('\n\t\t,'));
}

printAllCoordinates();
