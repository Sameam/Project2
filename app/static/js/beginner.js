var quiz = document.getElementById('quiz');
var results = document.getElementById('results');
var submit = document.getElementById('check');
var numCorrect = 0;

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
    numCorrect = 0;
		showResults(questions, quizContainer, resultsContainer);
    AjaxSubmit() 
	}
}

var myQuestions = [
	{
		question: "1. How to find central tendancy in the dataset?",
		answers: {
			a: 'Mean Median Mode',
			b: 'Mean',
      c: 'Standard deviation',
      d: 'Variance'
		},
		correctAnswer: 'a'
	},
	{
		question: "2. Find the mean and median of the following dataset: Dataset = 25,89,90,5,34,32,67,89,90",
		answers: {
			a: 'Mean=54.89 Median=33 ',
			b: 'Mean=34 Median=34',
      c: 'Mean=57.89 Median=67',
      d: 'Mean=5 Median=67'
		},
		correctAnswer: 'c'
  },
  {
		question: "3. What is normal distribution look like?",
		answers: {
			a: 'Bell shaped and Symmetrics ',
			b: 'Right Skewed',
      c: 'Left Skewed',
      d: 'Bell shaped and Asymmetrics'
		},
		correctAnswer: 'a'
  },
  {
    question: "4. What is histogram used for?",
		answers: {
			a: 'Outliers',
			b: 'Distribution',
      c: 'Dataset unbalance',
      d: 'Average'
		},
		correctAnswer: 'b'
  },
  {
    question: "5. What type of dataset is suitable with bar graph?",
		answers: {
			a: 'Categorical',
			b: 'Quantitative',
      c: 'Unbalance Dataset',
      d: 'Interval dataset'
		},
		correctAnswer: 'a'
  },
  {
    question: "6. Scenario: In your wallet, you have 5 10$ cash and 10 20$ cash? You want to find the probability whether when you take out the money is a 10$ or 20$ paper? What is this kind of probability event?",
		answers: {
			a: 'Independence Event',
			b: 'Dependence Event',
      c: 'Inclusive Event',
      d: 'Mutually Exclusive Event'
		},
		correctAnswer: 'd'
  },
  {
    question: "7. When the outcome of the first event affect the second event, it is called: ",
		answers: {
			a: 'Independence Event',
			b: 'Dependence Event',
      c: 'Inclusive Event',
      d: 'Mutually Exclusive Event'
		},
    correctAnswer: 'b'
  },
  {
    question: "8. Technique that allow us to use statistics such as mean or sample standard deviation to make generalization about population is called: ",
		answers: {
			a: 'Confidence Interval',
			b: 'Statistical test',
      c: 'Inferential Statistics',
      d: 'Descriptive Statistics'
		},
    correctAnswer: 'c'
  },
  {
    question: "9. Find the sample variance (var) and sample standard deviation (std) of the following dataset: Dataset = 25,89,90,5,34,32,67,89,90",
		answers: {
			a: 'Var = 1022.32, Std= 31.974',
			b: 'Var = 1150.11, Std= 33.913',
      c: 'Var = 1800, St= 42.426',
      d: 'Not enough information'
		},
    correctAnswer: 'b'
  },
  {
    question: "10. What is a single value estimate of parameter",
		answers: {
			a: 'Confidence Interval',
			b: 'Sample error',
      c: 'Point estimate',
      d: 'All of the above'
		},
    correctAnswer: 'c'
  },
];

generateQuiz(myQuestions, quiz, results, submit);

function AjaxSubmit() {
  var data = {
    "score": numCorrect,
  };
  $.ajax({
    type: 'POST',
    url: '/score1',
    data: data, 
    dataType: 'json',
    async : false,
    success: function(data) { 
    },
  });
}




