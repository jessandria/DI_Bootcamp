let sentence = "The movie is not that bad, I like it";


let wordNot = sentence.indexOf("not");


let wordBad = sentence.indexOf("bad");

if (wordBad > wordNot && wordNot !== -1 && wordBad !== -1) {
    
    let partBeforeNot = sentence.substring(0, wordNot);
    let partAfterBad = sentence.substring(wordBad + 3);
    let newSentence = partBeforeNot + "good" + partAfterBad;

    
    console.log(newSentence);
} else {
    
    console.log(sentence);
}
