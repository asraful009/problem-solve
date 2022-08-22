var lengthOfLastWord = function (s) {
  const arr = s.trim().split(" ");
  return arr[arr.length - 1].length;
};
console.log(
  "   fly me   to   the moon  ",
  lengthOfLastWord("   fly me   to   the moon  ")
);
