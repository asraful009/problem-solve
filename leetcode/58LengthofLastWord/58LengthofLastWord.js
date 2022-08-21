var lengthOfLastWord = function (s) {
  const arr = s.trim().split(" ");
  return arr[arr.length - 2].length;
};
