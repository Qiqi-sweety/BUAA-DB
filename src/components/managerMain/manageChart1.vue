<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div id="manageChart1" :style="{width:'1500px', height: '500px'}"></div>
    </div>
  </template>
   
  <script>
  export default {
    name: "manageChart1",
    mounted() {
      // eslint-disable-next-line @typescript-eslint/no-var-requires
      let echarts = require("echarts");
      let myChart = echarts.init(document.getElementById("manageChart1"));
      // 绘制图表
      myChart.setOption({
        title: {
            text: '店铺数据统计图'
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          top: "5%",
          left: "center",
        },
        dataset: {
    source: [
      ['store', '总销量', '总收入', '平均评分'],
      ['喜茶', 43.3, 85.8, 4],
      ['美食苑', 83.1, 73.4, 4],
      ['共享咖啡', 86.4, 65.2, 5],
      ['海棠咖啡', 72.4, 53.9, 4.5]
    ]
  },
  xAxis: { type: 'category' },
  yAxis: {},
  // Declare several bar series, each will be mapped
  // to a column of dataset.source by default.
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }],
      });
    },
  };
  </script>