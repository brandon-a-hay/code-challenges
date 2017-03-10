// // you can write to stdout for debugging purposes, e.g.
// // console.log('this is a debug message');

// function solution(S) {
//     // write your code in JavaScript (Node.js 6.4.0)
//     // replace sentence ending chars with | and split on that
//     var sentences = S.replace(/[?.!]/g, '|').split('|');

//     var result = 0;

//     sentences.forEach(s => {
//         var words = s.split(' ');
//         var validWordCount = 0;
//         for (var i = 0; i < words.length; i++) {
//             if (words[i] !== '') {
//                 validWordCount++;
//             }
//         }
//         result = Math.max(validWordCount, result);
//     });

//     return result;
// }

// solution("Forget  CVs..Save time . x x");

function solution(A) {
    var strokesCount = 0;
    var currStrokeHeight = 0;

    for (var i = 0; i < A.length; i++) {
        if (currStrokeHeight < A[i]) {
            // next building is taller than our current stroke height
            // add the difference between heights to strokesCount
            strokesCount += A[i] - currStrokeHeight;
        }
        currStrokeHeight = A[i];
    }

    return strokesCount;
}
var a = [1,3,1,3,2,1];
solution(a);


// function solution(A, B) {
//     // write your code in JavaScript (Node.js 6.4.0)
//     return ((A * B) >>> 0).toString(2).split("0").length;
// }