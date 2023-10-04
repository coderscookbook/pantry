// https://www.w3schools.com/tags/ref_httpmethods.asp

// Simulated Server Object 
const server = {
  users: {
    1: { id: 1, name: "John Doe", email: "john@example.com" },
    2: { id: 2, name: "Jane Smith", email: "jane@example.com" },
  },
};

// Function to simulate the server-side behavior of handling PUT requests
function handlePUTRequest(url, data) {
  // In a real server, you would process the data and update the resource accordingly
  const userId = url.split("/").pop();
  const user = server.users[userId];

  if (user) {
    Object.assign(user, data);
    return { success: true, message: "User data updated successfully." };
  } else {
    return { success: false, message: "User not found." };
  }
}

// Function to simulate the server-side behavior of handling GET requests
function handleGETRequest(url) {
  // In a real server, you would fetch the resource from the database and return it
  const userId = url.split("/").pop();
  const user = server.users[userId];

  if (user) {
    return { success: true, data: user };
  } else {
    return { success: false, message: "User not found." };
  }
}

// Example usage of PUT method with JSON data
const putData = { name: "Updated User", email: "updated@example.com" };
const userIdToUpdate = 1;
const putRequestURL = `/api/users/${userIdToUpdate}`;

const putResponse = handlePUTRequest(putRequestURL, putData);
console.log("PUT Request Response:", putResponse);

// Example usage of GET method
const userIdToRetrieve = 2;
const getRequestURL = `/api/users/${userIdToRetrieve}`;

const getResponse = handleGETRequest(getRequestURL);
console.log("GET Request Response:", getResponse);
