"use strict";

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
 * Complete the 'decryptPassword' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */
function setCharAt(str, index, chr) {
  if (index > str.length - 1) return str;
  return str.substring(0, index) + chr + str.substring(index + 1);
}

function decryptPassword(s) {
  // console.log(s);
  let ret = "";
  let allNumber = "";

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "0" || isNaN(s[i])) {
      s = s.substring(i);
      break;
    }
    if (!isNaN(s[i])) {
      allNumber += s[i];
    }
  }
  allNumber = allNumber.split("").reverse().join("");

  let ss = s.split("");
  for (let i = 0; i < ss.length; i++) {
    if (ss[i] === "*") {
      // console.log({ si: ss[i], s1: ss[i - 1], s2: ss[i - 2] });
      let t = ss[i - 2];
      ss[i - 2] = s[i - 1];
      ss[i - 1] = t;
      ss[i] = "";
    }
  }
  s = ss.join("");
  // console.log({ s, allNumber });
  let numIndex = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "0") {
      ret += allNumber[numIndex++];
    } else {
      ret += s[i];
    }
  }
  console.log({ ret });
  return ret;
}

function main() {
  // const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
  const ws = fs.createWriteStream("o");

  const s = readLine();

  const result = decryptPassword(s);

  ws.write(result + "\n");

  ws.end();
}
