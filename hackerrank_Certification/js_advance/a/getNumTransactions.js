'use strict';

const fs = require('fs');
const https = require('https');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
      inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');
    main();
});

function readLine() {
      return inputString[currentLine++];
}

async function get_page(url) {
  let data = '';
  return new Promise((resolve) => {
    https.get(url, res => {
      res.on('data', chunk => { data += chunk })
      res.on('end', () => {
          resolve(data);
      })
    });
  });
}

async function getNumTransactions(username) {
    // write your code here
    // API endpoint: https://jsonmock.hackerrank.com/api/article_users?username=<username>
    // API endpoint: https://jsonmock.hackerrank.com/api/transactions?&userId=<userId>

  let pageindex  = 1;
  let total = -1;
  while (true) {
    const url = `https://jsonmock.hackerrank.com/api/article_users?username=${username}`;
    const res = JSON.parse(await get_page(url));
    // console.log(res);
    for(let i=0; i<res.data.length; i++) {
      // console.log(res.data[i].username);
      if(res.data[i].username === username) {
        if(total === -1) {
          total = 0;
        }
        const urlUser = `https://jsonmock.hackerrank.com/api/transactions?&userId=${res.data[i].id}`;
        const resUser = JSON.parse(await get_page(urlUser));
        // console.log(resUser);
        total += resUser.total;
      }
    }
    // break;
    if(res.total_pages === pageindex || res.total_pages === 0) break;
    pageindex+=1;
  }
  // console.log(total);
  return (total === -1 ? `Username Not Found`:`${total}`);
}
async function main() {
    process.env.OUTPUT_PATH = "./o"
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    const username = readLine().trim();
    const result = await getNumTransactions(username);
    console.log(result);
    ws.write(result.toString());
}