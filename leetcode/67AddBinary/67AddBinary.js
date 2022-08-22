/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
  let ret = "";
  let c = 0;

  let lenA = a.length - 1;
  let lenB = b.length - 1;

  while (lenA >= 0 || lenB >= 0) {
    let sum = c;

    if (lenA >= 0) sum += a[lenA].charAt(0) - "0".charAt(0);
    if (lenB >= 0) sum += b[lenB].charAt(0) - "0".charAt(0);
    //console.log(sum);
    ret += `${sum % 2}`;
    c = Math.floor(sum / 2);

    lenA--;
    lenB--;
  }
  if (c !== 0) ret += "1";
  return ret.split("").reverse().join("");
};
console.log(addBinary("1010", "1011")); // 10101
