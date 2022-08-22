var plusOne = function (digits) {
  if (digits.length == 0) return digits;
  let c = 1;
  for (let i = digits.length - 1; i >= 0; i--) {
    let v = digits[i] + c;
    c = Math.floor(v / 10.0);
    v = v % 10;
    console.log(v, c);
    digits[i] = v;
  }
  if (c !== 0) digits = [c, ...digits];
  return digits;
};
let arr = [0];

console.log(plusOne(arr));
