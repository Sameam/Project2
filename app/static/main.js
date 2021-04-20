// drawing a histogram
const ctx = document.getElementById('histogram').getContext('2d');

const chart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [0,1, 2, 3, 4, 5,6,7,8,9],
    datasets: [{
      label: 'Number of Arrivals',
      data: [3,6,19, 28, 32, 26,17,5,2],
      backgroundColor: 'blue',
    }]
  },
  options: {
    scales: {
      xAxes: [{
        display: false,
        barPercentage: 1.3,
        ticks: {
          max: 8,
        }
      }, {
        display: true,
        ticks: {
          autoSkip: false,
          max: 10,
        }
      }],
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});

const data1 = [
    { x: 10000, y: 1100 },
     { x: 11000, y: 1200 },
     { x: 13000, y: 1250 },
     { x: 15000, y: 1280 },
     { x: 18000, y: 1600 },

     { x: 20000, y: 2200 },
     { x: 20700, y: 2200 },
     { x: 21000, y: 2200 },
     { x: 24500, y: 2200 },
     { x: 26500, y: 2530 },
     { x: 28500, y: 3040 },

     { x: 30000, y: 4030 },
     { x: 30400, y: 3040 },
     { x: 30600, y: 4060 },
     { x: 31000, y: 4040 },
     { x: 31500, y: 5100 },
     { x: 31900, y: 4200 },
     { x: 34400, y: 3030 },
     { x: 37400, y: 3020 },

     { x: 40000, y: 8210 },
     { x: 40500, y: 8040 },
     { x: 40500, y: 9060 },
     { x: 42300, y: 8300 },
     { x: 44100, y: 9300 },
     { x: 45200, y: 6300 },
     { x: 45400, y: 9900 },
     { x: 46600, y: 4200 },
     { x: 48500, y: 8200 },

     { x: 50000, y: 9040 },
     { x: 50300, y: 9200 },
     { x: 50700, y: 7020 },
     { x: 53000, y: 9040 },
     { x: 53300, y: 9030 },
     { x: 56700, y: 10120 },
     { x: 58700, y: 4020 },

     { x: 60000, y: 10200 },
     { x: 60450, y: 10100 },
     { x: 60400, y: 10400 },
     { x: 60900, y: 9400 },
     { x: 61000, y: 9400 },
     { x: 64000, y: 9000 },
     { x: 64100, y: 10600 },
     { x: 64400, y: 10400 },
     { x: 66000, y: 12400 },
     { x: 66400, y: 13400 }]

var scatter = document.getElementById("scatterplot").getContext("2d");
var myScatter = Chart.Scatter(scatter, {
    data: {
    datasets: [{
      label: "Savings & Income distribution of 50 unmarried people in Texas",
      borderColor: 'rgb(255, 99, 132)',
      data: data1
        }]
    },  
    options: {
        title: {
        display: true,
        text: 'Original Data'
    },
    showLines: false,
    elements: {
      point: {
        radius: 5
      }
    }
  }
});

