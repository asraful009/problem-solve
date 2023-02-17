const lerp = (a, b, t) => {
  return (1 - t) * a + t * b;
};
const binomial = (n, k) => {
  if (typeof n !== "number" || typeof k !== "number") return 0;
  let coeff = 1;
  for (let x = n - k + 1; x <= n; x++) coeff *= x;
  for (x = 1; x <= k; x++) coeff /= x;
  return coeff;
};
const bezierCurvesValues = (arr, rate) => {
  if (typeof rate !== "number") return;
  const bCValues = {};
  const coeff = [];
  console.log({ arr });
  for (let index = 0; index < arr.length; index++) {
    coeff.push(binomial(arr.length - 1, index));
  }
  console.log({ coeff });
  for (let t = 0.0; t <= 1.0; t += rate) {
    pointIndex = `${t.toFixed(5)}`;
    bCValues[pointIndex] = 0;
    for (let index = 0; index < arr.length; index++) {
      p1t = (1 - t) ** (arr.length - index + 1);
      pt = t ** index;
      // console.log({
      //   "(v)": arr[index],
      //   "(coeff)": coeff[index],
      //   "(t)": t,
      //   "(1-t)P": p1t,
      //   "(t)P": pt,
      // });
      bCValues[pointIndex] += coeff[index] * p1t * pt * arr[index];
    }
  }
  console.log({ bCValues });
};

let arr = [
  { x: 0.0, y: 0.0 },
  { x: 3.0, y: 10.0 },
  { x: 8.0, y: 10.0 },
  { x: 5.0, y: 0.0 },
];
bezierCurvesValues(
  arr.map((v) => v.x),
  0.13
);
// const point = [];
// for (let t = 0.0; t <= 1.0; t += 0.000373) {
//   point.push({
//     x: lerp(arr[0].x, arr[arr.length - 1].y, t).toFixed(5),
//     y: lerp(arr[0].x, arr[arr.length - 1].y, t).toFixed(5),
//   });
// }
// console.log(JSON.stringify(point));
