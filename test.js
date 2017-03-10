function reverseWords(str) {
  // "Do or do not. There is no try."
  // find each word using space delimiter
  var words = str.split(" ");
  var result = [];
  for (var i = words.length - 1; i >= 0; i--) {
    result.push(words[i]);
  }
  console.log(result.join(" "));
}
reverseWords("Do or do not, there is no try.");
