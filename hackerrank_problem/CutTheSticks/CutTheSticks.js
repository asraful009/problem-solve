// "use strict";

const { log } = require("console");
const fs = require("fs");

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

/*
 * Complete the 'cutTheSticks' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function cutTheSticks(arr) {
  let arrt = Array.from(arr);
  arrt = arrt.sort((a, b) => a - b);
  // console.log(arrt);
  let ret = [];
  while (arrt.length > 0) {
    let neg = arrt[0];
    // console.log({ arrt, neg });
    let tmpCount = 0;
    let temp = [];
    for (let i = 0; i < arrt.length; i++) {
      tmpCount++;
      arrt[i] -= neg;
      if (arrt[i] > 0) temp.push(arrt[i]);
    }
    // console.log({ s: "before", arrt, temp });
    arrt = temp;
    ret.push(tmpCount);
    // console.log({ s: "after", arrt, temp });
  }
  // console.log(ret);
  return ret;
}

function main() {
  const ws = fs.createWriteStream("o");

  const n = parseInt(readLine().trim(), 10);

  const arr = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

  const result = cutTheSticks(arr);

  ws.write(result.join("\n") + "\n");

  ws.end();
}
