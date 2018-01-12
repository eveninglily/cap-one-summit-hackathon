// graphs
/*function drawBarChart() {
  var ctx = document.getElementById("histogram").getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      }
    }
  });
}*/

function drawPieChart() {
  var ctx = document.getElementById('pieChart').getContext('2d');
  var mydoughnutChart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ["Listings Available", "Listings Not Available"],
      datasets: [{
        label: ["Listings Available", "Listings Not Available"],
        backgroundColor: ['rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)'],
        data: [60, 40],

      }]
    },
    options: {
      animation: {
        animateScale: true
      }
    }
  });
}

function drawLineChart() {
  var ctx = document.getElementById('lineChart').getContext('2d');
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: [20, 10],
  });
}

$(document).ready(function() {
  //drawBarChart()
  drawPieChart()
  drawLineChart()
});
