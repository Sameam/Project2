var quiz = document.getElementById('quiz');
var results = document.getElementById('results');
var submit = document.getElementById('check');

function generateQuiz(questions, quizContainer, resultsContainer, submitButton){

	function showQuestions(questions, quizContainer){
    // we'll need a place to store the output and the answer choices
    var output = [];
    var answers;

    // for each question...
    for(var i=0; i<questions.length; i++){
      
      // first reset the list of answers
      answers = [];

      // for each available answer to this question...
      for(letter in questions[i].answers){

        // ...add an html radio button
        answers.push(
          '<label>'
            + '<input type="radio" name="question'+i+'" value="'+letter+'">'
            + letter + ': '
            + questions[i].answers[letter]
          + '</label>'
        );
      }

      // add this question and its answers to the output
      output.push(
        '<div class="question">' + questions[i].question + '</div>'
        + '<div class="answers">' + answers.join('') + '</div>'
      );
    }

    // finally combine our output list into one string of html and put it on the page
    quizContainer.innerHTML = output.join('');
  }

	function showResults(questions, quizContainer, resultsContainer){
    // code will go here
    // gather answer containers from our quiz
    var answerContainers = quizContainer.querySelectorAll('.answers');
    
    // keep track of user's answers
    var userAnswer = '';
    var numCorrect = 0;
    
    // for each question...
    for(var i=0; i<questions.length; i++){

      // find selected answer
      userAnswer = (answerContainers[i].querySelector('input[name=question'+i+']:checked')||{}).value;
      
      // if answer is correct
      if(userAnswer===questions[i].correctAnswer){
        // add to the number of correct answers
        numCorrect++;
        
        // color the answers green
        answerContainers[i].style.color = 'lightgreen';
      }
      // if answer is wrong or blank
      else{
        // color the answers red
        answerContainers[i].style.color = 'red';
      }
    }

    // show number of correct answers out of total
    resultsContainer.innerHTML = "Your score is " + numCorrect + ' out of ' + questions.length;
  }

	// show the questions
	showQuestions(questions, quizContainer);

	// when user clicks submit, show results
	submitButton.onclick = function(){
		showResults(questions, quizContainer, resultsContainer);
	}
}

var intermediateQuestions = [
	{
		question: "1. Scenario: The probabilities of three teams A, B and C winning a badminton competition are 1/3, 1/5 and 1/9 respectively. Find the probability either A or B or C will win",
		answers: {
			a: '<math><mfrac><mi> 1 </mi><mi> 3 </mi></mfrac></math>',
			b: '<math><mfrac><mi> 1 </mi><mi> 5 </mi></mfrac></math>',
      c: '<math><mfrac><mi> 29 </mi><mi> 45 </mi></mfrac></math>',
      d: '<math><mfrac><mi> 7 </mi><mi> 15 </mi></mfrac></math>'
		},
		correctAnswer: 'c'
  },
  {
		question: "2. We are 95% confidence that average score for web development class is between [50,80]. What is the Confidence Interval=(CI)?",
		answers: {
			a: '95% CI = 80',
			b: '95% CI = 50',
      c: '95% CI = [50,80]',
      d: '95% CI = 30'
		},
		correctAnswer: 'c'
  },
  {
		question: "3. Graph use for check correlation",
		answers: {
			a: 'Scatterplot',
			b: 'Density Plot',
      c: 'Barplot',
      d: 'Histogram'
		},
		correctAnswer: 'a'
  },
	{
		question: "4.  Set that is selected from a subset without replacement without considered the order",
		answers: {
			a: 'Permutation',
			b: 'Combination',
      c: 'Point estimate',
      d: 'Interval'
		},
		correctAnswer: 'b'
  },
  {
		question: "5.  Set that is selected from a subset without replacement and considered the order",
		answers: {
			a: 'Permutation',
			b: 'Combination',
      c: 'Point estimate',
      d: 'Interval'
		},
		correctAnswer: 'a'
  },
  {
		question: "6. How many ways can the first 3 places be awarded in a race involving  5 contestants?",
		answers: {
			a: '125',
			b: '60',
      c: '5',
      d: '3'
		},
		correctAnswer: 'b'
  },
  {
		question: "7. 3 elements a,b,c, how many permutation can make without repetition?",
		answers: {
			a: '12',
			b: '6',
      c: '9',
      d: '3'
		},
		correctAnswer: 'b'
  },
  {
		question: "8. 3 elements a,b,c, how many permutation can make with repetition?",
		answers: {
			a: '12',
			b: '6',
      c: '9',
      d: '3'
		},
    correctAnswer: 'a'
  },
  {
		question: "9. What is ratio between the number of wanted outcome compare to the number of all possible outcome?",
		answers: {
			a: 'Statistics',
			b: 'ANOVA',
      c: 'Statistical test',
      d: 'Probability'
		},
    correctAnswer: 'a'
  },
  {
		question: "9. what is probabilities of getting head when you toss a coin?",
		answers: {
			a: '<math><mfrac><mi> 1 </mi><mi> 2 </mi></mfrac></math>',
			b: '1',
      c: '<math><mfrac><mi> 1 </mi><mi> 3 </mi></mfrac></math>',
      d: '<math><mfrac><mi> 1 </mi><mi> 5 </mi></mfrac></math>'
		},
    correctAnswer: 'a'
  },
];


generateQuiz(intermediateQuestions, quiz, results, submit);