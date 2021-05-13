var quiz = document.getElementById('quiz');
var results = document.getElementById('results');
var submit = document.getElementById('submit');


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

var myQuestions = [
	{
		question: "1. 2 main types of statistical tests ",
		answers: {
			a: 't_test, ANOVA',
			b: 'Parametric, Non_parametric',
      c: 'p-value, significant level',
      d: 't_test, p_value'
		},
		correctAnswer: 'b'
	},
	{
		question: "2. How many steps in hypothesis testing?",
		answers: {
			a: '2',
			b: '3',
      c: '4',
      d: '5'
		},
		correctAnswer: 'd'
  },
  {
		question: "3. How many types of regression testing? ",
		answers: {
			a: '1',
			b: '2',
      c: '3',
      d: '4'
		},
		correctAnswer: 'c'
  },
  {
    question: "4. What do we compare to p-value to make conclusion?",
		answers: {
			a: 't-critical',
			b: 'hypothesis',
      c: 'signicant level',
      d: 'null hypothesis'
		},
		correctAnswer: 'c'
  },
  {
    question: "5. Assumption of regression",
		answers: {
			a: 'Linear',
			b: 'qualitative data',
      c: 'Unbalance Dataset',
      d: 'Interval dataset'
		},
		correctAnswer: 'a'
  },
  {
    question: "6. One condition that must satisfy on multiple linear regression is:",
		answers: {
			a: 'Collinearity',
			b: 'Non_collinearity',
      c: 'More than 2 variables',
      d: 'Not correlated'
		},
		correctAnswer: 'b'
  },
  {
    question: "7. Another name for dependent variable, ",
		answers: {
			a: 'Predictor',
			b: 'Predicted',
      c: 'Mean',
      d: 'Beta'
		},
    correctAnswer: 'b'
  },
  {
    question: "8. Another name for independent variable, ",
		answers: {
			a: 'Predictor',
			b: 'Predicted',
      c: 'Mean',
      d: 'Beta'
		},
    correctAnswer: 'a'
  },
  {
    question: "9. What is regression used for?",
		answers: {
			a: 'Make prediction',
			b: 'Test hypothesis',
      c: 'Test research question',
      d: 'Calculate the past dataset'
		},
    correctAnswer: 'a'
  },
  {
    question: "10. Scenario: You want to tes a group of sport students the different between before they taking protein and training and after taking protein and training. What is the suitable statistical test?",
		answers: {
			a: '1 t_test',
			b: '2 t-test',
      c: 'Paired t-test',
      d: 'All of the above'
		},
    correctAnswer: 'c'
  },
];



generateQuiz(myQuestions, quiz, results, submit);
