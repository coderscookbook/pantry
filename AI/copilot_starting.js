// https://docs.github.com/en/copilot/getting-started-with-github-copilot?tool=vscode
/* Keyboard Shortcuts for Copilot:
    Option + Shift + K          -   to see the keyboard shortcuts
    
    Option + ] or [             -   to accept or reject a suggestion
    Option + Shift + ] or [     -   to accept or reject all suggestions
    Option + Enter              -   to accept a suggestion and move to the next line
    Option + Shift + Enter      -   to accept a suggestion and stay on the same line
    Option + Shift + Space      -   to see more suggestions

    Ctrl + Enter                -   to see multiple additional options in new tab

    Tip: at end of each line, press enter, tab to accept suggestion, and repeat
*/
    
// Creating code from comments example:
// finda ll images without alternate text
// and give the a red border
function process() {
    const images = document.querySelectorAll('img');
    for (const image of images) {
        if (!image.alt) {
            image.style.border = '5px solid red';
        }
    }
}

// Express server on port 3000
const express = require('express');
const app = express();
const port = 3000;

// Return the current time
app.get('/', (req, res) => {
    res.send(`The time is ${new Date()}`);
});

// Start the server
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
}
);
