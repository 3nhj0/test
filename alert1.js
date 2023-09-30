const fs = require('fs');

const fileName = 'enhj0.txt';

// Create an empty file
fs.writeFile(fileName, '', (err) => {
  if (err) throw err;
  console.log(`File '${fileName}' created successfully!`);
});
