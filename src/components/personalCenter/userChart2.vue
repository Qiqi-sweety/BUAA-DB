<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div>
      <div id="userChart2" :style="{ width: '1500px', height: '600px'}"></div>
    </div>
  </template>
   
  <script>
  export default {
    name: "userChart2",
    mounted() {
      // eslint-disable-next-line @typescript-eslint/no-var-requires
      let echarts = require("echarts");
      let myChart = echarts.init(document.getElementById("userChart2"));
      // 绘制图表
      myChart.setOption({
        // title: {
        //     text: '订单数量和支出按月统计图'
        // },
        tooltip: {
          trigger: "item",
        },
        legend: {
          top: "5%",
          left: "center",
        },
        xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug','Sept','Oct','Nov','Dec']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name:  '订单数量',
      type: 'line',
      stack: 'Total',
      data: [120, 132, 101, 134, 90, 230, 210,100,100,150,200,250]
    },
    {
      name: '支出',
      type: 'line',
      stack: 'Total',
      data: [220, 182, 191, 234, 290, 330, 310,98,500,456,300,200]
    },
    
  ]


      });
    },
  };
  </script>