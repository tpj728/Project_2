google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBarColors);

function drawBarColors() {
      var data = google.visualization.arrayToDataTable(plot_data);

      var options = {
        title: 'Car Value Depreciation (2016 vs 2019)',
        chartArea: {width: '50%'},
        colors: ['#000000', '#c8c8c8'],
        hAxis: {
          title: 'Price ($)',
          minValue: 0
        },
        vAxis: {
          title: 'Car'
        },
        height: 700
      };
      var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
      chart.draw(data, options);
    }

console.log(plot_data)

console.log(typeof plot_data)