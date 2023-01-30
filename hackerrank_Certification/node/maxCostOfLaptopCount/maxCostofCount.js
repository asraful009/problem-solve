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
 * Complete the 'maxCost' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY cost
 *  2. STRING_ARRAY labels
 *  3. INTEGER dailyCount
 */

function maxCost(cost, labels, dailyCount) {
  // console.log({ cost, labels, dailyCount });
  let max = 0;
  let len = cost.length;
  let currentDailyCount = 0;
  let currentDailyCost = 0;
  for (let i = 0; i < len; i++) {
    if (currentDailyCount === dailyCount) {
      if (currentDailyCost > max) max = currentDailyCost;
      // console.log({ currentDailyCost, currentDailyCount });
      currentDailyCost = 0;
      currentDailyCount = 0;
    }
    if (labels[i] === "legal") {
      currentDailyCount++;
    }
    currentDailyCost += cost[i];
  }
  // console.log({ max });
  return max;
}

function main() {
  // const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
  const ws = fs.createWriteStream("o");

  const costCount = parseInt(readLine().trim(), 10);

  let cost = [];

  for (let i = 0; i < costCount; i++) {
    const costItem = parseInt(readLine().trim(), 10);
    cost.push(costItem);
  }

  const labelsCount = parseInt(readLine().trim(), 10);

  let labels = [];

  for (let i = 0; i < labelsCount; i++) {
    const labelsItem = readLine();
    labels.push(labelsItem);
  }

  const dailyCount = parseInt(readLine().trim(), 10);

  const result = maxCost(cost, labels, dailyCount);

  ws.write(result + "\n");

  ws.end();
}
