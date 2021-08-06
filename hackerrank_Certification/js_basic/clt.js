"use strict";

const fs = require("fs");
const https = require("https");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");

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

async function getTeams(year, k) {
  // write your code here
  // API endpoint template: https://jsonmock.hackerrank.com/api/football_matches?competition=UEFA%20Champions%20League&year=<YEAR>&page=<PAGE_NUMBER>
  let pageindex  = 1;
  let teams = {};
  while (true) {
    const url = `https://jsonmock.hackerrank.com/api/football_matches?competition=UEFA%20Champions%20League&year=${year}&page=${pageindex}`;
    // console.log(url);
    const res = JSON.parse(await get_page(url));
    // console.log(res);
    for(let i=0; i<res.data.length; i++) {
      if(teams[res.data[i].team1] === undefined) teams[res.data[i].team1] = 0;
      // teams[res.data[i].team1]+= parseInt(res.data[i].team1goals);
      teams[res.data[i].team1]+= 1;
      if(teams[res.data[i].team2] === undefined) teams[res.data[i].team2] = 0;
      // teams[res.data[i].team2]+= parseInt(res.data[i].team2goals);
      teams[res.data[i].team2]+= 1;
    }
    if(res.total_pages === pageindex) break;
    pageindex+=1;
  }
  // console.log({year, k, teams});
  let topTeams = [];
  let teamNames = Object.keys(teams);
  for(let i=0; i<teamNames.length; i++) {
    if(teams[teamNames[i]] >= k ) {
      topTeams.push(teamNames[i]);
    }
  }
  topTeams.sort();
  // console.log(topTeams);
  return topTeams;
}

async function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const year = parseInt(readLine().trim());
  const k = parseInt(readLine().trim());

  const teams = await getTeams(year, k);

  for (const team of teams) {
    ws.write(`${team}\n`);
    // console.log(team);
  }
}
