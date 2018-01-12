// graphs
function drawBarChart(barArray) {
  var ctx = document.getElementById("histogram").getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ["Drinking and Gambling", "Food", "Shopping", "Other"],
      datasets: [{
        label: 'Spending',
        data: barArray,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)'
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)'
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
}

$(document).ready(function() {
  processData();
});

function processData() {
        var json = $.getJSON('/totals').done(function(data) {
            var totalFraudulent = data["drinking_and_gambling"][0] + data["food"][0] + data["other"][0] + data["shopping"][0];
            var pieArray = [data["drinking_and_gambling"][0]/totalFraudulent,
                        data["food"][0]/totalFraudulent, data["other"][0]/totalFraudulent,
                        data["shopping"][0]/totalFraudulent];

            drawPieChart(pieArray);
        });

        var json = $.getJSON('/transactions').done(function(data) {
            var totalArray = [0, 0, 0, 0];
            for(var i = 0; i < data.length; i++) {
              var purchase = data[i];
              if(purchase["purchase_category"] == "drinking_and_gambling") totalArray[0] += purchase["purchase_amount"];
              if(purchase["purchase_category"] == "food") totalArray[1] += purchase["purchase_amount"];
              if(purchase["purchase_category"] == "shopping") totalArray[2] += purchase["purchase_amount"];
              if(purchase["purchase_category"] == "other") totalArray[3] += purchase["purchase_amount"];
            }

            drawBarChart(totalArray);
        });
    }

function drawPieChart(pieArray) {
  var ctx = document.getElementById('pieChart').getContext('2d');
  var mydoughnutChart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ["Drinking and Gambling", "Food", "other", "shopping"],
      datasets: [{
        label: ["Listings Available", "Listings Not Available"],
        backgroundColor: ['rgba(255,99,132,1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)', 'rgba(255, 159, 64, 1)'],
        data: pieArray,

      }]
    },
    options: {
      animation: {
        animateScale: true
      }
    }
  });
}
