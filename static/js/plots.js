//Google Charts
google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBarColors);

function drawBarColors() {
      var data = google.visualization.arrayToDataTable(plotData);

      var options = {
        title: 'Car Value Depreciation (2016 vs 2019)',
        chartArea: {width: '50%'},
        colors: ['#20308C', '#8C2020'],
        hAxis: {
          title: 'Price ($)',
          minValue: 0
        },
        vAxis: {
          title: 'Car'
        },
        height: 700
      };
      var chart = new google.visualization.BarChart(document.getElementById('bar_chart'));
      chart.draw(data, options);
    }


// Plotly
function plotlyInit() {
    var data = [{
      values: modelValues,
      labels: modelLabels,
      hole: .4,
      type: 'pie' 
    }];

    var layout = {
        title: 'Car Popularity by Model, Make, and Body Style',
        height: 600,
        width: 750
      };    
      
    Plotly.newPlot('donut_chart', data, layout);
  }
  
function updatePlotly(newV, newL) {
  
    Plotly.restyle('donut_chart', "values", [newV]);
    Plotly.restyle('donut_chart', "labels", [newL]);
  }
  
function getData(dataset) {

    var values = [];
    var labels = [];
  
    switch (dataset) {
    case "modelset":
      values = modelValues;
      labels = modelLabels;
      break;
    case "makeset":
      values = makeValues;
      labels = makeLabels;
      break;      
    case "bodyset":
      values = bodyValues;
      labels = bodyLabels;
      break;
    default:
      values = modelValues;
      labels = modelLabels;
      break;
    }
  
    updatePlotly(values, labels);
  }
  
  plotlyInit();