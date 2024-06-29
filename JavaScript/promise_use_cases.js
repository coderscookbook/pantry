/************************************************************************************/
// Loading Data From an API
/************************************************************************************/
// UseCase: fetch data from a remote server and process it when available
fetch('https://randomuser.me/api/')
  .then(response => response.json())
  .then(data => console.log("DATA1: ", data))
  .catch(error => console.log("Failed to load data", error));

/************************************************************************************/
// Waiting for Multiple Requests to Complete
/************************************************************************************/
// UseCase: execute multiple API calls simultaneously and wati for all of them to complete
Promise.all([
  fetch('https://ipinfo.io/161.185.160.93/geo'),
  fetch('https://randomuser.me/api/')
]).then(responses => {
  return Promise.all(responses.map( res => res.json()));
}).then(data => console.log("DATA2: ", data));

/************************************************************************************/
// User Authentication
/************************************************************************************/
// UseCase: simulate user login, resolving on success and rejecting on failure
function loginUser(email, password) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
       if (email === 'user@example.com' && password === 'password123') {
        resolve({ userId: 1, profile: "Admin Profile" });
       } else {
        reject(new Error("Authentication Failed!"));
       }
    }, 1000);
  });
}

/************************************************************************************/
// Data Processing Pipeline
/************************************************************************************/
// UseCase: chain operations where each step depends on the successful completion of the previous step
fetch('https://randomuser.me/api/')
  .then(response => response.json)
  .then(data => processData(data))
  .then(processedData => console.log("ProcessedData: ", processedData))
  .catch(error => console.error("Failed in processing pipeline", error));

function processData(data){
  // Process data
  const modifiedData = data;
  return modifiedData;
}
/************************************************************************************/
// IMAGE LOADING
/************************************************************************************/
// UseCase: Load an image, perform actions once its loaded or handle errors
/* HTML CODE: 
<!DOCTYPE html>
<html>

<head>
	<title>Parcel Sandbox</title>
	<meta charset="UTF-8" />
</head>

<body>
	<div id="app"></div>

	<script src="src/index.js">
	</script>
</body>

</html>
*/

// script.js
import "./styles.css";

document.getElementById("app").innerHTML = `
<h1>Hello Vanilla!</h1>
<div>
  We use Parcel to bundle this sandbox, you can find more info about Parcel
  <a href="https://parceljs.org" target="_blank" rel="noopener noreferrer">here</a>.
</div>
<div id="image-container"></div>
`;

// Image Loading
// UseCase: load an image and perform actions once it is fully loaded or handle errors if it fails to load
function loadImage(url) {
  return new Promise((resolve, reject) => {
    const image = new Image();
    image.onload = () => resolve(image);
    image.onerror = () => reject(new Error('Failed to load image'));
    image.src = url;
  });
}

const url = 'https://cdn5.vectorstock.com/i/1000x1000/50/64/cute-drawing-a-poke-bowl-kawaii-food-vector-37915064.jpg';
loadImage(url).then(image => {
  document.getElementById('image-container').appendChild(image);
}).catch(error => {
  console.error(error);
  document.getElementById('image-container').innerHTML = 'Failed to load image';
});


/************************************************************************************/
// Timeouts
/************************************************************************************/
// UseCase: execute some action after a delay, without blocking the main thread
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

delay(1000).then(() => console.log("Delayed for 1 second"));
