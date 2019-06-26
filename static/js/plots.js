google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBarColors);

function drawBarColors() {
      var data = google.visualization.arrayToDataTable(plotData);

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
      var chart = new google.visualization.BarChart(document.getElementById('bar_chart'));
      chart.draw(data, options);
    }


var data = [{
    values: modelValues,
    labels: modelLabels,
    type: 'pie'
  }];
  
  var layout = {
    height: 400,
    width: 500
  };
  

function plotlyInit() {
    var data = [{
      values: modelValues,
      labels: modelLabels,
      type: 'pie' 
    }];

    var layout = {
        height: 600,
        width: 750
      };    
      
    Plotly.newPlot('pie_chart', data, layout);
  }
  
function updatePlotly(newV, newL) {
  
    Plotly.restyle('pie_chart', "values", [newV]);
    Plotly.restyle('pie_chart', "labels", [newL]);
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